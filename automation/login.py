import base64
import re
import time
import threading

from PIL import Image
import pytesseract
from playwright.sync_api import Page

from utils.logger import LogWriter

LOGIN_URL = "https://www.catalogos.perucompras.gob.pe/AccesoGeneral"
CATALOGO_URL = "https://www.catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp"
DASHBOARD_URL = "https://www.catalogos.perucompras.gob.pe/"

# Ruta de Tesseract: portable (junto al .exe) o del sistema
import sys, os

# Asegurar que resource_helper se pueda importar desde cualquier cwd
try:
    from resource_helper import resource_path
except ImportError:
    _root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _root not in sys.path:
        sys.path.insert(0, _root)
    from resource_helper import resource_path


def _find_tesseract() -> str:
    # 1. Bundled portable (PyInstaller o desarrollo)
    portable = resource_path("tesseract/tesseract.exe")
    if os.path.isfile(portable):
        return portable
    # 2. Instalación estándar de winget / UB-Mannheim
    std = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.isfile(std):
        return std
    # 3. Buscar en PATH
    import shutil
    found = shutil.which("tesseract")
    if found:
        return found
    return "tesseract"

pytesseract.pytesseract.tesseract_cmd = _find_tesseract()


def _eliminar_modales(page: Page):
    try:
        sel = "#btnSalir, #btnWSSalir, .modal-close, button:has-text('Cerrar'), [data-dismiss='modal']"
        el = page.locator(sel).first
        if el.count() > 0 and el.is_visible(timeout=1000):
            el.click(force=True)
    except Exception:
        pass
    time.sleep(0.3)

def _trigger_materialize_validation(page: Page, input_id: str):
    page.evaluate(f"""
        var el = document.getElementById('{input_id}');
        if (el) {{
            el.dispatchEvent(new Event('input', {{ bubbles: true }}));
            el.dispatchEvent(new Event('change', {{ bubbles: true }}));
            el.dispatchEvent(new Event('blur', {{ bubbles: true }}));
            el.classList.remove('invalid');
            el.classList.add('valid');
        }}
    """)


def _ocr_captcha(image_bytes: bytes) -> str:
    """OCR del CAPTCHA."""
    from PIL import Image
    from io import BytesIO
    import re

    img = Image.open(BytesIO(image_bytes)).convert("L")
    config = "--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    try:
        text = pytesseract.image_to_string(img, config=config)
        return re.sub(r"[^A-Z0-9]", "", text)[:6]
    except Exception:
        return ""



def _solve_captcha(page: Page, log: LogWriter, stop_event: threading.Event, captcha_bridge=None) -> str | None:
    """Intenta OCR con reintentos. Si falla, pide al usuario vía CaptchaBridge."""
    for attempt in range(1, 5):
        if stop_event.is_set():
            return None

        img = page.locator("#imgCaptcha").first
        if img.count() == 0:
            log.error("#imgCaptcha no encontrado")
            return None

        try:
            img_bytes = img.screenshot()
        except Exception:
            try:
                bbox = img.bounding_box()
                if bbox:
                    img_bytes = page.screenshot(clip=bbox)
                else:
                    continue
            except Exception:
                continue

        if not img_bytes:
            continue

        code = _ocr_captcha(img_bytes)
        log.info(f"OCR intento {attempt}: detectado '{code}' ({len(code)} chars)")

        if len(code) >= 4:
            return code

        log.error(f"OCR dio pocos caracteres ({len(code)}), refrescando CAPTCHA...")
        try:
            page.locator("#spnActualizarCaptcha").first.click(force=True)
            time.sleep(2)
        except Exception:
            pass

    # OCR falló en todos los intentos → pedir al usuario
    if captcha_bridge is not None:
        log.info("OCR no pudo resolver el CAPTCHA. Solicitando entrada manual en la UI...")
        log.info("Mirá la imagen del CAPTCHA en la pantalla e ingresá el código.")

        for manual_attempt in range(1, 4):
            if stop_event.is_set():
                return None

            img = page.locator("#imgCaptcha").first
            try:
                img_bytes = img.screenshot()
            except Exception:
                continue

            code = captcha_bridge.request(img_bytes)
            if code and len(code) >= 4:
                log.info(f"Código manual recibido: {code}")
                return code

            log.error(f"Código manual inválido ({len(code) if code else 0} chars), refrescando...")
            try:
                page.locator("#spnActualizarCaptcha").first.click(force=True)
                time.sleep(2)
            except Exception:
                pass

    return None


def do_login(
    page: Page,
    usuario: str,
    password: str,
    captcha_key: str | None,
    log: LogWriter,
    stop_event: threading.Event,
    captcha_bridge=None,
    max_retries: int = 5,
) -> bool:
    """Intenta login hasta max_retries veces (por si el CAPTCHA falla)."""
    log.info(f"Navegando a {LOGIN_URL}")
    page.goto(LOGIN_URL, wait_until="networkidle")
    page.wait_for_load_state("domcontentloaded")
    time.sleep(3)

    for retry in range(1, max_retries + 1):
        if stop_event.is_set():
            return False

        log.info(f"Intento de login {retry}/{max_retries}")

        result = _attempt_login_once(
            page, usuario, password, captcha_key,
            log, stop_event, captcha_bridge,
        )

        if result:
            # Navegar directo al catálogo de ofertas (evita modales del dashboard)
            current = page.url
            if "t_ProductoOfertadoAmp" not in current:
                log.info("Navegando al catálogo de ofertas...")
                try:
                    page.goto(CATALOGO_URL, wait_until="networkidle")
                    time.sleep(2)
                except Exception:
                    pass
            return True

        if result is False and retry < max_retries and not stop_event.is_set():
            log.info(f"Login falló (intento {retry}), refrescando página para reintentar...")
            try:
                page.goto(LOGIN_URL, wait_until="networkidle")
                time.sleep(2)
            except Exception:
                pass

    log.error(f"Login falló tras {max_retries} intentos.")
    return False


def _attempt_login_once(
    page: Page,
    usuario: str,
    password: str,
    captcha_key: str | None,
    log: LogWriter,
    stop_event: threading.Event,
    captcha_bridge=None,
) -> bool:
    """Un solo intento de login. Retorna True si éxito, False si falló."""
    try:
        _eliminar_modales(page)

        if stop_event.is_set():
            return False

        log.info("Rellenando credenciales de Peru Compras...")

        user_input = page.locator("#ID_Usuario").first
        pass_input = page.locator("#Contrasena").first

        if user_input.count() == 0 or pass_input.count() == 0:
            log.error("No se encontraron los campos #ID_Usuario / #Contrasena.")
            return False

        user_input.fill(usuario)
        _trigger_materialize_validation(page, "ID_Usuario")

        pass_input.fill(password)
        _trigger_materialize_validation(page, "Contrasena")

        time.sleep(0.5)

        if stop_event.is_set():
            return False

        # --- Resolver CAPTCHA con OCR + fallback manual ---
        log.info("Resolviendo CAPTCHA con OCR...")
        captcha_code = _solve_captcha(page, log, stop_event, captcha_bridge)

        if not captcha_code or len(captcha_code) < 4:
            log.error("No se pudo resolver el CAPTCHA.")
            return False

        captcha_input = page.locator("#CodigoCaptcha").first
        captcha_input.fill(captcha_code)
        _trigger_materialize_validation(page, "CodigoCaptcha")
        time.sleep(0.3)

        if stop_event.is_set():
            return False

        # --- Click en botón Ingresar ---
        log.info("Click en botón Ingresar...")
        login_btn = page.locator("#btnLogin").first
        if login_btn.count() == 0:
            log.error("No se encontró el botón #btnLogin.")
            return False

        login_btn.click(force=True)

        try:
            page.wait_for_load_state("networkidle", timeout=25000)
        except Exception:
            pass
        time.sleep(3)

        if stop_event.is_set():
            return False

        current_url = page.url

        # Verificar si seguimos EXACTAMENTE en la página de login
        from urllib.parse import urlparse
        parsed = urlparse(current_url)
        path = parsed.path.rstrip("/")

        if path == "/AccesoGeneral":
            error_msg = ""
            try:
                error_el = page.locator(".red-text, [class*='error'], #form-errors li").first
                if error_el.count() > 0:
                    error_msg = error_el.inner_text(timeout=2000)
            except Exception:
                pass
            log.error(
                f"Login falló — seguimos en la página de login. "
                f"{'Mensaje: ' + error_msg if error_msg else 'CAPTCHA incorrecto o credenciales inválidas.'}"
            )
            return False

        # Si caímos en ValidarAcceso, retroceder para completar el login
        if "ValidarAcceso" in path:
            log.info("Detectada página ValidarAcceso, retrocediendo...")
            try:
                page.go_back()
                time.sleep(2)
            except Exception:
                pass
            # Verificar dónde quedamos
            new_url = page.url
            parsed2 = urlparse(new_url)
            if parsed2.path.rstrip("/") == "/AccesoGeneral":
                log.error("go_back() nos devolvió al login. Reintentando...")
                return False
            log.ok(f"Login exitoso -> {new_url[:80]}")
            return True

        log.ok(f"Login exitoso en Peru Compras -> {current_url[:80]}")
        return True

    except Exception as e:
        log.error(f"Excepción en intento de login: {e}")
        return False

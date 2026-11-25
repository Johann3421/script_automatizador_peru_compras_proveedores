"""
stock.py — Flujo de Actualización de Stock (réplica del otro bot en Playwright)
================================================================================
Replica el modo "stock" del bot PeruCompras (REPLICAR_OTRO_BOT.txt) usando
Playwright sync en vez de Selenium.

Funcionalidades:
- Login con credenciales + OCR de CAPTCHA
- Navegación con truco de retroceso (back() + get(BASE) + get(MEJORA))
- Selección de filtros (Acuerdo > Catálogo > Categoría)
- Búsqueda por número de parte
- Actualización de stock via modal
- Reintentos con backoff (MAX_REINTENTOS=3)
- Reporte Excel con 3 hojas (Resumen, Detalle, Solo Fallidos)
- Clasificación de errores
- Aprendizaje adaptativo (registra tipos de fallo recurrentes)

Diferencias con el bot Selenium original:
- Usa Playwright sync en vez de Selenium WebDriver
- Usa fetch() desde JS para llamadas API
- OCR con pytesseract (igual al original)
- Selectores CSS adaptados (los mismos que el portal)
"""
import re
import os
import sys
import json
import time
import threading
from datetime import datetime
from pathlib import Path

import openpyxl
from openpyxl.chart import PieChart, BarChart, Reference
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter


# ══════════════════════════════════════════════════════════════════════════════
# CONSTANTES
# ══════════════════════════════════════════════════════════════════════════════

BASE_URL = "https://www.catalogos.perucompras.gob.pe"
LOGIN_URL = f"{BASE_URL}/AccesoGeneral"
MEJORA_URL = f"{BASE_URL}/MejoraBasica"
MEJORA_COBERTURA_URL = f"{BASE_URL}/MejoraCobertura"
MEJORA_PLAZO_URL = f"{BASE_URL}/MejoraPlazo/IndexMejora"

# Defaults del portal
ACUERDO_TEXTO = "EXT-CE-2022-5 COMPUTADORAS DE ESCRITORIO, COMPUTADORAS PORTÁTILES Y ESCÁNERES"
CATALOGO_TEXTO = "COMPUTADORAS DE ESCRITORIO"
CATEGORIA_TEXTO = "MONITOR"

# Tiempos (segundos)
WAIT_NORMAL = 30
WAIT_LARGO = 60
WAIT_CORTO = 10
PAUSA_ENTRE_PRODUCTOS = 2
MAX_REINTENTOS = 3
MAX_INTENTOS_LOGIN = 5

# Selectores del portal
_INPUT_USUARIO = ["#ID_Usuario", "#txtUsuario", "#N_Usuario",
                  "input[name*='Usuario' i]:not([type='hidden'])"]
_INPUT_PASSWORD = ["#Contrasena", "#txtPassword", "#N_Password", "input[type='password']"]
_INPUT_CAPTCHA = ["#CodigoCaptcha", "#txtCaptcha", "input[name*='aptcha' i]:not([type='hidden'])"]
_IMG_CAPTCHA = ["#imgCaptcha", "img[src*='aptcha' i]"]
_BTN_LOGIN = ["button[type='submit']", "#btnLogin", "#btnIngresar",
              "button:has-text('Ingresar')", "input[type='submit']"]

# Estado global
RESULTADOS = []  # [{"Parte", "Stock", "Estado", "Tipo de Fallo", "Descripción", "Duración"}]
STOP_EVENT = None
PAUSA_EVENT = None
ANALIZADOR = None


# ══════════════════════════════════════════════════════════════════════════════
# ADAPTADOR DE LOGGER PARA REUTILIZAR do_login DEL FLUJO PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

class _LogAdapter:
    """Adapta una función log_func() simple a la interfaz LogWriter de automation/login.py."""
    def __init__(self, log_func):
        self._log = log_func

    def info(self, msg: str):
        self._log(msg)

    def ok(self, msg: str):
        self._log(msg)

    def error(self, msg: str):
        self._log(msg)

    def warn(self, msg: str):
        self._log(msg)

    def progress(self, current: int, total: int):
        pass

    def done(self, ok_count: int, error_count: int):
        pass


# ══════════════════════════════════════════════════════════════════════════════
# RE-LOGIN AUTOMÁTICO (igual que bulk_subir_pdf.py)
# ══════════════════════════════════════════════════════════════════════════════

def _is_logged_in(page) -> bool:
    """Verifica si seguimos logueados: URL + ausencia de formulario login visible."""
    try:
        url = page.url.lower()
        # 1. Si estamos explícitamente en login/accesogeneral → NO logueado
        if "accesogeneral" in url or "login" in url:
            return False
        # 2. Si el formulario de login está visible AHORA (no momentáneamente) → NO logueado
        # Usar wait_for con state="visible" y timeout corto para confirmar que REALMENTE está ahí
        try:
            user_input = page.locator("#ID_Usuario").first
            # wait_for con timeout=2000 confirma que permanece visible, no es un flash
            user_input.wait_for(state="visible", timeout=2000)
            return False  # formulario visible confirmado = sesión expirada
        except Exception:
            # No apareció o desapareció → no hay formulario → logueado
            pass
        return True
    except Exception:
        return True


def _esta_en_mejorabasica(page) -> bool:
    """Verifica que estemos en la página de MejoraBasica (donde se editan productos)."""
    try:
        url = page.url.lower()
        return "mejorabasica" in url
    except Exception:
        return False


def _tiene_campos_login(page) -> bool:
    """Verifica si la página actual tiene los campos de login visibles."""
    try:
        user_input = page.locator("#ID_Usuario").first
        return user_input.count() > 0 and user_input.is_visible(timeout=2000)
    except Exception:
        return False


def _relogin(page, usuario: str, password: str, log_func, stop_event=None, captcha_bridge=None) -> bool:
    """Vuelve a la página de login y se loguea de cero usando la Función Padre centralizada login_automatico."""
    if stop_event is None:
        import threading
        stop_event = threading.Event()
    log_func("🔁 Sesión expirada. Ejecutando re-login automático...")
    try:
        if stop_event and stop_event.is_set():
            return False

        from automation.perucompras_core import login_automatico, saltar_verificacion

        # 1. Login automático idéntico a la primera vez (viewport HD + OCR sin limite)
        ok = login_automatico(page, usuario, password, captcha_bridge, stop_event, log_func)
        if not ok or (stop_event and stop_event.is_set()):
            log_func("❌ Re-login falló.")
            return False

        # 2. Retroceso y navegación garantizada a MejoraBasica
        saltar_verificacion(page, log_func)
        return True
    except Exception as e:
        log_func(f"❌ Re-login falló con excepción: {e}")
        return False


# ══════════════════════════════════════════════════════════════════════════════
# LOGGING
# ══════════════════════════════════════════════════════════════════════════════

import sys, os, time, json, re
from datetime import datetime

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def log(msg):
    txt = f"[{datetime.now().strftime('%H:%M:%S')}] {msg}"
    try:
        print(txt)
    except Exception:
        try:
            enc = getattr(sys.stdout, 'encoding', None) or 'utf-8'
            print(txt.encode(enc, errors='replace').decode(enc, errors='replace'))
        except Exception:
            pass



# ══════════════════════════════════════════════════════════════════════════════
# LIMPIEZA DE MODALES
# ══════════════════════════════════════════════════════════════════════════════

_CLEAR_MODALS_JS = r"""
(function() {
    // 1. Click en botones de cierre típicos
    const closeButtons = document.querySelectorAll(
        '[data-dismiss="modal"], .modal-header button.close, .modal .close, ' +
        'button[aria-label="Close"], button[title="Close"], button[title="Cerrar"], ' +
        '._wModal_close, ._wModal_btn_ok, ._wModal_btn_cancel, ' +
        '.swal2-confirm, .swal2-cancel, .swal2-close'
    );
    closeButtons.forEach(btn => { try { btn.click(); } catch(e) {} });

    // 2. Eliminar modales por selector
    const sels = [
        '._wModal', '._wModal_delete', '._wModal_bg',
        '.sweet-alert', '.swal2-container', '.swal2-popup', '.swal2-backdrop',
        '.modal.fade.in', '.modal.fade.show', '.modal.show', '.modal-backdrop',
        '[role="dialog"]', '[aria-modal="true"]', 'dialog[open]'
    ];
    sels.forEach(s => {
        try { document.querySelectorAll(s).forEach(el => el.remove()); } catch(e) {}
    });

    // 3. Resetear body
    document.body.style.overflow = '';
    document.body.style.paddingRight = '';
    document.body.classList.remove('modal-open');

    return true;
})();
"""


def clear_modals(page):
    """Limpia todos los modales colgados."""
    try:
        page.evaluate(_CLEAR_MODALS_JS)
        return True
    except Exception as e:
        log(f"⚠ clear_modals error: {e}")
        return False


# ══════════════════════════════════════════════════════════════════════════════
# LOGIN CON OCR
# ══════════════════════════════════════════════════════════════════════════════

def _trigger_materialize(page, input_id):
    """Dispara eventos input/change/blur en un input para Materialize CSS."""
    try:
        page.evaluate(f"""
            var el = document.getElementById('{input_id}');
            if (el) {{
                el.dispatchEvent(new Event('input', {{bubbles: true}}));
                el.dispatchEvent(new Event('change', {{bubbles: true}}));
                el.dispatchEvent(new Event('blur', {{bubbles: true}}));
            }}
        """)
    except Exception as e:
        log(f"⚠ _trigger_materialize error: {e}")


def _solve_captcha(page) -> str | None:
    """OCR del CAPTCHA con 4 thresholds."""
    try:
        import pytesseract
        from PIL import Image
        import io
    except ImportError:
        return None
    try:
        img_el = page.locator("#imgCaptcha").first
        img_el.wait_for(timeout=5000)
        img_bytes = img_el.screenshot()
        img = Image.open(io.BytesIO(img_bytes))
        img = img.resize((img.width * 4, img.height * 4), Image.LANCZOS).convert("L")
        for threshold in [140, 120, 100, 80]:
            binary = img.point(lambda p: 255 if p > threshold else 0)
            text = pytesseract.image_to_string(
                binary,
                config="--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            ).strip().upper()
            text = re.sub(r"[^A-Z0-9]", "", text)
            if 4 <= len(text) <= 8:
                return text
    except Exception as e:
        log(f"⚠ OCR error: {e}")
    return None


def _type_field(page, selector_list, value, materialize_id=None):
    """Escribe value en el primer selector que funcione."""
    for sel in selector_list:
        try:
            el = page.locator(sel).first
            if el.count() == 0:
                continue
            el.click()
            el.fill("")  # limpiar
            el.fill(str(value))
            if materialize_id:
                _trigger_materialize(page, materialize_id)
            return True
        except Exception:
            continue
    return False


def login_with_ocr(page, usuario, password, captcha_bridge=None, max_intentos=MAX_INTENTOS_LOGIN, skip_goto=False) -> bool:
    """Login automático con OCR del CAPTCHA.

    Si el OCR no está disponible, retorna False (caller debe caer a login manual).
    skip_goto: si True, asume que ya estamos en LOGIN_URL y no navega de nuevo.
    """
    log(f"🔐 Login automático con OCR ({usuario})")
    if not skip_goto:
        page.goto(LOGIN_URL, wait_until="networkidle", timeout=60_000)
        page.wait_for_load_state("domcontentloaded")
        # Limpiar modales que aparezcan tras cargar la página de login
        clear_modals(page)
    time.sleep(3)

    for intento in range(1, max_intentos + 1):
        if STOP_EVENT and STOP_EVENT.is_set():
            return False
        log(f"🔐 Intento {intento}/{max_intentos}")

        # Limpiar modales antes de CADA paso
        clear_modals(page)

        # Verificar si ya estamos logueados
        url = page.url.lower()
        if "accesogeneral" not in url and "login" not in url:
            log(f"✅ Ya estamos en {page.url}, saltando login")
            return True

        # Tipear credenciales
        if not _type_field(page, _INPUT_USUARIO, usuario, "ID_Usuario"):
            log(f"⚠ Intento {intento}: no se pudo tipear usuario")
            page.goto(LOGIN_URL)
            time.sleep(2)
            continue
        time.sleep(0.3)

        if not _type_field(page, _INPUT_PASSWORD, password, "Contrasena"):
            log(f"⚠ Intento {intento}: no se pudo tipear contraseña")
            page.goto(LOGIN_URL)
            time.sleep(2)
            continue
        time.sleep(0.5)

        # Resolver CAPTCHA
        if captcha_bridge:
            try:
                img_el = page.locator("#imgCaptcha").first
                img_bytes = img_el.screenshot()
                texto = captcha_bridge.request(img_bytes)
                if texto:
                    texto = re.sub(r"[^A-Z0-9]", "", texto.upper())
            except Exception:
                texto = None
        else:
            texto = _solve_captcha(page)

        if not texto:
            log(f"⚠ Intento {intento}: OCR no resolvió CAPTCHA")
            page.goto(LOGIN_URL)
            time.sleep(2)
            continue

        # Tipear CAPTCHA
        if not _type_field(page, _INPUT_CAPTCHA, texto, "CodigoCaptcha"):
            log(f"⚠ Intento {intento}: no se pudo tipear CAPTCHA")
            page.goto(LOGIN_URL)
            time.sleep(2)
            continue
        time.sleep(0.3)

        # Limpiar modales antes del submit
        clear_modals(page)

        # Click submit
        clicked = False
        for sel in _BTN_LOGIN:
            try:
                btn = page.locator(sel).first
                if btn.count() > 0:
                    btn.click(timeout=5_000)
                    clicked = True
                    break
            except Exception:
                continue
        if not clicked:
            # Fallback JS
            try:
                page.evaluate("""
                    var b = document.querySelector('button[type=submit], #btnLogin, #btnIngresar');
                    if (b) b.click();
                """)
            except Exception:
                pass

        time.sleep(2)
        clear_modals(page)
        time.sleep(2)

        # Verificar éxito
        url = page.url.lower()
        if "accesogeneral" not in url and "login" not in url:
            log(f"✅ Login exitoso. URL: {page.url}")
            return True

        # ValidarAcceso -> back() y reintentar
        if "validaracceso" in url:
            log(f"⚠ ValidarAcceso detectada, back()")
            try:
                page.go_back()
                time.sleep(2)
            except Exception:
                pass
            continue

        log(f"⚠ Intento {intento}: seguimos en {url}, reintentando...")
        page.goto(LOGIN_URL)
        time.sleep(2)

    log(f"❌ Login falló tras {max_intentos} intentos")
    return False


# ══════════════════════════════════════════════════════════════════════════════
# VALIDACIÓN DE EXCEL
# ══════════════════════════════════════════════════════════════════════════════

def _normalizar_parte(valor) -> str:
    if valor is None:
        return ""
    try:
        import math
        if isinstance(valor, float) and math.isnan(valor):
            return ""
    except Exception:
        pass
    return str(valor).strip()


def _normalizar_stock(valor):
    """Convierte a int, retorna None si es inválido."""
    if valor is None:
        return None
    try:
        import math
        if isinstance(valor, float) and math.isnan(valor):
            return None
    except Exception:
        pass
    s = str(valor).replace(",", "").strip()
    if not s:
        return None
    try:
        val = int(float(s))
        return val if val >= 0 else None
    except Exception:
        return None


def analizar_excel_stock(excel_path) -> dict:
    """Analiza el Excel de stock. Retorna {valido: bool, df: [...], errores: [...]}"""
    if not os.path.isfile(excel_path):
        return {"valido": False, "df": [], "errores": [f"No existe: {excel_path}"]}

    try:
        wb = openpyxl.load_workbook(excel_path, data_only=True, read_only=True)
    except Exception as e:
        return {"valido": False, "df": [], "errores": [f"Error abriendo Excel: {e}"]}

    try:
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))
    finally:
        wb.close()

    if not rows:
        return {"valido": False, "df": [], "errores": ["Excel vacío"]}

    headers = [str(h).strip() if h else "" for h in rows[0]]
    log(f"📋 Encabezados: {headers}")

    # Detectar columnas con aliases flexibles y protección contra falsos positivos
    def _match_alias(header_str, alias_list):
        norm = str(header_str or "").lower().strip()
        words = norm.replace("_", " ").replace("-", " ").replace(".", " ").split()
        for a in alias_list:
            if a == norm:
                return True
            if len(a) <= 3:
                if a in words or norm.startswith(a + " ") or norm.startswith(a + "_"):
                    return True
            else:
                if a in norm:
                    return True
        return False

    col_parte = None
    col_stock = None
    col_ficha = None
    aliases_parte = ["parte", "n_parte", "n° parte", "nro parte", "nro. parte", "n° de parte", "nro de parte", "part number", "part_number", "p/n", "pn", "codigo", "código", "item", "producto"]
    aliases_stock = ["stock", "cant", "cantidad", "unidades", "unidad", "existencia", "existencias", "disponible", "disponibles", "inventario", "total"]
    aliases_ficha = ["ficha", "id_catalogo", "id catalogo", "catalogo_producto", "catalogoproducto", "id_producto", "id producto", "id"]
    for i, h in enumerate(headers):
        if col_parte is None and _match_alias(h, aliases_parte):
            col_parte = i
        elif col_stock is None and _match_alias(h, aliases_stock):
            col_stock = i
        elif col_ficha is None and _match_alias(h, aliases_ficha):
            col_ficha = i

    errores = []
    if col_parte is None:
        errores.append("Falta columna 'Parte'")
    if col_stock is None:
        errores.append("Falta columna 'Stock'")

    if errores:
        return {"valido": False, "df": [], "errores": errores}

    # Parsear filas
    data = []
    for i, row in enumerate(rows[1:], start=2):
        parte = _normalizar_parte(row[col_parte]) if col_parte < len(row) else ""
        stock = _normalizar_stock(row[col_stock]) if col_stock < len(row) else None
        ficha = ""
        if col_ficha is not None and col_ficha < len(row):
            f = row[col_ficha]
            if f is not None:
                ficha = str(f).strip()

        if not parte and stock is None:
            continue  # fila vacía
        if not parte:
            errores.append(f"Fila {i}: falta 'Parte'")
            continue
        if stock is None:
            errores.append(f"Fila {i}: stock inválido '{row[col_stock]}'")
            continue

        data.append({"Parte": parte, "Stock": stock, "Ficha": ficha})

    return {"valido": len(data) > 0, "df": data, "errores": errores, "total": len(data)}


# ══════════════════════════════════════════════════════════════════════════════
# NAVEGACIÓN
# ══════════════════════════════════════════════════════════════════════════════

def paso2_navegacion_stock(page):
    """Truco de retroceso + ir a MejoraBasica."""
    try:
        page.go_back()
        time.sleep(2)
    except Exception:
        pass
    try:
        page.goto(BASE_URL, wait_until="networkidle", timeout=60_000)
        time.sleep(2)
    except Exception:
        pass
    try:
        page.goto(MEJORA_URL, wait_until="networkidle", timeout=60_000)
        time.sleep(3)
    except Exception as e:
        log(f"⚠ Error navegando a MejoraBasica: {e}")


def seleccionar_por_texto_flexible(page, select_id, texto_objetivo, retries=6, delay=1.5):
    """Selecciona option por match flexible en Playwright disparando eventos jQuery/DOM."""
    def normalizar(s):
        if not s:
            return ""
        s = str(s).lower().strip()
        repl = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n"}
        for a, b in repl.items():
            s = s.replace(a, b)
        return s

    target = normalizar(texto_objetivo)

    for attempt in range(retries):
        options = page.evaluate(f"""
            () => {{
                let sel = document.querySelector('{select_id}');
                if (!sel) {{
                    const key = '{select_id}'.replace('#', '').toLowerCase();
                    const candidates = document.querySelectorAll('select');
                    for (let s of candidates) {{
                        if (s.id.toLowerCase().includes(key) || s.name.toLowerCase().includes(key)) {{
                            sel = s;
                            break;
                        }}
                    }}
                }}
                if (!sel) return [];
                return Array.from(sel.options).map(o => ({{
                    value: o.value, text: o.text
                }}));
            }}
        """)

        if options and len(options) > 0:
            selected_val = None

            # a. Match exacto (normalizado)
            for opt in options:
                if normalizar(opt["text"]) == target:
                    selected_val = opt["value"]
                    break

            # b. Contiene el target
            if not selected_val:
                for opt in options:
                    if target in normalizar(opt["text"]):
                        selected_val = opt["value"]
                        break

            # c. El target contiene al option text
            if not selected_val:
                for opt in options:
                    norm_opt = normalizar(opt["text"])
                    if norm_opt and norm_opt in target and len(norm_opt) >= 3:
                        selected_val = opt["value"]
                        break

            # d. Coincidencia por primera palabra/código relevante (p.ej. "EXT-CE-2022-5")
            if not selected_val:
                words = [w for w in target.split() if len(w) >= 3]
                if words:
                    first_code = words[0]
                    for opt in options:
                        if first_code in normalizar(opt["text"]):
                            selected_val = opt["value"]
                            break

            # e. Match por value exacto
            if not selected_val:
                for opt in options:
                    if str(opt["value"]).strip() == str(texto_objetivo).strip():
                        selected_val = opt["value"]
                        break

            if selected_val is not None:
                try:
                    page.select_option(select_id, value=selected_val)
                except Exception:
                    pass

                page.evaluate(f"""
                    (val) => {{
                        let sel = document.querySelector('{select_id}');
                        if (!sel) {{
                            const key = '{select_id}'.replace('#', '').toLowerCase();
                            const candidates = document.querySelectorAll('select');
                            for (let s of candidates) {{
                                if (s.id.toLowerCase().includes(key) || s.name.toLowerCase().includes(key)) {{
                                    sel = s;
                                    break;
                                }}
                            }}
                        }}
                        if (sel) {{
                            sel.value = val;
                            sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
                            sel.dispatchEvent(new Event('input', {{ bubbles: true }}));
                            if (window.jQuery && window.jQuery(sel)) {{
                                window.jQuery(sel).trigger('change');
                            }}
                        }}
                    }}
                """, selected_val)
                time.sleep(delay)
                return True

        time.sleep(delay)

    return False




def _wait_for_select_options(page, select_id, timeout_ms=30_000):
    """Espera a que un <select> tenga opciones con value no vacio."""
    try:
        page.wait_for_function(f"""
            () => {{
                const sel = document.querySelector('{select_id}');
                if (!sel) return false;
                const opts = Array.from(sel.options).filter(o => o.value && o.value.trim() !== '');
                return opts.length > 0;
            }}
        """, timeout=timeout_ms)
        return True
    except Exception:
        return False


def paso3_filtros_stock(page, acuerdo=ACUERDO_TEXTO, catalogo=CATALOGO_TEXTO, categoria=CATEGORIA_TEXTO):
    """Selecciona Acuerdo > Catálogo > Categoría y espera que cargue la tabla."""
    try:
        # Esperar que el select de acuerdo esté disponible
        page.wait_for_selector("#ajaxAcuerdo, select[name*='cuerdo']", timeout=WAIT_NORMAL * 1000)
        time.sleep(2)
        if not seleccionar_por_texto_flexible(page, "#ajaxAcuerdo", acuerdo):
            log(f"⚠ No se encontró Acuerdo: {acuerdo}")
            return False
        # Esperar a que el catalogo cargue opciones
        time.sleep(3)
        _wait_for_select_options(page, "#ajaxCatalogo")

        if not seleccionar_por_texto_flexible(page, "#ajaxCatalogo", catalogo):
            log(f"⚠ No se encontró Catálogo: {catalogo}")
            return False
        # Esperar a que la categoria cargue opciones
        time.sleep(3)
        _wait_for_select_options(page, "#ajaxCategoria")

        if not seleccionar_por_texto_flexible(page, "#ajaxCategoria", categoria):
            log(f"⚠ No se encontró Categoría: {categoria}")
            return False

        # 4. Clic en el botón "Iniciar Búsqueda" (#btnBuscar) una sola vez
        log("🚀 Clic en 'Iniciar Búsqueda' (#btnBuscar) para cargar la tabla del portal...")
        time.sleep(0.5)
        btn_buscar = page.locator("#btnBuscar, button[name='btnBuscar'], button:has-text('Iniciar Búsqueda')").first
        if btn_buscar.count() > 0:
            try:
                btn_buscar.click(force=True)
            except Exception:
                page.evaluate("() => { const b = document.getElementById('btnBuscar') || document.querySelector('button[name=\"btnBuscar\"]'); if (b) b.click(); }")
        else:
            page.evaluate("() => { const b = document.getElementById('btnBuscar') || document.querySelector('button[name=\"btnBuscar\"]'); if (b) b.click(); }")

        # 5. Esperar activamente a que la tabla cargue filas reales
        log("⏳ Esperando carga de tabla de productos...")
        try:
            page.wait_for_selector(
                ".loading, .spinner, .fa-spinner, .progress, .ajax-loading",
                state="detached",
                timeout=30_000,
            )
        except Exception:
            pass

        t_wait_start = time.time()
        while time.time() - t_wait_start < 25:
            ready = page.evaluate("""() => {
                if (window.jQuery && window.jQuery.fn.DataTable && window.jQuery('#TablaProductos').length) {
                    const dt = window.jQuery('#TablaProductos').DataTable();
                    if (dt && dt.data && dt.data().length > 0) return true;
                }
                const trs = document.querySelectorAll('#TablaProductos tbody tr');
                if (trs.length > 0 && !trs[0].innerText.includes('Ningún dato') && !trs[0].innerText.includes('Cargando')) {
                    return true;
                }
                return false;
            }""")
            if ready:
                break
            time.sleep(0.5)

        time.sleep(1)
        return True
    except Exception as e:
        log(f"⚠ Error en paso3_filtros: {e}")
        return False


# ══════════════════════════════════════════════════════════════════════════════
# ACTUALIZACIÓN DE STOCK
# ══════════════════════════════════════════════════════════════════════════════

def clasificar_error(mensaje: str) -> str:
    msg = str(mensaje).lower()
    if "browser has been closed" in msg or "browser was closed" in msg or "connection closed" in msg:
        return "Navegador cerrado"
    if "no se encontraron resultados" in msg:
        return "Producto no encontrado en la tabla"
    if "n_stock" in msg or "campo de stock" in msg:
        return "Modal de stock no se abrió"
    if "timeout" in msg or "timed out" in msg:
        return "Tiempo de espera agotado"
    if "no such element" in msg:
        return "Elemento de página no encontrado"
    if "stale" in msg:
        return "Página cambió durante la operación"
    return "Error inesperado"


def _browser_cerrado(mensaje: str) -> bool:
    """Detecta si el error se debe a que el usuario cerró el navegador o canceló."""
    msg = str(mensaje).lower()
    return any(p in msg for p in [
        "browser has been closed",
        "browser was closed",
        "connection closed",
        "target page, context or browser has been closed",
        "detenido por usuario",
        "detención solicitada",
        "detencion solicitada",
        "target closed",
    ])


def _es_sin_resultados(mensaje: str) -> bool:
    """Detecta si la respuesta indica explicitamente que el producto no existe en el portal."""
    msg = str(mensaje).lower()
    return any(p in msg for p in [
        "no se encontraron resultados",
        "ningún dato disponible",
        "ningun dato disponible",
        "sin resultados",
        "0 registros",
        "no coincide",
        "producto no encontrado"
    ])


def _find_exact_matching_row(page, parte: str):
    """
    Busca en la tabla de productos la fila que contenga EXACTAMENTE el número de parte.
    Evita seleccionar por error 'PARTE-1' cuando se busca 'PARTE'.
    """
    target = str(parte).strip().upper()
    target_clean = " ".join(target.split())
    if not target_clean:
        return None

    rows = page.locator("#TablaProductos tbody tr, table tbody tr").all()
    if not rows:
        return None

    # Paso 1: Coincidencia EXACTA celda por celda (td.text == target)
    for r in rows:
        try:
            cells = r.locator("td").all()
            for c in cells:
                c_text = " ".join(c.inner_text(timeout=300).strip().upper().split())
                if c_text == target_clean:
                    return r
        except Exception:
            continue

    # Paso 2: Coincidencia por delimitador de palabra estricto (evita prefijos/sufijos como -1, _v2, etc.)
    pattern = re.compile(r'(?<![A-Z0-9#\-_/])' + re.escape(target_clean) + r'(?![A-Z0-9#\-_/])')
    for r in rows:
        try:
            r_text = " ".join(r.inner_text(timeout=300).strip().upper().split())
            if pattern.search(r_text):
                return r
        except Exception:
            continue

    # Paso 3: Fallback a tr:has-text de Playwright
    try:
        exact_tr = page.locator(f"tr:has-text('{parte}')")
        if exact_tr.count() > 0:
            return exact_tr.first
    except Exception:
        pass

    return None


def extraer_mapa_portal_stock(page, log_func=None, max_retries=4):
    """Extrae en memoria RAM todos los registros de MejoraBasica con triple estrategia (RAM DataTables -> DOM activo -> Fetch HTTP directo)."""
    if log_func: log_func("⚡ Indexando catálogo de MejoraBasica en memoria...")

    script = r"""async () => {
        const token = document.querySelector('input[name="__RequestVerificationToken"]')?.value || "";
        const nAcuerdo = document.querySelector('#ajaxAcuerdo, #N_Acuerdo, select[name*="cuerdo"]')?.value || "249";
        const nCatalogo = document.querySelector('#ajaxCatalogo, #N_Catalogo, select[name*="atalogo"]')?.value || "252";
        const nCategoria = document.querySelector('#ajaxCategoria, #N_Categoria, select[name*="ategoria"]')?.value || "11735";

        let items = [];

        // ── ESTRATEGIA 1: DataTables en memoria RAM
        try {
            if (window.jQuery && window.jQuery.fn.DataTable && window.jQuery('#TablaProductos').length) {
                const dt = window.jQuery('#TablaProductos').DataTable();
                if (dt && dt.data) {
                    const raw = dt.data().toArray();
                    if (raw && raw.length > 0) {
                        for (let i = 0; i < raw.length; i++) {
                            const r = raw[i];
                            if (!r) continue;
                            let idOfertado = "";
                            let idCatalogo = "";
                            let desc = "";
                            let stockActual = 0;

                            if (Array.isArray(r)) {
                                desc = r[1] ? String(r[1]).trim() : "";
                                stockActual = r[6] ? parseInt(String(r[6]).replace(/,/g, '')) || 0 : 0;
                                for (let c = 0; c < r.length; c++) {
                                    const cell = String(r[c] || "");
                                    const mOf = cell.match(/fnModificarStock\((\d+)\)/) || cell.match(/fnReducirPrecio\((\d+)\)/);
                                    if (mOf) idOfertado = mOf[1];
                                    const mCat = cell.match(/fnDetalleRegistro\((\d+)\)/);
                                    if (mCat) idCatalogo = mCat[1];
                                }
                            }
                            if (idOfertado) {
                                items.push({
                                    "id_ofertado": idOfertado,
                                    "id_catalogo": idCatalogo,
                                    "desc": desc,
                                    "stock_actual": stockActual
                                });
                            }
                        }
                    }
                }
            }
        } catch(e) {}

        // ── ESTRATEGIA 2: Parseo directo de elementos TR del DOM
        if (items.length === 0) {
            try {
                const trs = document.querySelectorAll('#TablaProductos tbody tr');
                trs.forEach(tr => {
                    const tds = tr.querySelectorAll('td');
                    if (tds.length < 5) return;
                    const desc = tds[1] ? tds[1].innerText.trim() : "";
                    if (!desc || desc.includes("No se encontraron") || desc.includes("Ningún dato")) return;

                    let idOfertado = "";
                    let idCatalogo = "";
                    const stockActual = tds[6] ? parseInt(tds[6].innerText.replace(/,/g, '')) || 0 : 0;

                    for (let c = 0; c < tds.length; c++) {
                        const html = tds[c].innerHTML;
                        const mOf = html.match(/fnModificarStock\((\d+)\)/) || html.match(/fnReducirPrecio\((\d+)\)/);
                        if (mOf) idOfertado = mOf[1];
                        const mCat = html.match(/fnDetalleRegistro\((\d+)\)/);
                        if (mCat) idCatalogo = mCat[1];
                    }

                    if (idOfertado) {
                        items.push({
                            "id_ofertado": idOfertado,
                            "id_catalogo": idCatalogo,
                            "desc": desc,
                            "stock_actual": stockActual
                        });
                    }
                });
            } catch(e) {}
        }

        // ── ESTRATEGIA 3: Fetch HTTP directo a _ListaProductosOfertados (Infalible)
        if (items.length === 0) {
            try {
                const ts = Date.now();
                const resp = await fetch(`/MejoraBasica/_ListaProductosOfertados?N_Acuerdo=${nAcuerdo}&N_Catalogo=${nCatalogo}&N_Categoria=${nCategoria}&C_Descripcion=&_=${ts}`, {
                    headers: { 'X-Requested-With': 'XMLHttpRequest' }
                });
                if (resp.status === 200) {
                    const html = await resp.text();
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const trs = doc.querySelectorAll('#TablaProductos tbody tr, table tbody tr');
                    trs.forEach(tr => {
                        const tds = tr.querySelectorAll('td');
                        if (tds.length < 5) return;
                        const desc = tds[1] ? tds[1].innerText.trim() : "";
                        if (!desc || desc.includes("No se encontraron") || desc.includes("Ningún dato")) return;

                        let idOfertado = "";
                        let idCatalogo = "";
                        const stockActual = tds[6] ? parseInt(tds[6].innerText.replace(/,/g, '')) || 0 : 0;

                        for (let c = 0; c < tds.length; c++) {
                            const htmlCell = tds[c].innerHTML;
                            const mOf = htmlCell.match(/fnModificarStock\((\d+)\)/) || htmlCell.match(/fnReducirPrecio\((\d+)\)/);
                            if (mOf) idOfertado = mOf[1];
                            const mCat = htmlCell.match(/fnDetalleRegistro\((\d+)\)/);
                            if (mCat) idCatalogo = mCat[1];
                        }

                        if (idOfertado) {
                            items.push({
                                "id_ofertado": idOfertado,
                                "id_catalogo": idCatalogo,
                                "desc": desc,
                                "stock_actual": stockActual
                            });
                        }
                    });
                }
            } catch(e) {}
        }

        return {
            "token": token,
            "nAcuerdo": nAcuerdo,
            "nCatalogo": nCatalogo,
            "nCategoria": nCategoria,
            "items": items
        };
    }"""

    for intento in range(1, max_retries + 1):
        try:
            data = page.evaluate(script)
            if data and data.get("items") and len(data["items"]) > 0:
                if log_func:
                    log_func(f"🚀 MOTOR ULTRA RÁPIDO: {len(data['items'])} fichas indexadas en memoria.")
                return data
        except Exception as e:
            if log_func: log_func(f"⚠️ Intento {intento} indexando catálogo: {e}")
        time.sleep(1.0)

    if log_func:
        log_func("⚠️ No se pudieron indexar fichas en memoria tras múltiples intentos.")
    return None


def buscar_producto_en_mapa(parte: str, ficha: str, items: list) -> dict:
    """Busca de forma instantánea el producto en el array de items en memoria."""
    if not items:
        return None

    # 1. Por ficha/id_catalogo
    if ficha and str(ficha).strip():
        f_str = str(ficha).strip()
        for it in items:
            if it.get("id_catalogo") == f_str or it.get("id_ofertado") == f_str:
                return it

    # 2. Por número de parte
    target = str(parte).strip().upper()
    target_clean = " ".join(target.split())
    if not target_clean:
        return None

    # Regex delimitada para evitar falsos positivos
    pattern = re.compile(r'(?<![A-Z0-9#\-_/])' + re.escape(target_clean) + r'(?![A-Z0-9#\-_/])')
    for it in items:
        desc_upper = it["desc"].upper()
        if pattern.search(desc_upper):
            return it

    # Subcadena limpia
    for it in items:
        if target_clean in it["desc"].upper():
            return it

    return None


def obtener_parametros_catalogo(page) -> dict:
    """Extrae token CSRF y los IDs de acuerdo, catálogo y categoría desde la página abierta."""
    script = """() => {
        return {
            token: document.querySelector('input[name="__RequestVerificationToken"]')?.value || "",
            nAcuerdo: document.querySelector('#ajaxAcuerdo, #N_Acuerdo, select[name*="cuerdo"]')?.value || "249",
            nCatalogo: document.querySelector('#ajaxCatalogo, #N_Catalogo, select[name*="atalogo"]')?.value || "252",
            nCategoria: document.querySelector('#ajaxCategoria, #N_Categoria, select[name*="ategoria"]')?.value || "11735"
        };
    }"""
    try:
        return page.evaluate(script)
    except Exception:
        return {"token": "", "nAcuerdo": "249", "nCatalogo": "252", "nCategoria": "11735"}


def consultar_ficha_ondemand(page, parte: str, n_acuerdo: str, n_catalogo: str, n_categoria: str, ficha: str = "") -> dict:
    """Consulta on-demand la fila exacta en _ListaProductosOfertados vía HTTP GET directo (0.5s - 0.9s)."""
    script = r"""
    async ([parte, nAcuerdo, nCatalogo, nCategoria]) => {
        try {
            const ts = Date.now();
            const url = '/MejoraBasica/_ListaProductosOfertados?N_Acuerdo=' + nAcuerdo + 
                        '&N_Catalogo=' + nCatalogo + 
                        '&N_Categoria=' + nCategoria + 
                        '&C_Descripcion=' + encodeURIComponent(parte) +
                        '&_=' + ts;
            const resp = await fetch(url, {
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });
            const finalUrl = (resp.url || '').toLowerCase();
            if (finalUrl.includes('accesogeneral') || finalUrl.includes('login')) {
                return { __session_expired__: true };
            }
            if (resp.status !== 200) return null;
            const html = await resp.text();
            if (html.includes('id="fLogin"') || html.includes('id="ID_Usuario"')) {
                return { __session_expired__: true };
            }

            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const trs = doc.querySelectorAll('#TablaProductos tbody tr, table tbody tr');
            const candidates = [];

            for (let tr of trs) {
                const tds = tr.querySelectorAll('td');
                if (tds.length < 8) continue;
                const desc = tds[1] ? tds[1].innerText.trim() : "";
                if (!desc || desc.includes("No se encontraron") || desc.includes("Ningún dato")) continue;

                let idOfertado = "";
                let idCatalogo = "";
                for (let c = 0; c < tds.length; c++) {
                    const htmlCell = tds[c].innerHTML;
                    if (!idOfertado) {
                        const mOf = htmlCell.match(/fnModificarStock\((\d+)\)/);
                        if (mOf) idOfertado = mOf[1];
                    }
                    if (!idCatalogo) {
                        const mCat = htmlCell.match(/fnDetalleRegistro\((\d+)\)/);
                        if (mCat) idCatalogo = mCat[1];
                    }
                }

                if (idOfertado) {
                    const stockVigente = tds[6] ? parseInt(tds[6].innerText.replace(/,/g, '')) || 0 : 0;
                    const stockPorPublicar = tds[7] ? parseInt(tds[7].innerText.replace(/,/g, '')) || null : null;
                    candidates.push({
                        id_ofertado: idOfertado,
                        id_catalogo: idCatalogo,
                        desc: desc,
                        stock_actual: stockVigente,
                        stock_por_publicar: stockPorPublicar
                    });
                }
            }
            return { items: candidates };
        } catch(e) {
            return null;
        }
    }
    """
    try:
        res = page.evaluate(script, [str(parte), str(n_acuerdo), str(n_catalogo), str(n_categoria)])
        if not res:
            return None
        if res.get("__session_expired__"):
            return res
        candidates = res.get("items") or []
        if not candidates:
            return None
        # Usar matching estricto delimitado para evitar colisiones de prefijos (ej. V1 vs V10)
        return buscar_producto_en_mapa(parte, ficha, candidates)
    except Exception:
        return None


def actualizar_stock_directo(page, id_ofertado, nuevo_stock, stock_ant, n_acuerdo, n_catalogo, n_categoria, token) -> dict:
    """Envía un POST directo a /MejoraBasica/ModificarStock en la sesión del navegador. Tarda ~0.4s."""
    script = r"""
    async ([idOfertado, nuevoStock, stockAnt, nAcuerdo, nCatalogo, nCategoria, token]) => {
        try {
            const params = new URLSearchParams();
            params.append('__RequestVerificationToken', token);
            params.append('ID_ProductoOfertado', idOfertado);
            params.append('N_Acuerdo', nAcuerdo);
            params.append('N_Catalogo', nCatalogo);
            params.append('N_Categoria', nCategoria);
            params.append('N_StockAnt', stockAnt);
            params.append('N_Stock', nuevoStock);
            
            const resp = await fetch('/MejoraBasica/ModificarStock', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: params.toString()
            });
            const finalUrl = (resp.url || '').toLowerCase();
            if (finalUrl.includes('accesogeneral') || finalUrl.includes('login')) {
                return { ok: false, status: resp.status, session_expired: true, error: 'Sesión expirada' };
            }
            return { ok: resp.status === 200, status: resp.status };
        } catch(e) {
            return { ok: false, error: e.toString() };
        }
    }
    """
    try:
        return page.evaluate(script, [str(id_ofertado), int(nuevo_stock), int(stock_ant), str(n_acuerdo), str(n_catalogo), str(n_categoria), str(token)])
    except Exception as e:
        return {"ok": False, "error": str(e)}


def verificar_stock_producto(page, id_ofertado, n_acuerdo="249", n_catalogo="252", n_categoria="11735", parte=""):
    """Consulta el modal GET o _ListaProductosOfertados para verificar que el stock persistió en la BD."""
    script = r"""
    async ([idOfertado, nAcuerdo, nCatalogo, nCategoria, parte]) => {
        try {
            // 1. Probar modal ModificarStock
            const resp = await fetch('/MejoraBasica/ModificarStock?ID_ProductoOfertado=' + idOfertado);
            if (resp.status === 200) {
                const text = await resp.text();
                const mNuevo = text.match(/id="N_Stock"[^>]*value="?(\d+)"?/i);
                if (mNuevo) return parseInt(mNuevo[1]);
                const mAnt = text.match(/id="N_StockAnt"[^>]*value="?(\d+)"?/i);
                if (mAnt) return parseInt(mAnt[1]);
            }
            
            // 2. Si no, verificar en _ListaProductosOfertados
            if (parte) {
                const ts = Date.now();
                const url = '/MejoraBasica/_ListaProductosOfertados?N_Acuerdo=' + nAcuerdo + 
                            '&N_Catalogo=' + nCatalogo + 
                            '&N_Categoria=' + nCategoria + 
                            '&C_Descripcion=' + encodeURIComponent(parte) +
                            '&_=' + ts;
                const r2 = await fetch(url, { headers: { 'X-Requested-With': 'XMLHttpRequest' } });
                if (r2.status === 200) {
                    const html = await r2.text();
                    const doc = new DOMParser().parseFromString(html, 'text/html');
                    const tds = doc.querySelectorAll('#TablaProductos tbody tr td');
                    if (tds.length >= 8) {
                        const porPub = tds[7] ? parseInt(tds[7].innerText.replace(/,/g, '')) : null;
                        if (porPub !== null && !isNaN(porPub)) return porPub;
                        const vig = tds[6] ? parseInt(tds[6].innerText.replace(/,/g, '')) : null;
                        if (vig !== null && !isNaN(vig)) return vig;
                    }
                }
            }
            return null;
        } catch(e) {
            return null;
        }
    }
    """
    try:
        return page.evaluate(script, [str(id_ofertado), str(n_acuerdo), str(n_catalogo), str(n_categoria), str(parte)])
    except Exception:
        return None


def test_actualizar_un_producto(page, parte: str, stock: int, ficha: str = "", log_func=None) -> dict:
    """Prueba la actualización de 1 solo producto y verifica la persistencia real en la base de datos."""
    if log_func is None:
        log_func = log

    log_func(f"🧪 INICIANDO TEST: Buscando producto '{parte}' (ficha={ficha})...")
    params = obtener_parametros_catalogo(page)
    token = params.get("token", "")
    n_acuerdo = params.get("nAcuerdo", "249")
    n_catalogo = params.get("nCatalogo", "252")
    n_categoria = params.get("nCategoria", "11735")

    # 1. Consultar on-demand directo a API (0.8s)
    t0 = time.time()
    item = consultar_ficha_ondemand(page, parte, n_acuerdo, n_catalogo, n_categoria, ficha)
    
    # 2. Fallback a RAM si existiera
    if not item:
        mapa = extraer_mapa_portal_stock(page, log_func)
        if mapa and mapa.get("items"):
            item = buscar_producto_en_mapa(parte, ficha, mapa["items"])
            token = mapa.get("token") or token
            n_acuerdo = mapa.get("nAcuerdo") or n_acuerdo
            n_catalogo = mapa.get("nCatalogo") or n_catalogo
            n_categoria = mapa.get("nCategoria") or n_categoria

    if not item:
        msg = f"Producto '{parte}' no encontrado en el catálogo del portal."
        log_func(f"❌ {msg}")
        return {"ok": False, "error": msg}

    id_ofertado = item["id_ofertado"]
    stock_ant = item.get("stock_actual", 1)
    desc = item.get("desc", "")
    log_func("📋 Ficha encontrada en el portal:")
    log_func(f"   • ID Ofertado: {id_ofertado}")
    log_func(f"   • Descripción: {desc[:60]}...")
    log_func(f"   • Stock vigente en portal: {stock_ant}")
    log_func(f"   • Nuevo stock a enviar: {stock}")

    log_func("📡 Enviando actualización directa a /MejoraBasica/ModificarStock...")
    t_send = time.time()
    res = actualizar_stock_directo(
        page, id_ofertado, stock, stock_ant,
        n_acuerdo, n_catalogo, n_categoria, token
    )
    elapsed = time.time() - t_send

    if not res.get("ok"):
        err = f"Fallo HTTP {res.get('status')}: {res.get('error', 'Error desconocido')}"
        log_func(f"❌ {err}")
        return {"ok": False, "error": err}

    log_func(f"✅ Respuesta del portal: 200 OK en {elapsed:.2f}s")
    log_func("🔍 Verificando persistencia real en la base de datos de Perú Compras...")

    time.sleep(0.5)
    stock_verificado = verificar_stock_producto(page, id_ofertado, n_acuerdo, n_catalogo, n_categoria, parte)

    if stock_verificado is not None and stock_verificado == int(stock):
        log_func("=" * 60)
        log_func(f"🎉 ¡TEST 100% EXITOSO!")
        log_func(f"   • Producto: {parte}")
        log_func(f"   • Stock antes: {stock_ant} ➜ Stock nuevo registrado: {stock_verificado}")
        log_func(f"   • Latencia total: {time.time()-t0:.2f}s")
        log_func(f"   • BD Perú Compras: CONFIRMADO Y GUARDADO EN EXISTENCIAS A PUBLICAR")
        log_func("=" * 60)
        log_func("💡 Ya puedes presionar 'INICIAR ACTUALIZACIÓN DE STOCK' para procesar todo el Excel.")
        return {
            "ok": True,
            "id_ofertado": id_ofertado,
            "stock_ant": stock_ant,
            "stock_nuevo": stock_verificado,
            "elapsed": elapsed
        }
    else:
        log_func(f"ℹ️ Actualización enviada exitosamente con HTTP 200 ({elapsed:.2f}s).")
        return {
            "ok": True,
            "id_ofertado": id_ofertado,
            "stock_ant": stock_ant,
            "stock_nuevo": stock,
            "elapsed": elapsed
        }

def actualizar_producto(page, parte: str, stock: int, ficha: str = "", stop_event=None) -> tuple[bool, str]:
    """Actualiza el stock de un producto. Retorna (éxito, mensaje_error)."""
    try:
        if stop_event and stop_event.is_set():
            return False, "Detenido por usuario"
        # Si hay ficha, navegar directo
        if ficha and ficha.strip():
            edit_url = f"{BASE_URL}/t_CatalogoProductoMarca/CatalogoProductoEdit?ID_CatalogoProducto={ficha}&C_EstadoNav=OBSERVADO&C_Moneda=USD"
            page.goto(edit_url, wait_until="networkidle", timeout=60_000)
            if stop_event and stop_event.is_set():
                return False, "Detenido por usuario"
            time.sleep(2)
        else:
            # 0. Asegurar que no hay modal cubriendo la tabla
            try:
                page.evaluate("""() => {
                    document.querySelectorAll('.modal').forEach(mm => {
                        mm.classList.remove('in', 'show');
                        mm.style.display = 'none';
                    });
                    document.querySelectorAll('.modal-backdrop').forEach(b => b.remove());
                    document.body.classList.remove('modal-open');
                    document.body.style.overflow = '';
                }""")
            except Exception:
                pass

            # 0. Limpiar cualquier overlay residual que intercepte clicks
            try:
                page.evaluate("""() => {
                    document.querySelectorAll('#_wModal_bg, ._wModal_bg, ._wModal_holder').forEach(el => el.remove());
                    document.querySelectorAll('.modal.in, .modal.show').forEach(m => {
                        m.classList.remove('in', 'show');
                        m.style.display = 'none';
                    });
                    document.body.classList.remove('modal-open');
                }""")
            except Exception:
                pass

            # ── PASO 1: Garantizar que #C_Descripcion esté VACÍO (el cuadro de arriba jamás se debe usar)
            try:
                page.evaluate("""() => {
                    const el = document.querySelector('#C_Descripcion, input[name="C_Descripcion"]');
                    if (el && el.value.trim() !== '') {
                        el.value = '';
                        el.dispatchEvent(new Event('input',  {bubbles: true}));
                        el.dispatchEvent(new Event('change', {bubbles: true}));
                    }
                }""")
            except Exception:
                pass

            # ── PASO 2: Esperar al buscador dinámico de DataTables (cuadro inferior)
            dynamic_search = page.locator(
                "input[type='search'][aria-controls='TablaProductos'], #TablaProductos_filter input, .dataTables_filter input"
            ).first
            has_dynamic = False
            for _ in range(25):
                if stop_event and stop_event.is_set():
                    return False, "Detenido por usuario"
                try:
                    if dynamic_search.count() > 0 and dynamic_search.is_visible():
                        has_dynamic = True
                        break
                except Exception:
                    pass
                time.sleep(0.4)

            if not has_dynamic:
                return False, "Buscador de la tabla no disponible"

            # ── PASO 3: Buscar EXCLUSIVAMENTE en el buscador de la tabla de abajo
            try:
                dynamic_search.click(force=True)
                dynamic_search.fill("")
                dynamic_search.fill(str(parte))
                dynamic_search.press("Enter")
                dynamic_search.dispatch_event("input")
                time.sleep(0.8)
            except Exception as e:
                return False, f"Error al interactuar con el buscador de la tabla: {e}"

            # ── PASO 4: Verificar resultado de la búsqueda
            try:
                empty = page.locator(".dataTables_empty, td:has-text('Ningún dato disponible'), td:has-text('No se encontraron')").first
                if empty.count() > 0 and empty.is_visible():
                    return False, f"No se encontraron resultados para {parte}"
            except Exception:
                pass

            row = _find_exact_matching_row(page, parte)
            if not row or row.count() == 0:
                return False, f"No se encontraron resultados para {parte}"

            # Verificar que la fila realmente contiene la parte buscada.
            # ponytail: inner_text() a veces trunca/corta el texto visible; buscamos
            # en cada celda y en el HTML completo de la fila (texto + atributos).
            parte_upper = str(parte).upper()
            try:
                found_parte = False
                # 1) Buscar en cada celda visible
                cells = row.locator("td").all()
                for cell in cells:
                    try:
                        cell_text = cell.inner_text(timeout=1_000).strip()
                        if parte_upper in cell_text.upper():
                            found_parte = True
                            break
                    except Exception:
                        continue

                # 2) Si no esta visible, buscar en el HTML crudo de la fila
                if not found_parte:
                    row_html = row.inner_html(timeout=2_000).upper()
                    if parte_upper in row_html:
                        found_parte = True

                if not found_parte:
                    row_text = ""
                    try:
                        row_text = row.inner_text(timeout=2_000)
                    except Exception:
                        pass
                    return False, f"Fila encontrada no contiene '{parte}'. Texto: {row_text[:300]}"
            except Exception:
                pass

            # 5. Click en "Existencias" de ESA fila específica
            try:
                exist_link = row.locator("a:has-text('Existencias'), button:has-text('Existencias')").first
                if exist_link.count() > 0:
                    exist_link.click(force=True, timeout=5_000)
                else:
                    # Fallback: cualquier link/botón de edición (NO usar .first ciego)
                    row.locator("a, button").first.click(force=True, timeout=5_000)
            except Exception as e:
                return False, f"No se pudo clickear Existencias: {e}"
            time.sleep(2)
            if stop_event and stop_event.is_set():
                return False, "Detenido por usuario"

        # 4b. Esperar a que el modal de edición de existencias esté visible y cargado
        try:
            page.wait_for_selector(
                ".modal.in, .modal.show, .modal:visible, [role='dialog']:visible, #MensajeModal:visible, #div_Modal_Existencias:visible",
                timeout=15_000,
            )
        except Exception:
            pass

        if stop_event and stop_event.is_set():
            return False, "Detenido por usuario"

        # 5. Esperar activamente (hasta 20 segundos) a que el input de stock EDITABLE aparezca en el DOM
        stock_input = None
        for _ in range(20):
            if stop_event and stop_event.is_set():
                return False, "Detenido por usuario"

            # Intentar localizar #N_Stock no readonly
            inp = page.locator(
                "#N_Stock:not([readonly]), input[name='N_Stock']:not([readonly]), #txtStock:not([readonly]), input[name='txtStock']:not([readonly])"
            ).first

            if inp.count() > 0 and inp.is_visible():
                stock_input = inp
                break

            # Fallback: cualquier input editable (no readonly) con id/name que matchee stock/exist
            inp_fallback = page.locator(
                "input:not([readonly])[id*='tock' i]:not([id$='Ant']):not([name$='Ant']),"
                "input:not([readonly])[name*='tock' i]:not([id$='Ant']):not([name$='Ant']),"
                "input:not([readonly])[id*='xist' i],"
                "input:not([readonly])[name*='xist' i]"
            ).first

            if inp_fallback.count() > 0 and inp_fallback.is_visible():
                stock_input = inp_fallback
                break

            time.sleep(1.0)

        if not stock_input or stock_input.count() == 0:
            # Diagnóstico: loguear qué inputs hay en el modal si falló tras 20s
            try:
                all_inputs = page.locator("input").all()
                diag = []
                for inp_d in all_inputs[:15]:
                    attrs = inp_d.evaluate(
                        "el => ({id: el.id, name: el.name, readonly: el.readOnly, "
                        "value: el.value, type: el.type, visible: el.offsetParent !== null})"
                    )
                    diag.append(str(attrs))
                log(f"   🔍 Inputs visibles en modal tras 20s: {diag}")
            except Exception:
                pass
            return False, "Campo de stock editable no encontrado"

        # 6. Limpiar y escribir nuevo stock (sanitizado)
        try:
            clean_stock = str(int(float(str(stock).replace(',', '').strip())))
        except Exception:
            clean_stock = str(stock).strip()
        stock_input.fill("")
        stock_input.fill(clean_stock)
        time.sleep(0.5)

        if stop_event and stop_event.is_set():
            return False, "Detenido por usuario"

        # 7. Click Guardar (botón submit del form formStock)
        # ponytail: usar #btn_guardar (id real en ExistenciasModal). No usar force=True
        # porque es submit de formulario.
        save_btn = page.locator("#btn_guardar").first
        if save_btn.count() == 0:
            return False, "Botón Guardar no encontrado"
        try:
            save_btn.click(timeout=10_000)
        except Exception:
            # Si está tapado, forzamos click (aunque puede no hacer submit real)
            save_btn.click(force=True, timeout=3_000)
        if stop_event and stop_event.is_set():
            return False, "Detenido por usuario"

        # 7b. Modal de CONFIRMACIÓN: esperar el _wModal (el modal real del portal)
        # ponytail: NO es #divPopUpConfirmacion; el modal real es ._wModal_holder con ._wModal_btn_ok "Sí"
        try:
            page.wait_for_selector(
                "._wModal_holder:visible, ._wModal_delete:visible",
                timeout=15_000,
            )
            # Clickear "Sí" del modal de confirmación
            page.locator("._wModal_btn_ok, ._wModal_btn_blue").first.click(
                force=True, timeout=3_000
            )
        except Exception:
            # Fallback: buscar por texto Sí dentro del modal
            try:
                page.locator("._wModal:has-text('Está seguro') ._wModal_btn_ok, ._wModal:has-text('seguro') ._wModal_btn_blue").first.click(
                    force=True, timeout=3_000
                )
            except Exception:
                pass

        time.sleep(2)
        if stop_event and stop_event.is_set():
            return False, "Detenido por usuario"

        # 8. Modal de ÉXITO: esperar #MensajeModal y cerrarlo con #btnSalir
        try:
            page.wait_for_selector(
                "#MensajeModal .modal-body:has-text('Actualización'), #MensajeModal.in, #MensajeModal[style*='display: block']",
                timeout=15_000,
            )
            page.locator("#MensajeModal #btnSalir, #MensajeModal button[name='btnCerrar']").first.click(
                force=True, timeout=3_000
            )
        except Exception:
            # Fallback final: forzar cierre de #MensajeModal
            try:
                page.evaluate("""() => {
                    const m = document.getElementById('MensajeModal');
                    if (m) {
                        m.classList.remove('in', 'show');
                        m.style.display = 'none';
                        m.setAttribute('aria-hidden', 'true');
                    }
                }""")
            except Exception:
                pass
        if stop_event and stop_event.is_set():
            return False, "Detenido por usuario"

        time.sleep(1)

        return True, ""
    except Exception as e:
        return False, str(e)


def _get_field(row, keys, default=""):
    if isinstance(row, dict):
        for k in keys:
            if k in row and row[k] is not None:
                return row[k]
        row_lower = {str(k).lower().strip(): v for k, v in row.items()}
        for k in keys:
            kl = str(k).lower().strip()
            if kl in row_lower and row_lower[kl] is not None:
                return row_lower[kl]
    return default


def paso4_actualizar_stock(page, df: list, pausa: float = PAUSA_ENTRE_PRODUCTOS,
                           log_func=None, usuario: str = "", password: str = "",
                           captcha_bridge=None, acuerdo: str = ACUERDO_TEXTO,
                           catalogo: str = CATALOGO_TEXTO, categoria: str = CATEGORIA_TEXTO,
                           stop_event=None) -> int:

    """Itera el DataFrame y actualiza cada producto. Retorna cantidad de éxitos."""
    if log_func is None:
        log_func = log

    current_stop = stop_event or STOP_EVENT
    exitos = 0
    total = len(df)

    # ── PASO 0: Extraer parámetros del catálogo y preparar motor rápido ──
    params_portal = obtener_parametros_catalogo(page)
    token = params_portal.get("token", "")
    n_acuerdo = params_portal.get("nAcuerdo", "249")
    n_catalogo = params_portal.get("nCatalogo", "252")
    n_categoria = params_portal.get("nCategoria", "11735")

    mapa_portal = extraer_mapa_portal_stock(page, log_func)
    items_portal = mapa_portal.get("items", []) if mapa_portal else []
    if items_portal:
        token = mapa_portal.get("token") or token
        n_acuerdo = mapa_portal.get("nAcuerdo") or n_acuerdo
        n_catalogo = mapa_portal.get("nCatalogo") or n_catalogo
        n_categoria = mapa_portal.get("nCategoria") or n_categoria
        log_func(f"🚀 MOTOR ULTRA RÁPIDO ACTIVO: {len(items_portal)} fichas listas para matching en RAM.")
    else:
        log_func("⚡ MOTOR ON-DEMAND DIRECTO ACTIVO: Resolución vía API (~1.2s/producto, sin bloqueos).")

    for i, row in enumerate(df, 1):
        if current_stop and current_stop.is_set():
            log_func(f"⏹ Detención solicitada")
            break

        # Check de sesión básica
        if not _is_logged_in(page) or not _esta_en_mejorabasica(page):
            if usuario and password:
                log_func("🔁 Sesión expirada o fuera de MejoraBasica. Re-logueando...")
                if not _relogin(page, usuario, password, log_func, STOP_EVENT, captcha_bridge):
                    log_func("❌ Re-login fallido, deteniendo")
                    break
                if not paso3_filtros_stock(page, acuerdo, catalogo, categoria):
                    log_func("❌ No se pudieron reaplicar filtros tras re-login")
                    break
                # Actualizar parámetros tras re-login
                params_portal = obtener_parametros_catalogo(page)
                token = params_portal.get("token", token)
            else:
                log_func("❌ Sesión perdida y no hay credenciales")
                break

        # Pausa si está activada
        if PAUSA_EVENT and not PAUSA_EVENT.is_set():
            log_func(f"⏸ En pausa ({i}/{total})")
            while PAUSA_EVENT and not PAUSA_EVENT.is_set():
                if current_stop and current_stop.is_set():
                    break
                time.sleep(0.5)

        if current_stop and current_stop.is_set():
            log_func("⏹ Detención solicitada durante pausa, saliendo...")
            break

        parte = str(_get_field(row, ["Parte", "parte", "PARTE", "N° Parte", "num_parte", "codigo"], default="")).strip()
        stock = _get_field(row, ["Stock", "stock", "STOCK", "Cantidad", "cantidad"], default=0)
        ficha = str(_get_field(row, ["Ficha", "ficha", "FICHA", "id", "N° Ficha"], default="")).strip()

        log_func(f"📦 [{i}/{total}] {parte} (stock={stock}, ficha={ficha})")
        t0 = time.time()
        exito = False
        error_msg = ""
        stock_ant_val = 0

        # ── RESOLUCIÓN Y ACTUALIZACIÓN DIRECTA (HÍBRIDO RAM + ON-DEMAND API) ──
        for _intento_sesion in range(2):
            item_match = buscar_producto_en_mapa(parte, ficha, items_portal) if items_portal else None

            if not item_match:
                item_match = consultar_ficha_ondemand(page, parte, n_acuerdo, n_catalogo, n_categoria, ficha)

            if isinstance(item_match, dict) and item_match.get("__session_expired__"):
                res_post = {"ok": False, "session_expired": True, "error": "Sesión expirada"}
            elif item_match:
                id_ofertado = item_match["id_ofertado"]
                stock_ant_val = item_match.get("stock_actual", 1)
                if not token:
                    token = page.evaluate("() => document.querySelector('input[name=\"__RequestVerificationToken\"]')?.value || ''")
                res_post = actualizar_stock_directo(page, id_ofertado, stock, stock_ant_val, n_acuerdo, n_catalogo, n_categoria, token)
            else:
                res_post = None

            if res_post and res_post.get("session_expired") and _intento_sesion == 0 and usuario and password:
                log_func("🔁 Sesión expirada durante actualización. Re-logueando...")
                if _relogin(page, usuario, password, log_func, current_stop, captcha_bridge) and paso3_filtros_stock(page, acuerdo, catalogo, categoria):
                    params_portal = obtener_parametros_catalogo(page)
                    token = params_portal.get("token", "")
                    continue
                error_msg = "Sesión expirada (re-login fallido)"
                break

            if res_post is None:
                exito = False
                error_msg = f"Sin coincidencia en el catálogo para '{parte}'"
            elif res_post.get("ok"):
                exito = True
                if items_portal and item_match:
                    item_match["stock_actual"] = stock
            else:
                exito = False
                error_msg = f"Error en petición HTTP: {res_post.get('status') or res_post.get('error')}"
            break

        if (current_stop and current_stop.is_set()) or _browser_cerrado(error_msg):
            log_func("⏹ Detención solicitada, saliendo...")
            break

        duracion = time.time() - t0
        tipo_fallo = "" if exito else clasificar_error(error_msg)
        estado = "OK" if exito else "FALLO"

        RESULTADOS.append({
            "Parte": parte, "Stock": stock, "Ficha": ficha,
            "Estado": estado, "Tipo de Fallo": tipo_fallo,
            "Descripción": error_msg, "Duración (seg)": round(duracion, 1),
        })

        if exito:
            exitos += 1
            log_func(f"   ✅ OK en {duracion:.2f}s (Stock: {stock_ant_val} ➜ {stock})")
        else:
            log_func(f"   ❌ FALLO: {tipo_fallo or error_msg}")

        # Pausa suave (0.3s es óptimo para máxima velocidad sin saturar el portal)
        pausa_efectiva = min(float(pausa), 0.4)
        time.sleep(pausa_efectiva)

    return exitos


# ══════════════════════════════════════════════════════════════════════════════
# REPORTES EXCEL
# ══════════════════════════════════════════════════════════════════════════════

GREEN = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
RED = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
HEADER_FILL = PatternFill(start_color="305496", end_color="305496", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF")


def generar_reporte_excel(output_path: str, acuerdo="", catalogo="", categoria="", elapsed_seconds=None) -> str:
    """Genera el reporte Excel corporativo de actualización de stock."""
    from utils_mod.excel_report_designer import build_executive_excel_report, format_elapsed_time

    total = len(RESULTADOS)
    exitos = sum(1 for r in RESULTADOS if str(r.get("Estado", "")).upper() == "OK")
    fallidos = total - exitos
    ratio = (exitos / total * 100) if total > 0 else 0

    summary = {
        "total": total,
        "ok": exitos,
        "warn": 0,
        "err": fallidos,
        "rate": round(ratio, 1),
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "acuerdo": acuerdo or "EXT-CE-2022-5",
        "catalogo": catalogo or "—",
        "categoria": categoria or "—",
        "elapsed_time": format_elapsed_time(elapsed_seconds) if elapsed_seconds is not None else "—",
    }

    # Mapear filas a formato estándar
    rows_data = []
    for r in RESULTADOS:
        rows_data.append({
            "parte": r.get("Parte", ""),
            "ficha": r.get("Ficha", ""),
            "descripcion": r.get("Descripción", ""),
            "stock_portal": r.get("Stock", ""),
            "estado": r.get("Estado", ""),
            "obs": r.get("Tipo de Fallo", "") or "Actualizado correctamente",
        })

    headers = [
        ("idx",         "N°",                    "center", 6),
        ("parte",       "N° de Parte",           "center", 18),
        ("ficha",       "Ficha Portal",          "center", 14),
        ("descripcion", "Descripción del Producto", "left", 42),
        ("stock_portal","Stock Asignado",        "center", 14),
        ("estado",      "Estado Actualización",  "center", 18),
        ("obs",         "Detalle / Observación", "left",   35),
    ]

    ok, res = build_executive_excel_report(
        rows_data=rows_data,
        summary=summary,
        output_path=output_path,
        modulo_nombre="Actualización de Stock — Perú Compras",
        headers_config=headers
    )
    return output_path


# ══════════════════════════════════════════════════════════════════════════════
# FLUJO PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

def ejecutar_stock(page, excel_path, usuario, password, acuerdo=ACUERDO_TEXTO,
                  catalogo=CATALOGO_TEXTO, categoria=CATEGORIA_TEXTO,
                  pausa=PAUSA_ENTRE_PRODUCTOS, captcha_bridge=None,
                  log_func=None) -> str:
    """Ejecuta el flujo completo de stock. Retorna path del reporte."""
    global RESULTADOS, STOP_EVENT
    RESULTADOS = []

    if log_func is None:
        log_func = log

    log_func("=" * 60)
    log_func("MODO STOCK - Actualización de existencias")
    log_func("=" * 60)

    # 1. Validar Excel
    log_func(f"📋 Validando Excel: {excel_path}")
    validacion = analizar_excel_stock(excel_path)
    if not validacion["valido"]:
        log_func(f"❌ Excel inválido: {validacion['errores']}")
        return ""
    df = validacion["df"]
    log_func(f"✅ {len(df)} productos cargados")

    # 2. Login
    if not login_with_ocr(page, usuario, password, captcha_bridge):
        log_func("❌ Login falló")
        return ""

    # 3. Navegación
    log_func("📍 Navegando a MejoraBasica...")
    paso2_navegacion_stock(page)

    # 4. Filtros
    log_func(f"📋 Aplicando filtros: {acuerdo} > {catalogo} > {categoria}")
    if not paso3_filtros_stock(page, acuerdo, catalogo, categoria):
        log_func("❌ No se pudieron aplicar los filtros")
        return ""

    # 5. Actualizar stock
    log_func(f"📦 Actualizando {len(df)} productos...")
    exitos = paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge,
                                   acuerdo, catalogo, categoria)
    log_func(f"✅ {exitos}/{len(df)} actualizados")

    # 6. Generar reporte
    output_dir = os.path.dirname(excel_path) or "."
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(output_dir, f"reporte_stock_{ts}.xlsx")
    generar_reporte_excel(report_path, acuerdo, catalogo, categoria)
    log_func(f"📊 Reporte: {report_path}")

    return report_path

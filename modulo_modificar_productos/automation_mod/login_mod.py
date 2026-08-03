"""
login_mod.py — Login en Peru Compras para el módulo de modificación de productos.

Reutiliza la lógica de OCR del CAPTCHA del proyecto principal (automation/login.py)
a través de imports relativos del sistema de archivos, SIN modificar ese archivo.

Si se ejecuta desde modulo_modificar_productos/ directamente, se asegura que
el path raíz del proyecto esté en sys.path para poder importar automation.login.
"""
import sys
import os
import time
import threading

from playwright.sync_api import Page

# ── Asegurar que el directorio raíz del proyecto esté en sys.path ──
# Así podemos reutilizar automation.login sin copiar el código
_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_MODULE_DIR, "..", ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from automation.login import do_login, LOGIN_URL  # noqa: E402 — reutilizamos el login existente

# URL del portal de gestión de productos del proveedor
# (diferente a t_ProductoOfertadoAmp que es el catálogo de precios)
# TODO: ajustar esta URL una vez identificada la sección correcta del portal
GESTION_PRODUCTOS_URL = "https://www.catalogos.perucompras.gob.pe/t_CatalogoProducto"


def login_y_navegar(
    page: Page,
    usuario: str,
    password: str,
    log,
    stop_event: threading.Event,
    captcha_bridge=None,
) -> bool:
    """
    Hace login en Peru Compras y navega a la sección de gestión de productos.
    Retorna True si todo OK, False si falla.

    Reutiliza do_login() del proyecto principal (misma URL de login, mismo CAPTCHA).
    La diferencia es la cuenta (usuario/password diferentes) y la URL de destino.
    """
    log.info("=== Módulo Modificar Productos: iniciando login ===")
    log.info(f"Usuario: {usuario}")

    # do_login navega a t_ProductoOfertadoAmp por defecto después del login.
    # Para este módulo lo dejamos así y luego re-navegamos a la sección correcta.
    ok = do_login(
        page=page,
        usuario=usuario,
        password=password,
        captcha_key=None,
        log=log,
        stop_event=stop_event,
        captcha_bridge=captcha_bridge,
    )

    if not ok:
        log.error("Login fallido. Abortando.")
        return False

    log.ok("Login exitoso.")

    # Navegar a la sección de gestión de productos
    log.info(f"Navegando a gestión de productos: {GESTION_PRODUCTOS_URL}")
    try:
        page.goto(GESTION_PRODUCTOS_URL, wait_until="networkidle", timeout=30_000)
        time.sleep(2)
        log.ok(f"En: {page.url}")
        return True
    except Exception as e:
        log.error(f"Error navegando a gestión de productos: {e}")
        log.warn("Continuando desde la posición actual...")
        return True  # Login OK aunque la nav falle — se puede manejar luego

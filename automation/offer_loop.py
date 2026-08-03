"""
Offer Loop — Subida de precios.

Estrategia principal: bulk upload vía HTTP directo (automation/bulk_upload.py).
Fallback 1x1 con Playwright para filas individuales si es necesario.

Velocidad estimada bulk: ~500-1000 productos/minuto.
"""
import time
import threading

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeout
from utils.logger import LogWriter
from automation import login as login_mod
from automation import navigation as nav_mod
from automation.bulk_upload import process_bulk_upload

BATCH_SIZE = 50


def _safe_wait_networkidle(page, log, timeout=60_000):
    try:
        page.wait_for_load_state("networkidle", timeout=timeout)
    except PlaywrightTimeout:
        log.warn("[net] Servidor lento, continuando...")
    except Exception:
        pass


def _dismiss_confirm_modal(page: Page):
    """Cierra el modal de confirmacion tras enviar ofertas."""
    time.sleep(1.5)
    try:
        page.evaluate("""
            if (typeof ocultarMensajeCantidadUnidadesPresentacion === 'function') ocultarMensajeCantidadUnidadesPresentacion();
            document.querySelectorAll('.modal-backdrop,.modal.open,.modal.show,.swal2-container,#MensajeModal2,.sweet-alert,._wModal,._wModal_delete,#_wModal_bg').forEach(el=>el.remove());
            document.body.style.overflow='';
            document.body.classList.remove('modal-open');
            document.body.style.paddingRight='';
        """)
        sel = "._wModal_btn_ok, ._wModal_close, ._wModal_btn_cancel, .swal2-confirm, .swal2-close, button.swal2-confirm, #MensajeModal2 button[data-dismiss='modal'], .modal button[data-dismiss='modal'], .modal .close, #MensajeModal2 .close, #btnSalir, button:has-text('Aceptar'), button:has-text('OK'), button:has-text('Cerrar'), a:has-text('Cerrar')"
        el = page.locator(sel).first
        if el.count() > 0 and el.is_visible(timeout=2000):
            el.click(force=True)
    except Exception:
        pass
    time.sleep(0.5)


def _dismiss_price_modal(page):
    modal = page.locator("#MensajeModal2")
    if modal.count() > 0 and modal.is_visible():
        msg = page.locator("#Msg").inner_text().strip()
        try:
            btn = page.locator("#MensajeModal2 button[data-dismiss='modal']").last
            if btn.count() > 0 and btn.is_visible():
                btn.click(force=True)
            else:
                page.locator("#MensajeModal2 .close").first.click(force=True)
        except Exception:
            page.evaluate("$('#MensajeModal2').modal('hide')")
        time.sleep(1.5)
        page.evaluate("""
            document.querySelectorAll('.modal-backdrop').forEach(el=>el.remove());
            document.body.classList.remove('modal-open');
            document.body.style.overflow='';
            document.body.style.paddingRight='';
        """)
        time.sleep(0.5)
        return msg
    return None


def run_offer_loop(
    page: Page,
    rows: list[dict],
    parte_col: str,
    precio_col: str,
    log: LogWriter,
    stop_event: threading.Event,
    credentials: dict,
    captcha_key: str,
    credenciales_rus: str,
    credenciales_pass: str,
    captcha_bridge=None,
    catalog_bridge=None,
    pre_selected=None,
):
    """
    Procesa ofertas en MASA vía HTTP directo (bulk upload).
    Mantiene la misma firma para compatibilidad con _execute().

    Returns: list[dict] con status por fila (index, status, parte, precio, ...)
    """
    # Verificar sesión activa
    current_url = page.url
    if "AccesoGeneral" in current_url:
        log.info("Sesion expirada, re-autenticando...")
        success = login_mod.do_login(
            page, credenciales_rus, credenciales_pass,
            captcha_key, log, stop_event,
            captcha_bridge=captcha_bridge,
        )
        if not success:
            log.error("Re-autenticacion fallida. Abortando.")
            return [{"index": i, "status": "error", "parte": str(r.get(parte_col, "")), "precio": str(r.get(precio_col, ""))}
                    for i, r in enumerate(rows)]

        nav_mod.setup_catalog_search(page, log, catalog_bridge, pre_selected=pre_selected)

    # ── BULK UPLOAD: enviar todo vía HTTP directo ──
    log.info("=" * 50)
    log.info("  MODO BULK UPLOAD — HTTP directo")
    log.info("=" * 50)

    results = process_bulk_upload(
        page, rows, parte_col, precio_col,
        log, stop_event, pre_selected,
    )

    if results is None:
        log.error("Bulk upload devolvio None, usando resultados vacios")
        results = []

    # Asegurar que cada resultado tenga index
    for i, r in enumerate(results):
        if "index" not in r:
            r["index"] = i

    # Contar resultados
    ok_count = sum(1 for r in results if r.get("status") == "ok")
    error_count = sum(1 for r in results if r.get("status") not in ("ok", "pendiente"))

    log.done(ok_count, error_count)
    log.info("Resumen: %d OK, %d errores de %d filas." % (ok_count, error_count, len(rows)))

    return results

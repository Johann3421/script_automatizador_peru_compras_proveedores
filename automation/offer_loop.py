import time
import threading

from playwright.sync_api import Page
from utils.logger import LogWriter
from automation import login as login_mod
from automation import navigation as nav_mod


def _dismiss_price_modal(page: Page) -> str | None:
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
            document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
            document.body.classList.remove('modal-open');
            document.body.style.overflow = '';
            document.body.style.paddingRight = '';
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
):
    ok_count = 0
    error_count = 0
    total = len(rows)
    results = []

    for i, row in enumerate(rows):
        if stop_event.is_set():
            log.info("Detencion solicitada por el usuario.")
            break

        current_url = page.url
        if "AccesoGeneral" in current_url and "CatalogoProductoIndex" not in current_url:
            log.info("Sesion expirada, re-autenticando...")
            success = login_mod.do_login(
                page, credenciales_rus, credenciales_pass,
                captcha_key, log, stop_event,
                captcha_bridge=captcha_bridge,
            )
            if not success:
                log.error("Re-autenticacion fallida. Abortando.")
                break
            nav_mod.setup_catalog_search(page, log, catalog_bridge)

        parte_val = str(row.get(parte_col) or "").strip()
        precio_val = str(row.get(precio_col) or "").strip()

        if not parte_val:
            log.error("Fila %d/%d: N° de Parte vacio, saltando." % (i + 1, total))
            error_count += 1
            results.append({"index": i, "status": "sin_part_number", "precio": precio_val})
            log.progress(i + 1, total)
            continue

        try:
            # 1. Buscar producto
            log.info("Fila %d/%d: Buscando '%s'..." % (i + 1, total, parte_val))
            search_input = page.locator("#C_Descripcion").first
            if search_input.count() == 0:
                log.error("No se encontro el campo #C_Descripcion.")
                error_count += 1
                results.append({"index": i, "status": "error_ui", "parte": parte_val, "precio": precio_val})
                log.progress(i + 1, total)
                continue

            search_input.click()
            search_input.fill("")
            search_input.fill(parte_val)
            time.sleep(0.3)

            if stop_event.is_set():
                break

            # 2. Click Buscar
            btn_buscar = page.locator("#btnBuscar").first
            if btn_buscar.count() == 0:
                log.error("No se encontro #btnBuscar en CatalogoProductoIndex.")
                error_count += 1
                results.append({"index": i, "status": "error_ui", "parte": parte_val, "precio": precio_val})
                log.progress(i + 1, total)
                continue

            btn_buscar.click(force=True)
            time.sleep(3)
            page.wait_for_load_state("networkidle", timeout=15000)
            time.sleep(1)

            if stop_event.is_set():
                break

            # 3. Verificar si hay resultados
            empty_msg = page.locator(".dataTables_empty").first
            if empty_msg.count() > 0 and empty_msg.is_visible(timeout=2000):
                log.warn("Fila %d/%d: '%s' no encontrado en el catalogo." % (i + 1, total, parte_val))
                error_count += 1
                results.append({"index": i, "status": "no_encontrado", "parte": parte_val, "precio": precio_val})
                log.progress(i + 1, total)
                time.sleep(0.5)
                continue

            # 4. Buscar el input de precio
            price_input = page.locator("input.cls_txtMonto").first
            if price_input.count() == 0:
                no_result = page.locator("td:has-text('No se encontraron'), .dataTables_empty").first
                if no_result.count() > 0 and no_result.is_visible(timeout=2000):
                    log.warn("Fila %d/%d: '%s' no encontrado." % (i + 1, total, parte_val))
                    results.append({"index": i, "status": "no_encontrado", "parte": parte_val, "precio": precio_val})
                else:
                    log.error("Fila %d/%d: No se encontro el campo de precio." % (i + 1, total))
                    results.append({"index": i, "status": "error_ui", "parte": parte_val, "precio": precio_val})
                error_count += 1
                log.progress(i + 1, total)
                time.sleep(1)
                continue

            # 5. Llenar precio
            price_input.click()
            price_input.fill("")
            price_input.fill(precio_val)
            time.sleep(0.8)

            # 6. Disparar validacion y verificar modal
            page.keyboard.press("Tab")
            time.sleep(2.5)

            modal_msg = _dismiss_price_modal(page)

            if modal_msg:
                if "excede" in modal_msg.lower() or "supera" in modal_msg.lower():
                    status = "excede"
                    color_info = "ROJO"
                elif "inferior" in modal_msg.lower() or "menor" in modal_msg.lower() or "minimo" in modal_msg.lower():
                    status = "inferior"
                    color_info = "AZUL"
                else:
                    try:
                        p = float(precio_val.replace(",", ""))
                    except ValueError:
                        p = 0
                    if p > 50000:
                        status = "excede"
                    elif p < 5:
                        status = "inferior"
                    else:
                        status = "fuera_rango"

                log.warn("Fila %d/%d: Precio S/. %s fuera de rango (%s)." % (
                    i + 1, total, precio_val, modal_msg[:60]))
                error_count += 1
                results.append({
                    "index": i, "status": status, "parte": parte_val,
                    "precio": precio_val, "modal_msg": modal_msg,
                })
                # Limpiar precio invalido
                price_input.click()
                price_input.fill("")
                time.sleep(0.3)
            else:
                log.ok("Fila %d/%d: '%s' = %s" % (i + 1, total, parte_val, precio_val))
                ok_count += 1
                results.append({
                    "index": i, "status": "ok", "parte": parte_val, "precio": precio_val,
                })

        except Exception as e:
            log.error("Fila %d/%d: Error procesando '%s' - %s" % (i + 1, total, parte_val, e))
            error_count += 1
            results.append({"index": i, "status": "error", "parte": parte_val, "precio": precio_val})

        log.progress(i + 1, total)
        if not stop_event.is_set():
            time.sleep(1.5)

    # 7. Click en "Enviar Oferta"
    if ok_count > 0 and not stop_event.is_set():
        log.info("Procesamiento finalizado. Click en 'Enviar Oferta'...")
        try:
            btn_enviar = page.locator("#btn_enviarOferta2").first
            if btn_enviar.count() > 0:
                btn_enviar.click(force=True)
                page.wait_for_load_state("networkidle", timeout=15000)
                time.sleep(2)
                log.ok("Oferta enviada correctamente.")
            else:
                log.error("No se encontro el boton #btn_enviarOferta2.")
        except Exception as e:
            log.error("Error al enviar oferta: %s" % e)

    log.done(ok_count, error_count)
    log.info("Resumen: %d OK, %d errores de %d filas." % (ok_count, error_count, total))
    return results

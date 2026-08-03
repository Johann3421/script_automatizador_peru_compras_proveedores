"""
bulk_modificar.py — Flujo masivo optimizado vía API + navegación directa.

Estrategia:
  1. Login una vez
  2. Buscar cada producto vía API (_CatalogoProductoIndex GET)
  3. Navegar DIRECTAMENTE a CatalogoProductoEdit?ID=XXXX (sin pasar por lista)
  4. Subir PDF + Guardar + cerrar modal
  5. Añadir ISO 9001 + ISO 14001
  6. Siguiente producto (goto edit URL directamente)
  7. Si la sesión expira: re-login automático y continuar

Ventaja: elimina la carga de la tabla de búsqueda y las interacciones
         de filtrar/buscar/retornar entre productos.
"""
import re
import time
import os
import threading

BASE_URL = "https://www.catalogos.perucompras.gob.pe"
URL_TABLA_API = f"{BASE_URL}/t_CatalogoProductoMarca/_CatalogoProductoIndex"
URL_EDIT = f"{BASE_URL}/t_CatalogoProductoMarca/CatalogoProductoEdit"
URL_LOGIN = f"{BASE_URL}/AccesoGeneral/Login"
PDF_DIR = r"D:\SISTEMAS 02\Downloads\COMPUTADORAS\COMPUTADORAS"
URL_MANAGEMENT = f"{BASE_URL}/t_CatalogoProductoMarca"


def buscar_producto_api(page, parte: str, catalogo: str, categoria: str, estado: str,
                        log, timeout: int = 30_000) -> dict | None:
    import time as _time
    url = (
        f"{URL_TABLA_API}"
        f"?N_Catalogo={catalogo}"
        f"&N_Categoria={categoria}"
        f"&C_Descripcion={parte}"
        f"&C_EstadoNav={estado}"
        f"&_={int(_time.time()*1000)}"
    )
    try:
        resp = page.request.get(url, timeout=timeout)
        html = resp.text()
        ids = re.findall(r"ID_CatalogoProducto=(\d+)", html)
        if ids:
            return {"id": ids[0], "descripcion": parte}
        try:
            import json as _json
            data = _json.loads(html)
            records = data.get("data", data.get("aaData", []))
            if records:
                r = records[0]
                nid = str(r.get("N_CatalogoProducto") or r.get("ID_CatalogoProducto", ""))
                if nid:
                    return {"id": nid, "descripcion": parte}
        except Exception:
            pass
    except Exception as e:
        log.warn(f"  API search error: {e}")
    return None


def _is_logged_in(page) -> bool:
    """Verifica si seguimos logueados mirando la URL actual."""
    try:
        url = page.url.lower()
        if "accesogeneral" in url or "login" in url:
            return False
        return True
    except Exception:
        return True


def _relogin(page, usuario: str, password: str, log, stop_event, captcha_bridge=None) -> bool:
    """Re-loguea y navega a la página de gestión."""
    log.warn("  Re-logueando...")
    try:
        from automation.login import do_login
        ok = do_login(page, usuario, password, "", log, stop_event, captcha_bridge)
        if not ok:
            return False
        log.ok("  Re-login exitoso")
        page.goto(URL_MANAGEMENT, wait_until="networkidle", timeout=60_000)
        time.sleep(2)
        return True
    except Exception as e:
        log.error(f"  Re-login falló: {e}")
        return False


def run_bulk_modificar(page, rows: list[dict], pre_selected: dict,
                        log, stop_event, captcha_bridge=None,
                        usuario: str = "", password: str = "") -> list[dict]:
    catalogo = pre_selected.get("catalogo", "252")
    categoria = pre_selected.get("categoria", "11735")
    estado = pre_selected.get("estado", "OBSERVADO")

    from automation_mod.navegacion_productos import (
        subir_pdf_en_edicion, guardar_cambios,
        agregar_caracteristicas, cerrar_modal_mensaje,
    )

    results = []
    total = len(rows)
    consec_fail = 0
    idx = 0

    while idx < total:
        if stop_event.is_set():
            break

        parte = rows[idx]["parte"]
        ruta_pdf = os.path.join(PDF_DIR, f"{parte}.pdf")
        log.info(f"[{idx+1}/{total}] {parte}")

        # ── Check session before each product ──
        if not _is_logged_in(page) or consec_fail >= 3:
            if usuario and password:
                if not _relogin(page, usuario, password, log, stop_event, captcha_bridge):
                    log.error("Re-login fallido, deteniendo")
                    break
                consec_fail = 0
            else:
                log.error("Sesión perdida y no hay credenciales para re-loguear")
                break

        # ── Cerrar modales colgados ──
        page.evaluate("""
            document.querySelectorAll('.modal-backdrop, .modal.open, .modal.show, #MensajeModal, #wm_caracteristicaNueva')
                .forEach(el => { try { el.remove(); } catch(e) {} });
            document.body.style.overflow = '';
            document.body.classList.remove('modal-open');
        """)

        # ── Buscar vía API ──
        prod = buscar_producto_api(page, parte, catalogo, categoria, estado, log)
        if not prod:
            log.warn(f"  ✗ No encontrado vía API: {parte}")
            results.append({"index": idx, "parte": parte, "status": "not_found"})
            consec_fail += 1
            idx += 1
            continue

        id_prod = prod["id"]
        log.info(f"  ID: {id_prod}")

        # ── Navegar directamente a edición ──
        edit_url = f"{URL_EDIT}?ID_CatalogoProducto={id_prod}&C_EstadoNav={estado}&C_Moneda=USD"
        try:
            page.goto(edit_url, wait_until="networkidle", timeout=60_000)
        except Exception:
            pass
        time.sleep(1.5)

        # Check if redirected to login
        if not _is_logged_in(page):
            log.warn("  Redirigido a login, sesión expirada")
            consec_fail = 3  # forzará re-login en próxima iteración
            results.append({"index": idx, "parte": parte, "status": "session_lost"})
            # No incrementar idx, se reintentará este producto
            continue

        # ── Subir PDF ──
        if not subir_pdf_en_edicion(page, ruta_pdf, log, stop_event):
            log.warn(f"  ✗ PDF no subido: {parte}")
            results.append({"index": idx, "parte": parte, "status": "pdf_failed"})
            consec_fail += 1
            idx += 1
            continue

        # ── Guardar ──
        if not guardar_cambios(page, log, stop_event):
            log.warn(f"  ✗ Error al guardar: {parte}")
            results.append({"index": idx, "parte": parte, "status": "save_failed"})
            consec_fail += 1
            idx += 1
            continue

        # ── Añadir ISOs ──
        try:
            cert_result = agregar_caracteristicas(page, log, stop_event)
            if cert_result.get("added"):
                log.info(f"  ISOs añadidas: {cert_result['added']}")
            if cert_result.get("skipped"):
                log.info(f"  ISOs ya existían: {cert_result['skipped']}")
            log.ok(f"  ✓ {parte} completado")
            results.append({"index": idx, "parte": parte, "status": "ok"})
            consec_fail = 0
        except Exception as e:
            log.error(f"  ✗ Error en ISOs: {e}")
            results.append({"index": idx, "parte": parte, "status": "certs_failed"})
            consec_fail += 1

        idx += 1

    return results

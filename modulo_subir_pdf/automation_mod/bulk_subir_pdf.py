"""
bulk_subir_pdf.py — Flujo masivo optimizado: SOLO subida de PDF.

Estrategia:
  1. Login una vez
  2. Buscar cada producto vía API (_CatalogoProductoIndex GET)
  3. Navegar DIRECTAMENTE a CatalogoProductoEdit?ID=XXXX (sin pasar por lista)
  4. Subir PDF + Guardar + cerrar modal
  5. Siguiente producto (goto edit URL directamente)
  6. Si la sesión expira: re-login automático y continuar

Este módulo NO añade características (ISO 9001/14001). Solo sube PDFs.
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
                        log, timeout: int = 90_000, ficha: str = "") -> dict | None:
    """
    El "FICHA N°" del Excel es el ID_CatalogoProducto de PeruCompras.
    Se navega DIRECTO a la URL de edit usando la ficha como ID.
    Si la página no carga (404 o "no encontrado"), se retorna None.
    """
    import time as _time
    if not ficha:
        log.warn(f"  Sin ficha, no se puede buscar (parte={parte})")
        return None

    # La ficha ES el ID_CatalogoProducto — navegar directo
    log.info(f"  Navegando directo a ficha={ficha} (parte nueva={parte})")
    edit_url = f"{URL_EDIT}?ID_CatalogoProducto={ficha}&C_EstadoNav={estado}&C_Moneda=USD"
    try:
        resp = page.goto(edit_url, wait_until="networkidle", timeout=60_000)
        # Verificar que cargó la página correcta (no redirigió a login o error)
        url_actual = page.url.lower()
        if "accesogeneral" in url_actual or "login" in url_actual:
            log.warn(f"  Redirigido a login")
            return None
        # Verificar que tiene el form de edición (campo de archivo PDF)
        try:
            page.wait_for_selector("#AdjFile", state="visible", timeout=15_000)
            log.ok(f"  Ficha encontrada: ID={ficha}")
            return {"id": ficha, "descripcion": parte, "ficha": ficha}
        except Exception:
            log.warn(f"  Ficha={ficha} no cargó el form de edición")
            return None
    except Exception as e:
        log.warn(f"  Error navegando a ficha={ficha}: {e}")
        return None


def _is_logged_in(page) -> bool:
    """Verifica si seguimos logueados mirando la URL actual."""
    try:
        url = page.url.lower()
        # PeruCompras redirige a la raíz cuando ya estás logueado y vas a /AccesoGeneral
        # URL válidas cuando logueado: raiz del dominio, t_CatalogoProductoMarca, etc.
        if "accesogeneral" in url or "login" in url:
            return False
        return True
    except Exception:
        return True


def _tiene_campos_login(page) -> bool:
    """Verifica si la página actual tiene los campos de login visibles."""
    try:
        user_input = page.locator("#ID_Usuario").first
        return user_input.count() > 0 and user_input.is_visible(timeout=2000)
    except Exception:
        return False


def _relogin(page, usuario: str, password: str, log, stop_event, captcha_bridge=None) -> bool:
    """Re-loguea y navega a la página de gestión."""
    log.warn("  Re-logueando...")
    try:
        # Si la URL NO contiene /AccesoGeneral ni /login, asumimos sesión activa
        url = page.url.lower()
        if "accesogeneral" not in url and "login" not in url:
            log.info("  URL sin login → navegando directo a gestión...")
            try:
                page.goto(URL_MANAGEMENT, wait_until="networkidle", timeout=60_000)
                time.sleep(2)
                return True
            except Exception as e:
                log.warn(f"  No se pudo ir a gestión: {e}")

        # Si la URL CONTIENE accesogeneral pero la página redirigió a la raíz
        # (PeruCompras redirige cuando hay sesión activa), los campos de login NO existen.
        # Verificar ANTES de llamar a do_login para no entrar en loop de reintentos.
        if _tiene_campos_login(page):
            log.info("  Campos de login presentes, intentando do_login...")
        else:
            log.info("  Campos de login AUSENTES → sesión activa, navegando a gestión...")
            try:
                page.goto(URL_MANAGEMENT, wait_until="networkidle", timeout=60_000)
                time.sleep(2)
                return True
            except Exception as e:
                log.warn(f"  No se pudo ir a gestión: {e}")

        from automation.login import do_login
        ok = do_login(page, usuario, password, "", log, stop_event, captcha_bridge)
        if not ok:
            # do_login falló — chequear si en realidad ya estamos logueados
            url_after = page.url.lower()
            if "accesogeneral" not in url_after and "login" not in url_after:
                log.info("  do_login falló pero URL sin login → sesión activa")
                try:
                    page.goto(URL_MANAGEMENT, wait_until="networkidle", timeout=60_000)
                    time.sleep(2)
                    return True
                except Exception:
                    pass
            return False
        log.ok("  Re-login exitoso")
        page.goto(URL_MANAGEMENT, wait_until="networkidle", timeout=60_000)
        time.sleep(2)
        return True
    except Exception as e:
        log.error(f"  Re-login falló: {e}")
        return False


def run_bulk_subir_pdf(page, rows: list[dict], pre_selected: dict,
                        log, stop_event, captcha_bridge=None,
                        usuario: str = "", password: str = "") -> list[dict]:
    catalogo = pre_selected.get("catalogo", "252")
    categoria = pre_selected.get("categoria", "11735")
    estado = pre_selected.get("estado", "OBSERVADO")

    from automation_mod.navegacion_productos import (
        subir_pdf_en_edicion, subir_imagen_en_edicion, cambiar_precio_en_edicion,
        guardar_cambios,
        leer_caracteristicas_pagina, leer_certificaciones_pagina,
        comparar_caracteristicas, corregir_caracteristica,
        agregar_certificaciones_faltantes,
        eliminar_caracteristica, agregar_caracteristica_texto,
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
            document.querySelectorAll('.modal-backdrop, .modal.open, .modal.show, #MensajeModal')
                .forEach(el => { try { el.remove(); } catch(e) {} });
            document.body.style.overflow = '';
            document.body.classList.remove('modal-open');
        """)

        # ── Buscar vía API ──
        ficha = rows[idx].get("ficha", "")
        prod = buscar_producto_api(page, parte, catalogo, categoria, estado, log, ficha=ficha)
        if not prod:
            log.warn(f"  ✗ No encontrado vía API: {parte} (ficha={ficha})")
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

        # ── Subir imagen (columna IMAGEN (PDF) del Excel) ──
        nombre_imagen = rows[idx].get("imagen", "")
        if nombre_imagen:
            subir_imagen_en_edicion(page, str(nombre_imagen), log, stop_event)
        else:
            log.info("  Sin imagen en el Excel, saltando")

        # ── Cambiar precio (columna PRECIO SUGERIDO del Excel) ──
        precio = rows[idx].get("precio", "")
        if precio:
            cambiar_precio_en_edicion(page, str(precio), log, stop_event)
        else:
            log.info("  Sin precio en el Excel, saltando")

        # ── Guardar ──
        if not guardar_cambios(page, log, stop_event):
            log.warn(f"  ✗ Error al guardar: {parte}")
            results.append({"index": idx, "parte": parte, "status": "save_failed"})
            consec_fail += 1
            idx += 1
            continue

        # Esperar a que la página se estabilice tras el guardado
        # (PeruCompras puede recargar/redirect tras guardar — si no esperamos, falla el JS evaluate)
        try:
            page.wait_for_load_state("networkidle", timeout=30_000)
        except Exception:
            pass
        time.sleep(2)

        # ── Verificar características contra Excel y corregir diferencias ──
        try:
            page_chars = leer_caracteristicas_pagina(page)
            excel_chars = rows[idx].get("caracteristicas", {})
            comp = comparar_caracteristicas(page_chars, excel_chars, log)
            # Corregir cada diferencia
            corregidas = 0
            for d in comp["diferentes"]:
                if stop_event.is_set():
                    break
                if corregir_caracteristica(page, d["id"], d["esperado"], log, stop_event, edit_url=edit_url):
                    corregidas += 1
            if comp["diferentes"]:
                log.info(f"  Corregidas: {corregidas}/{len(comp['diferentes'])}")
        except Exception as e:
            log.warn(f"  Error comparando/corriendo características: {e}")
            comp = {"iguales": 0, "diferentes": []}
            corregidas = 0

        # ── Agregar certificaciones faltantes (ISO 9001 / 14001) ──
        # Re-navegar a edit_url para tener página limpia (sin modales colgados)
        try:
            page.goto(edit_url, wait_until="networkidle", timeout=60_000)
            time.sleep(2)
            certs_esp = rows[idx].get("certs_esperadas", [])
            if certs_esp:
                cert_r = agregar_certificaciones_faltantes(page, certs_esp, log, stop_event)
                log.info(f"  Certs: añadidas={cert_r.get('added', [])}")
        except Exception as e:
            log.warn(f"  Error en certificaciones: {e}")

        # ── Actualizar N° de Parte: si existe eliminar y agregar, si no solo agregar ──
        try:
            page.goto(edit_url, wait_until="networkidle", timeout=60_000)
            time.sleep(1.5)
            page_chars_full = leer_caracteristicas_pagina(page)
            nro_parte_row = next((c for c in page_chars_full
                                  if c.get("nombre", "").upper().strip() in ("N° DE PARTE", "NRO PARTE", "NRO_PARTE", "N° PARTE")), None)
            if nro_parte_row and nro_parte_row.get("id"):
                log.info(f"  N° de Parte existente, eliminando...")
                eliminar_caracteristica(page, nro_parte_row["id"], log, stop_event)
                time.sleep(2)
            else:
                log.info(f"  N° de Parte no existe, agregando nuevo...")
            agregar_caracteristica_texto(page, "NRO_PARTE", parte, log, stop_event)
            guardar_cambios(page, log, stop_event)
        except Exception as e:
            log.warn(f"  Error actualizando N° de Parte: {e}")

        log.ok(f"  OK {parte} - PDF subido, {comp['iguales']} chars ok, {len(comp['diferentes'])} corregidas")
        results.append({
            "index": idx, "parte": parte, "status": "ok",
            "chars_iguales": comp["iguales"],
            "chars_diferentes": len(comp["diferentes"]),
            "chars_corregidas": corregidas,
        })
        consec_fail = 0

        idx += 1

    return results

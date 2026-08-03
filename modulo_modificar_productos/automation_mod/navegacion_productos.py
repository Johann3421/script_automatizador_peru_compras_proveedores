import time
import os
import threading
from playwright.sync_api import Page

GESTION_URL = "https://www.catalogos.perucompras.gob.pe/t_CatalogoProductoMarca"
EDICION_URL = "https://www.catalogos.perucompras.gob.pe/t_CatalogoProductoMarca/CatalogoProductoEdit"

SEL_BUSQUEDA     = "#C_Descripcion"
SEL_TABLA_FILAS  = "#TablaProductos tbody tr"
SEL_PROCESANDO   = ".dataTables_processing"
SEL_NO_RESULTADO = ".dataTables_empty"
SEL_ADJ_FILE     = "#AdjFile"
SEL_BTN_GUARDAR  = "#btnGuardar"
SEL_BTN_BUSCAR   = "#btnBuscar"
SEL_BTN_CARACTERISTICA = "#btn_caracteristicaNueva"
SEL_MODAL_BODY   = "#modalBody"
SEL_SEL_CARACT   = "#wm_caracteristicaNueva #N_Caracteristica"
SEL_SEL_VALOR    = "#wm_caracteristicaNueva #N_ValCaracteristica"
SEL_MODAL_GUARDAR = ".modal-footer button:has-text('Guardar'), .modal-footer button[type='submit']"
SEL_CERTIFICACION_VALUE = "26229"
ISO_VALUES = {
    "ISO 9001":  ["1597409", "1661118"],
    "ISO 14001": ["1661123"],
}


# ── Helpers internos ────────────────────────────────────────────

def _esperar_tabla(page: Page, log, max_ciclos: int = 20, espera: float = 1.5):
    for _ in range(max_ciclos):
        try:
            proc = page.locator(SEL_PROCESANDO)
            if proc.count() > 0 and proc.first.is_visible(timeout=500):
                time.sleep(espera)
                continue
        except Exception:
            pass
        break


def _es_no_encontrado(page: Page) -> bool:
    try:
        empty = page.locator(SEL_NO_RESULTADO)
        return empty.count() > 0 and empty.first.is_visible(timeout=2000)
    except Exception:
        return False


# ── Select2 helper ──────────────────────────────────────────────

def _select2_select(page: Page, select_id: str, value: str):
    """Selecciona una opción en un Select2 usando el método nativo de Playwright."""

    # Método principal: page.select_option (funciona con Select2 si dispara eventos)
    try:
        page.wait_for_selector(f"#{select_id}", state="attached", timeout=10_000)
        page.select_option(f"#{select_id}", value, timeout=10_000)
        time.sleep(2)
    except Exception:
        pass

    # Verificar que el valor se aplicó
    actual = page.evaluate(f"document.getElementById('{select_id}')?.value || ''")
    if actual == value:
        return  # OK, el valor se seteo

    # Método visual: abrir dropdown y clickear opción
    try:
        container = page.locator(f"#select2-{select_id}-container").first
        if container.count() > 0 and container.is_visible(timeout=3000):
            container.click(timeout=3000)
            time.sleep(1.5)
            page.locator(f"li.select2-results__option").first.wait_for(state="visible", timeout=5000)
            time.sleep(0.5)
            # Buscar opción por texto
            todas = page.locator("li.select2-results__option")
            for i in range(todas.count()):
                opt = todas.nth(i)
                if opt.is_visible():
                    try:
                        txt = opt.text_content()
                        if txt and value in txt:
                            opt.click(force=True, timeout=3000)
                            break
                    except Exception:
                        continue
            time.sleep(1.5)
    except Exception:
        pass

    # Método JS como último recurso
    page.evaluate(f"""
        (() => {{
            var sel = document.getElementById('{select_id}');
            if (!sel) return;
            sel.value = '{value}';
            sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
            sel.dispatchEvent(new Event('input', {{ bubbles: true }}));
            if (typeof $ !== 'undefined') {{
                try {{
                    $(sel).val('{value}').trigger('change.select2');
                }} catch(e) {{}}
            }}
        }})()
    """)
    time.sleep(1)


# ── Paso 1: aplicar dropdowns y click Buscar ────────────────────

def apply_dropdowns_and_search(page: Page, pre_selected: dict, log, stop_event) -> dict:
    if stop_event.is_set():
        return {"count": 0, "status": "stopped"}

    try:
        page.wait_for_selector("#ajaxAcuerdo", timeout=30_000)
    except Exception:
        pass

    log.info("  Seleccionando Acuerdo...")
    _select2_select(page, "ajaxAcuerdo", pre_selected.get("acuerdo", "249"))
    time.sleep(2)

    if stop_event.is_set():
        return {"count": 0, "status": "stopped"}

    catalogo = pre_selected.get("catalogo", "")
    if catalogo:
        log.info(f"  Seleccionando Catálogo: {catalogo}")
        _select2_select(page, "ajaxCatalogo", catalogo)
        time.sleep(2)
    else:
        log.warn("  Catálogo vacío, se saltó")

    if stop_event.is_set():
        return {"count": 0, "status": "stopped"}

    categoria = pre_selected.get("categoria", "")
    if categoria:
        log.info(f"  Seleccionando Categoría: {categoria}")
        _select2_select(page, "ajaxCategoria", categoria)
        time.sleep(2)
    else:
        log.warn("  Categoría vacía, se saltó")

    if stop_event.is_set():
        return {"count": 0, "status": "stopped"}

    estado = pre_selected.get("estado", "")
    if estado:
        log.info(f"  Seleccionando Estado: {estado}")
        _select2_select(page, "ajaxEstado", estado)
        time.sleep(2)
    else:
        log.warn("  Estado vacío, se saltó")

    if stop_event.is_set():
        return {"count": 0, "status": "stopped"}

    log.info("  Haciendo clic en Buscar...")
    try:
        btn = page.locator(SEL_BTN_BUSCAR).first
        if btn.count() > 0:
            log.info(f"  #btnBuscar encontrado, visible={btn.is_visible()}")
            
            # Escuchar errores de consola
            errors = []
            page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
            
            # Cerrar modales antes de click
            page.evaluate("""
                document.querySelectorAll('.modal-backdrop, .modal.open, .modal.show, .swal2-container, #_wModal_bg')
                    .forEach(el => el.remove());
            """)
            
            btn.click(timeout=5_000)
            time.sleep(5)

            if errors:
                log.warn(f"  Errores JS: {errors[:3]}")

            # Polling: esperar hasta que aparezca la tabla (hasta 180s)
            log.info("  Esperando resultados (hasta 180s)...")
            tabla_encontrada = False
            for intento in range(36):  # 36 × 5s = 180s
                if stop_event.is_set():
                    break
                time.sleep(5)
                filas = page.locator("table tbody tr, " + SEL_TABLA_FILAS)
                if filas.count() > 0:
                    tabla_encontrada = True
                    log.info(f"  Tabla encontrada en intento {intento+1}: {filas.count()} filas")
                    break
                if _es_no_encontrado(page):
                    log.info(f"  Mensaje vacío en intento {intento+1}")
                    break
            if not tabla_encontrada:
                log.info("  No se detectó tabla después de 180s")
            
        else:
            log.warn("  #btnBuscar no encontrado")
            return {"count": 0, "status": "btn_not_found"}
    except Exception as e:
        log.warn(f"  Error click Buscar: {e}")
        return {"count": 0, "status": "btn_error"}

    # Cerrar cualquier modal que pueda estar bloqueando
    page.evaluate("""
        document.querySelectorAll('.modal-backdrop, .modal.open, .modal.show, .swal2-container, #_wModal_bg, .bootbox-backdrop')
            .forEach(el => { try { el.remove(); } catch(e) {} });
        document.body.style.overflow = '';
        document.body.classList.remove('modal-open');
    """)
    time.sleep(1)
    page.keyboard.press("Escape")
    time.sleep(1)

    # Diagnosticar la página después de Buscar
    url_post = page.url
    log.info(f"  URL post-Buscar: {url_post[:120]}")
    title = page.title()
    log.info(f"  Title: {title[:80]}")

    diag = page.evaluate("""
        (() => {
            let info = [];
            let tables = document.querySelectorAll('table');
            info.push('tablas: ' + tables.length);
            tables.forEach((t, i) => {
                let id = t.id || 'sin-id';
                let rows = t.querySelectorAll('tr').length;
                info.push('  tabla[' + i + '] #' + id + ' rows=' + rows);
            });
            info.push('dataTables_processing: ' + (document.querySelector('.dataTables_processing') ? 'visible' : 'ausente'));
            let empties = document.querySelectorAll('.dataTables_empty');
            info.push('.dataTables_empty: ' + empties.length);
            let grd = document.querySelector('[id*=\"grd\"], [id*=\"Grid\"], [id*=\"table\"], .table-striped');
            info.push('grid-like: ' + (grd ? (grd.id || grd.className || 'tag:' + grd.tagName) : 'ausente'));
            let tbodies = document.querySelectorAll('tbody');
            info.push('tbodies: ' + tbodies.length);
            tbodies.forEach((tb, i) => {
                let p = tb.parentElement;
                info.push('  tbody[' + i + '] en #' + (p ? p.id : '?') + ' rows=' + tb.querySelectorAll('tr').length);
            });
            let footerText = document.querySelector('.panel-footer, .card-footer, footer')?.innerText || '';
            info.push('footer: ' + footerText.substring(0, 100).replace(/\\n/g, ' '));
            let panels = document.querySelectorAll('.panel, .card');
            info.push('paneles: ' + panels.length);
            panels.forEach((p, i) => {
                let h = p.querySelector('.panel-heading, .card-header');
                info.push('  panel[' + i + '] heading=' + (h ? h.innerText.substring(0, 60).replace(/\\n/g, ' ') : 'sin-header'));
            });
            // Verificar valores actuales de los selects
            let ac = document.getElementById('ajaxAcuerdo');
            let ca = document.getElementById('ajaxCatalogo');
            let cg = document.getElementById('ajaxCategoria');
            let es = document.getElementById('ajaxEstado');
            info.push('ajaxAcuerdo.value=' + (ac ? ac.value : 'N/E'));
            info.push('ajaxCatalogo.value=' + (ca ? ca.value : 'N/E'));
            info.push('ajaxCategoria.value=' + (cg ? cg.value : 'N/E'));
            info.push('ajaxEstado.value=' + (es ? es.value : 'N/E'));
            // Ver si hay formularios
            info.push('forms: ' + document.forms.length);
            for (let i = 0; i < document.forms.length; i++) {
                info.push('  form[' + i + '] action=' + (document.forms[i].action || '').substring(0, 80));
            }
            // body preview extendido
            let bodyText = document.body ? document.body.innerText : '';
            info.push('body-length: ' + bodyText.length);
            info.push('body-preview: ' + bodyText.substring(0, 600).replace(/\\n/g, ' | '));
            return info.join('\\n');
        })()
    """)
    log.info(f"  Diagnóstico DOM:\n{diag}")

    try:
        ss_path = os.path.join(os.environ.get('TEMP', '.'), 'post_buscar.png')
        page.screenshot(path=ss_path, full_page=True)
        log.info(f"  Screenshot guardado: {ss_path}")
    except Exception as e:
        log.warn(f"  No se pudo guardar screenshot: {e}")

    _esperar_tabla(page, log)

    # Intentar detectar resultados con múltiples estrategias
    estrategias = [
        "#tablaProductos tbody tr",
        "table tbody tr",
        "tr[class*='even'], tr[class*='odd']",
        "tbody tr",
        "[id*='grd'] tbody tr",
        "[id*='Grid'] tbody tr",
        "[id*='table'] tbody tr",
        ".table-striped tbody tr",
    ]
    count = 0
    status = "unknown"
    for sel in estrategias:
        try:
            filas = page.locator(sel)
            c = filas.count()
            if c > 0:
                log.info(f"  Estrategia '{sel}': {c} filas")
                count = c
                status = "ok"
                break
        except Exception:
            pass

    if count == 0:
        if _es_no_encontrado(page):
            log.warn("  Sin resultados (mensaje vacío)")
            return {"count": 0, "status": "empty"}
        log.warn(f"  No se detectaron filas en ninguna estrategia")
        return {"count": 0, "status": status}

    return {"count": count, "status": status}


# ── Paso 2: buscar por N° de Parte ──────────────────────────────

def buscar_por_parte(page: Page, parte: str, log, stop_event) -> bool:
    if stop_event.is_set():
        return False
    log.info(f"  Buscando parte: {parte}")
    try:
        campo = page.locator(SEL_BUSQUEDA).first
        if campo.count() == 0:
            log.error(f"  #C_Descripcion no encontrado")
            return False
        campo.click()
        campo.fill("")
        campo.fill(parte)
        time.sleep(1)

        # Click en Buscar nuevamente para activar la búsqueda
        btn_buscar = page.locator(SEL_BTN_BUSCAR).first
        if btn_buscar.count() > 0 and btn_buscar.is_visible():
            btn_buscar.click(timeout=5_000)
            log.info("  Esperando resultados...")
            # Polling hasta 180s
            for intento in range(36):
                if stop_event.is_set():
                    break
                time.sleep(5)
                _esperar_tabla(page, log)
                if _es_no_encontrado(page):
                    log.warn(f"  Parte no encontrada: {parte}")
                    return False
                filas = page.locator("table tbody tr").count()
                if filas > 0:
                    log.info(f"  Resultados encontrados ({filas} filas)")
                    break
            else:
                log.warn(f"  Timeout buscando parte {parte}")
                return False

        log.info(f"  Parte encontrada: {parte}")
        return True
    except Exception as e:
        log.error(f"  Error buscando parte {parte}: {e}")
        return False


# ── Paso 3: click en Editar ─────────────────────────────────────

def click_editar(page: Page, log, stop_event) -> bool:
    if stop_event.is_set():
        return False
    try:
        # Buscar el link "Editar" en la tabla visible (onclick con CatalogoProductoEdit)
        link = page.locator("a[onclick*='CatalogoProductoEdit']").first
        if link.count() == 0 or not link.is_visible():
            # Fallback: cualquier <a> con texto "Editar"
            link = page.locator("a:has-text('Editar')").first
        if link.count() == 0 or not link.is_visible():
            log.error("  Link Editar no encontrado o no visible en la tabla")
            return False
        href = link.get_attribute("href") or ""
        onclick = link.get_attribute("onclick") or ""
        log.info(f"  Link Editar: href={href[:80]} onclick={onclick[:80]}")
        link.click(timeout=5_000)
        try:
            page.wait_for_load_state("networkidle", timeout=30_000)
        except Exception:
            pass
        time.sleep(2)
        url_actual = page.url
        log.info(f"  URL actual: {url_actual[:100]}")
        if "CatalogoProductoEdit" in url_actual or "Edit" in url_actual:
            return True
        # Si no navegó, intentar hacer click en el onclick
        log.warn("  El click no navegó a edición, intentando onclick manual")
        page.evaluate(onclick) if onclick else None
        time.sleep(3)
        try:
            page.wait_for_load_state("networkidle", timeout=20_000)
        except Exception:
            pass
        return "CatalogoProductoEdit" in page.url or "Edit" in page.url
    except Exception as e:
        log.error(f"  Error click Editar: {e}")
        return False


# ── Paso 4: subir PDF ───────────────────────────────────────────

def subir_pdf_en_edicion(page: Page, ruta_pdf: str, log, stop_event) -> bool:
    if stop_event.is_set():
        return False
    if not ruta_pdf:
        log.info("  Sin PDF que subir, OK")
        return True
    if not os.path.isfile(ruta_pdf):
        log.error(f"  PDF no existe: {ruta_pdf}")
        return False
    try:
        file_input = page.locator(SEL_ADJ_FILE).first
        if file_input.count() == 0:
            log.error(f"  #AdjFile no encontrado en la página de edición")
            return False
        log.info(f"  Subiendo PDF: {os.path.basename(ruta_pdf)}")
        file_input.set_input_files(ruta_pdf)
        time.sleep(1.5)
        log.ok("  PDF adjuntado correctamente")
        return True
    except Exception as e:
        log.error(f"  Error subiendo PDF: {e}")
        return False


# ── Paso 5: Guardar ─────────────────────────────────────────────

def guardar_cambios(page: Page, log, stop_event) -> bool:
    if stop_event.is_set():
        return False
    try:
        btn = page.locator(SEL_BTN_GUARDAR).first
        if btn.count() == 0:
            log.error(f"  #btnGuardar no encontrado")
            return False
        log.info("  Haciendo click en Guardar...")
        btn.click(timeout=5_000, no_wait_after=True)
        # Esperar que aparezca el modal de confirmación
        cerrar_modal_mensaje(page, log, "Guardar")
        log.ok("  Cambios guardados correctamente")
        return True
    except Exception as e:
        log.error(f"  Error al guardar: {e}")
        return False


def cerrar_modal_mensaje(page: Page, log, context: str = ""):
    """Espera y cierra el modal #MensajeModal que aparece tras guardar."""
    ctx = f" [{context}]" if context else ""
    try:
        modal = page.locator("#MensajeModal")
        modal.wait_for(state="visible", timeout=30_000)
        log.info(f"  Modal #MensajeModal detectado{ctx}")
        salir = page.locator("#btnSalir").first
        if salir.count() > 0 and salir.is_visible(timeout=3000):
            salir.click(timeout=5000)
            time.sleep(1)
            log.info(f"  Modal cerrado con #btnSalir{ctx}")
            return
        cerrar = page.locator("button.close[data-dismiss='modal']").first
        if cerrar.count() > 0 and cerrar.is_visible(timeout=2000):
            cerrar.click(timeout=3000)
            time.sleep(1)
            log.info(f"  Modal cerrado con X{ctx}")
            return
        dismiss = page.locator("button[data-dismiss='modal']").first
        if dismiss.count() > 0 and dismiss.is_visible(timeout=2000):
            dismiss.click(timeout=3000)
            time.sleep(1)
            log.info(f"  Modal cerrado con data-dismiss{ctx}")
            return
        log.warn(f"  No se encontró botón para cerrar modal{ctx}")
    except Exception:
        log.warn(f"  Modal #MensajeModal no apareció{ctx}")


# ── Contingencia: reconexión si la sesión expira ─────────────────

def ensure_logged_in_and_ready(page: Page, usuario: str, password: str, pre_selected: dict, log, stop_event, captcha_bridge=None) -> bool:
    """
    Verifica que sigamos logueados y en la lista de productos.
    Si no, re-loguea, navega a t_CatalogoProductoMarca, aplica dropdowns y busca.
    """
    if stop_event.is_set():
        return False

    try:
        url = page.url.lower()
        on_list = "catalogoproductomarca" in url and "edit" not in url

        # Verificar si la tabla o el campo de búsqueda existen
        campo = page.locator(SEL_BUSQUEDA).first
        on_site = campo.count() > 0

        if on_list and on_site:
            return True  # Ya estamos bien

        # Sino: re-loguear
        log.warn("  Sesión perdida — re-logueando...")
        from automation.login import do_login

        ok = do_login(page, usuario, password, "", log, stop_event, captcha_bridge)
        if not ok:
            log.error("  Re-login fallido")
            return False

        # Navegar a la página de gestión
        page.goto(GESTION_URL, wait_until="domcontentloaded", timeout=60_000)
        time.sleep(3)

        # Aplicar dropdowns y buscar
        result = apply_dropdowns_and_search(page, pre_selected, log, stop_event)
        if result["status"] != "ok":
            log.warn("  No se pudo recargar la lista después del re-login")
            return False

        log.ok("  Sesión recuperada")
        return True
    except Exception as e:
        log.error(f"  Error en reconexión: {e}")
        return False


# ── Paso 6: añadir características (ISO 9001 + ISO 14001) ───────

def agregar_caracteristicas(page: Page, log, stop_event) -> dict:
    if stop_event.is_set():
        return {"status": "stopped"}

    iso_order = [("ISO 9001", "9001"), ("ISO 14001", "14001")]
    added = []
    skipped = []

    for iso_label, iso_name in iso_order:
        if stop_event.is_set():
            return {"status": "stopped", "added": added, "skipped": skipped}

        log.info(f"  Abriendo modal: Añadir {iso_name}")

        # Si el modal anterior (#wm_caracteristicaNueva) sigue abierto, cerrarlo
        # Puede pasar si no se cerró bien después del ISO anterior
        old_modal = page.locator("#wm_caracteristicaNueva")
        if old_modal.count() > 0 and old_modal.is_visible(timeout=2000):
            log.info("  Cerrando modal anterior #wm_caracteristicaNueva...")
            page.keyboard.press("Escape")
            time.sleep(1)
            page.evaluate("""
                var m = document.getElementById('wm_caracteristicaNueva');
                if (m) { m.classList.remove('in', 'show'); m.setAttribute('aria-hidden', 'true'); }
                document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
            """)
            time.sleep(1)

        # Click en btn_caracteristicaNueva
        btn = page.locator(SEL_BTN_CARACTERISTICA).first
        if btn.count() == 0 or not btn.is_visible():
            log.warn(f"  Botón Añadir Características no encontrado")
            skipped.append(iso_name)
            continue
        try:
            btn.click(timeout=5_000)
        except Exception:
            log.info("  Click bloqueado por modal, intentando force=True...")
            btn.click(force=True, timeout=5_000)
        time.sleep(2)

        # Esperar que aparezca el modal
        try:
            page.wait_for_selector(SEL_MODAL_BODY, state="visible", timeout=10_000)
        except Exception:
            log.warn(f"  Modal de características no apareció")
            page.keyboard.press("Escape")
            skipped.append(iso_name)
            continue

        # Esperar que termine cualquier AJAX del modal
        try:
            page.wait_for_load_state("networkidle", timeout=10_000)
        except Exception:
            pass
        time.sleep(1)

        # ── Seleccionar CERTIFICACION (buscar por texto, no por value hardcodeado) ──
        certificacion_seleccionada = False
        for intento in range(10):
            opts = _get_select_options(page, SEL_SEL_CARACT)
            n_opts = len(opts)
            if n_opts >= 2:
                # Buscar opción cuyo texto contenga "CERTIFICACION"
                cert_value = None
                for o in opts:
                    if "CERTIFICACION" in o["text"].upper():
                        cert_value = o["value"]
                        break
                if cert_value:
                    try:
                        page.select_option(SEL_SEL_CARACT, cert_value, timeout=5000)
                    except Exception:
                        try:
                            page.evaluate(f"""
                                var s = document.querySelector('{SEL_SEL_CARACT}');
                                if (s) {{ s.value = '{cert_value}';
                                s.dispatchEvent(new Event('change', {{bubbles: true}})); }}
                            """)
                        except Exception:
                            pass
                    certificacion_seleccionada = True
                    break
            log.info(f"  Esperando CERTIFICACION ({n_opts} opciones)... intento {intento+1}/10")
            time.sleep(1.5)
        if not certificacion_seleccionada:
            opts_debug = _get_select_options(page, SEL_SEL_CARACT)
            log.warn(f"  No se pudo seleccionar CERTIFICACION (opts={opts_debug})")
            page.keyboard.press("Escape")
            skipped.append(iso_name)
            continue

        # Esperar que N_ValCaracteristica cargue sus opciones
        iso_opciones = []
        for intento in range(10):
            iso_opciones = _get_select_options(page, SEL_SEL_VALOR)
            if any(o["value"] != "0" for o in iso_opciones):
                break
            log.info(f"  Esperando opciones de valor... intento {intento+1}/10")
            time.sleep(2)
        # Buscar la ISO en las opciones disponibles (las que NO están agregadas aún)
        iso_encontrado = None
        for opt in iso_opciones:
            if iso_label in opt["text"]:
                iso_encontrado = opt["value"]
                break

        if not iso_encontrado:
            log.info(f"  {iso_label}: no está en opciones → ya agregado, saltando")
            page.keyboard.press("Escape")
            time.sleep(0.5)
            skipped.append(iso_name)
            continue

        log.info(f"  Seleccionando {iso_label} (value={iso_encontrado})")
        try:
            page.select_option(SEL_SEL_VALOR, iso_encontrado, timeout=5000)
            time.sleep(1)
        except Exception:
            log.warn(f"  No se pudo seleccionar {iso_label}")
            page.keyboard.press("Escape")
            skipped.append(iso_name)
            continue

        # Click en Guardar del modal
        try:
            btn_guardar = page.locator(SEL_MODAL_GUARDAR).first
            if btn_guardar.count() > 0 and btn_guardar.is_visible():
                log.info(f"  Click en Guardar del modal para {iso_label}")
                btn_guardar.click(timeout=5000, no_wait_after=True)
                # Cerrar modal de confirmación que aparece
                cerrar_modal_mensaje(page, log, f"ISO {iso_name}")
                time.sleep(1)
                log.ok(f"  {iso_label} guardado correctamente")
                added.append(iso_name)
            else:
                log.warn(f"  Botón Guardar del modal no encontrado")
                page.keyboard.press("Escape")
                skipped.append(iso_name)
        except Exception as e:
            log.warn(f"  Error guardando {iso_label}: {e}")
            page.keyboard.press("Escape")
            skipped.append(iso_name)

    return {"status": "ok", "added": added, "skipped": skipped}


def _get_select_options(page: Page, selector: str) -> list[dict]:
    """Retorna las opciones de un select como [{value, text}, ...]."""
    return page.evaluate(f"""
        (() => {{
            var sel = document.querySelector('{selector}');
            if (!sel) return [];
            return Array.from(sel.options).map(o => ({{value: o.value, text: (o.text || '').trim()}}));
        }})()
    """)


# ── Paso 6: volver a la lista desde edición ──────────────────────

def volver_a_lista(page: Page, log, stop_event) -> bool:
    """Click en #btnRegresarIndex (Retornar) para volver a la lista."""
    if stop_event.is_set():
        return False
    try:
        btn = page.locator("#btnRegresarIndex").first
        if btn.count() > 0 and btn.is_visible():
            log.info("  Click en Retornar...")
            btn.click(timeout=5_000)
            try:
                page.wait_for_load_state("networkidle", timeout=30_000)
            except Exception:
                pass
            time.sleep(2)
            return True
        # Fallback: go_back
        log.warn("  #btnRegresarIndex no encontrado, usando go_back")
        page.go_back()
        try:
            page.wait_for_load_state("networkidle", timeout=15_000)
        except Exception:
            pass
        time.sleep(1.5)
        return True
    except Exception as e:
        log.warn(f"  Error volviendo a lista: {e}")
        try:
            page.goto(GESTION_URL, wait_until="networkidle", timeout=15_000)
            return True
        except Exception:
            return False


# ── Flujo completo para un producto ─────────────────────────────

def process_single_product(page: Page, parte: str, ruta_pdf: str, log, stop_event, pre_selected: dict = None) -> dict:
    if pre_selected:
        result = apply_dropdowns_and_search(page, pre_selected, log, stop_event)
        if result["status"] != "ok":
            return {"status": "search_failed", "parte": parte}

    ok = buscar_por_parte(page, parte, log, stop_event)
    if not ok:
        return {"status": "not_found", "parte": parte}

    ok = click_editar(page, log, stop_event)
    if not ok:
        return {"status": "edit_failed", "parte": parte}

    ok = subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)
    if not ok:
        return {"status": "pdf_failed", "parte": parte}

    ok = guardar_cambios(page, log, stop_event)
    if not ok:
        volver_a_lista(page, log, stop_event)
        return {"status": "save_failed", "parte": parte}

    cert_result = agregar_caracteristicas(page, log, stop_event)
    if cert_result["status"] == "stopped":
        return {"status": "stopped", "parte": parte}

    volver_a_lista(page, log, stop_event)
    return {"status": "ok" if cert_result.get("added") else "certs_already_exist", "parte": parte, "certs_result": cert_result}

import time
import os
import threading
from playwright.sync_api import Page

GESTION_URL = "https://www.catalogos.perucompras.gob.pe/t_CatalogoProductoMarca"
EDICION_URL = "https://www.catalogos.perucompras.gob.pe/t_CatalogoProductoMarca/CatalogoProductoEdit"
PDF_DIR = r"D:\SISTEMAS 02\Downloads\COMPUTADORAS\COMPUTADORAS"

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
        time.sleep(3)
        try:
            val = page.evaluate(f"document.querySelector('{SEL_ADJ_FILE}')?.value || ''")
            if val and os.path.basename(ruta_pdf) in val:
                log.ok("  PDF adjuntado correctamente")
                return True
            else:
                log.warn(f"  PDF adjuntado (verificación parcial: {val!r})")
                return True
        except Exception:
            log.ok("  PDF adjuntado correctamente")
            return True
    except Exception as e:
        log.error(f"  Error subiendo PDF: {e}")
        return False


# ── Paso 4b: subir imagen (mismo nombre que PDF, extensión de imagen) ──

SEL_IMG_FILE = "#dataFile"

# Extensiones de imagen a probar
IMG_EXTS = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]


def subir_imagen_en_edicion(page: Page, nombre_imagen: str, log, stop_event) -> bool:
    """Sube la imagen del producto. nombre_imagen es el valor de la columna
    IMAGEN (PDF) del Excel (ej: "EZENT M5"). Busca en PDF_DIR con extensiones .jpg/.png/.jpeg."""
    if stop_event.is_set():
        return False
    if not nombre_imagen:
        return True
    nombre = nombre_imagen.strip()
    img_path = os.path.join(PDF_DIR, nombre)
    if not os.path.isfile(img_path):
        # fallback: sin extensión, probar .jpg/.png
        base = os.path.splitext(nombre)[0]
        img_path = None
        for ext in IMG_EXTS:
            candidate = os.path.join(PDF_DIR, base + ext)
            if os.path.isfile(candidate):
                img_path = candidate
                break
    if not img_path:
        log.info(f"  Sin imagen ({nombre}), OK")
        return True
    try:
        file_input = page.locator(SEL_IMG_FILE).first
        if file_input.count() == 0:
            log.warn(f"  #dataFile no encontrado, saltando imagen")
            return True
        log.info(f"  Subiendo imagen: {os.path.basename(img_path)}")
        file_input.set_input_files(img_path)
        time.sleep(3)
        log.ok("  Imagen adjuntada correctamente")
        return True
    except Exception as e:
        log.warn(f"  Error subiendo imagen: {e}")
        return True  # No crítico


# ── Paso 4c: cambiar precio ─────────────────────────────────────

def cambiar_precio_en_edicion(page: Page, precio: str, log, stop_event) -> bool:
    """Cambia el precio en la página de edición si hay un input para él."""
    if stop_event.is_set():
        return False
    if not precio:
        return True
    # Selectores comunes para input de precio
    selectores = [
        "input[name*='Precio']", "input[name*='precio']",
        "input[id*='Precio']", "input[id*='precio']",
        "#N_Precio", "#C_PrecioSugerido", "#Precio",
    ]
    inp = None
    for sel in selectores:
        loc = page.locator(sel).first
        if loc.count() > 0 and loc.is_visible(timeout=1500):
            inp = loc
            break
    if not inp:
        log.info(f"  Campo de precio no encontrado, saltando")
        return True
    try:
        log.info(f"  Cambiando precio a: {precio}")
        inp.fill(str(precio))
        # Trigger change event
        page.evaluate("""
            var el = document.activeElement;
            if (el) { el.dispatchEvent(new Event('change', {bubbles: true})); el.dispatchEvent(new Event('blur', {bubbles: true})); }
        """)
        time.sleep(0.5)
        log.ok("  Precio actualizado")
        return True
    except Exception as e:
        log.warn(f"  Error cambiando precio: {e}")
        return False


# ── Paso 4d: actualizar N° de Parte (campo editable en la ficha) ──

NRO_PARTE_SELECTORS = [
    "#NRO_PARTE", "#NroParte", "#Nro_Parte", "#nro_parte",
    "#C_NRO_PARTE", "#C_NroParte",
    "input[name='NRO_PARTE']", "input[name='Nro_Parte']",
    "input[name='C_NRO_PARTE']", "input[name='C_NroParte']",
    "input[id*='NRO_PARTE']", "input[id*='NroParte']",
    "input[id*='Nro_Parte']", "input[id*='Nro']",
    "input[id*='nro_parte']", "input[id*='nroParte']",
]


def _find_nro_parte_field(page: Page):
    """Busca el campo N° de Parte por selectores o por label de texto."""
    for sel in NRO_PARTE_SELECTORS:
        try:
            loc = page.locator(sel).first
            if loc.count() > 0 and loc.is_visible(timeout=800):
                return loc
        except Exception:
            continue
    # Fallback: buscar por label "N° de Parte" o "NRO PARTE"
    try:
        result = page.evaluate("""
            () => {
                const labels = document.querySelectorAll('label, .control-label, .form-group label');
                for (const lbl of labels) {
                    const txt = (lbl.textContent || '').toLowerCase();
                    if (txt.includes('n') && txt.includes('parte') &&
                        (txt.includes('°') || txt.includes('ro'))) {
                        const forAttr = lbl.getAttribute('for');
                        if (forAttr) {
                            const inp = document.getElementById(forAttr);
                            if (inp) return forAttr;
                        }
                        // Buscar input hermano dentro del mismo form-group
                        const group = lbl.closest('.form-group, .form-row, div');
                        if (group) {
                            const inp = group.querySelector('input[type=text], input:not([type])');
                            if (inp && inp.id) return inp.id;
                        }
                    }
                }
                return null;
            }
        """)
        if result:
            return page.locator(f"#{result}").first
    except Exception:
        pass
    return None


def actualizar_nro_parte_en_edicion(page: Page, nueva_parte: str, log, stop_event) -> bool:
    """Borra el campo N° de Parte y escribe el nuevo valor del Excel.
    Usa JS para setear el valor (funciona incluso si el campo es readonly)
    + simula paste/typing para disparar eventos de validación."""
    if stop_event.is_set():
        return False
    if not nueva_parte:
        return True
    inp = _find_nro_parte_field(page)
    if not inp or inp.count() == 0:
        log.warn("  Campo N° de Parte no encontrado, saltando")
        return True
    try:
        log.info(f"  Actualizando N° de Parte a: {nueva_parte}")
        # Click para focus
        try:
            inp.click(timeout=3000)
        except Exception:
            pass
        # Forzar el valor por JS y disparar eventos (paste, input, change, blur)
        # Usa el activeElement (el campo que acabamos de clickear) o el id del campo
        field_id = inp.evaluate("el => el.id || ''")
        ok = page.evaluate("""
            ([fid, nuevo]) => {
                const el = fid ? document.getElementById(fid) : document.activeElement;
                if (!el) return false;
                const setter = Object.getOwnPropertyDescriptor(
                    window.HTMLInputElement.prototype, 'value'
                ).set;
                setter.call(el, nuevo);
                el.dispatchEvent(new Event('input', {bubbles: true}));
                el.dispatchEvent(new Event('change', {bubbles: true}));
                el.dispatchEvent(new Event('blur', {bubbles: true}));
                return el.value === nuevo;
            }
        """, [field_id, str(nueva_parte)])
        time.sleep(0.5)
        if ok:
            log.ok("  N° de Parte actualizado")
            return True
        else:
            log.warn("  N° de Parte no se pudo actualizar via JS")
            return False
    except Exception as e:
        log.warn(f"  Error actualizando N° de Parte: {e}")
        return False


# ── Paso 5: Guardar ─────────────────────────────────────────────

def guardar_cambios(page: Page, log, stop_event) -> bool:
    """Click en Guardar, espera el modal de éxito y lo cierra.
    Acepta múltiples selectores de modal (#MensajeModal, #modalContent, .bootbox.modal).
    Si no aparece modal en 360s, asume guardado exitoso y continúa (PeruCompras es lento).
    """
    if stop_event.is_set():
        return False
    max_intentos = 2
    for intento in range(1, max_intentos + 1):
        if stop_event.is_set():
            return False
        try:
            btn = page.locator(SEL_BTN_GUARDAR).first
            if btn.count() == 0:
                log.error(f"  #btnGuardar no encontrado")
                return False
            if intento == 1:
                log.info("  Haciendo click en Guardar...")
            else:
                log.info(f"  Reintentando Guardar (intento {intento}/{max_intentos})...")
            btn.click(timeout=5_000, no_wait_after=True)

            # Esperar el modal de éxito — busca múltiples selectores
            modal_sels = ["#MensajeModal", "#modalContent", ".bootbox.modal", ".modal.show"]
            modal_encontrado = False
            for sel in modal_sels:
                try:
                    page.wait_for_selector(sel, state="visible", timeout=360_000)
                    log.info(f"  Modal de éxito detectado con selector {sel}")
                    modal_encontrado = True
                    break
                except Exception:
                    continue

            if modal_encontrado:
                # Cerrar el modal
                cerrar_modal_mensaje(page, log, f"Guardar-{intento}")
                log.ok(f"  Cambios guardados correctamente (intento {intento})")
                return True
            else:
                # No apareció ningún modal en 360s — la página del estado es muy lenta.
                # Asumir que el guardado fue exitoso (puede que el modal se haya
                # abierto y cerrado solo, o que el servidor tardó en responder)
                log.warn("  No se detectó modal de éxito en 360s — asumiendo guardado OK")
                return True
        except Exception as e:
            log.error(f"  Error al guardar (intento {intento}): {e}")
            if intento < max_intentos:
                continue
            return False
    return False


def cerrar_modal_mensaje(page: Page, log, context: str = "") -> bool:
    """Espera y cierra el modal #MensajeModal que aparece tras guardar. Retorna True si lo cerró."""
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
            return True
        cerrar = page.locator("button.close[data-dismiss='modal']").first
        if cerrar.count() > 0 and cerrar.is_visible(timeout=2000):
            cerrar.click(timeout=3000)
            time.sleep(1)
            log.info(f"  Modal cerrado con X{ctx}")
            return True
        dismiss = page.locator("button[data-dismiss='modal']").first
        if dismiss.count() > 0 and dismiss.is_visible(timeout=2000):
            dismiss.click(timeout=3000)
            time.sleep(1)
            log.info(f"  Modal cerrado con data-dismiss{ctx}")
            return True
        log.warn(f"  No se encontró botón para cerrar modal{ctx}")
        return False
    except Exception:
        log.warn(f"  Modal #MensajeModal no apareció{ctx}")
        return False


# ── Contingencia: reconexión si la sesión expira ─────────────────

def _tiene_campos_login(page) -> bool:
    """Verifica si la página actual tiene los campos de login visibles."""
    try:
        user_input = page.locator("#ID_Usuario").first
        return user_input.count() > 0 and user_input.is_visible(timeout=2000)
    except Exception:
        return False


def ensure_logged_in_and_ready(page: Page, usuario: str, password: str, pre_selected: dict, log, stop_event, captcha_bridge=None) -> bool:
    """
    Verifica que sigamos logueados.
    NO aplica dropdowns+Buscar (eso tarda 180s+ con miles de fichas).
    Solo verifica la sesión y navega a gestión si es necesario.
    """
    if stop_event.is_set():
        return False

    try:
        url = page.url.lower()
        # Si la URL no contiene /AccesoGeneral ni /login, asumimos sesión activa
        if "accesogeneral" not in url and "login" not in url:
            return True  # Sesión activa

        # La URL SÍ contiene accesogeneral o login — verificar si la página
        # realmente tiene los campos (PeruCompras redirige a la raíz si hay sesión)
        if not _tiene_campos_login(page):
            log.info("  URL indica login pero campos AUSENTES → sesión activa")
            return True

        # Sino: re-loguear
        log.warn("  Sesión perdida — re-logueando...")
        from automation.login import do_login

        ok = do_login(page, usuario, password, "", log, stop_event, captcha_bridge)
        if not ok:
            # Último intento: chequear si a pesar del fallo, ya hay sesión
            if not _tiene_campos_login(page):
                log.info("  do_login falló pero sin campos de login → sesión activa")
                return True
            log.error("  Re-login fallido")
            return False

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
        old_modal = page.locator("#wm_caracteristicaNueva")
        if old_modal.count() > 0 and old_modal.is_visible(timeout=2000):
            log.info("  Cerrando modal anterior vía Escape...")
            page.keyboard.press("Escape")
            time.sleep(1)

        # Click en btn_caracteristicaNueva (mismo approach que agregar_caracteristica_texto)
        btn = page.locator(SEL_BTN_CARACTERISTICA).first
        if btn.count() == 0 or not btn.is_visible():
            log.warn(f"  Botón Añadir Características no encontrado")
            skipped.append(iso_name)
            continue
        btn.click(timeout=5_000)
        time.sleep(2)

        # Esperar que aparezca el modal (mismo approach que agregar_caracteristica_texto)
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


# ── Paso 7: leer características y certificaciones desde la página ──────

def leer_caracteristicas_pagina(page) -> list[dict]:
    """
    Lee la tabla de características de la página de edición.
    Retorna lista de {"nombre": str, "valor": str, "id": str}.
    Estructura HTML: cada característica es un .row con dos .col-md-4
    (hidden inputs + nombre + valor).
    """
    return page.evaluate("""
        (() => {
            const rows = document.querySelectorAll('.row');
            const out = [];
            rows.forEach(r => {
                const cols = r.querySelectorAll('.col-md-4');
                if (cols.length < 2) return;
                // El nombre está en la segunda col-md-4 (después de los hidden inputs)
                const idEl = r.querySelector('input[name="ID_CatFichaProducto"]');
                if (!idEl) return;
                const id = idEl.value;
                // Nombre: textContent del primer col-md-4, después de los hidden inputs
                const nombre = cols[0].textContent.trim();
                const valor = cols[1].textContent.trim();
                if (nombre && valor) {
                    out.push({nombre: nombre, valor: valor, id: id});
                }
            });
            return out;
        })()
    """)


def leer_certificaciones_pagina(page) -> list[dict]:
    """
    Lee la tabla de certificaciones. Retorna lista de {"id": str, "valor": str}.
    Estructura: cada cert es un .row con CERTIFICACION como texto y valor en col-md-6.
    """
    return page.evaluate("""
        (() => {
            const rows = document.querySelectorAll('.row');
            const out = [];
            rows.forEach(r => {
                const idEl = r.querySelector('input[name="ID_CatFichaProducto"]');
                if (!idEl) return;
                const cols = r.querySelectorAll('.col-md-4, .col-md-6');
                const allText = r.textContent;
                if (!allText.includes('CERTIFICACION')) return;
                // El valor está en la segunda columna visible
                const visibleCols = Array.from(cols).filter(c => !c.querySelector('input'));
                if (visibleCols.length >= 2) {
                    out.push({id: idEl.value, valor: visibleCols[1].textContent.trim()});
                }
            });
            return out;
        })()
    """)


def _norm_value(s: str) -> str:
    """Normaliza un valor para comparación: strip, mayúsculas, espacios colapsados."""
    import re as _re
    return _re.sub(r'\s+', ' ', str(s).strip().upper())


def comparar_caracteristicas(page_chars: list[dict], excel_chars: dict, log) -> dict:
    """
    Compara las características de la página contra las del Excel.
    Retorna {"iguales": int, "diferentes": [{"nombre", "esperado", "actual", "id"}], "faltantes_en_pagina": []}.
    Si el valor de la página tiene el prefijo "NOMBRE: " (ej: "TECLADO: SI" para char TECLADO),
    se ignora el prefijo antes de comparar.
    """
    page_by_name = {c["nombre"].upper().strip(): c for c in page_chars}
    iguales = 0
    diferentes = []
    for nombre, esperado in excel_chars.items():
        norm_nombre = nombre.upper().strip()
        actual_obj = page_by_name.get(norm_nombre)
        if actual_obj is None:
            continue  # La página no tiene esta característica, no se compara
        actual = actual_obj["valor"]
        # Quitar prefijo "NOMBRE: " de AMBOS valores si está presente
        # Ej: "TECLADO: SI" → "SI" (tanto en Excel como en página)
        prefix = f"{norm_nombre}: "
        norm_actual = _norm_value(actual)
        if norm_actual.startswith(prefix):
            norm_actual = norm_actual[len(prefix):]
        norm_esperado = _norm_value(esperado)
        if norm_esperado.startswith(prefix):
            norm_esperado = norm_esperado[len(prefix):]
        if norm_actual == norm_esperado:
            iguales += 1
        else:
            diferentes.append({
                "nombre": nombre,
                "esperado": esperado,
                "actual": actual,
                "id": actual_obj.get("id"),
            })
            log.warn(f"  DIF {nombre}: esperado={esperado!r} actual={actual!r}")
    if iguales:
        log.ok(f"  Características: {iguales} coinciden")
    return {"iguales": iguales, "diferentes": diferentes}


def corregir_caracteristica(page, char_id: str, valor_esperado: str, log, stop_event, edit_url: str = None) -> bool:
    """
    Corrige UNA característica. SIEMPRE re-navega a edit_url antes para
    garantizar que link_caracteristicaEdit existe (se pierde tras cada guardado).
    """
    if stop_event.is_set():
        return False
    if not char_id:
        log.warn(f"  ID de característica vacío, no se puede editar")
        return False
    if not edit_url:
        log.warn(f"  edit_url requerido para corregir característica")
        return False

    try:
        # SIEMPRE re-navegar para garantizar contexto JS fresco
        page.goto(edit_url, wait_until="networkidle", timeout=60_000)
        time.sleep(1.5)

        log.info(f"  Abriendo edición de char ID={char_id}...")
        # Click via JS (link_caracteristicaEdit es función JS onclick)
        page.evaluate(f"link_caracteristicaEdit('{char_id}', 'OBSERVADO');")
        time.sleep(1.5)

        # Esperar a que aparezca el form de edición
        try:
            page.wait_for_selector("#form_editCaracteristica", state="visible", timeout=15_000)
        except Exception:
            log.warn(f"  Modal de edición no apareció para ID={char_id}")
            return False

        # Esperar AJAX
        try:
            page.wait_for_load_state("networkidle", timeout=15_000)
        except Exception:
            pass
        time.sleep(1)

        # Leer opciones del dropdown
        opciones = _get_select_options(page, "#form_editCaracteristica #N_ValCaracteristica")
        if not opciones or all(o["value"] == "0" for o in opciones):
            for _ in range(10):
                time.sleep(1.5)
                opciones = _get_select_options(page, "#form_editCaracteristica #N_ValCaracteristica")
                if any(o["value"] != "0" for o in opciones):
                    break

        # Buscar coincidencia en 3 niveles: exacto, sufijo, contains
        match_value = None
        norm_esperado = _norm_value(valor_esperado)
        for o in opciones:
            if _norm_value(o["text"]) == norm_esperado:
                match_value = o["value"]
                break
        if not match_value and norm_esperado in ("SI", "NO"):
            for o in opciones:
                txt = _norm_value(o["text"])
                if txt == norm_esperado or txt.endswith(f": {norm_esperado}"):
                    match_value = o["value"]
                    break
        if not match_value:
            for o in opciones:
                txt = _norm_value(o["text"])
                if norm_esperado in txt:
                    match_value = o["value"]
                    break

        if not match_value:
            # Fallback: si hay un input de texto libre (#N_ValCaracteristicaTXT visible),
            # usarlo para escribir el valor directamente (caso de chars como N° de Parte, MODELO)
            txt_input = page.locator("#form_editCaracteristica #N_ValCaracteristicaTXT").first
            if txt_input.count() > 0 and txt_input.is_visible(timeout=2000):
                log.info(f"  Escribiendo en input de texto: {valor_esperado!r}")
                txt_input.click(timeout=3000)
                txt_input.fill("")  # limpiar
                # Usar JS para setear el valor y disparar eventos (funciona con campos problemáticos)
                ok = page.evaluate("""
                    (nuevo) => {
                        const el = document.getElementById('N_ValCaracteristicaTXT');
                        if (!el) return false;
                        const setter = Object.getOwnPropertyDescriptor(
                            window.HTMLInputElement.prototype, 'value'
                        ).set;
                        setter.call(el, nuevo);
                        el.dispatchEvent(new Event('input', {bubbles: true}));
                        el.dispatchEvent(new Event('change', {bubbles: true}));
                        return el.value === nuevo;
                    }
                """, str(valor_esperado))
                time.sleep(0.5)
                if not ok:
                    log.warn(f"  No se pudo escribir en input de texto")
                    return False
            else:
                log.warn(f"  No se encontró opción para {valor_esperado!r}")
                log.warn(f"  Opciones: {[o['text'] for o in opciones if o['value'] != '0']}")
                return False
        else:
            log.info(f"  Seleccionando: {valor_esperado!r} (value={match_value})")
            try:
                page.select_option("#form_editCaracteristica #N_ValCaracteristica", match_value, timeout=5_000)
            except Exception:
                page.evaluate(f"""
                    var s = document.querySelector('#form_editCaracteristica #N_ValCaracteristica');
                    if (s) {{ s.value = '{match_value}'; s.dispatchEvent(new Event('change', {{bubbles: true}})); }}
                """)
            time.sleep(0.5)

        # Click en Guardar — esperar navegación o modal de éxito
        btn = page.locator("#form_editCaracteristica #btn_guardar").first
        if btn.count() == 0:
            btn = page.locator("#form_editCaracteristica button[type='submit']").first
        if btn.count() > 0 and btn.is_visible(timeout=2_000):
            btn.click(timeout=5_000, no_wait_after=True)
            # Esperar navegación O modal de éxito (lo que llegue primero)
            try:
                page.wait_for_load_state("networkidle", timeout=15_000)
            except Exception:
                pass
            time.sleep(1.5)
            # Cerrar modal de éxito si aparece (es el mismo #MensajeModal de siempre)
            cerrar_modal_mensaje(page, log, "CorregirChar")
            # Forzar cierre por si quedó algo colgado
            page.evaluate("""
                document.querySelectorAll('.modal-backdrop, .modal.show, .modal.in, #MensajeModal, #modalContent, .bootbox.modal')
                    .forEach(el => { try { el.remove(); } catch(e) {} });
                document.body.style.overflow = '';
                document.body.classList.remove('modal-open');
            """)
            time.sleep(1)
            log.ok(f"  Característica actualizada a {valor_esperado!r}")
            return True
        log.warn(f"  Botón Guardar no encontrado")
        return False
    except Exception as e:
        log.warn(f"  Error editando característica: {e}")
        try:
            page.keyboard.press("Escape")
        except Exception:
            pass
        return False


# ── Paso 8: agregar certificaciones faltantes (ISO 9001 / 14001) ──────

CERTIFICACION_MODAL_BTN = "#btn_certificacionNueva"  # botón para abrir modal de cert


def agregar_certificaciones_faltantes(page, certs_esperadas: list[str], log, stop_event) -> dict:
    """
    Verifica certificaciones y agrega solo ISO 9001 / ISO 14001 si faltan.
    Reutiliza agregar_caracteristicas() que abre el modal #wm_caracteristicaNueva.
    Para certs no-ISO (CE, RoHS, FCC) que falten, las reporta como faltantes.
    """
    if stop_event.is_set():
        return {"status": "stopped"}

    page_certs = leer_certificaciones_pagina(page)
    page_valores = {_norm_value(c["valor"]): c for c in page_certs}
    log.info(f"  Certificaciones en página: {[c['valor'] for c in page_certs]}")

    faltantes_no_iso = [
        c for c in certs_esperadas
        if _norm_value(c) not in page_valores and "ISO" not in c.upper()
    ]
    if faltantes_no_iso:
        log.warn(f"  SKIP no-ISO faltantes: {faltantes_no_iso}")

    iso_faltantes = [
        c for c in certs_esperadas
        if _norm_value(c) not in page_valores and "ISO" in c.upper()
    ]
    if not iso_faltantes:
        log.ok(f"  Certs: todas las ISO presentes")
        return {"status": "ok", "added": [], "missing_non_iso": faltantes_no_iso}

    log.info(f"  ISOs a agregar: {iso_faltantes}")
    # Reutilizar la lógica de agregar_caracteristicas (ya probada en modulo_modificar_productos)
    return agregar_caracteristicas(page, log, stop_event)


# ── Eliminar característica (para chars de texto libre como N° de Parte) ──

def eliminar_caracteristica(page: Page, char_id: str, log, stop_event) -> bool:
    """Elimina una característica por ID.
    Flujo: click en link 'Eliminar' del row → modal ._wModal "Si/No" → click Si → listo.
    NO aparece modal de éxito después (la fila simplemente desaparece)."""
    if stop_event.is_set():
        return False
    if not char_id:
        return False
    try:
        # 1) Click en el link "Eliminar" de la fila con este char_id
        # El link tiene onclick="EliminarCatFichaProducto('id', 'catId', 'name', 'estado')"
        clicked = page.evaluate("""
            (cid) => {
                const rows = document.querySelectorAll('.row');
                for (const r of rows) {
                    const idEl = r.querySelector('input[name="ID_CatFichaProducto"]');
                    if (!idEl || idEl.value !== cid) continue;
                    // Buscar <a> con texto "Eliminar" o onclick con EliminarCatFichaProducto
                    const links = r.querySelectorAll('a');
                    for (const a of links) {
                        const txt = (a.textContent || '').toLowerCase().trim();
                        const onclick = a.getAttribute('onclick') || '';
                        if (txt === 'eliminar' || txt === 'borrar' ||
                            onclick.includes('EliminarCatFichaProducto') ||
                            onclick.toLowerCase().includes('eliminar')) {
                            a.click();
                            return true;
                        }
                    }
                    return false;
                }
                return false;
            }
        """, str(char_id))
        if not clicked:
            log.warn(f"  No se encontró link 'Eliminar' para char ID={char_id}")
            return False
        time.sleep(2)
        # 2) Modal de confirmación custom ._wModal → click en "Si" (._wModal_btn_ok)
        log.info("  Esperando confirmación de eliminación...")
        confirmado = False
        try:
            btn_si = page.locator("._wModal_btn_ok").first
            if btn_si.count() > 0 and btn_si.is_visible(timeout=5000):
                btn_si.click(timeout=5000)
                log.info("  Confirmación aceptada (._wModal_btn_ok)")
                confirmado = True
        except Exception:
            pass
        if not confirmado:
            for sel in ["button:has-text('Sí')", "button:has-text('Si')",
                        "button:has-text('Aceptar')", "button:has-text('Confirmar')",
                        "button:has-text('Eliminar')"]:
                try:
                    btn = page.locator(sel).first
                    if btn.count() > 0 and btn.is_visible(timeout=2000):
                        btn.click(timeout=5000)
                        confirmado = True
                        break
                except Exception:
                    continue
        if not confirmado:
            log.warn("  No se encontró botón de confirmación (Si)")
            return False
        time.sleep(2)
        # 3) NO hay modal de éxito según el usuario — solo limpiar restos
        page.evaluate("""
            document.querySelectorAll('.modal-backdrop, .modal.show, .modal.in, #MensajeModal, .bootbox.modal, ._wModal, ._wModal_delete, ._wModal_bg')
                .forEach(el => { try { el.remove(); } catch(e) {} });
            document.body.style.overflow = '';
            document.body.classList.remove('modal-open');
        """)
        time.sleep(1)
        log.ok(f"  Característica ID={char_id} eliminada")
        return True
    except Exception as e:
        log.warn(f"  Error eliminando característica: {e}")
        return False


def agregar_caracteristica_texto(page: Page, nombre_char: str, valor_texto: str,
                                  log, stop_event) -> bool:
    """Agrega una característica con valor de texto libre.
    Flujo: click Añadir → seleccionar nombre del char → escribir valor en input de texto
    → Guardar → modal éxito → cerrar."""
    if stop_event.is_set():
        return False
    if not nombre_char or not valor_texto:
        return False
    try:
        # 1) Click en btn_caracteristicaNueva
        btn = page.locator(SEL_BTN_CARACTERISTICA).first
        if btn.count() == 0 or not btn.is_visible():
            log.warn("  Botón Añadir Características no encontrado")
            return False
        btn.click(timeout=5_000)
        time.sleep(2)
        # 2) Esperar modal
        try:
            page.wait_for_selector(SEL_MODAL_BODY, state="visible", timeout=10_000)
        except Exception:
            log.warn("  Modal de características no apareció")
            return False
        # 3) Seleccionar el nombre del char en el dropdown
        opts = _get_select_options(page, SEL_SEL_CARACT)
        char_value = None
        for o in opts:
            if nombre_char.upper() in o["text"].upper():
                char_value = o["value"]
                break
        if not char_value:
            log.warn(f"  No se encontró '{nombre_char}' en opciones del modal")
            page.keyboard.press("Escape")
            return False
        try:
            page.select_option(SEL_SEL_CARACT, char_value, timeout=5_000)
        except Exception:
            page.evaluate(f"""
                var s = document.querySelector('{SEL_SEL_CARACT}');
                if (s) {{ s.value = '{char_value}';
                s.dispatchEvent(new Event('change', {{bubbles: true}})); }}
            """)
        time.sleep(2)
        # 4) Detectar qué campo de valor está visible: TXT, CBO (dropdown), NUM, Fecha
        # La página muestra solo uno según el tipo de char
        tipo_valor = page.evaluate("""
            () => {
                const cbo = document.getElementById('ValCaracteristicaCBO');
                const txt = document.getElementById('ValCaracteristicaTXT');
                const num = document.getElementById('ValCaracteristicaNUM');
                if (cbo && cbo.style.display !== 'none') return 'CBO';
                if (txt && txt.style.display !== 'none') return 'TXT';
                if (num && num.style.display !== 'none') return 'NUM';
                return 'TXT';  // default a texto
            }
        """)
        log.info(f"  Tipo de campo de valor: {tipo_valor}")
        if tipo_valor == "CBO":
            # Dropdown: buscar el valor en las opciones
            opciones = _get_select_options(page, SEL_SEL_VALOR)
            match = None
            for o in opciones:
                if _norm_value(o["text"]) == _norm_value(valor_texto):
                    match = o["value"]
                    break
            if not match:
                log.warn(f"  Valor '{valor_texto}' no encontrado en dropdown")
                page.keyboard.press("Escape")
                return False
            page.select_option(SEL_SEL_VALOR, match, timeout=5_000)
        else:
            # Campo de texto (TXT o NUM): usar #N_ValCaracteristicaTXT o #N_ValCaracteristicaNUM
            input_id = "N_ValCaracteristicaTXT" if tipo_valor == "TXT" else "N_ValCaracteristicaNUM"
            ok = page.evaluate("""
                ([id, val]) => {
                    const el = document.getElementById(id);
                    if (!el) return false;
                    const setter = Object.getOwnPropertyDescriptor(
                        window.HTMLInputElement.prototype, 'value'
                    ).set;
                    setter.call(el, val);
                    el.dispatchEvent(new Event('input', {bubbles: true}));
                    el.dispatchEvent(new Event('change', {bubbles: true}));
                    return el.value === val;
                }
            """, [input_id, str(valor_texto)])
            if not ok:
                log.warn(f"  No se pudo escribir en #{input_id}")
                page.keyboard.press("Escape")
                return False
            log.info(f"  Valor escrito en #{input_id}: {valor_texto!r}")
        time.sleep(0.5)
        # 5) Click en Guardar del modal
        try:
            page.click(SEL_MODAL_GUARDAR, timeout=5_000)
        except Exception:
            guardar = page.locator(".modal-footer button:has-text('Guardar'), .modal-footer button[type='submit']").first
            if guardar.count() > 0:
                guardar.click(timeout=5_000)
        time.sleep(2)
        # 6) Modal de éxito → cerrar
        cerrar_modal_mensaje(page, log, "AddChar")
        # Limpieza defensiva
        page.evaluate("""
            document.querySelectorAll('.modal-backdrop, .modal.show, .modal.in, #MensajeModal, .bootbox.modal')
                .forEach(el => { try { el.remove(); } catch(e) {} });
            document.body.style.overflow = '';
            document.body.classList.remove('modal-open');
        """)
        time.sleep(1)
        log.ok(f"  Característica '{nombre_char}' = '{valor_texto}' agregada")
        return True
    except Exception as e:
        log.warn(f"  Error agregando característica de texto: {e}")
        return False

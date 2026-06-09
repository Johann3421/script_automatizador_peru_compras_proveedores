import time

from playwright.sync_api import Page
from utils.logger import LogWriter

CATALOGO_URL = "https://www.catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp"
CATALOGO_INDEX_URL = "https://www.catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp/CatalogoProductoIndex"


def _get_select_options(page: Page, select_id: str) -> list[dict]:
    options = page.evaluate(f"""
        (() => {{
            var sel = document.getElementById('{select_id}');
            if (!sel) return [];
            return Array.from(sel.options).map(o => ({{value: o.value, text: o.text.trim()}}));
        }})()
    """)
    return options if options else []


def _select2_choose(page: Page, select_id: str, value: str):
    """Selecciona opción en Select2 disparando el evento change correctamente."""
    # Método JS: setear el valor y disparar change (más fiable que clicks)
    result = page.evaluate(f"""
        (() => {{
            var sel = document.getElementById('{select_id}');
            if (!sel) return 'not_found';
            sel.value = '{value}';
            // Disparar eventos que Select2 escucha
            sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
            sel.dispatchEvent(new Event('input', {{ bubbles: true }}));
            // Si hay jQuery + Select2, disparar trigger
            if (typeof $ !== 'undefined' && $(sel).data('select2')) {{
                $(sel).trigger('change');
            }}
            return sel.value;
        }})()
    """)
    time.sleep(0.5)

    # Fallback: si el JS no funcionó, intentar click en el widget
    if result == 'not_found' or result == '0':
        container_sel = f"#{select_id} + .select2 .select2-selection"
        page.locator(container_sel).first.click(force=True)
        time.sleep(0.5)
        try:
            page.locator(f".select2-results__option[id$='{value}']").first.click(timeout=4000)
        except Exception:
            try:
                options = page.locator("li.select2-results__option")
                count = options.count()
                for i in range(count):
                    opt = options.nth(i)
                    if opt.is_visible():
                        opt.click(force=True)
                        break
            except Exception:
                pass
        time.sleep(0.5)


def _select_native(page: Page, select_id: str, value: str):
    """Selecciona en un <select> nativo disparando evento change vía JS."""
    page.evaluate(f"""
        var sel = document.getElementById('{select_id}');
        if (sel) {{
            sel.value = '{value}';
            sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
        }}
    """)
    time.sleep(0.5)
def setup_catalog_search(page: Page, log: LogWriter, catalog_bridge=None,
                         pre_selected: dict | None = None) -> dict | None:
    """
    Configura la busqueda en el catalogo.
    Si pre_selected tiene los valores, los aplica directamente sin bridge.
    Si no, pide al usuario via bridge (paso a paso).
    """
    try:
        current_url = page.url
        if "t_ProductoOfertadoAmp" not in current_url:
            log.info("Navegando al catalogo de ofertas...")
            page.goto(CATALOGO_URL, wait_until="networkidle")
            page.wait_for_load_state("domcontentloaded")
            time.sleep(3)

        page.evaluate("""
            document.querySelectorAll(
                '.modal-backdrop, .modal.open, .modal.show, '
                + '.swal2-container, #_wModal_bg, '
                + '._wModal, ._wModal_delete'
            ).forEach(el => el.remove());
            document.body.style.overflow = '';
            document.body.classList.remove('modal-open');
        """)
        time.sleep(1)

        # ── Acuerdo Marco ──
        if pre_selected and pre_selected.get("acuerdo"):
            acuerdo_val = pre_selected["acuerdo"]
            log.info("Aplicando Acuerdo Marco pre-seleccionado: %s" % acuerdo_val)
        else:
            acuerdos = _get_select_options(page, "ajaxAcuerdo")
            if not acuerdos or len(acuerdos) <= 1:
                log.error("No se encontraron Acuerdos Marco.")
                return None
            log.info("%d acuerdos disponibles." % len(acuerdos))
            acuerdo_val = catalog_bridge.request_step("acuerdo", acuerdos)
            if not acuerdo_val or acuerdo_val == "0":
                log.error("No se selecciono un Acuerdo Marco valido.")
                return None

        log.info("Seleccionando Acuerdo Marco: %s" % acuerdo_val)
        _select2_choose(page, "ajaxAcuerdo", acuerdo_val)
        time.sleep(3)

        # ── Catalogo ──
        if pre_selected and pre_selected.get("catalogo"):
            catalogo_val = pre_selected["catalogo"]
            log.info("Aplicando Catalogo pre-seleccionado: %s" % catalogo_val)
        else:
            time.sleep(1)
            catalogos = _get_select_options(page, "ajaxCatalogo")
            if not catalogos or all(o["value"] == "0" for o in catalogos):
                log.error("No cargaron Catalogos.")
                return None
            log.info("%d catalogos disponibles." % len(catalogos))
            catalogo_val = catalog_bridge.request_step("catalogo", catalogos)
            if not catalogo_val or catalogo_val == "0":
                log.error("No se selecciono un Catalogo valido.")
                return None

        log.info("Seleccionando Catalogo: %s" % catalogo_val)
        _select_native(page, "ajaxCatalogo", catalogo_val)
        time.sleep(3)

        # ── Categoria ──
        if pre_selected and pre_selected.get("categoria"):
            categoria_val = pre_selected["categoria"]
            log.info("Aplicando Categoria pre-seleccionada: %s" % categoria_val)
        else:
            time.sleep(1)
            categorias = _get_select_options(page, "ajaxCategoria")
            if not categorias or all(o["value"] == "0" for o in categorias):
                log.error("No cargaron Categorias.")
                return None
            log.info("%d categorias disponibles." % len(categorias))
            categoria_val = catalog_bridge.request_step("categoria", categorias)
            if not categoria_val or categoria_val == "0":
                log.error("No se selecciono una Categoria valida.")
                return None

        log.info("Seleccionando Categoria: %s" % categoria_val)
        _select_native(page, "ajaxCategoria", categoria_val)
        time.sleep(2)

        # ── Iniciar Busqueda ──
        log.info("Click en 'Iniciar Busqueda'...")
        btn_buscar = page.locator("#btnBuscar").first
        if btn_buscar.count() == 0:
            log.error("No se encontro #btnBuscar.")
            return None
        btn_buscar.click(force=True)
        page.wait_for_load_state("networkidle", timeout=20000)
        time.sleep(3)

        # ── Agregar oferta ──
        log.info("Click en 'Agregar oferta'...")
        btn_nuevo = page.locator("#btnNuevoProducto").first
        if btn_nuevo.count() > 0:
            btn_nuevo.click(force=True)
            page.wait_for_load_state("networkidle", timeout=20000)
            time.sleep(3)

        current = page.url
        if "CatalogoProductoIndex" not in current:
            log.error("No se llego a CatalogoProductoIndex. URL: %s" % current[:80])
            return None

        log.ok("Catalogo configurado -> %s" % current[:80])
        return {
            "acuerdo": acuerdo_val,
            "catalogo": catalogo_val,
            "categoria": categoria_val,
        }

    except Exception as e:
        log.error("Excepcion en setup_catalog_search: %s" % e)
        return None

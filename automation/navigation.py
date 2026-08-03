import time

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeout
from utils.logger import LogWriter

CATALOGO_URL = "https://www.catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp"
CATALOGO_INDEX_URL = "https://www.catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp/CatalogoProductoIndex"

# Timeout base por operación (ms). Se dobla en cada reintento.
_BASE_TIMEOUT = 60_000
_MAX_RETRIES   = 4


def _retry_goto(page: Page, url: str, log: LogWriter,
                anchor_selector: str = "body",
                max_retries: int = _MAX_RETRIES):
    """
    Navega a `url` con reintentos exponenciales.
    Usa wait_until='domcontentloaded' (nunca 'networkidle') para evitar
    timeouts en páginas del Estado que siempre tienen peticiones pendientes.
    Luego espera que aparezca `anchor_selector` para confirmar que cargó.
    """
    for attempt in range(1, max_retries + 1):
        try:
            log.info(f"[goto] intento {attempt}/{max_retries} → {url[:60]}...")
            page.goto(url, wait_until="domcontentloaded",
                      timeout=_BASE_TIMEOUT * attempt)
            # Confirmar que el DOM tiene contenido real
            page.wait_for_selector(anchor_selector,
                                   timeout=_BASE_TIMEOUT * attempt)
            log.info(f"[goto] OK en intento {attempt}.")
            return
        except PlaywrightTimeout:
            log.warn(f"[goto] Timeout en intento {attempt}. "
                     + ("Reintentando..." if attempt < max_retries else "Máximo alcanzado."))
            if attempt < max_retries:
                time.sleep(3 * attempt)
        except Exception as e:
            log.warn(f"[goto] Error en intento {attempt}: {e}. "
                     + ("Reintentando..." if attempt < max_retries else "Abortando."))
            if attempt < max_retries:
                time.sleep(3 * attempt)
    log.error(f"[goto] No se pudo cargar {url} tras {max_retries} intentos.")


def _wait_for_network_quiet(page: Page, log: LogWriter,
                            idle_ms: int = 2000, timeout: int = 30_000):
    """
    Alternativa a networkidle: espera hasta `idle_ms` ms sin peticiones XHR.
    Aborta con gracia si el servidor tarda más de `timeout` ms.
    """
    try:
        page.wait_for_load_state("networkidle", timeout=timeout)
    except PlaywrightTimeout:
        # Si la página está saturada, seguimos igual con lo que tenemos
        log.warn("[red] networkidle no alcanzado, continuando de todos modos...")
    except Exception:
        pass



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


def _wait_for_options(page: Page, select_id: str, log: LogWriter,
                      timeout_ms: int = 25_000) -> list[dict]:
    """Espera hasta timeout_ms a que aparezcan opciones reales en un <select>."""
    deadline = time.time() + timeout_ms / 1000
    while time.time() < deadline:
        opts = _get_select_options(page, select_id)
        real = [o for o in opts if o["value"] != "0"]
        if real:
            return real
        time.sleep(0.5)
    return [o for o in _get_select_options(page, select_id) if o["value"] != "0"]


def setup_catalog_search(page: Page, log: LogWriter, catalog_bridge=None,
                         pre_selected: dict | None = None) -> dict | None:
    """
    Configura la busqueda en el catalogo.
    Flujo: pagina principal → Acuerdo → Catalogo → Categoria → Buscar
           → 'Agregar oferta' → CatalogoProductoIndex.
    Si pre_selected tiene los valores, los aplica directamente sin bridge.
    """
    fallback = (pre_selected or {}).copy()
    try:
        current_url = page.url
        if "t_ProductoOfertadoAmp" not in current_url:
            log.info("Navegando al catalogo de ofertas...")
            _retry_goto(page, CATALOGO_URL, log, anchor_selector="#ajaxAcuerdo")
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

        def _stop(msg):
            log.warn("%s — continuando con bulk upload" % msg)
            return fallback

        # ── Acuerdo Marco ──
        if pre_selected and pre_selected.get("acuerdo"):
            acuerdo_val = pre_selected["acuerdo"]
            log.info("Aplicando Acuerdo Marco pre-seleccionado: %s" % acuerdo_val)
        else:
            acuerdos = _get_select_options(page, "ajaxAcuerdo")
            if not acuerdos or len(acuerdos) <= 1:
                return _stop("No se encontraron Acuerdos Marco.")
            log.info("%d acuerdos disponibles." % len(acuerdos))
            acuerdo_val = catalog_bridge.request_step("acuerdo", acuerdos)
            if not acuerdo_val or acuerdo_val == "0":
                return _stop("No se selecciono un Acuerdo Marco valido.")

        log.info("Seleccionando Acuerdo Marco: %s" % acuerdo_val)
        _select2_choose(page, "ajaxAcuerdo", acuerdo_val)
        catalogos = _wait_for_options(page, "ajaxCatalogo", log, timeout_ms=60_000)
        if not catalogos:
            return _stop("No cargaron Catalogos tras seleccionar Acuerdo.")
        log.info("%d catalogos cargados." % len(catalogos))

        # ── Catalogo ──
        if pre_selected and pre_selected.get("catalogo"):
            catalogo_val = pre_selected["catalogo"]
            if not any(o["value"] == catalogo_val for o in catalogos):
                return _stop("Catalogo pre-seleccionado %s no disponible." % catalogo_val)
            log.info("Usando Catalogo pre-seleccionado: %s" % catalogo_val)
        else:
            catalogo_val = catalog_bridge.request_step("catalogo", catalogos)
            if not catalogo_val or catalogo_val == "0":
                return _stop("No se selecciono un Catalogo valido.")

        log.info("Seleccionando Catalogo: %s" % catalogo_val)
        _select_native(page, "ajaxCatalogo", catalogo_val)
        categorias = _wait_for_options(page, "ajaxCategoria", log, timeout_ms=60_000)
        if not categorias:
            return _stop("No cargaron Categorias tras seleccionar Catalogo.")
        log.info("%d categorias cargadas." % len(categorias))

        # ── Categoria ──
        if pre_selected and pre_selected.get("categoria"):
            categoria_val = pre_selected["categoria"]
            if not any(o["value"] == categoria_val for o in categorias):
                return _stop("Categoria pre-seleccionada %s no disponible." % categoria_val)
            log.info("Usando Categoria pre-seleccionada: %s" % categoria_val)
        else:
            categoria_val = catalog_bridge.request_step("categoria", categorias)
            if not categoria_val or categoria_val == "0":
                return _stop("No se selecciono una Categoria valida.")

        log.info("Seleccionando Categoria: %s" % categoria_val)
        _select_native(page, "ajaxCategoria", categoria_val)
        time.sleep(2)

        # ── Iniciar Busqueda ──
        log.info("Click en 'Iniciar Busqueda'...")
        for intento in range(3):
            try:
                page.wait_for_selector("#btnBuscar", timeout=60_000)
                page.locator("#btnBuscar").first.click(force=True)
                _wait_for_network_quiet(page, log, timeout=120_000)
                time.sleep(5)
                break
            except PlaywrightTimeout:
                log.warn(f"Intento {intento+1}/3: #btnBuscar no respondio, reintentando...")
                time.sleep(5)
        else:
            log.warn("No se encontro #btnBuscar tras 3 intentos, continuando...")

        # ── Agregar oferta ──
        log.info("Esperando boton 'Agregar oferta'...")
        for intento in range(3):
            try:
                page.wait_for_selector("#btnNuevoProducto", timeout=60_000)
                log.info("Click en 'Agregar oferta'.")
                page.locator("#btnNuevoProducto").first.click(force=True)
                _wait_for_network_quiet(page, log, timeout=120_000)
                time.sleep(5)
                break
            except PlaywrightTimeout:
                log.warn(f"Intento {intento+1}/3: #btnNuevoProducto no aparecio en 60s, reintentando...")
                if intento < 2:
                    time.sleep(5)
                    page.locator("#btnBuscar").first.click(force=True)
                    _wait_for_network_quiet(page, log, timeout=120_000)
                    time.sleep(5)
        else:
            log.warn("No aparecio #btnNuevoProducto tras 3 intentos.")

        # ── Verificar URL ──
        current = page.url
        if "CatalogoProductoIndex" not in current:
            try:
                page.wait_for_url("**CatalogoProductoIndex**", timeout=20_000)
                current = page.url
            except PlaywrightTimeout:
                pass

        if "CatalogoProductoIndex" not in current:
            log.warn("No se llego a CatalogoProductoIndex, continuando con bulk upload...")
            return {
                "acuerdo": acuerdo_val,
                "catalogo": catalogo_val,
                "categoria": categoria_val,
            }

        log.ok("Catalogo configurado -> %s" % current[:80])
        return {
            "acuerdo": acuerdo_val,
            "catalogo": catalogo_val,
            "categoria": categoria_val,
        }

    except Exception as e:
        log.warn("Excepcion en setup_catalog_search: %s — continuando con bulk upload" % e)
        fallback = pre_selected or {}
        return {
            "acuerdo": fallback.get("acuerdo", ""),
            "catalogo": fallback.get("catalogo", ""),
            "categoria": fallback.get("categoria", ""),
        }

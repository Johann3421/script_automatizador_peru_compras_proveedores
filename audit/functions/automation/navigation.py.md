# Auditoría de Funciones: `automation/navigation.py`

- **Lenguaje:** `python`
- **Líneas de código:** 289
- **Hash SHA256:** `86b27e8760a0`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _retry_goto(page, url, log, anchor_selector, max_retries)`
- **Línea inicial:** 14 | **Línea final:** 43
- **Firma completa:** `def _retry_goto(page, url, log, anchor_selector, max_retries)`
- **Propósito:** Navega a `url` con reintentos exponenciales.
Usa wait_until='domcontentloaded' (nunca 'networkidle') para evitar
timeouts en páginas del Estado que siempre tienen peticiones pendientes.
Luego espera que aparezca `anchor_selector` para confirmar que cargó.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `info, range, goto, error, sleep, wait_for_selector, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _wait_for_network_quiet(page, log, idle_ms, timeout)`
- **Línea inicial:** 46 | **Línea final:** 58
- **Firma completa:** `def _wait_for_network_quiet(page, log, idle_ms, timeout)`
- **Propósito:** Alternativa a networkidle: espera hasta `idle_ms` ms sin peticiones XHR.
Aborta con gracia si el servidor tarda más de `timeout` ms.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `warn, wait_for_load_state`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _get_select_options(page, select_id)`
- **Línea inicial:** 62 | **Línea final:** 70
- **Firma completa:** `def _get_select_options(page, select_id)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _select2_choose(page, select_id, value)`
- **Línea inicial:** 73 | **Línea final:** 111
- **Firma completa:** `def _select2_choose(page, select_id, value)`
- **Propósito:** Selecciona opción en Select2 disparando el evento change correctamente.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `count, range, is_visible, locator, click, sleep, nth, evaluate`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def _select_native(page, select_id, value)`
- **Línea inicial:** 114 | **Línea final:** 123
- **Firma completa:** `def _select_native(page, select_id, value)`
- **Propósito:** Selecciona en un <select> nativo disparando evento change vía JS.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sleep, evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _wait_for_options(page, select_id, log, timeout_ms)`
- **Línea inicial:** 126 | **Línea final:** 136
- **Firma completa:** `def _wait_for_options(page, select_id, log, timeout_ms)`
- **Propósito:** Espera hasta timeout_ms a que aparezcan opciones reales en un <select>.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_get_select_options, sleep, time`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def setup_catalog_search(page, log, catalog_bridge, pre_selected)`
- **Línea inicial:** 139 | **Línea final:** 289
- **Firma completa:** `def setup_catalog_search(page, log, catalog_bridge, pre_selected)`
- **Propósito:** Configura la busqueda en el catalogo.
Flujo: pagina principal → Acuerdo → Catalogo → Categoria → Buscar
       → 'Agregar oferta' → CatalogoProductoIndex.
Si pre_selected tiene los valores, los aplica directamente sin bridge.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_get_select_options, click, _select2_choose, info, request_step, sleep, wait_for_url, evaluate, warn, copy`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 34)

### `def _stop(msg)`
- **Línea inicial:** 166 | **Línea final:** 168
- **Firma completa:** `def _stop(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `warn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

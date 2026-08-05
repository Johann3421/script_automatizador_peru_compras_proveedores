# Documentación Técnica: `automation/navigation.py`

- **Ruta relativa:** `automation/navigation.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 289
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _retry_goto(page, url, log, anchor_selector, max_retries)` (Línea 14)
- **Propósito:** Navega a `url` con reintentos exponenciales.
Usa wait_until='domcontentloaded' (nunca 'networkidle') para evitar
timeouts en páginas del Estado que siempre tienen peticiones pendientes.
Luego espera que aparezca `anchor_selector` para confirmar que cargó.
- **Firma:** `def _retry_goto(page, url, log, anchor_selector, max_retries)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _wait_for_network_quiet(page, log, idle_ms, timeout)` (Línea 46)
- **Propósito:** Alternativa a networkidle: espera hasta `idle_ms` ms sin peticiones XHR.
Aborta con gracia si el servidor tarda más de `timeout` ms.
- **Firma:** `def _wait_for_network_quiet(page, log, idle_ms, timeout)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_select_options(page, select_id)` (Línea 62)
- **Propósito:** Sin docstring.
- **Firma:** `def _get_select_options(page, select_id)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _select2_choose(page, select_id, value)` (Línea 73)
- **Propósito:** Selecciona opción en Select2 disparando el evento change correctamente.
- **Firma:** `def _select2_choose(page, select_id, value)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _select_native(page, select_id, value)` (Línea 114)
- **Propósito:** Selecciona en un <select> nativo disparando evento change vía JS.
- **Firma:** `def _select_native(page, select_id, value)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _wait_for_options(page, select_id, log, timeout_ms)` (Línea 126)
- **Propósito:** Espera hasta timeout_ms a que aparezcan opciones reales en un <select>.
- **Firma:** `def _wait_for_options(page, select_id, log, timeout_ms)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def setup_catalog_search(page, log, catalog_bridge, pre_selected)` (Línea 139)
- **Propósito:** Configura la busqueda en el catalogo.
Flujo: pagina principal → Acuerdo → Catalogo → Categoria → Buscar
       → 'Agregar oferta' → CatalogoProductoIndex.
Si pre_selected tiene los valores, los aplica directamente sin bridge.
- **Firma:** `def setup_catalog_search(page, log, catalog_bridge, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

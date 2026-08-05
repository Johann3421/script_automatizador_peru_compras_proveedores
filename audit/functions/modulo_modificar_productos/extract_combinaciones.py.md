# Auditoría de Funciones: `modulo_modificar_productos/extract_combinaciones.py`

- **Lenguaje:** `python`
- **Líneas de código:** 272
- **Hash SHA256:** `c22145aa6f0b`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def ts()`
- **Línea inicial:** 41 | **Línea final:** 42
- **Firma completa:** `def ts()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def info(msg)`
- **Línea inicial:** 45 | **Línea final:** 46
- **Firma completa:** `def info(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `ts, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _get_options(page, select_id)`
- **Línea inicial:** 49 | **Línea final:** 57
- **Firma completa:** `def _get_options(page, select_id)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _select_value(page, select_id, value)`
- **Línea inicial:** 60 | **Línea final:** 94
- **Firma completa:** `def _select_value(page, select_id, value)`
- **Propósito:** Selecciona opcion (Select2-aware).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `count, range, is_visible, locator, click, sleep, endswith, nth, min, evaluate`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def _wait_options(page, select_id, timeout)`
- **Línea inicial:** 97 | **Línea final:** 104
- **Firma completa:** `def _wait_options(page, select_id, timeout)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sleep, _get_options, time`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def explore_level(page, select_order, depth, options)`
- **Línea inicial:** 107 | **Línea final:** 141
- **Firma completa:** `def explore_level(page, select_order, depth, options)`
- **Propósito:** Recorre exhaustivamente. Para CADA opcion en el nivel actual:
  - la selecciona
  - espera que carguen opciones en el SIGUIENTE nivel
  - llama recursivamente
select_order: lista ordenada de IDs (ej. ['ajaxCatalogo','ajaxCategoria','ajaxEstado'])
depth: indice actual dentro de select_order
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, append, _select_value, enumerate, _wait_options, explore_level, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _get_select_ids(page)`
- **Línea inicial:** 144 | **Línea final:** 153
- **Firma completa:** `def _get_select_ids(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _retry_goto(page, url, max_retries)`
- **Línea inicial:** 156 | **Línea final:** 168
- **Firma completa:** `def _retry_goto(page, url, max_retries)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `info, range, goto, sleep, wait_for_selector`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def main()`
- **Línea inicial:** 171 | **Línea final:** 268
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `do_login, info, close_browser, init_browser, wait_for_timeout, open, Event, explore_level, sleep, _select_value`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 12)

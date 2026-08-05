# Documentación Técnica: `modulo_modificar_productos/extract_combinaciones.py`

- **Ruta relativa:** `modulo_modificar_productos/extract_combinaciones.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 272
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def ts()` (Línea 41)
- **Propósito:** Sin docstring.
- **Firma:** `def ts()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def info(msg)` (Línea 45)
- **Propósito:** Sin docstring.
- **Firma:** `def info(msg)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_options(page, select_id)` (Línea 49)
- **Propósito:** Sin docstring.
- **Firma:** `def _get_options(page, select_id)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _select_value(page, select_id, value)` (Línea 60)
- **Propósito:** Selecciona opcion (Select2-aware).
- **Firma:** `def _select_value(page, select_id, value)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _wait_options(page, select_id, timeout)` (Línea 97)
- **Propósito:** Sin docstring.
- **Firma:** `def _wait_options(page, select_id, timeout)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def explore_level(page, select_order, depth, options)` (Línea 107)
- **Propósito:** Recorre exhaustivamente. Para CADA opcion en el nivel actual:
  - la selecciona
  - espera que carguen opciones en el SIGUIENTE nivel
  - llama recursivamente
select_order: lista ordenada de IDs (ej. ['ajaxCatalogo','ajaxCategoria','ajaxEstado'])
depth: indice actual dentro de select_order
- **Firma:** `def explore_level(page, select_order, depth, options)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_select_ids(page)` (Línea 144)
- **Propósito:** Sin docstring.
- **Firma:** `def _get_select_ids(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _retry_goto(page, url, max_retries)` (Línea 156)
- **Propósito:** Sin docstring.
- **Firma:** `def _retry_goto(page, url, max_retries)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def main()` (Línea 171)
- **Propósito:** Sin docstring.
- **Firma:** `def main()`
- **Retorno / Efectos:** Consulta código fuente.

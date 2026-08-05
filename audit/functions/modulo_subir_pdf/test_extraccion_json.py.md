# Auditoría de Funciones: `modulo_subir_pdf/test_extraccion_json.py`

- **Lenguaje:** `python`
- **Líneas de código:** 196
- **Hash SHA256:** `54416a8e7d12`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def extraer_json_crudo()`
- **Línea inicial:** 66 | **Línea final:** 149
- **Firma completa:** `def extraer_json_crudo()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `replace, init_browser, Event, int, info, close, open, sleep, dump, evaluate`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def _imprimir_resumen(data)`
- **Línea inicial:** 152 | **Línea final:** 186
- **Firma completa:** `def _imprimir_resumen(data)`
- **Propósito:** Imprime un resumen legible del JSON extraído.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `keys, print, list, isinstance, items, type, get, str, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def info(self, msg)`
- **Línea inicial:** 58 | **Línea final:** 58
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 59 | **Línea final:** 59
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 60 | **Línea final:** 60
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 61 | **Línea final:** 61
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

# Auditoría de Funciones: `modulo_subir_pdf/test_ficha_endpoint.py`

- **Lenguaje:** `python`
- **Líneas de código:** 78
- **Hash SHA256:** `4d9fa931b0af`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def main()`
- **Línea inicial:** 18 | **Línea final:** 75
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola, Navegación / Red HTTP
- **Dependencias / Invocaciones:** `do_login, info, close_browser, text, goto, print, append, init_browser, PrintLog, Event`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 17)

### `def info(self, m)`
- **Línea inicial:** 13 | **Línea final:** 13
- **Firma completa:** `def info(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, m)`
- **Línea inicial:** 14 | **Línea final:** 14
- **Firma completa:** `def warn(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, m)`
- **Línea inicial:** 15 | **Línea final:** 15
- **Firma completa:** `def error(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, m)`
- **Línea inicial:** 16 | **Línea final:** 16
- **Firma completa:** `def ok(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def on_request(req)`
- **Línea inicial:** 31 | **Línea final:** 37
- **Firma completa:** `def on_request(req)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def on_response(res)`
- **Línea inicial:** 38 | **Línea final:** 49
- **Firma completa:** `def on_response(res)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, get, text`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

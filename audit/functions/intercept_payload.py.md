# Auditoría de Funciones: `intercept_payload.py`

- **Lenguaje:** `python`
- **Líneas de código:** 229
- **Hash SHA256:** `36672f00cee4`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def log_msg(msg)`
- **Línea inicial:** 55 | **Línea final:** 57
- **Firma completa:** `def log_msg(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `strftime, now, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def is_interesting(url, method, post_data)`
- **Línea inicial:** 60 | **Línea final:** 69
- **Firma completa:** `def is_interesting(url, method, post_data)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, search`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def save_results()`
- **Línea inicial:** 72 | **Línea final:** 89
- **Firma completa:** `def save_results()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `isoformat, open, get, now, dump, log_msg, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def main()`
- **Línea inicial:** 92 | **Línea final:** 225
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `init_browser, Event, load, log_msg, is_closed, isoformat, lower, exit, open, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 22)

### `def on_request(request)`
- **Línea inicial:** 105 | **Línea final:** 154
- **Firma completa:** `def on_request(request)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `isoformat, dict, append, lower, save_results, loads, is_interesting, get, now, log_msg`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

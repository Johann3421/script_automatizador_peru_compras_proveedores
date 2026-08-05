# Auditoría de Funciones: `modulo_subir_pdf/test_buscar_ficha.py`

- **Lenguaje:** `python`
- **Líneas de código:** 246
- **Hash SHA256:** `a67d6c741822`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def probar_api_con_param(page, nombre, params, log)`
- **Línea inicial:** 43 | **Línea final:** 78
- **Firma completa:** `def probar_api_con_param(page, nombre, params, log)`
- **Propósito:** Probar el API con un set de params y reportar resultado.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, keys, text, time, list, replace, loads, items, isinstance, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def interceptar_busqueda_real(page, log)`
- **Línea inicial:** 81 | **Línea final:** 132
- **Firma completa:** `def interceptar_busqueda_real(page, log)`
- **Propósito:** Interceptar la búsqueda real que hace la UI cuando se busca por N° de parte.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `info, dict, goto, append, click, sleep, _select2_select, warn, locator, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def main()`
- **Línea inicial:** 135 | **Línea final:** 242
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `replace, init_browser, Event, startswith, findall, set_viewport_size, info, input, interceptar_busqueda_real, warn`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def info(self, m)`
- **Línea inicial:** 37 | **Línea final:** 37
- **Firma completa:** `def info(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, m)`
- **Línea inicial:** 38 | **Línea final:** 38
- **Firma completa:** `def warn(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, m)`
- **Línea inicial:** 39 | **Línea final:** 39
- **Firma completa:** `def error(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, m)`
- **Línea inicial:** 40 | **Línea final:** 40
- **Firma completa:** `def ok(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def on_request(req)`
- **Línea inicial:** 104 | **Línea final:** 111
- **Firma completa:** `def on_request(req)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, dict`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

# Auditoría de Funciones: `modulo_subir_pdf/discovery_perucompras.py`

- **Lenguaje:** `python`
- **Líneas de código:** 489
- **Hash SHA256:** `1eac40cc0556`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def log(msg)`
- **Línea inicial:** 153 | **Línea final:** 154
- **Firma completa:** `def log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `strftime, now, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def do_login(page)`
- **Línea inicial:** 161 | **Línea final:** 208
- **Firma completa:** `def do_login(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `click, wait_for, screenshot, point, open, input, BytesIO, sub, range, resize`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def extract_urls_from_js(js_text)`
- **Línea inicial:** 215 | **Línea final:** 223
- **Firma completa:** `def extract_urls_from_js(js_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `any, startswith, strip, findall, set, add, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def extract_urls_from_html(html_text)`
- **Línea inicial:** 226 | **Línea final:** 244
- **Firma completa:** `def extract_urls_from_html(html_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `extract_urls_from_js, split, startswith, set, BeautifulSoup, add, find_all`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def analizar_js(page)`
- **Línea inicial:** 251 | **Línea final:** 299
- **Firma completa:** `def analizar_js(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `extract_urls_from_js, len, text, list, append, split, sorted, extract_urls_from_html, log, sleep`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def clasificar_respuesta(status, url_final_str, html_text)`
- **Línea inicial:** 306 | **Línea final:** 320
- **Firma completa:** `def clasificar_respuesta(status, url_final_str, html_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, str`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def fuzz_endpoints(page, candidatos)`
- **Línea inicial:** 323 | **Línea final:** 359
- **Firma completa:** `def fuzz_endpoints(page, candidatos)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clasificar_respuesta, text, append, find, sorted, hasattr, extract_urls_from_html, log, sleep, get`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def crawl_accesibles(accesibles, ya_visitados)`
- **Línea inicial:** 366 | **Línea final:** 375
- **Firma completa:** `def crawl_accesibles(accesibles, ya_visitados)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `list, log, get, startswith, set, add, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def generar_reporte(js_info, resultados, output_dir)`
- **Línea inicial:** 382 | **Línea final:** 420
- **Firma completa:** `def generar_reporte(js_info, resultados, output_dir)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, append, items, get, log, now, strftime, len, write_text`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def main()`
- **Línea inicial:** 427 | **Línea final:** 485
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print, mkdir, launch, set_viewport_size, sort, exit, close, open, new_context, dump`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

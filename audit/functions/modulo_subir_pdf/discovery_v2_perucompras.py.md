# Auditoría de Funciones: `modulo_subir_pdf/discovery_v2_perucompras.py`

- **Lenguaje:** `python`
- **Líneas de código:** 603
- **Hash SHA256:** `6775dd3feff4`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def log(msg)`
- **Línea inicial:** 122 | **Línea final:** 123
- **Firma completa:** `def log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `strftime, now, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def do_login(page, stop_event)`
- **Línea inicial:** 130 | **Línea final:** 174
- **Firma completa:** `def do_login(page, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `click, is_set, wait_for, screenshot, point, open, BytesIO, input, sub, range`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 12)

### `def extract_all_urls(text)`
- **Línea inicial:** 181 | **Línea final:** 198
- **Firma completa:** `def extract_all_urls(text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, split, any, startswith, strip, findall, set, add, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def probe(page, path, method, data, log_func)`
- **Línea inicial:** 201 | **Línea final:** 287
- **Firma completa:** `def probe(page, path, method, data, log_func)`
- **Propósito:** Hace una request y devuelve metadata de la respuesta.
Usa fetch() desde JS para garantizar cookies y timeout correcto.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `search, bool, lower, max, find, sorted, extract_all_urls, get, startswith, get_text`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 19)

### `def recon_files(page)`
- **Línea inicial:** 294 | **Línea final:** 303
- **Firma completa:** `def recon_files(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log, sleep, append, probe`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def analizar_js_profundo(page)`
- **Línea inicial:** 306 | **Línea final:** 352
- **Firma completa:** `def analizar_js_profundo(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `len, text, list, append, split, replace, sorted, extract_all_urls, log, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def enumerar_acciones(page)`
- **Línea inicial:** 355 | **Línea final:** 370
- **Firma completa:** `def enumerar_acciones(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, log, sleep, len, probe`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def probar_post(page)`
- **Línea inicial:** 373 | **Línea final:** 392
- **Firma completa:** `def probar_post(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, log, sleep, len, probe`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def bruteforce_ids(page)`
- **Línea inicial:** 395 | **Línea final:** 406
- **Firma completa:** `def bruteforce_ids(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log, sleep, append, probe`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def analizar_headers_tecnologia(page)`
- **Línea inicial:** 409 | **Línea final:** 435
- **Firma completa:** `def analizar_headers_tecnologia(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log, evaluate, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def crawl_recursivo(page, seeds, max_depth)`
- **Línea inicial:** 438 | **Línea final:** 458
- **Firma completa:** `def crawl_recursivo(page, seeds, max_depth)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, append, log, sleep, get, startswith, any, set, add, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def generar_reporte_v2(all_results, output_dir)`
- **Línea inicial:** 465 | **Línea final:** 523
- **Firma completa:** `def generar_reporte_v2(all_results, output_dir)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `setdefault, upper, join, append, isinstance, items, sorted, log, get, values`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 23)

### `def main()`
- **Línea inicial:** 530 | **Línea final:** 599
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `recon_files, print, enumerar_acciones, mkdir, startswith, launch, fromkeys, set_viewport_size, generar_reporte_v2, bruteforce_ids`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

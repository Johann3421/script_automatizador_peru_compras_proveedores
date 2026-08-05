# Documentación Técnica: `modulo_subir_pdf/discovery_v2_perucompras.py`

- **Ruta relativa:** `modulo_subir_pdf/discovery_v2_perucompras.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 603
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def log(msg)` (Línea 122)
- **Propósito:** Sin docstring.
- **Firma:** `def log(msg)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def do_login(page, stop_event)` (Línea 130)
- **Propósito:** Sin docstring.
- **Firma:** `def do_login(page, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def extract_all_urls(text)` (Línea 181)
- **Propósito:** Sin docstring.
- **Firma:** `def extract_all_urls(text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def probe(page, path, method, data, log_func)` (Línea 201)
- **Propósito:** Hace una request y devuelve metadata de la respuesta.
Usa fetch() desde JS para garantizar cookies y timeout correcto.
- **Firma:** `def probe(page, path, method, data, log_func)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def recon_files(page)` (Línea 294)
- **Propósito:** Sin docstring.
- **Firma:** `def recon_files(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def analizar_js_profundo(page)` (Línea 306)
- **Propósito:** Sin docstring.
- **Firma:** `def analizar_js_profundo(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def enumerar_acciones(page)` (Línea 355)
- **Propósito:** Sin docstring.
- **Firma:** `def enumerar_acciones(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def probar_post(page)` (Línea 373)
- **Propósito:** Sin docstring.
- **Firma:** `def probar_post(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def bruteforce_ids(page)` (Línea 395)
- **Propósito:** Sin docstring.
- **Firma:** `def bruteforce_ids(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def analizar_headers_tecnologia(page)` (Línea 409)
- **Propósito:** Sin docstring.
- **Firma:** `def analizar_headers_tecnologia(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def crawl_recursivo(page, seeds, max_depth)` (Línea 438)
- **Propósito:** Sin docstring.
- **Firma:** `def crawl_recursivo(page, seeds, max_depth)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def generar_reporte_v2(all_results, output_dir)` (Línea 465)
- **Propósito:** Sin docstring.
- **Firma:** `def generar_reporte_v2(all_results, output_dir)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def main()` (Línea 530)
- **Propósito:** Sin docstring.
- **Firma:** `def main()`
- **Retorno / Efectos:** Consulta código fuente.

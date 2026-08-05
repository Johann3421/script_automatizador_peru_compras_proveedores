# Documentación Técnica: `modulo_subir_pdf/discovery_perucompras.py`

- **Ruta relativa:** `modulo_subir_pdf/discovery_perucompras.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 489
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def log(msg)` (Línea 153)
- **Propósito:** Sin docstring.
- **Firma:** `def log(msg)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def do_login(page)` (Línea 161)
- **Propósito:** Sin docstring.
- **Firma:** `def do_login(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def extract_urls_from_js(js_text)` (Línea 215)
- **Propósito:** Sin docstring.
- **Firma:** `def extract_urls_from_js(js_text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def extract_urls_from_html(html_text)` (Línea 226)
- **Propósito:** Sin docstring.
- **Firma:** `def extract_urls_from_html(html_text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def analizar_js(page)` (Línea 251)
- **Propósito:** Sin docstring.
- **Firma:** `def analizar_js(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def clasificar_respuesta(status, url_final_str, html_text)` (Línea 306)
- **Propósito:** Sin docstring.
- **Firma:** `def clasificar_respuesta(status, url_final_str, html_text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def fuzz_endpoints(page, candidatos)` (Línea 323)
- **Propósito:** Sin docstring.
- **Firma:** `def fuzz_endpoints(page, candidatos)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def crawl_accesibles(accesibles, ya_visitados)` (Línea 366)
- **Propósito:** Sin docstring.
- **Firma:** `def crawl_accesibles(accesibles, ya_visitados)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def generar_reporte(js_info, resultados, output_dir)` (Línea 382)
- **Propósito:** Sin docstring.
- **Firma:** `def generar_reporte(js_info, resultados, output_dir)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def main()` (Línea 427)
- **Propósito:** Sin docstring.
- **Firma:** `def main()`
- **Retorno / Efectos:** Consulta código fuente.

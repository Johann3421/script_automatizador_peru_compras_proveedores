# Auditoría de Funciones: `modulo_subir_pdf/utils_mod/audit_reporter.py`

- **Lenguaje:** `python`
- **Líneas de código:** 293
- **Hash SHA256:** `603e5aa57b14`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def audit_results(rows_data)`
- **Línea inicial:** 10 | **Línea final:** 43
- **Firma completa:** `def audit_results(rows_data)`
- **Propósito:** Analiza una lista de dicts o tuplas con la información del proceso.
row: dict(parte, descripcion, precio, stock, estado, obs)
Retorna un diccionario summary con métricas de auditoría.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, round, get, now, str, strftime, max, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def export_excel_report(rows_data, summary, output_path, modulo_nombre)`
- **Línea inicial:** 46 | **Línea final:** 178
- **Firma completa:** `def export_excel_report(rows_data, summary, output_path, modulo_nombre)`
- **Propósito:** Genera un informe completo de auditoría en formato Excel (.xlsx).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, len, lower, merge_cells, Font, Alignment, save, get_column_letter, cell, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 24)

### `def export_pdf_report(rows_data, summary, output_path, modulo_nombre)`
- **Línea inicial:** 181 | **Línea final:** 293
- **Firma completa:** `def export_pdf_report(rows_data, summary, output_path, modulo_nombre)`
- **Propósito:** Genera un informe detallado de auditoría en formato PDF (.pdf) estructurado en HTML printable.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `write, lower, open, get, endswith, str, enumerate`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

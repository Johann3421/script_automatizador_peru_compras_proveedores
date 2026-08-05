# Documentación Técnica: `modulo_subir_pdf/utils_mod/audit_reporter.py`

- **Ruta relativa:** `modulo_subir_pdf/utils_mod/audit_reporter.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 293
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def audit_results(rows_data)` (Línea 10)
- **Propósito:** Analiza una lista de dicts o tuplas con la información del proceso.
row: dict(parte, descripcion, precio, stock, estado, obs)
Retorna un diccionario summary con métricas de auditoría.
- **Firma:** `def audit_results(rows_data)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def export_excel_report(rows_data, summary, output_path, modulo_nombre)` (Línea 46)
- **Propósito:** Genera un informe completo de auditoría en formato Excel (.xlsx).
- **Firma:** `def export_excel_report(rows_data, summary, output_path, modulo_nombre)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def export_pdf_report(rows_data, summary, output_path, modulo_nombre)` (Línea 181)
- **Propósito:** Genera un informe detallado de auditoría en formato PDF (.pdf) estructurado en HTML printable.
- **Firma:** `def export_pdf_report(rows_data, summary, output_path, modulo_nombre)`
- **Retorno / Efectos:** Consulta código fuente.

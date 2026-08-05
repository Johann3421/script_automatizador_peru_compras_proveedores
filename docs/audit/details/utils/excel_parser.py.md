# Documentación Técnica: `utils/excel_parser.py`

- **Ruta relativa:** `utils/excel_parser.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 84
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def get_sheets(filepath)` (Línea 4)
- **Propósito:** Sin docstring.
- **Firma:** `def get_sheets(filepath)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def find_header_row(ws, max_scan)` (Línea 11)
- **Propósito:** Sin docstring.
- **Firma:** `def find_header_row(ws, max_scan)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def get_columns(filepath, sheet_name)` (Línea 34)
- **Propósito:** Sin docstring.
- **Firma:** `def get_columns(filepath, sheet_name)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def parse_excel(filepath, sheet_name, header_row)` (Línea 51)
- **Propósito:** Sin docstring.
- **Firma:** `def parse_excel(filepath, sheet_name, header_row)`
- **Retorno / Efectos:** Consulta código fuente.

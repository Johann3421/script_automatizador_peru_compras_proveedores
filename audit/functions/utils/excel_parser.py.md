# Auditoría de Funciones: `utils/excel_parser.py`

- **Lenguaje:** `python`
- **Líneas de código:** 84
- **Hash SHA256:** `3f287d00e01d`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def get_sheets(filepath)`
- **Línea inicial:** 4 | **Línea final:** 8
- **Firma completa:** `def get_sheets(filepath)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `close, load_workbook`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def find_header_row(ws, max_scan)`
- **Línea inicial:** 11 | **Línea final:** 31
- **Firma completa:** `def find_header_row(ws, max_scan)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, isinstance, cell, strip, min, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def get_columns(filepath, sheet_name)`
- **Línea inicial:** 34 | **Línea final:** 48
- **Firma completa:** `def get_columns(filepath, sheet_name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, append, close, cell, strip, str, find_header_row, load_workbook`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def parse_excel(filepath, sheet_name, header_row)`
- **Línea inicial:** 51 | **Línea final:** 84
- **Firma completa:** `def parse_excel(filepath, sheet_name, header_row)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, append, isinstance, close, cell, enumerate, strip, str, find_header_row, int`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

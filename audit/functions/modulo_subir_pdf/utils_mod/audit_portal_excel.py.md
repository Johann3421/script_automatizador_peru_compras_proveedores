# Auditoría de Funciones: `modulo_subir_pdf/utils_mod/audit_portal_excel.py`

- **Lenguaje:** `python`
- **Líneas de código:** 251
- **Hash SHA256:** `a336310bfcd0`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _header_font(bold, size, color)`
- **Línea inicial:** 33 | **Línea final:** 34
- **Firma completa:** `def _header_font(bold, size, color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Font`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _normal_font(bold, size, color)`
- **Línea inicial:** 36 | **Línea final:** 37
- **Firma completa:** `def _normal_font(bold, size, color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Font`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _fill(hex_color)`
- **Línea inicial:** 39 | **Línea final:** 40
- **Firma completa:** `def _fill(hex_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `PatternFill`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _border()`
- **Línea inicial:** 42 | **Línea final:** 44
- **Firma completa:** `def _border()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Side, Border`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _center()`
- **Línea inicial:** 46 | **Línea final:** 47
- **Firma completa:** `def _center()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Alignment`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _left()`
- **Línea inicial:** 49 | **Línea final:** 50
- **Firma completa:** `def _left()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Alignment`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_summary_sheet(ws, resumen)`
- **Línea inicial:** 55 | **Línea final:** 133
- **Firma completa:** `def _build_summary_sheet(ws, resumen)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, _header_font, _fill, _center, merge_cells, Font, get, cell, zip, now`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _build_detail_sheet(ws, filas)`
- **Línea inicial:** 151 | **Línea final:** 215
- **Firma completa:** `def _build_detail_sheet(ws, filas)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_header_font, _fill, _center, isinstance, Font, get_column_letter, get, cell, enumerate, _border`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def generar_excel_auditoria(filas, resumen, ruta_salida)`
- **Línea inicial:** 220 | **Línea final:** 251
- **Firma completa:** `def generar_excel_auditoria(filas, resumen, ruta_salida)`
- **Propósito:** Genera el Excel de auditoria.

filas: list[dict] — cada dict con:
    parte, descripcion, stock_excel, precio_excel, ficha,
    stock_portal, estado_portal, diferencia, resultado
    resultado in {"OK", "DIFERENCIA", "NO ENCONTRADO"}

resumen: dict — total, ok, dif, missing, tasa, acuerdo, catalogo,
    categoria, excel_file, timestamp

ruta_salida: str — path completo del .xlsx

Retorna (True, ruta_salida) | (False, mensaje_error)
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `create_sheet, makedirs, remove, _build_summary_sheet, _build_detail_sheet, save, dirname, Workbook, format_exc`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

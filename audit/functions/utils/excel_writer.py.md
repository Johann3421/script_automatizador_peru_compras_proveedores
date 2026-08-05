# Auditoría de Funciones: `utils/excel_writer.py`

- **Lenguaje:** `python`
- **Líneas de código:** 48
- **Hash SHA256:** `15db211cfee6`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def write_results(source_path, sheet_name, results)`
- **Línea inicial:** 14 | **Línea final:** 48
- **Firma completa:** `def write_results(source_path, sheet_name, results)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, load_workbook, close, save, get, cell, now, strftime, find_header_row, splitext`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

# Auditoría de Funciones: `modulo_subir_pdf/utils_mod/excel_writer_mod.py`

- **Lenguaje:** `python`
- **Líneas de código:** 58
- **Hash SHA256:** `f06e8efc8edd`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def find_data_start(ws)`
- **Línea inicial:** 12 | **Línea final:** 18
- **Firma completa:** `def find_data_start(ws)`
- **Propósito:** Encuentra la primera fila de datos (header + 1).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, strip, str, min`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def write_colored_results(source_path, sheet_name, results)`
- **Línea inicial:** 21 | **Línea final:** 58
- **Firma completa:** `def write_colored_results(source_path, sheet_name, results)`
- **Propósito:** Colorea el Excel según los resultados.
Verde (ok) = 100% match, Amarillo (differ) = falla, Rojo (not_found) = no existe.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, load_workbook, close, save, get, cell, now, strftime, find_data_start, splitext`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

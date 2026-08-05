# Auditoría de Funciones: `demo_pywebview.py`

- **Lenguaje:** `python`
- **Líneas de código:** 152
- **Hash SHA256:** `bfecb249beff`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def main()`
- **Línea inicial:** 130 | **Línea final:** 148
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `set_window, join, print, isfile, exit, create_window, PeruComprasApi, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def __init__(self)`
- **Línea inicial:** 21 | **Línea final:** 24
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def set_window(self, window)`
- **Línea inicial:** 26 | **Línea final:** 27
- **Firma completa:** `def set_window(self, window)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def minimize(self)`
- **Línea inicial:** 30 | **Línea final:** 32
- **Firma completa:** `def minimize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `minimize`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def maximize(self)`
- **Línea inicial:** 34 | **Línea final:** 36
- **Firma completa:** `def maximize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `toggle_fullscreen`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def close(self)`
- **Línea inicial:** 38 | **Línea final:** 40
- **Firma completa:** `def close(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def select_file(self)`
- **Línea inicial:** 43 | **Línea final:** 69
- **Firma completa:** `def select_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy, attributes, parse_excel, get_sheets, withdraw, Tk, askopenfilename, get, detect_columns, basename`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def load_sheet(self, sheet_name)`
- **Línea inicial:** 71 | **Línea final:** 77
- **Firma completa:** `def load_sheet(self, sheet_name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, detect_columns, parse_excel`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_process(self)`
- **Línea inicial:** 80 | **Línea final:** 82
- **Firma completa:** `def start_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def stop_process(self)`
- **Línea inicial:** 84 | **Línea final:** 86
- **Firma completa:** `def stop_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def start_stock_process(self, params)`
- **Línea inicial:** 88 | **Línea final:** 90
- **Firma completa:** `def start_stock_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def stop_stock_process(self)`
- **Línea inicial:** 92 | **Línea final:** 94
- **Firma completa:** `def stop_stock_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def start_stock_audit(self, params)`
- **Línea inicial:** 96 | **Línea final:** 98
- **Firma completa:** `def start_stock_audit(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def export_audit(self, fmt)`
- **Línea inicial:** 102 | **Línea final:** 127
- **Firma completa:** `def export_audit(self, fmt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy, attributes, upper, asksaveasfilename, export_excel_report, withdraw, Tk, export_pdf_report, audit_results`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

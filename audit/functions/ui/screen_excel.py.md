# Auditoría de Funciones: `ui/screen_excel.py`

- **Lenguaje:** `python`
- **Líneas de código:** 139
- **Hash SHA256:** `c8100a40decf`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def __init__(self, app, container)`
- **Línea inicial:** 8 | **Línea final:** 78
- **Firma completa:** `def __init__(self, app, container)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFrame, grid, CTkScrollableFrame, CTkComboBox, CTkFont, __init__, super, CTkLabel, CTkButton, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def on_enter(self)`
- **Línea inicial:** 80 | **Línea final:** 81
- **Firma completa:** `def on_enter(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _pick_file(self)`
- **Línea inicial:** 83 | **Línea final:** 105
- **Firma completa:** `def _pick_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `parse_excel, chr, split, configure, get_columns, askopenfilename, _refresh_preview, set, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _refresh_preview(self)`
- **Línea inicial:** 107 | **Línea final:** 121
- **Firma completa:** `def _refresh_preview(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy, clear, join, append, list, items, enumerate, pack, CTkLabel`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _on_back(self)`
- **Línea inicial:** 123 | **Línea final:** 124
- **Firma completa:** `def _on_back(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `show_screen`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_start(self)`
- **Línea inicial:** 126 | **Línea final:** 139
- **Firma completa:** `def _on_start(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, show_screen`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

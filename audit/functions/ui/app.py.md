# Auditoría de Funciones: `ui/app.py`

- **Lenguaje:** `python`
- **Líneas de código:** 101
- **Hash SHA256:** `2804903d0325`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def __init__(self)`
- **Línea inicial:** 12 | **Línea final:** 16
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Event, Lock`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def request(self, image_bytes)`
- **Línea inicial:** 18 | **Línea final:** 25
- **Firma completa:** `def request(self, image_bytes)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait, clear`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def respond(self, code)`
- **Línea inicial:** 27 | **Línea final:** 31
- **Firma completa:** `def respond(self, code)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def __init__(self)`
- **Línea inicial:** 36 | **Línea final:** 41
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Event, Lock`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def request_step(self, step, options)`
- **Línea inicial:** 43 | **Línea final:** 52
- **Firma completa:** `def request_step(self, step, options)`
- **Propósito:** Bloquea hasta que el usuario seleccione un valor para este paso.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait, clear`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def respond_step(self, value)`
- **Línea inicial:** 54 | **Línea final:** 58
- **Firma completa:** `def respond_step(self, value)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def __init__(self, root)`
- **Línea inicial:** 62 | **Línea final:** 91
- **Firma completa:** `def __init__(self, root)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `ScreenLogin, show_screen, CatalogBridge, Event, ScreenExcel, geometry, ScreenRun, pack, CaptchaBridge, minsize`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def show_screen(self, name)`
- **Línea inicial:** 93 | **Línea final:** 101
- **Firma completa:** `def show_screen(self, name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_rowconfigure, grid, on_enter, grid_remove, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

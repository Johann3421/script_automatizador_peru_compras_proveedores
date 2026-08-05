# Auditoría de Funciones: `modulo_subir_pdf/ctk_compat.py`

- **Lenguaje:** `python`
- **Líneas de código:** 452
- **Hash SHA256:** `f176bd1e6df6`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _ignore()`
- **Línea inicial:** 35 | **Línea final:** 41
- **Firma completa:** `def _ignore()`
- **Propósito:** Descarta kwargs CTk que tkinter no acepta.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `items`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _patch_scrollable(master)`
- **Línea inicial:** 44 | **Línea final:** 48
- **Firma completa:** `def _patch_scrollable(master)`
- **Propósito:** Si master es un CTkScrollableFrame (o cualquier contenedor con get_inner), redirigir al inner frame.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, get_inner`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def set_appearance_mode(mode)`
- **Línea inicial:** 451 | **Línea final:** 451
- **Firma completa:** `def set_appearance_mode(mode)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def set_default_color_theme(t)`
- **Línea inicial:** 452 | **Línea final:** 452
- **Firma completa:** `def set_default_color_theme(t)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __init__(self, family, size, weight)`
- **Línea inicial:** 54 | **Línea final:** 55
- **Firma completa:** `def __init__(self, family, size, weight)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __iter__(self)`
- **Línea inicial:** 56 | **Línea final:** 57
- **Firma completa:** `def __iter__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `iter`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __repr__(self)`
- **Línea inicial:** 58 | **Línea final:** 59
- **Firma completa:** `def __repr__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __init__(self, master, fg_color, corner_radius, border_width, border_color, height, width, scrollbar_button_color)`
- **Línea inicial:** 65 | **Línea final:** 75
- **Firma completa:** `def __init__(self, master, fg_color, corner_radius, border_width, border_color, height, width, scrollbar_button_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `super, configure, __init__, _patch_scrollable`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def configure(self, cnf, fg_color)`
- **Línea inicial:** 77 | **Línea final:** 85
- **Firma completa:** `def configure(self, cnf, fg_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, isinstance, configure, super, update`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def __init__(self, master, fg_color, scrollbar_button_color)`
- **Línea inicial:** 96 | **Línea final:** 110
- **Firma completa:** `def __init__(self, master, fg_color, scrollbar_button_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Scrollbar, configure, bind_all, Canvas, create_window, __init__, pack, super, bind, Frame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _on_inner_cfg(self, e)`
- **Línea inicial:** 112 | **Línea final:** 113
- **Firma completa:** `def _on_inner_cfg(self, e)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `bbox, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_canvas_cfg(self, e)`
- **Línea inicial:** 115 | **Línea final:** 116
- **Firma completa:** `def _on_canvas_cfg(self, e)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `itemconfig`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_wheel(self, e)`
- **Línea inicial:** 118 | **Línea final:** 120
- **Firma completa:** `def _on_wheel(self, e)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `int, yview_scroll`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def grid_columnconfigure(self)`
- **Línea inicial:** 123 | **Línea final:** 123
- **Firma completa:** `def grid_columnconfigure(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def grid_rowconfigure(self)`
- **Línea inicial:** 124 | **Línea final:** 124
- **Firma completa:** `def grid_rowconfigure(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_rowconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def get_inner(self)`
- **Línea inicial:** 129 | **Línea final:** 129
- **Firma completa:** `def get_inner(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __init__(self, master, text, font, text_color, fg_color, anchor, wraplength, corner_radius, justify)`
- **Línea inicial:** 135 | **Línea final:** 144
- **Firma completa:** `def __init__(self, master, text, font, text_color, fg_color, anchor, wraplength, corner_radius, justify)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `tuple, hasattr, _patch_scrollable, cget, __init__, super`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def configure(self, cnf, text, text_color, fg_color)`
- **Línea inicial:** 146 | **Línea final:** 158
- **Firma completa:** `def configure(self, cnf, text, text_color, fg_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, isinstance, items, configure, super, update`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def __init__(self, master, text, font, fg_color, hover_color, text_color, border_color, border_width, corner_radius, width, height, state, anchor, command)`
- **Línea inicial:** 164 | **Línea final:** 187
- **Firma completa:** `def __init__(self, master, text, font, fg_color, hover_color, text_color, border_color, border_width, corner_radius, width, height, state, anchor, command)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `tuple, dict, hasattr, _patch_scrollable, configure, cget, __init__, super, bind`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def configure(self, text, fg_color, text_color, state, hover_color)`
- **Línea inicial:** 190 | **Línea final:** 203
- **Firma completa:** `def configure(self, text, fg_color, text_color, state, hover_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, items, configure, super, update`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def __init__(self, master, placeholder_text, show, fg_color, border_color, text_color, height, width, corner_radius)`
- **Línea inicial:** 209 | **Línea final:** 221
- **Firma completa:** `def __init__(self, master, placeholder_text, show, fg_color, border_color, text_color, height, width, corner_radius)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `dict, insert, _patch_scrollable, __init__, super, max`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def configure(self, show, placeholder_text, state, values)`
- **Línea inicial:** 223 | **Línea final:** 234
- **Firma completa:** `def configure(self, show, placeholder_text, state, values)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, items, configure, super, update`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def __init__(self, master, values, state, command, width, height)`
- **Línea inicial:** 241 | **Línea final:** 251
- **Firma completa:** `def __init__(self, master, values, state, command, width, height)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `command, _patch_scrollable, get, __init__, super, max, bind, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def configure(self, values, state, command)`
- **Línea inicial:** 253 | **Línea final:** 270
- **Firma completa:** `def configure(self, values, state, command)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, command, configure, get, super, set, bind, update`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def set(self, value)`
- **Línea inicial:** 272 | **Línea final:** 274
- **Firma completa:** `def set(self, value)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, delete`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __init__(self, master, text, font, text_color, fg_color, border_color, corner_radius)`
- **Línea inicial:** 288 | **Línea final:** 297
- **Firma completa:** `def __init__(self, master, text, font, text_color, fg_color, border_color, corner_radius)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `IntVar, tuple, hasattr, _patch_scrollable, cget, __init__, super`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def get(self)`
- **Línea inicial:** 299 | **Línea final:** 300
- **Firma completa:** `def get(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def select(self)`
- **Línea inicial:** 302 | **Línea final:** 302
- **Firma completa:** `def select(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def deselect(self)`
- **Línea inicial:** 303 | **Línea final:** 303
- **Firma completa:** `def deselect(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def configure(self)`
- **Línea inicial:** 305 | **Línea final:** 311
- **Firma completa:** `def configure(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `super, pop, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def __init__(self, master, font, fg_color, wrap, border_width, border_color, text_color, corner_radius)`
- **Línea inicial:** 317 | **Línea final:** 327
- **Firma completa:** `def __init__(self, master, font, fg_color, wrap, border_width, border_color, text_color, corner_radius)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `super, tuple, __init__, _patch_scrollable`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def configure(self, state, fg_color, text_color)`
- **Línea inicial:** 329 | **Línea final:** 339
- **Firma completa:** `def configure(self, state, fg_color, text_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, items, configure, super, update`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def __init__(self, master, height, fg_color, progress_color, corner_radius)`
- **Línea inicial:** 346 | **Línea final:** 355
- **Firma completa:** `def __init__(self, master, height, fg_color, progress_color, corner_radius)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Style, configure, _patch_scrollable, __init__, super`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def set(self, value)`
- **Línea inicial:** 358 | **Línea final:** 360
- **Firma completa:** `def set(self, value)`
- **Propósito:** value en rango 0.0 – 1.0
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `float`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def get(self)`
- **Línea inicial:** 362 | **Línea final:** 363
- **Firma completa:** `def get(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def configure(self, cnf)`
- **Línea inicial:** 365 | **Línea final:** 372
- **Firma completa:** `def configure(self, cnf)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, isinstance, configure, super, update`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def __init__(self, master, from_, to, number_of_steps, fg_color, progress_color, button_color, corner_radius, command)`
- **Línea inicial:** 378 | **Línea final:** 384
- **Firma completa:** `def __init__(self, master, from_, to, number_of_steps, fg_color, progress_color, button_color, corner_radius, command)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `command, float, configure, _patch_scrollable, __init__, super`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def set(self, value)`
- **Línea inicial:** 386 | **Línea final:** 387
- **Firma completa:** `def set(self, value)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `super, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def configure(self, cnf, command)`
- **Línea inicial:** 389 | **Línea final:** 398
- **Firma completa:** `def configure(self, cnf, command)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pop, isinstance, command, float, configure, super, update`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def __init__(self)`
- **Línea inicial:** 405 | **Línea final:** 422
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Style, theme_use, configure, __init__, super, map`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def configure(self, fg_color)`
- **Línea inicial:** 424 | **Línea final:** 431
- **Firma completa:** `def configure(self, fg_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `super, pop, configure`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def __init__(self, master)`
- **Línea inicial:** 437 | **Línea final:** 439
- **Firma completa:** `def __init__(self, master)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `super, configure, __init__`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def configure(self, fg_color)`
- **Línea inicial:** 441 | **Línea final:** 446
- **Firma completa:** `def configure(self, fg_color)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `super, pop, configure`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

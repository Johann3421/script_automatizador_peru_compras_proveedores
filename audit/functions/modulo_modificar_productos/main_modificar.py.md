# Auditoría de Funciones: `modulo_modificar_productos/main_modificar.py`

- **Lenguaje:** `python`
- **Líneas de código:** 1076
- **Hash SHA256:** `34e29dd13e34`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def __init__(self)`
- **Línea inicial:** 36 | **Línea final:** 41
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Event, Lock`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def request(self, img)`
- **Línea inicial:** 43 | **Línea final:** 55
- **Firma completa:** `def request(self, img)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_set, wait, clear, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def respond(self, code)`
- **Línea inicial:** 57 | **Línea final:** 61
- **Firma completa:** `def respond(self, code)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def __init__(self)`
- **Línea inicial:** 69 | **Línea final:** 95
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `poll_queue, _build_ui, set_appearance_mode, Event, _load_dropdown_json, geometry, __init__, Queue, set_default_color_theme, CaptchaBridge`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _load_dropdown_json(self)`
- **Línea inicial:** 97 | **Línea final:** 107
- **Firma completa:** `def _load_dropdown_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `isfile, load, open, join`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _build_ui(self)`
- **Línea inicial:** 111 | **Línea final:** 202
- **Firma completa:** `def _build_ui(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_rowconfigure, _build_opciones_section, _build_catalog_section, _build_excel_section, grid, _build_execution_section, grid_columnconfigure, CTkScrollableFrame, pack, CTkFont`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_credentials_section(self, parent)`
- **Línea inicial:** 206 | **Línea final:** 249
- **Firma completa:** `def _build_credentials_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, CTkFrame, grid, CTkCheckBox, CTkEntry, _section_label, CTkFont, CTkLabel, CTkButton, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _toggle_password(self)`
- **Línea inicial:** 251 | **Línea final:** 254
- **Firma completa:** `def _toggle_password(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_excel_section(self, parent)`
- **Línea inicial:** 258 | **Línea final:** 313
- **Firma completa:** `def _build_excel_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFrame, grid, _section_label, CTkComboBox, pack, CTkFont, CTkLabel, CTkButton, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _pick_excel(self)`
- **Línea inicial:** 315 | **Línea final:** 335
- **Firma completa:** `def _pick_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_sheets, configure, _on_sheet_changed, askopenfilename, set, basename`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_sheet_changed(self, choice)`
- **Línea inicial:** 337 | **Línea final:** 403
- **Firma completa:** `def _on_sheet_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `parse_excel, isdigit, iter_rows, append, replace, lower, close, configure, strip, str`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 28)

### `def _build_catalog_section(self, parent)`
- **Línea inicial:** 407 | **Línea final:** 457
- **Firma completa:** `def _build_catalog_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_catalogo_changed, CTkFrame, grid, get, _section_label, CTkComboBox, CTkFont, _opts_texts, set, CTkLabel`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _opts_texts(self, data)`
- **Línea inicial:** 459 | **Línea final:** 460
- **Firma completa:** `def _opts_texts(self, data)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _find_children(self, combo_text)`
- **Línea inicial:** 462 | **Línea final:** 468
- **Firma completa:** `def _find_children(self, combo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _on_catalogo_changed(self, choice)`
- **Línea inicial:** 470 | **Línea final:** 479
- **Firma completa:** `def _on_catalogo_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_find_children, configure, _on_categoria_changed, _opts_texts, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _on_categoria_changed(self, choice)`
- **Línea inicial:** 481 | **Línea final:** 498
- **Firma completa:** `def _on_categoria_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, configure, get, strip, _opts_texts, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _build_opciones_section(self, parent)`
- **Línea inicial:** 502 | **Línea final:** 538
- **Firma completa:** `def _build_opciones_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFrame, grid, configure, _section_label, CTkFont, set, CTkLabel, CTkSlider, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_execution_section(self, parent)`
- **Línea inicial:** 542 | **Línea final:** 591
- **Firma completa:** `def _build_execution_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_rowconfigure, CTkProgressBar, CTkTextbox, _build_captcha_panel, CTkFrame, grid, configure, _section_label, _make_stat, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _make_stat(self, parent, label, color, col)`
- **Línea inicial:** 593 | **Línea final:** 599
- **Firma completa:** `def _make_stat(self, parent, label, color, col)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFrame, grid, pack, CTkLabel, CTkFont`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_captcha_panel(self, parent)`
- **Línea inicial:** 603 | **Línea final:** 631
- **Firma completa:** `def _build_captcha_panel(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_captcha_submit, bind, grid, grid_remove, grid_columnconfigure, CTkEntry, CTkFont, CTkLabel, CTkButton, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _show_captcha(self, image_bytes)`
- **Línea inicial:** 633 | **Línea final:** 640
- **Firma completa:** `def _show_captcha(self, image_bytes)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `CTkImage, grid, delete, resize, open, configure, focus_set, BytesIO`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _hide_captcha_panel(self)`
- **Línea inicial:** 642 | **Línea final:** 643
- **Firma completa:** `def _hide_captcha_panel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_remove`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_captcha_submit(self)`
- **Línea inicial:** 645 | **Línea final:** 650
- **Firma completa:** `def _on_captcha_submit(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, strip, _hide_captcha_panel, respond, _log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _section_label(self, parent, text, row)`
- **Línea inicial:** 654 | **Línea final:** 658
- **Firma completa:** `def _section_label(self, parent, text, row)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid, CTkFont, CTkLabel`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(self, msg, level)`
- **Línea inicial:** 660 | **Línea final:** 665
- **Firma completa:** `def _log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, append, see, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_test(self)`
- **Línea inicial:** 669 | **Línea final:** 711
- **Firma completa:** `def _on_test(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, split, delete, configure, hasattr, get, strip, _hide_captcha_panel, _val`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _execute_test(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 713 | **Línea final:** 832
- **Firma completa:** `def _execute_test(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `process_single_product, init_browser, apply_dropdowns_and_search, LogWriter, is_set, set_viewport_size, after, info, put, hasattr`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 29)

### `def _on_launch(self)`
- **Línea inicial:** 836 | **Línea final:** 913
- **Firma completa:** `def _on_launch(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, parse_excel, bool, split, delete, configure, get, strip, _hide_captcha_panel, _val`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)`
- **Línea inicial:** 915 | **Línea final:** 990
- **Firma completa:** `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `init_browser, LogWriter, is_set, set_viewport_size, info, put, hasattr, sleep, basename, warn`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 21)

### `def _on_stop(self)`
- **Línea inicial:** 992 | **Línea final:** 997
- **Firma completa:** `def _on_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, set, _log, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _reset_after_stop(self)`
- **Línea inicial:** 999 | **Línea final:** 1003
- **Firma completa:** `def _reset_after_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def poll_queue(self)`
- **Línea inicial:** 1007 | **Línea final:** 1067
- **Firma completa:** `def poll_queue(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, len, _show_captcha, isinstance, configure, get, is_set, str, set, _log`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def _val(combo)`
- **Línea inicial:** 682 | **Línea final:** 684
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 897 | **Línea final:** 899
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

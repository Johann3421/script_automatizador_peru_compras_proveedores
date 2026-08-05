# Auditoría de Funciones: `ui/screen_run.py`

- **Lenguaje:** `python`
- **Líneas de código:** 359
- **Hash SHA256:** `e211b8844238`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def __init__(self, app, container)`
- **Línea inicial:** 18 | **Línea final:** 81
- **Firma completa:** `def __init__(self, app, container)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkProgressBar, CTkTextbox, _build_captcha_panel, rowconfigure, grid, CTkFrame, grid_remove, configure, CTkButton, _build_catalog_panel`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_captcha_panel(self)`
- **Línea inicial:** 85 | **Línea final:** 112
- **Firma completa:** `def _build_captcha_panel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_captcha_submit, bind, grid, grid_remove, grid_columnconfigure, CTkEntry, CTkFont, CTkLabel, CTkButton, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _show_captcha(self, image_bytes)`
- **Línea inicial:** 114 | **Línea final:** 122
- **Firma completa:** `def _show_captcha(self, image_bytes)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `CTkImage, _hide_catalog, grid, delete, resize, open, configure, focus_set, BytesIO`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _hide_captcha(self)`
- **Línea inicial:** 124 | **Línea final:** 125
- **Firma completa:** `def _hide_captcha(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_remove`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_captcha_submit(self)`
- **Línea inicial:** 127 | **Línea final:** 132
- **Firma completa:** `def _on_captcha_submit(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_append_log, get, strip, _hide_captcha, respond`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _build_catalog_panel(self)`
- **Línea inicial:** 136 | **Línea final:** 163
- **Firma completa:** `def _build_catalog_panel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid, grid_remove, grid_columnconfigure, CTkComboBox, CTkFont, CTkLabel, CTkButton, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _show_catalog_step(self, step, options)`
- **Línea inicial:** 165 | **Línea final:** 179
- **Firma completa:** `def _show_catalog_step(self, step, options)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid, configure, get, _hide_captcha, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _hide_catalog(self)`
- **Línea inicial:** 181 | **Línea final:** 182
- **Firma completa:** `def _hide_catalog(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_remove`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_catalog_step_submit(self)`
- **Línea inicial:** 184 | **Línea final:** 190
- **Firma completa:** `def _on_catalog_step_submit(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `respond_step, split, configure, _append_log, get, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def on_enter(self)`
- **Línea inicial:** 194 | **Línea final:** 217
- **Firma completa:** `def on_enter(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `poll_queue, clear, _hide_catalog, delete, grid_remove, configure, _hide_captcha, set, Thread, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _run_automation(self)`
- **Línea inicial:** 219 | **Línea final:** 273
- **Firma completa:** `def _run_automation(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `do_login, info, close_browser, init_browser, LogWriter, error, is_set, run_offer_loop, setup_catalog_search, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def poll_queue(self)`
- **Línea inicial:** 275 | **Línea final:** 298
- **Firma completa:** `def poll_queue(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, _show_captcha, is_set, _handle_item, _show_catalog_step, get_nowait`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def _handle_item(self, item)`
- **Línea inicial:** 300 | **Línea final:** 328
- **Firma completa:** `def _handle_item(self, item)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, grid, configure, _append_log, get, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _append_log(self, msg, level)`
- **Línea inicial:** 330 | **Línea final:** 334
- **Firma completa:** `def _append_log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, see, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_stop(self)`
- **Línea inicial:** 336 | **Línea final:** 339
- **Firma completa:** `def _on_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, _append_log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _download_log(self)`
- **Línea inicial:** 341 | **Línea final:** 356
- **Firma completa:** `def _download_log(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `writerow, asksaveasfilename, open, _append_log, writer`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_new(self)`
- **Línea inicial:** 358 | **Línea final:** 359
- **Firma completa:** `def _on_new(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `show_screen`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

# Auditoría de Funciones: `modulo_subir_pdf/main_subir_pdf.py`

- **Lenguaje:** `python`
- **Líneas de código:** 3463
- **Hash SHA256:** `1e0ef0006b12`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _make_stock_log(append_fn)`
- **Línea inicial:** 171 | **Línea final:** 179
- **Firma completa:** `def _make_stock_log(append_fn)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_StockLog, str, append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def run_app()`
- **Línea inicial:** 3322 | **Línea final:** 3457
- **Firma completa:** `def run_app()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr, join, Event, CaptchaBridge, insert, strftime, _load_dropdown_json, start, isfile, set_window`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 19)

### `def __init__(self, parent)`
- **Línea inicial:** 81 | **Línea final:** 142
- **Firma completa:** `def __init__(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `attributes, set, super, configure, geometry, CTkFont, CTkProgressBar, place, __init__, after`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _step(self)`
- **Línea inicial:** 144 | **Línea final:** 152
- **Firma completa:** `def _step(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, set, configure, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _finish(self)`
- **Línea inicial:** 154 | **Línea final:** 159
- **Firma completa:** `def _finish(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `deiconify, destroy`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def __init__(self)`
- **Línea inicial:** 200 | **Línea final:** 205
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Event, Lock`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def request(self, img)`
- **Línea inicial:** 207 | **Línea final:** 219
- **Firma completa:** `def request(self, img)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait, is_set, clear, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def respond(self, code)`
- **Línea inicial:** 221 | **Línea final:** 225
- **Firma completa:** `def respond(self, code)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def __init__(self)`
- **Línea inicial:** 269 | **Línea final:** 299
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Event, CaptchaBridge, geometry, poll_queue, set_appearance_mode, Queue, SplashScreen, __init__, minsize, withdraw`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _load_dropdown_json(self)`
- **Línea inicial:** 301 | **Línea final:** 325
- **Firma completa:** `def _load_dropdown_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `insert, dirname, open, resource_path, abspath, isfile, load`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _setup_styles(self)`
- **Línea inicial:** 365 | **Línea final:** 391
- **Firma completa:** `def _setup_styles(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `map, Style, theme_use, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _set_taskbar_icon(self)`
- **Línea inicial:** 393 | **Línea final:** 402
- **Firma completa:** `def _set_taskbar_icon(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `GetParent, ShowWindow, winfo_id, SetWindowLongW, GetWindowLongW`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _start_drag(self, event)`
- **Línea inicial:** 404 | **Línea final:** 406
- **Firma completa:** `def _start_drag(self, event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _drag_window(self, event)`
- **Línea inicial:** 408 | **Línea final:** 413
- **Firma completa:** `def _drag_window(self, event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `winfo_x, winfo_y, geometry, getattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _close_window(self)`
- **Línea inicial:** 415 | **Línea final:** 418
- **Firma completa:** `def _close_window(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `exit, destroy`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _open_config_dialog(self)`
- **Línea inicial:** 420 | **Línea final:** 503
- **Firma completa:** `def _open_config_dialog(self)`
- **Propósito:** Abre la ventana modal de Configuración y Preferencias del Sistema.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `update_idletasks, geometry, Button, title, winfo_screenheight, pack, showinfo, insert, Label, resizable`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _open_about_dialog(self)`
- **Línea inicial:** 505 | **Línea final:** 555
- **Firma completa:** `def _open_about_dialog(self)`
- **Propósito:** Abre la ventana modal Acerca del Sistema.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `update_idletasks, geometry, configure, Button, Label, Toplevel, title, transient, winfo_screenheight, grab_set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _minimize_window(self)`
- **Línea inicial:** 557 | **Línea final:** 565
- **Firma completa:** `def _minimize_window(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `update_idletasks, overrideredirect, iconify, bind`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _on_window_map(self, event)`
- **Línea inicial:** 567 | **Línea final:** 576
- **Firma completa:** `def _on_window_map(self, event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `state, _set_taskbar_icon, getattr, overrideredirect, unbind`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _toggle_maximize(self)`
- **Línea inicial:** 578 | **Línea final:** 598
- **Firma completa:** `def _toggle_maximize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `state, ShowWindow, config, getattr, winfo_id, hasattr`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def _build_ui(self)`
- **Línea inicial:** 618 | **Línea final:** 987
- **Firma completa:** `def _build_ui(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `build_instructions_tab, _on_catalogo_changed, bind, _on_sheet_changed, tag_configure, _set_taskbar_icon, Button, add_separator, config, place`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _clear_excel(self)`
- **Línea inicial:** 989 | **Línea final:** 997
- **Firma completa:** `def _clear_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_children, delete, config, hasattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _switch_view(self, view_id)`
- **Línea inicial:** 999 | **Línea final:** 1022
- **Firma completa:** `def _switch_view(self, view_id)`
- **Propósito:** Cambia la vista activa y resalta el tab horizontal correspondiente.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_forget, config, get, items, grid, hasattr`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _collect_tree_rows(self)`
- **Línea inicial:** 1026 | **Línea final:** 1041
- **Firma completa:** `def _collect_tree_rows(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_children, len, append, hasattr, item`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _run_auditor_check(self, modulo_nombre)`
- **Línea inicial:** 1043 | **Línea final:** 1051
- **Firma completa:** `def _run_auditor_check(self, modulo_nombre)`
- **Propósito:** Ejecuta el chequeo rápido del auditor sobre las fichas procesadas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `audit_results, config, _collect_tree_rows, hasattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _export_audit_report(self, fmt, modulo_nombre)`
- **Línea inicial:** 1053 | **Línea final:** 1089
- **Firma completa:** `def _export_audit_report(self, fmt, modulo_nombre)`
- **Propósito:** Genera y guarda el informe de auditoría en Excel (.xlsx) o PDF/HTML.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `replace, _run_auditor_check, asksaveasfilename, export_pdf_report, showwarning, strftime, showerror, export_excel_report, now, upper`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _update_tools_excel_status(self)`
- **Línea inicial:** 1091 | **Línea final:** 1105
- **Firma completa:** `def _update_tools_excel_status(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `config, len, getattr, basename, hasattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _build_advanced_tools_tab(self, parent)`
- **Línea inicial:** 1107 | **Línea final:** 1214
- **Firma completa:** `def _build_advanced_tools_tab(self, parent)`
- **Propósito:** Vista de Herramientas Avanzadas — diagnóstico y scrapers en Tkinter nativo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, Canvas, bind, Frame, create_window, Label, make_action_btn, _update_tools_excel_status, Button, create_tool_card`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _build_stock_tab(self, left_col, right_col, parent)`
- **Línea inicial:** 1218 | **Línea final:** 1472
- **Firma completa:** `def _build_stock_tab(self, left_col, right_col, parent)`
- **Propósito:** Vista de Análisis de Stock — paleta institucional light.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_stock_acuerdo_changed, _section_label, enumerate, grid_columnconfigure, pack, Event, set, insert, CTkButton, get`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _export_stock_audit_report(self, fmt)`
- **Línea inicial:** 1489 | **Línea final:** 1523
- **Firma completa:** `def _export_stock_audit_report(self, fmt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `round, asksaveasfilename, export_pdf_report, showwarning, getattr, strftime, showerror, export_excel_report, now, upper`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_load_stock_excel(self)`
- **Línea inicial:** 1525 | **Línea final:** 1553
- **Firma completa:** `def _on_load_stock_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, len, askopenfilename, join, basename, analizar_excel_stock`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_download_stock_template(self)`
- **Línea inicial:** 1555 | **Línea final:** 1577
- **Firma completa:** `def _on_download_stock_template(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_append_stock_log, asksaveasfilename, save, Workbook, append`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _load_stock_combos_json(self)`
- **Línea inicial:** 1579 | **Línea final:** 1595
- **Firma completa:** `def _load_stock_combos_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `_append_stock_log, insert, dirname, open, resource_path, abspath, load`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_acuerdo_changed(self, acuerdo_text)`
- **Línea inicial:** 1597 | **Línea final:** 1617
- **Firma completa:** `def _on_stock_acuerdo_changed(self, acuerdo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, _on_stock_catalogo_changed, get, add, sorted`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_catalogo_changed(self, catalogo_text)`
- **Línea inicial:** 1619 | **Línea final:** 1640
- **Firma completa:** `def _on_stock_catalogo_changed(self, catalogo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, get, add, sorted, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_start(self)`
- **Línea inicial:** 1642 | **Línea final:** 1691
- **Firma completa:** `def _on_stock_start(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_append_stock_log, configure, Thread, get, clear, float, start, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def _on_stock_stop(self)`
- **Línea inicial:** 1693 | **Línea final:** 1707
- **Firma completa:** `def _on_stock_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, _append_stock_log, configure, getattr, close`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _append_stock_log(self, msg)`
- **Línea inicial:** 1709 | **Línea final:** 1718
- **Firma completa:** `def _append_stock_log(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, see, configure, insert`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _execute_stock(self, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Línea inicial:** 1720 | **Línea final:** 1729
- **Firma completa:** `def _execute_stock(self, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_stock`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_stock_audit_start(self)`
- **Línea inicial:** 1733 | **Línea final:** 1815
- **Firma completa:** `def _on_stock_audit_start(self)`
- **Propósito:** Handler del botón '🔍 Auditar Portal'.
Valida credenciales y utiliza el Excel ya subido en la aplicación (pestaña Stock u Ofertas),
luego lanza execute_auditor en un hilo en segundo plano.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_append_stock_log, configure, Thread, str, bool, get, getattr, clear, showwarning, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 34)

### `def _on_audit_done(self, filas, resumen)`
- **Línea inicial:** 1817 | **Línea final:** 1878
- **Firma completa:** `def _on_audit_done(self, filas, resumen)`
- **Propósito:** Callback llamado por execute_auditor cuando termina.
Siempre se ejecuta en el hilo del auditor — usa self.after() para UI.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_append_stock_log, configure, asksaveasfilename, get, join, generar_excel_auditoria, strftime, after, _ui_done, Popen`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def _build_credentials_section(self, parent)`
- **Línea inicial:** 1879 | **Línea final:** 1931
- **Firma completa:** `def _build_credentials_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFont, insert, CTkButton, _section_label, grid, grid_columnconfigure, CTkCheckBox, CTkLabel, CTkEntry, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _toggle_password(self)`
- **Línea inicial:** 1933 | **Línea final:** 1936
- **Firma completa:** `def _toggle_password(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_excel_section(self, parent)`
- **Línea inicial:** 1940 | **Línea final:** 2003
- **Firma completa:** `def _build_excel_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFont, CTkButton, CTkComboBox, _section_label, grid, grid_columnconfigure, pack, CTkLabel, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _pick_excel(self)`
- **Línea inicial:** 2005 | **Línea final:** 2036
- **Firma completa:** `def _pick_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_sheets, set, configure, _on_sheet_changed, insert, config, _update_tools_excel_status, askopenfilename, delete, basename`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _on_sheet_changed(self, choice)`
- **Línea inicial:** 2038 | **Línea final:** 2107
- **Firma completa:** `def _on_sheet_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `parse_excel, config, enumerate, set, insert, get_children, get, len, delete, detect_columns`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 31)

### `def _build_catalog_section(self, parent)`
- **Línea inicial:** 2111 | **Línea final:** 2169
- **Firma completa:** `def _build_catalog_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, dict, _on_catalogo_changed, CTkFont, get, CTkComboBox, _section_label, grid, grid_columnconfigure, CTkLabel`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _opts_texts(self, data)`
- **Línea inicial:** 2171 | **Línea final:** 2172
- **Firma completa:** `def _opts_texts(self, data)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _find_children(self, combo_text)`
- **Línea inicial:** 2174 | **Línea final:** 2180
- **Firma completa:** `def _find_children(self, combo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, get, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _on_catalogo_changed(self, choice)`
- **Línea inicial:** 2182 | **Línea final:** 2191
- **Firma completa:** `def _on_catalogo_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, _find_children, _opts_texts, _on_categoria_changed`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _on_categoria_changed(self, choice)`
- **Línea inicial:** 2193 | **Línea final:** 2210
- **Firma completa:** `def _on_categoria_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, get, split, _opts_texts, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_extract_json_portal(self)`
- **Línea inicial:** 2212 | **Línea final:** 2247
- **Firma completa:** `def _on_extract_json_portal(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `evaluate_js, Thread, bool, get, getattr, print, len, dumps, basename, start`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def _build_opciones_section(self, parent)`
- **Línea inicial:** 2251 | **Línea final:** 2292
- **Firma completa:** `def _build_opciones_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, CTkFont, CTkSlider, _section_label, grid, grid_columnconfigure, CTkLabel, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_execution_section(self, parent)`
- **Línea inicial:** 2296 | **Línea final:** 2356
- **Firma completa:** `def _build_execution_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_make_stat, set, _build_captcha_panel, configure, CTkFont, CTkProgressBar, CTkTextbox, tag_config, _section_label, grid`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _make_stat(self, parent, label, color, col)`
- **Línea inicial:** 2358 | **Línea final:** 2366
- **Firma completa:** `def _make_stat(self, parent, label, color, col)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFont, grid, pack, CTkLabel, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_captcha_panel(self, parent)`
- **Línea inicial:** 2370 | **Línea final:** 2403
- **Firma completa:** `def _build_captcha_panel(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `bind, CTkButton, CTkFont, grid, CTkEntry, _on_captcha_submit, grid_columnconfigure, CTkLabel, grid_remove, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _show_captcha(self, image_bytes)`
- **Línea inicial:** 2405 | **Línea final:** 2412
- **Firma completa:** `def _show_captcha(self, image_bytes)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `configure, focus_set, resize, open, grid, delete, CTkImage, BytesIO`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _hide_captcha_panel(self)`
- **Línea inicial:** 2414 | **Línea final:** 2415
- **Firma completa:** `def _hide_captcha_panel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_remove`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_captcha_submit(self)`
- **Línea inicial:** 2417 | **Línea final:** 2422
- **Firma completa:** `def _on_captcha_submit(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, _hide_captcha_panel, respond, _log, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _section_label(self, parent, text, row)`
- **Línea inicial:** 2426 | **Línea final:** 2432
- **Firma completa:** `def _section_label(self, parent, text, row)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid, CTkLabel, CTkFont`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(self, msg, level)`
- **Línea inicial:** 2434 | **Línea final:** 2439
- **Firma completa:** `def _log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, see, configure, insert`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_test(self)`
- **Línea inicial:** 2443 | **Línea final:** 2485
- **Firma completa:** `def _on_test(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, _val, Thread, bool, get, _hide_captcha_panel, clear, delete, split`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_certs_only(self)`
- **Línea inicial:** 2487 | **Línea final:** 2533
- **Firma completa:** `def _on_certs_only(self)`
- **Propósito:** Handler del botón 'Solo Certificaciones': entra a cada ficha y agrega ISO 9001/14001.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, _val, Thread, bool, get, _hide_captcha_panel, clear, delete, split`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_extract(self)`
- **Línea inicial:** 2535 | **Línea final:** 2569
- **Firma completa:** `def _on_extract(self)`
- **Propósito:** Handler del botón 'Extraer Reportes': descarga reportes de Producto Ofertado.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, Thread, bool, get, _hide_captcha_panel, clear, delete, start, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _execute_extract(self, usuario, password, headless)`
- **Línea inicial:** 2570 | **Línea final:** 2572
- **Firma completa:** `def _execute_extract(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_extract`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _execute_certs_only(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2573 | **Línea final:** 2575
- **Firma completa:** `def _execute_certs_only(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_certs_only`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_nro_parte(self)`
- **Línea inicial:** 2576 | **Línea final:** 2623
- **Firma completa:** `def _on_nro_parte(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, _val, Thread, bool, get, _hide_captcha_panel, clear, delete, split`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _execute_nro_parte(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2625 | **Línea final:** 2627
- **Firma completa:** `def _execute_nro_parte(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_nro_parte`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_compare(self)`
- **Línea inicial:** 2628 | **Línea final:** 2665
- **Firma completa:** `def _on_compare(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, _val, Thread, bool, get, _hide_captcha_panel, clear, getattr, delete`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_compare(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2667 | **Línea final:** 2669
- **Firma completa:** `def _execute_compare(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_compare`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_discovery(self)`
- **Línea inicial:** 2670 | **Línea final:** 2693
- **Firma completa:** `def _on_discovery(self)`
- **Propósito:** Handler del botón 'Discovery': ejecuta el script discovery_perucompras.py.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, Thread, bool, get, _hide_captcha_panel, clear, getattr, delete, start`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_discovery(self, usuario, password, headless)`
- **Línea inicial:** 2695 | **Línea final:** 2697
- **Firma completa:** `def _execute_discovery(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_discovery`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_discovery2(self)`
- **Línea inicial:** 2698 | **Línea final:** 2721
- **Firma completa:** `def _on_discovery2(self)`
- **Propósito:** Handler del botón 'Discovery v2': scraping profundo multi-técnica.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, Thread, bool, get, _hide_captcha_panel, clear, getattr, delete, start`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_discovery2(self, usuario, password, headless)`
- **Línea inicial:** 2723 | **Línea final:** 2725
- **Firma completa:** `def _execute_discovery2(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_discovery2`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _execute_test(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2726 | **Línea final:** 2728
- **Firma completa:** `def _execute_test(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_test`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_launch(self)`
- **Línea inicial:** 2743 | **Línea final:** 2810
- **Firma completa:** `def _on_launch(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, _val, Thread, bool, len, _hide_captcha_panel, clear, get, delete`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)`
- **Línea inicial:** 2812 | **Línea final:** 2822
- **Firma completa:** `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_stop(self)`
- **Línea inicial:** 2823 | **Línea final:** 2832
- **Firma completa:** `def _on_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, set, configure, _log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _reset_after_stop(self)`
- **Línea inicial:** 2834 | **Línea final:** 2844
- **Firma completa:** `def _reset_after_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def poll_queue(self)`
- **Línea inicial:** 2869 | **Línea final:** 2929
- **Firma completa:** `def poll_queue(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, configure, isinstance, is_set, str, get, len, after, get_nowait, _log`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def __init__(self, val)`
- **Línea inicial:** 2968 | **Línea final:** 2969
- **Firma completa:** `def __init__(self, val)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def get(self)`
- **Línea inicial:** 2970 | **Línea final:** 2971
- **Firma completa:** `def get(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def set(self, val)`
- **Línea inicial:** 2972 | **Línea final:** 2974
- **Firma completa:** `def set(self, val)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def configure(self)`
- **Línea inicial:** 2975 | **Línea final:** 2975
- **Firma completa:** `def configure(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def config(self)`
- **Línea inicial:** 2976 | **Línea final:** 2976
- **Firma completa:** `def config(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def delete(self)`
- **Línea inicial:** 2977 | **Línea final:** 2977
- **Firma completa:** `def delete(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def insert(self)`
- **Línea inicial:** 2978 | **Línea final:** 2978
- **Firma completa:** `def insert(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def see(self)`
- **Línea inicial:** 2979 | **Línea final:** 2979
- **Firma completa:** `def see(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def pack(self)`
- **Línea inicial:** 2980 | **Línea final:** 2980
- **Firma completa:** `def pack(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def place(self)`
- **Línea inicial:** 2981 | **Línea final:** 2981
- **Firma completa:** `def place(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def grid(self)`
- **Línea inicial:** 2982 | **Línea final:** 2982
- **Firma completa:** `def grid(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def destroy(self)`
- **Línea inicial:** 2983 | **Línea final:** 2983
- **Firma completa:** `def destroy(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def bind(self)`
- **Línea inicial:** 2984 | **Línea final:** 2984
- **Firma completa:** `def bind(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def unbind(self)`
- **Línea inicial:** 2985 | **Línea final:** 2985
- **Firma completa:** `def unbind(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __call__(self)`
- **Línea inicial:** 2986 | **Línea final:** 2986
- **Firma completa:** `def __call__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __init__(self, app)`
- **Línea inicial:** 2992 | **Línea final:** 2995
- **Firma completa:** `def __init__(self, app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def set_window(self, w)`
- **Línea inicial:** 2997 | **Línea final:** 2998
- **Firma completa:** `def set_window(self, w)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def get_catalog_options(self)`
- **Línea inicial:** 3000 | **Línea final:** 3002
- **Firma completa:** `def get_catalog_options(self)`
- **Propósito:** Devuelve las opciones desplegables del archivo JSON.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def minimize(self)`
- **Línea inicial:** 3005 | **Línea final:** 3006
- **Firma completa:** `def minimize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `minimize`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def maximize(self)`
- **Línea inicial:** 3008 | **Línea final:** 3009
- **Firma completa:** `def maximize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `toggle_fullscreen`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def close(self)`
- **Línea inicial:** 3011 | **Línea final:** 3012
- **Firma completa:** `def close(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def select_file(self)`
- **Línea inicial:** 3015 | **Línea final:** 3032
- **Firma completa:** `def select_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_sheets, attributes, Tk, parse_excel, destroy, get, askopenfilename, withdraw, detect_columns, basename`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def select_stock_file(self)`
- **Línea inicial:** 3035 | **Línea final:** 3072
- **Firma completa:** `def select_stock_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_sheets, attributes, Tk, parse_excel, destroy, iterrows, str, get, askopenfilename, withdraw`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def select_json_file(self)`
- **Línea inicial:** 3075 | **Línea final:** 3105
- **Firma completa:** `def select_json_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `attributes, Tk, destroy, isinstance, parse_excel_precios, str, get, askopenfilename, withdraw, endswith`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def load_sheet(self, sheet_name)`
- **Línea inicial:** 3107 | **Línea final:** 3113
- **Firma completa:** `def load_sheet(self, sheet_name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `parse_excel, detect_columns, get, getattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_process(self, params)`
- **Línea inicial:** 3116 | **Línea final:** 3130
- **Firma completa:** `def start_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, get, _DummyWidget, float, _on_launch`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def stop_process(self)`
- **Línea inicial:** 3132 | **Línea final:** 3137
- **Firma completa:** `def stop_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _on_stop`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_stock_process(self, params)`
- **Línea inicial:** 3140 | **Línea final:** 3170
- **Firma completa:** `def start_stock_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_stock_start, str, get, _DummyWidget, getattr, analizar_excel_stock, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def start_stock_audit(self, params)`
- **Línea inicial:** 3172 | **Línea final:** 3200
- **Firma completa:** `def start_stock_audit(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, get, _DummyWidget, getattr, _on_stock_audit_start, analizar_excel_stock, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def extract_json_portal(self, params)`
- **Línea inicial:** 3202 | **Línea final:** 3217
- **Firma completa:** `def extract_json_portal(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _on_extract_json_portal, get, _DummyWidget, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def start_json_process(self, params)`
- **Línea inicial:** 3219 | **Línea final:** 3267
- **Firma completa:** `def start_json_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `evaluate_js, str, isinstance, Thread, bool, get, _DummyWidget, getattr, print, _get_id_categoria`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def run_tool_test(self, params)`
- **Línea inicial:** 3269 | **Línea final:** 3270
- **Firma completa:** `def run_tool_test(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `extract_json_portal`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def stop_stock_process(self)`
- **Línea inicial:** 3273 | **Línea final:** 3279
- **Firma completa:** `def stop_stock_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_stock_stop, str, hasattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def download_stock_template(self)`
- **Línea inicial:** 3281 | **Línea final:** 3288
- **Firma completa:** `def download_stock_template(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_download_stock_template, hasattr, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def export_audit(self, fmt)`
- **Línea inicial:** 3291 | **Línea final:** 3296
- **Firma completa:** `def export_audit(self, fmt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_export_audit_report, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def info(self, msg)`
- **Línea inicial:** 174 | **Línea final:** 174
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 175 | **Línea final:** 175
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 176 | **Línea final:** 176
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 177 | **Línea final:** 177
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 178 | **Línea final:** 178
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def card_sec(title)`
- **Línea inicial:** 452 | **Línea final:** 456
- **Firma completa:** `def card_sec(title)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Frame, pack, Label`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _save()`
- **Línea inicial:** 494 | **Línea final:** 496
- **Firma completa:** `def _save()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy, showinfo`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def make_win_btn(parent, text, cmd, hover_bg, hover_fg, width)`
- **Línea inicial:** 645 | **Línea final:** 652
- **Firma completa:** `def make_win_btn(parent, text, cmd, hover_bg, hover_fg, width)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `bind, Label, config, pack, cmd`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def add_sep(titulo)`
- **Línea inicial:** 826 | **Línea final:** 832
- **Firma completa:** `def add_sep(titulo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid, Frame, pack, Label`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def st_seg(texto, color, bold)`
- **Línea inicial:** 969 | **Línea final:** 975
- **Firma completa:** `def st_seg(texto, color, bold)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Frame, Label, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_cfg(e)`
- **Línea inicial:** 1126 | **Línea final:** 1127
- **Firma completa:** `def _on_cfg(e)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `bbox, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_canvas_cfg(e)`
- **Línea inicial:** 1129 | **Línea final:** 1131
- **Firma completa:** `def _on_canvas_cfg(e)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `itemconfig`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def create_tool_card(title, subtitle)`
- **Línea inicial:** 1169 | **Línea final:** 1187
- **Firma completa:** `def create_tool_card(title, subtitle)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Frame, pack, Label`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def make_action_btn(parent_row, text, command, bg, fg)`
- **Línea inicial:** 1189 | **Línea final:** 1195
- **Firma completa:** `def make_action_btn(parent_row, text, command, bg, fg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Button, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _ui_done()`
- **Línea inicial:** 1821 | **Línea final:** 1873
- **Firma completa:** `def _ui_done()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_append_stock_log, configure, asksaveasfilename, get, join, generar_excel_auditoria, strftime, Popen, makedirs, hasattr`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def _log(msg)`
- **Línea inicial:** 2220 | **Línea final:** 2228
- **Firma completa:** `def _log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `evaluate_js, getattr, print, dumps, hasattr`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_done(fichas, filepath)`
- **Línea inicial:** 2230 | **Línea final:** 2240
- **Firma completa:** `def _on_done(fichas, filepath)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate_js, len, getattr, basename, dumps, hasattr`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _val(combo)`
- **Línea inicial:** 2456 | **Línea final:** 2458
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, get, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2503 | **Línea final:** 2505
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, get, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2588 | **Línea final:** 2590
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, get, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2639 | **Línea final:** 2641
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, get, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2793 | **Línea final:** 2795
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, get, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(self, msg, level)`
- **Línea inicial:** 3327 | **Línea final:** 3342
- **Firma completa:** `def _log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `see, configure, evaluate_js, insert, str, strftime, dumps, hasattr`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _append_stock_log(self, msg)`
- **Línea inicial:** 3344 | **Línea final:** 3359
- **Firma completa:** `def _append_stock_log(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `see, configure, evaluate_js, insert, str, strftime, dumps, hasattr`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def __getattr__(self, name)`
- **Línea inicial:** 3361 | **Línea final:** 3364
- **Firma completa:** `def __getattr__(self, name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_DummyWidget, setattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(app_inst, msg)`
- **Línea inicial:** 3241 | **Línea final:** 3248
- **Firma completa:** `def _log(app_inst, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `evaluate_js, str, print, dumps, hasattr`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

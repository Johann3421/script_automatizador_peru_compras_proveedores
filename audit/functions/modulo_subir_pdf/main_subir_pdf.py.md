# Auditoría de Funciones: `modulo_subir_pdf/main_subir_pdf.py`

- **Lenguaje:** `python`
- **Líneas de código:** 3497
- **Hash SHA256:** `56fe55dea0be`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _make_stock_log(append_fn)`
- **Línea inicial:** 171 | **Línea final:** 179
- **Firma completa:** `def _make_stock_log(append_fn)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_StockLog, append_fn, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _get_user_pass(app, params)`
- **Línea inicial:** 3219 | **Línea final:** 3330
- **Firma completa:** `def _get_user_pass(app, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `_DummyWidget, str, _get_id_categoria, start, extract_json_portal, print, _get_id_catalogo, _on_download_stock_template, evaluate_js, _get_id_acuerdo`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 39)

### `def run_app()`
- **Línea inicial:** 3356 | **Línea final:** 3491
- **Firma completa:** `def run_app()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, _DummyWidget, set_window, resource_path, str, start, create_window, join, Queue, evaluate_js`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 19)

### `def __init__(self, parent)`
- **Línea inicial:** 81 | **Línea final:** 142
- **Firma completa:** `def __init__(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `resizable, geometry, super, configure, place, CTkProgressBar, after, pack, CTkFont, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _step(self)`
- **Línea inicial:** 144 | **Línea final:** 152
- **Firma completa:** `def _step(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `len, after, configure, set`
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
- **Dependencias / Invocaciones:** `clear, is_set, set, wait`
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
- **Dependencias / Invocaciones:** `super, set_default_color_theme, _build_ui, withdraw, title, set_appearance_mode, Queue, poll_queue, SplashScreen, __init__`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _load_dropdown_json(self)`
- **Línea inicial:** 301 | **Línea final:** 325
- **Firma completa:** `def _load_dropdown_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `insert, load, resource_path, open, isfile, dirname, abspath`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _setup_styles(self)`
- **Línea inicial:** 365 | **Línea final:** 391
- **Firma completa:** `def _setup_styles(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `theme_use, map, Style, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _set_taskbar_icon(self)`
- **Línea inicial:** 393 | **Línea final:** 402
- **Firma completa:** `def _set_taskbar_icon(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `ShowWindow, winfo_id, GetWindowLongW, SetWindowLongW, GetParent`
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
- **Dependencias / Invocaciones:** `geometry, winfo_y, winfo_x, getattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _close_window(self)`
- **Línea inicial:** 415 | **Línea final:** 418
- **Firma completa:** `def _close_window(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy, exit`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _open_config_dialog(self)`
- **Línea inicial:** 420 | **Línea final:** 503
- **Firma completa:** `def _open_config_dialog(self)`
- **Propósito:** Abre la ventana modal de Configuración y Preferencias del Sistema.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `showinfo, update_idletasks, Entry, winfo_screenheight, geometry, resizable, title, BooleanVar, transient, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _open_about_dialog(self)`
- **Línea inicial:** 505 | **Línea final:** 555
- **Firma completa:** `def _open_about_dialog(self)`
- **Propósito:** Abre la ventana modal Acerca del Sistema.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `resizable, Label, Toplevel, configure, title, grab_set, transient, update_idletasks, pack, Frame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _minimize_window(self)`
- **Línea inicial:** 557 | **Línea final:** 565
- **Firma completa:** `def _minimize_window(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `iconify, bind, update_idletasks, overrideredirect`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _on_window_map(self, event)`
- **Línea inicial:** 567 | **Línea final:** 576
- **Firma completa:** `def _on_window_map(self, event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr, unbind, state, _set_taskbar_icon, overrideredirect`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _toggle_maximize(self)`
- **Línea inicial:** 578 | **Línea final:** 598
- **Firma completa:** `def _toggle_maximize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `ShowWindow, hasattr, winfo_id, getattr, config, state`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def _build_ui(self)`
- **Línea inicial:** 618 | **Línea final:** 987
- **Firma completa:** `def _build_ui(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Treeview, config, place, add_cascade, build_instructions_tab, _switch_view, showinfo, pack_propagate, add_command, build_precios_json_tab`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _clear_excel(self)`
- **Línea inicial:** 989 | **Línea final:** 997
- **Firma completa:** `def _clear_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_children, delete, hasattr, config`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _switch_view(self, view_id)`
- **Línea inicial:** 999 | **Línea final:** 1022
- **Firma completa:** `def _switch_view(self, view_id)`
- **Propósito:** Cambia la vista activa y resalta el tab horizontal correspondiente.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, config, get, grid_forget, grid, items`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _collect_tree_rows(self)`
- **Línea inicial:** 1026 | **Línea final:** 1041
- **Firma completa:** `def _collect_tree_rows(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, append, get_children, len, item`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _run_auditor_check(self, modulo_nombre)`
- **Línea inicial:** 1043 | **Línea final:** 1051
- **Firma completa:** `def _run_auditor_check(self, modulo_nombre)`
- **Propósito:** Ejecuta el chequeo rápido del auditor sobre las fichas procesadas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `audit_results, hasattr, _collect_tree_rows, config`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _export_audit_report(self, fmt, modulo_nombre)`
- **Línea inicial:** 1053 | **Línea final:** 1089
- **Firma completa:** `def _export_audit_report(self, fmt, modulo_nombre)`
- **Propósito:** Genera y guarda el informe de auditoría en Excel (.xlsx) o PDF/HTML.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, asksaveasfilename, showwarning, showinfo, export_pdf_report, _run_auditor_check, replace, export_excel_report, now, showerror`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _update_tools_excel_status(self)`
- **Línea inicial:** 1091 | **Línea final:** 1105
- **Firma completa:** `def _update_tools_excel_status(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, getattr, config, basename, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _build_advanced_tools_tab(self, parent)`
- **Línea inicial:** 1107 | **Línea final:** 1214
- **Firma completa:** `def _build_advanced_tools_tab(self, parent)`
- **Propósito:** Vista de Herramientas Avanzadas — diagnóstico y scrapers en Tkinter nativo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `create_window, Label, bbox, Canvas, configure, create_tool_card, pack, make_action_btn, Frame, grid_rowconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _build_stock_tab(self, left_col, right_col, parent)`
- **Línea inicial:** 1218 | **Línea final:** 1472
- **Firma completa:** `def _build_stock_tab(self, left_col, right_col, parent)`
- **Propósito:** Vista de Análisis de Stock — paleta institucional light.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkCheckBox, enumerate, CTkProgressBar, CTkTextbox, grid_columnconfigure, CTkEntry, CTkOptionMenu, Queue, CTkButton, pack`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _export_stock_audit_report(self, fmt)`
- **Línea inicial:** 1489 | **Línea final:** 1523
- **Firma completa:** `def _export_stock_audit_report(self, fmt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, round, getattr, asksaveasfilename, showwarning, showinfo, export_pdf_report, export_excel_report, now, showerror`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_load_stock_excel(self)`
- **Línea inicial:** 1525 | **Línea final:** 1553
- **Firma completa:** `def _on_load_stock_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, configure, askopenfilename, basename, analizar_excel_stock, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_download_stock_template(self)`
- **Línea inicial:** 1555 | **Línea final:** 1577
- **Firma completa:** `def _on_download_stock_template(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, asksaveasfilename, save, _append_stock_log, Workbook`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _load_stock_combos_json(self)`
- **Línea inicial:** 1579 | **Línea final:** 1595
- **Firma completa:** `def _load_stock_combos_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `insert, dirname, load, resource_path, open, _append_stock_log, abspath`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_acuerdo_changed(self, acuerdo_text)`
- **Línea inicial:** 1597 | **Línea final:** 1617
- **Firma completa:** `def _on_stock_acuerdo_changed(self, acuerdo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `add, configure, get, set, _on_stock_catalogo_changed, sorted`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_catalogo_changed(self, catalogo_text)`
- **Línea inicial:** 1619 | **Línea final:** 1640
- **Firma completa:** `def _on_stock_catalogo_changed(self, catalogo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `add, configure, strip, get, set, sorted`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_start(self)`
- **Línea inicial:** 1642 | **Línea final:** 1691
- **Firma completa:** `def _on_stock_start(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `float, configure, strip, Thread, get, start, _append_stock_log, clear`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def _on_stock_stop(self)`
- **Línea inicial:** 1693 | **Línea final:** 1707
- **Firma completa:** `def _on_stock_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, getattr, set, close, _append_stock_log`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _append_stock_log(self, msg)`
- **Línea inicial:** 1709 | **Línea final:** 1718
- **Firma completa:** `def _append_stock_log(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, insert, see, configure`
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
- **Dependencias / Invocaciones:** `hasattr, configure, getattr, strip, str, showwarning, bool, Thread, exists, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 34)

### `def _on_audit_done(self, filas, resumen)`
- **Línea inicial:** 1817 | **Línea final:** 1878
- **Firma completa:** `def _on_audit_done(self, filas, resumen)`
- **Propósito:** Callback llamado por execute_auditor cuando termina.
Siempre se ejecuta en el hilo del auditor — usa self.after() para UI.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, hasattr, join, generar_excel_auditoria, configure, asksaveasfilename, after, _ui_done, get, Popen`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def _build_credentials_section(self, parent)`
- **Línea inicial:** 1879 | **Línea final:** 1931
- **Firma completa:** `def _build_credentials_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, CTkEntry, CTkCheckBox, CTkButton, CTkFont, grid, _section_label, CTkFrame, CTkLabel, grid_columnconfigure`
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
- **Dependencias / Invocaciones:** `CTkButton, pack, CTkFont, CTkComboBox, grid, _section_label, CTkFrame, CTkLabel, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _pick_excel(self)`
- **Línea inicial:** 2005 | **Línea final:** 2036
- **Firma completa:** `def _pick_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, delete, insert, configure, _on_sheet_changed, config, askopenfilename, set, basename, get_sheets`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _on_sheet_changed(self, choice)`
- **Línea inicial:** 2038 | **Línea final:** 2107
- **Firma completa:** `def _on_sheet_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `enumerate, config, str, isdigit, load_workbook, len, append, parse_excel, hasattr, delete`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 31)

### `def _build_catalog_section(self, parent)`
- **Línea inicial:** 2111 | **Línea final:** 2169
- **Firma completa:** `def _build_catalog_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `dict, get, _opts_texts, CTkFont, set, CTkComboBox, grid, _section_label, CTkFrame, CTkLabel`
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
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _on_catalogo_changed(self, choice)`
- **Línea inicial:** 2182 | **Línea final:** 2191
- **Firma completa:** `def _on_catalogo_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_categoria_changed, configure, _opts_texts, set, _find_children`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _on_categoria_changed(self, choice)`
- **Línea inicial:** 2193 | **Línea final:** 2210
- **Firma completa:** `def _on_categoria_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, strip, get, _opts_texts, split, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_extract_json_portal(self)`
- **Línea inicial:** 2212 | **Línea final:** 2247
- **Firma completa:** `def _on_extract_json_portal(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `hasattr, print, strip, getattr, Thread, bool, get, evaluate_js, start, basename`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def _build_opciones_section(self, parent)`
- **Línea inicial:** 2251 | **Línea final:** 2292
- **Firma completa:** `def _build_opciones_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkSlider, configure, CTkFont, set, grid, _section_label, CTkFrame, CTkLabel, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_execution_section(self, parent)`
- **Línea inicial:** 2296 | **Línea final:** 2356
- **Firma completa:** `def _build_execution_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, _build_captcha_panel, CTkProgressBar, pack, tag_config, set, CTkTextbox, CTkFont, grid_rowconfigure, _make_stat`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _make_stat(self, parent, label, color, col)`
- **Línea inicial:** 2358 | **Línea final:** 2366
- **Firma completa:** `def _make_stat(self, parent, label, color, col)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFont, pack, grid, CTkFrame, CTkLabel`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_captcha_panel(self, parent)`
- **Línea inicial:** 2370 | **Línea final:** 2403
- **Firma completa:** `def _build_captcha_panel(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkEntry, CTkButton, CTkFont, _on_captcha_submit, bind, grid_remove, grid, CTkFrame, CTkLabel, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _show_captcha(self, image_bytes)`
- **Línea inicial:** 2405 | **Línea final:** 2412
- **Firma completa:** `def _show_captcha(self, image_bytes)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `CTkImage, delete, focus_set, configure, BytesIO, open, grid, resize`
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
- **Dependencias / Invocaciones:** `_hide_captcha_panel, strip, get, respond, _log`
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
- **Dependencias / Invocaciones:** `append, insert, see, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_test(self)`
- **Línea inicial:** 2443 | **Línea final:** 2485
- **Firma completa:** `def _on_test(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `delete, hasattr, configure, strip, _hide_captcha_panel, Thread, bool, get, split, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_certs_only(self)`
- **Línea inicial:** 2487 | **Línea final:** 2533
- **Firma completa:** `def _on_certs_only(self)`
- **Propósito:** Handler del botón 'Solo Certificaciones': entra a cada ficha y agrega ISO 9001/14001.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `delete, hasattr, configure, strip, _hide_captcha_panel, Thread, bool, get, split, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_extract(self)`
- **Línea inicial:** 2535 | **Línea final:** 2569
- **Firma completa:** `def _on_extract(self)`
- **Propósito:** Handler del botón 'Extraer Reportes': descarga reportes de Producto Ofertado.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `delete, configure, strip, _hide_captcha_panel, Thread, bool, get, set, start, clear`
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
- **Dependencias / Invocaciones:** `delete, configure, strip, _hide_captcha_panel, Thread, bool, get, split, set, start`
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
- **Dependencias / Invocaciones:** `delete, hasattr, configure, strip, _hide_captcha_panel, getattr, Thread, bool, get, split`
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
- **Dependencias / Invocaciones:** `delete, configure, strip, _hide_captcha_panel, getattr, Thread, bool, get, set, start`
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
- **Dependencias / Invocaciones:** `delete, configure, strip, _hide_captcha_panel, getattr, Thread, bool, get, set, start`
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
- **Dependencias / Invocaciones:** `delete, configure, strip, _hide_captcha_panel, Thread, get, bool, split, set, start`
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
- **Dependencias / Invocaciones:** `_log, after, configure, set`
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
- **Dependencias / Invocaciones:** `configure, str, after, get, get_nowait, isinstance, _show_captcha, set, _log, len`
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
- **Dependencias / Invocaciones:** `parse_excel, withdraw, askopenfilename, get, detect_columns, basename, destroy, get_sheets, attributes, Tk`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def select_stock_file(self)`
- **Línea inicial:** 3035 | **Línea final:** 3072
- **Firma completa:** `def select_stock_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, iterrows, parse_excel, withdraw, str, askopenfilename, get, detect_columns, basename, destroy`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def select_json_file(self)`
- **Línea inicial:** 3075 | **Línea final:** 3105
- **Firma completa:** `def select_json_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `withdraw, endswith, load, str, askopenfilename, get, parse_excel_precios, open, isinstance, basename`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def load_sheet(self, sheet_name)`
- **Línea inicial:** 3107 | **Línea final:** 3113
- **Firma completa:** `def load_sheet(self, sheet_name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, parse_excel, getattr, detect_columns`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_process(self, params)`
- **Línea inicial:** 3116 | **Línea final:** 3130
- **Firma completa:** `def start_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `float, _DummyWidget, str, _on_launch, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def stop_process(self)`
- **Línea inicial:** 3132 | **Línea final:** 3137
- **Firma completa:** `def stop_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_stop, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_stock_process(self, params)`
- **Línea inicial:** 3140 | **Línea final:** 3170
- **Firma completa:** `def start_stock_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr, _DummyWidget, strip, str, get, _on_stock_start, analizar_excel_stock`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def start_stock_audit(self, params)`
- **Línea inicial:** 3172 | **Línea final:** 3200
- **Firma completa:** `def start_stock_audit(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr, _DummyWidget, strip, str, get, _on_stock_audit_start, analizar_excel_stock`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def extract_json_portal(self, params)`
- **Línea inicial:** 3202 | **Línea final:** 3217
- **Firma completa:** `def extract_json_portal(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_DummyWidget, strip, _on_extract_json_portal, str, get`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def start_json_process(self, params)`
- **Línea inicial:** 3238 | **Línea final:** 3290
- **Firma completa:** `def start_json_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `hasattr, print, getattr, strip, _DummyWidget, _get_id_catalogo, bool, get, _get_id_categoria, _get_user_pass`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def stop_json_process(self)`
- **Línea inicial:** 3292 | **Línea final:** 3299
- **Firma completa:** `def stop_json_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `hasattr, print, set, str`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def run_tool_test(self, params)`
- **Línea inicial:** 3301 | **Línea final:** 3302
- **Firma completa:** `def run_tool_test(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `extract_json_portal`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def stop_stock_process(self)`
- **Línea inicial:** 3305 | **Línea final:** 3313
- **Firma completa:** `def stop_stock_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, _on_stock_stop, set, str`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def download_stock_template(self)`
- **Línea inicial:** 3315 | **Línea final:** 3322
- **Firma completa:** `def download_stock_template(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, str, _on_download_stock_template`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def export_audit(self, fmt)`
- **Línea inicial:** 3325 | **Línea final:** 3330
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
- **Dependencias / Invocaciones:** `append_fn, str`
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
- **Dependencias / Invocaciones:** `Frame, Label, pack`
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
- **Dependencias / Invocaciones:** `cmd, Label, config, pack, bind`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def add_sep(titulo)`
- **Línea inicial:** 826 | **Línea final:** 832
- **Firma completa:** `def add_sep(titulo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Frame, Label, pack, grid`
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
- **Dependencias / Invocaciones:** `configure, bbox`
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
- **Dependencias / Invocaciones:** `Frame, Label, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def make_action_btn(parent_row, text, command, bg, fg)`
- **Línea inicial:** 1189 | **Línea final:** 1195
- **Firma completa:** `def make_action_btn(parent_row, text, command, bg, fg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `pack, Button`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _ui_done()`
- **Línea inicial:** 1821 | **Línea final:** 1873
- **Firma completa:** `def _ui_done()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, hasattr, join, generar_excel_auditoria, configure, asksaveasfilename, get, Popen, _append_stock_log, makedirs`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def _log(msg)`
- **Línea inicial:** 2220 | **Línea final:** 2228
- **Firma completa:** `def _log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `hasattr, print, getattr, evaluate_js, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_done(fichas, filepath)`
- **Línea inicial:** 2230 | **Línea final:** 2240
- **Firma completa:** `def _on_done(fichas, filepath)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, getattr, evaluate_js, basename, len, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _val(combo)`
- **Línea inicial:** 2456 | **Línea final:** 2458
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2503 | **Línea final:** 2505
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2588 | **Línea final:** 2590
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2639 | **Línea final:** 2641
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2793 | **Línea final:** 2795
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(self, msg, level)`
- **Línea inicial:** 3361 | **Línea final:** 3376
- **Firma completa:** `def _log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, hasattr, insert, configure, str, evaluate_js, see, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _append_stock_log(self, msg)`
- **Línea inicial:** 3378 | **Línea final:** 3393
- **Firma completa:** `def _append_stock_log(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, hasattr, insert, configure, str, evaluate_js, see, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def __getattr__(self, name)`
- **Línea inicial:** 3395 | **Línea final:** 3398
- **Firma completa:** `def __getattr__(self, name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `setattr, _DummyWidget`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(app_inst, msg)`
- **Línea inicial:** 3264 | **Línea final:** 3272
- **Firma completa:** `def _log(app_inst, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print, getattr, str, evaluate_js, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

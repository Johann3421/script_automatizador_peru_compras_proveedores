# Auditoría de Funciones: `modulo_subir_pdf/main_subir_pdf.py`

- **Lenguaje:** `python`
- **Líneas de código:** 3323
- **Hash SHA256:** `4e4cbefdb2bd`
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

### `def run_app()`
- **Línea inicial:** 3182 | **Línea final:** 3317
- **Firma completa:** `def run_app()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate_js, Event, str, SubirPdfWebApi, set_window, insert, getattr, hasattr, create_window, strftime`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 19)

### `def __init__(self, parent)`
- **Línea inicial:** 81 | **Línea final:** 142
- **Firma completa:** `def __init__(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, place, attributes, CTkProgressBar, resizable, configure, CTkFont, overrideredirect, winfo_screenwidth, geometry`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _step(self)`
- **Línea inicial:** 144 | **Línea final:** 152
- **Firma completa:** `def _step(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, set, len, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _finish(self)`
- **Línea inicial:** 154 | **Línea final:** 159
- **Firma completa:** `def _finish(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy, deiconify`
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
- **Dependencias / Invocaciones:** `is_set, wait, clear, set`
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
- **Dependencias / Invocaciones:** `poll_queue, _build_ui, set_appearance_mode, withdraw, Event, _load_dropdown_json, geometry, SplashScreen, __init__, Queue`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _load_dropdown_json(self)`
- **Línea inicial:** 301 | **Línea final:** 325
- **Firma completa:** `def _load_dropdown_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `resource_path, insert, isfile, open, abspath, load, dirname`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _setup_styles(self)`
- **Línea inicial:** 365 | **Línea final:** 391
- **Firma completa:** `def _setup_styles(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `map, theme_use, Style, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _set_taskbar_icon(self)`
- **Línea inicial:** 393 | **Línea final:** 402
- **Firma completa:** `def _set_taskbar_icon(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `winfo_id, GetParent, GetWindowLongW, ShowWindow, SetWindowLongW`
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
- **Dependencias / Invocaciones:** `winfo_x, geometry, getattr, winfo_y`
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
- **Dependencias / Invocaciones:** `showinfo, resizable, Checkbutton, Entry, winfo_screenwidth, pack, Frame, update_idletasks, winfo_screenheight, transient`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _open_about_dialog(self)`
- **Línea inicial:** 505 | **Línea final:** 555
- **Firma completa:** `def _open_about_dialog(self)`
- **Propósito:** Abre la ventana modal Acerca del Sistema.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `transient, Button, resizable, Label, configure, Toplevel, geometry, winfo_screenwidth, Frame, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _minimize_window(self)`
- **Línea inicial:** 557 | **Línea final:** 565
- **Firma completa:** `def _minimize_window(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `iconify, bind, overrideredirect, update_idletasks`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _on_window_map(self, event)`
- **Línea inicial:** 567 | **Línea final:** 576
- **Firma completa:** `def _on_window_map(self, event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `state, getattr, overrideredirect, unbind, _set_taskbar_icon`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _toggle_maximize(self)`
- **Línea inicial:** 578 | **Línea final:** 598
- **Firma completa:** `def _toggle_maximize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `winfo_id, state, getattr, hasattr, ShowWindow, config`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def _build_ui(self)`
- **Línea inicial:** 618 | **Línea final:** 987
- **Firma completa:** `def _build_ui(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `showinfo, tag_configure, Checkbutton, _on_launch, Entry, _on_sheet_changed, _build_stock_tab, zip, build_instructions_tab, pack`
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
- **Dependencias / Invocaciones:** `grid, items, hasattr, get, grid_forget, config`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _collect_tree_rows(self)`
- **Línea inicial:** 1026 | **Línea final:** 1041
- **Firma completa:** `def _collect_tree_rows(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `item, append, get_children, hasattr, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _run_auditor_check(self, modulo_nombre)`
- **Línea inicial:** 1043 | **Línea final:** 1051
- **Firma completa:** `def _run_auditor_check(self, modulo_nombre)`
- **Propósito:** Ejecuta el chequeo rápido del auditor sobre las fichas procesadas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `config, _collect_tree_rows, hasattr, audit_results`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _export_audit_report(self, fmt, modulo_nombre)`
- **Línea inicial:** 1053 | **Línea final:** 1089
- **Firma completa:** `def _export_audit_report(self, fmt, modulo_nombre)`
- **Propósito:** Genera y guarda el informe de auditoría en Excel (.xlsx) o PDF/HTML.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `showinfo, _run_auditor_check, upper, asksaveasfilename, export_excel_report, replace, showwarning, showerror, export_pdf_report, now`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _update_tools_excel_status(self)`
- **Línea inicial:** 1091 | **Línea final:** 1105
- **Firma completa:** `def _update_tools_excel_status(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr, hasattr, basename, config, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _build_advanced_tools_tab(self, parent)`
- **Línea inicial:** 1107 | **Línea final:** 1214
- **Firma completa:** `def _build_advanced_tools_tab(self, parent)`
- **Propósito:** Vista de Herramientas Avanzadas — diagnóstico y scrapers en Tkinter nativo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_rowconfigure, Button, create_tool_card, Scrollbar, Label, _update_tools_excel_status, configure, make_action_btn, itemconfig, Canvas`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _build_stock_tab(self, left_col, right_col, parent)`
- **Línea inicial:** 1218 | **Línea final:** 1472
- **Firma completa:** `def _build_stock_tab(self, left_col, right_col, parent)`
- **Propósito:** Vista de Análisis de Stock — paleta institucional light.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkTextbox, _export_stock_audit_report, _load_stock_combos_json, Event, _section_label, pack, CTkLabel, CTkButton, insert, CTkOptionMenu`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _export_stock_audit_report(self, fmt)`
- **Línea inicial:** 1489 | **Línea final:** 1523
- **Firma completa:** `def _export_stock_audit_report(self, fmt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `showinfo, upper, asksaveasfilename, export_excel_report, round, getattr, showwarning, showerror, export_pdf_report, now`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_load_stock_excel(self)`
- **Línea inicial:** 1525 | **Línea final:** 1553
- **Firma completa:** `def _on_load_stock_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, configure, askopenfilename, analizar_excel_stock, basename, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_download_stock_template(self)`
- **Línea inicial:** 1555 | **Línea final:** 1577
- **Firma completa:** `def _on_download_stock_template(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `asksaveasfilename, append, _append_stock_log, save, Workbook`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _load_stock_combos_json(self)`
- **Línea inicial:** 1579 | **Línea final:** 1595
- **Firma completa:** `def _load_stock_combos_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `resource_path, insert, _append_stock_log, open, abspath, load, dirname`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_acuerdo_changed(self, acuerdo_text)`
- **Línea inicial:** 1597 | **Línea final:** 1617
- **Firma completa:** `def _on_stock_acuerdo_changed(self, acuerdo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sorted, configure, get, _on_stock_catalogo_changed, set, add`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_catalogo_changed(self, catalogo_text)`
- **Línea inicial:** 1619 | **Línea final:** 1640
- **Firma completa:** `def _on_stock_catalogo_changed(self, catalogo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sorted, configure, get, strip, set, add`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_start(self)`
- **Línea inicial:** 1642 | **Línea final:** 1691
- **Firma completa:** `def _on_stock_start(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, _append_stock_log, float, configure, get, strip, Thread, start`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def _on_stock_stop(self)`
- **Línea inicial:** 1693 | **Línea final:** 1707
- **Firma completa:** `def _on_stock_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_append_stock_log, close, getattr, configure, set`
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
- **Dependencias / Invocaciones:** `clear, exists, bool, _append_stock_log, getattr, hasattr, configure, showwarning, get, analizar_excel_stock`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 34)

### `def _on_audit_done(self, filas, resumen)`
- **Línea inicial:** 1817 | **Línea final:** 1878
- **Firma completa:** `def _on_audit_done(self, filas, resumen)`
- **Propósito:** Callback llamado por execute_auditor cuando termina.
Siempre se ejecuta en el hilo del auditor — usa self.after() para UI.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, join, asksaveasfilename, makedirs, _append_stock_log, generar_excel_auditoria, Popen, hasattr, configure, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def _build_credentials_section(self, parent)`
- **Línea inicial:** 1879 | **Línea final:** 1931
- **Firma completa:** `def _build_credentials_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, CTkFrame, grid, CTkCheckBox, CTkEntry, _section_label, CTkFont, CTkLabel, CTkButton, grid_columnconfigure`
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
- **Dependencias / Invocaciones:** `CTkFrame, grid, _section_label, CTkComboBox, pack, CTkFont, CTkLabel, CTkButton, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _pick_excel(self)`
- **Línea inicial:** 2005 | **Línea final:** 2036
- **Firma completa:** `def _pick_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_sheets, insert, delete, _update_tools_excel_status, _on_sheet_changed, hasattr, configure, askopenfilename, set, basename`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _on_sheet_changed(self, choice)`
- **Línea inicial:** 2038 | **Línea final:** 2107
- **Firma completa:** `def _on_sheet_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_children, replace, _update_tools_excel_status, str, detect_columns, config, insert, lower, close, hasattr`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 31)

### `def _build_catalog_section(self, parent)`
- **Línea inicial:** 2111 | **Línea final:** 2169
- **Firma completa:** `def _build_catalog_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `dict, _on_catalogo_changed, CTkFrame, grid, get, _section_label, CTkComboBox, CTkFont, _opts_texts, set`
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
- **Dependencias / Invocaciones:** `_find_children, configure, _on_categoria_changed, _opts_texts, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _on_categoria_changed(self, choice)`
- **Línea inicial:** 2193 | **Línea final:** 2210
- **Firma completa:** `def _on_categoria_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, configure, get, strip, _opts_texts, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _build_opciones_section(self, parent)`
- **Línea inicial:** 2214 | **Línea final:** 2255
- **Firma completa:** `def _build_opciones_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFrame, grid, configure, _section_label, CTkFont, set, CTkLabel, CTkSlider, grid_columnconfigure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_execution_section(self, parent)`
- **Línea inicial:** 2259 | **Línea final:** 2319
- **Firma completa:** `def _build_execution_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_rowconfigure, CTkProgressBar, CTkTextbox, _build_captcha_panel, CTkFrame, grid, configure, _section_label, _make_stat, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _make_stat(self, parent, label, color, col)`
- **Línea inicial:** 2321 | **Línea final:** 2329
- **Firma completa:** `def _make_stat(self, parent, label, color, col)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFrame, grid, pack, CTkLabel, CTkFont`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_captcha_panel(self, parent)`
- **Línea inicial:** 2333 | **Línea final:** 2366
- **Firma completa:** `def _build_captcha_panel(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_captcha_submit, bind, grid, grid_remove, grid_columnconfigure, CTkEntry, CTkFont, CTkLabel, CTkButton, CTkFrame`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _show_captcha(self, image_bytes)`
- **Línea inicial:** 2368 | **Línea final:** 2375
- **Firma completa:** `def _show_captcha(self, image_bytes)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `CTkImage, grid, delete, resize, open, configure, focus_set, BytesIO`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _hide_captcha_panel(self)`
- **Línea inicial:** 2377 | **Línea final:** 2378
- **Firma completa:** `def _hide_captcha_panel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_remove`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_captcha_submit(self)`
- **Línea inicial:** 2380 | **Línea final:** 2385
- **Firma completa:** `def _on_captcha_submit(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, strip, _hide_captcha_panel, respond, _log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _section_label(self, parent, text, row)`
- **Línea inicial:** 2389 | **Línea final:** 2395
- **Firma completa:** `def _section_label(self, parent, text, row)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid, CTkFont, CTkLabel`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(self, msg, level)`
- **Línea inicial:** 2397 | **Línea final:** 2402
- **Firma completa:** `def _log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, append, see, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_test(self)`
- **Línea inicial:** 2406 | **Línea final:** 2448
- **Firma completa:** `def _on_test(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, split, delete, configure, hasattr, get, strip, _hide_captcha_panel, _val`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_certs_only(self)`
- **Línea inicial:** 2450 | **Línea final:** 2496
- **Firma completa:** `def _on_certs_only(self)`
- **Propósito:** Handler del botón 'Solo Certificaciones': entra a cada ficha y agrega ISO 9001/14001.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, split, delete, configure, hasattr, get, strip, _hide_captcha_panel, _val`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_extract(self)`
- **Línea inicial:** 2498 | **Línea final:** 2532
- **Firma completa:** `def _on_extract(self)`
- **Propósito:** Handler del botón 'Extraer Reportes': descarga reportes de Producto Ofertado.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, delete, configure, get, strip, _hide_captcha_panel, set, Thread, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _execute_extract(self, usuario, password, headless)`
- **Línea inicial:** 2533 | **Línea final:** 2535
- **Firma completa:** `def _execute_extract(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_extract`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _execute_certs_only(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2536 | **Línea final:** 2538
- **Firma completa:** `def _execute_certs_only(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_certs_only`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_nro_parte(self)`
- **Línea inicial:** 2539 | **Línea final:** 2586
- **Firma completa:** `def _on_nro_parte(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, split, delete, configure, get, strip, _hide_captcha_panel, _val, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _execute_nro_parte(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2588 | **Línea final:** 2590
- **Firma completa:** `def _execute_nro_parte(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_nro_parte`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_compare(self)`
- **Línea inicial:** 2591 | **Línea final:** 2628
- **Firma completa:** `def _on_compare(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, split, delete, getattr, configure, hasattr, get, strip, _hide_captcha_panel`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_compare(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2630 | **Línea final:** 2632
- **Firma completa:** `def _execute_compare(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_compare`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_discovery(self)`
- **Línea inicial:** 2633 | **Línea final:** 2656
- **Firma completa:** `def _on_discovery(self)`
- **Propósito:** Handler del botón 'Discovery': ejecuta el script discovery_perucompras.py.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, delete, getattr, configure, get, strip, _hide_captcha_panel, set, Thread`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_discovery(self, usuario, password, headless)`
- **Línea inicial:** 2658 | **Línea final:** 2660
- **Firma completa:** `def _execute_discovery(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_discovery`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_discovery2(self)`
- **Línea inicial:** 2661 | **Línea final:** 2684
- **Firma completa:** `def _on_discovery2(self)`
- **Propósito:** Handler del botón 'Discovery v2': scraping profundo multi-técnica.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, delete, getattr, configure, get, strip, _hide_captcha_panel, set, Thread`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_discovery2(self, usuario, password, headless)`
- **Línea inicial:** 2686 | **Línea final:** 2688
- **Firma completa:** `def _execute_discovery2(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_discovery2`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _execute_test(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2689 | **Línea final:** 2691
- **Firma completa:** `def _execute_test(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_test`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_launch(self)`
- **Línea inicial:** 2706 | **Línea final:** 2773
- **Firma completa:** `def _on_launch(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, bool, split, delete, configure, get, strip, _hide_captcha_panel, _val, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)`
- **Línea inicial:** 2775 | **Línea final:** 2785
- **Firma completa:** `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_stop(self)`
- **Línea inicial:** 2786 | **Línea final:** 2795
- **Firma completa:** `def _on_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, set, _log, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _reset_after_stop(self)`
- **Línea inicial:** 2797 | **Línea final:** 2807
- **Firma completa:** `def _reset_after_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def poll_queue(self)`
- **Línea inicial:** 2832 | **Línea final:** 2892
- **Firma completa:** `def poll_queue(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, len, _show_captcha, isinstance, configure, get, is_set, str, set, _log`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def __init__(self, val)`
- **Línea inicial:** 2931 | **Línea final:** 2932
- **Firma completa:** `def __init__(self, val)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def get(self)`
- **Línea inicial:** 2933 | **Línea final:** 2934
- **Firma completa:** `def get(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def set(self, val)`
- **Línea inicial:** 2935 | **Línea final:** 2937
- **Firma completa:** `def set(self, val)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def configure(self)`
- **Línea inicial:** 2938 | **Línea final:** 2938
- **Firma completa:** `def configure(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def config(self)`
- **Línea inicial:** 2939 | **Línea final:** 2939
- **Firma completa:** `def config(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def delete(self)`
- **Línea inicial:** 2940 | **Línea final:** 2940
- **Firma completa:** `def delete(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def insert(self)`
- **Línea inicial:** 2941 | **Línea final:** 2941
- **Firma completa:** `def insert(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def see(self)`
- **Línea inicial:** 2942 | **Línea final:** 2942
- **Firma completa:** `def see(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def pack(self)`
- **Línea inicial:** 2943 | **Línea final:** 2943
- **Firma completa:** `def pack(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def place(self)`
- **Línea inicial:** 2944 | **Línea final:** 2944
- **Firma completa:** `def place(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def grid(self)`
- **Línea inicial:** 2945 | **Línea final:** 2945
- **Firma completa:** `def grid(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def destroy(self)`
- **Línea inicial:** 2946 | **Línea final:** 2946
- **Firma completa:** `def destroy(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def bind(self)`
- **Línea inicial:** 2947 | **Línea final:** 2947
- **Firma completa:** `def bind(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def unbind(self)`
- **Línea inicial:** 2948 | **Línea final:** 2948
- **Firma completa:** `def unbind(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __call__(self)`
- **Línea inicial:** 2949 | **Línea final:** 2949
- **Firma completa:** `def __call__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __init__(self, app)`
- **Línea inicial:** 2955 | **Línea final:** 2958
- **Firma completa:** `def __init__(self, app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def set_window(self, w)`
- **Línea inicial:** 2960 | **Línea final:** 2961
- **Firma completa:** `def set_window(self, w)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def get_catalog_options(self)`
- **Línea inicial:** 2963 | **Línea final:** 2965
- **Firma completa:** `def get_catalog_options(self)`
- **Propósito:** Devuelve las opciones desplegables del archivo JSON.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def minimize(self)`
- **Línea inicial:** 2968 | **Línea final:** 2969
- **Firma completa:** `def minimize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `minimize`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def maximize(self)`
- **Línea inicial:** 2971 | **Línea final:** 2972
- **Firma completa:** `def maximize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `toggle_fullscreen`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def close(self)`
- **Línea inicial:** 2974 | **Línea final:** 2975
- **Firma completa:** `def close(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def select_file(self)`
- **Línea inicial:** 2978 | **Línea final:** 2995
- **Firma completa:** `def select_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy, attributes, parse_excel, get_sheets, withdraw, Tk, askopenfilename, get, detect_columns, basename`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def select_stock_file(self)`
- **Línea inicial:** 2998 | **Línea final:** 3035
- **Firma completa:** `def select_stock_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy, attributes, parse_excel, get_sheets, append, withdraw, Tk, askopenfilename, get, analizar_excel_stock`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def load_sheet(self, sheet_name)`
- **Línea inicial:** 3037 | **Línea final:** 3043
- **Firma completa:** `def load_sheet(self, sheet_name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, detect_columns, parse_excel, getattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_process(self, params)`
- **Línea inicial:** 3046 | **Línea final:** 3060
- **Firma completa:** `def start_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_launch, float, _DummyWidget, get, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def stop_process(self)`
- **Línea inicial:** 3062 | **Línea final:** 3067
- **Firma completa:** `def stop_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _on_stop`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_stock_process(self, params)`
- **Línea inicial:** 3070 | **Línea final:** 3100
- **Firma completa:** `def start_stock_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr, _DummyWidget, get, analizar_excel_stock, str, strip, _on_stock_start`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def start_stock_audit(self, params)`
- **Línea inicial:** 3102 | **Línea final:** 3130
- **Firma completa:** `def start_stock_audit(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_stock_audit_start, getattr, _DummyWidget, get, analizar_excel_stock, strip, str`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def stop_stock_process(self)`
- **Línea inicial:** 3133 | **Línea final:** 3139
- **Firma completa:** `def stop_stock_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _on_stock_stop, hasattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def download_stock_template(self)`
- **Línea inicial:** 3141 | **Línea final:** 3148
- **Firma completa:** `def download_stock_template(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_download_stock_template, str, hasattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def export_audit(self, fmt)`
- **Línea inicial:** 3151 | **Línea final:** 3156
- **Firma completa:** `def export_audit(self, fmt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _export_audit_report`
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
- **Dependencias / Invocaciones:** `Label, Frame, pack`
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
- **Dependencias / Invocaciones:** `cmd, Label, pack, bind, config`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def add_sep(titulo)`
- **Línea inicial:** 826 | **Línea final:** 832
- **Firma completa:** `def add_sep(titulo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid, Label, Frame, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def st_seg(texto, color, bold)`
- **Línea inicial:** 969 | **Línea final:** 975
- **Firma completa:** `def st_seg(texto, color, bold)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Label, Frame, pack`
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
- **Dependencias / Invocaciones:** `Label, Frame, pack`
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
- **Dependencias / Invocaciones:** `join, asksaveasfilename, makedirs, _append_stock_log, generar_excel_auditoria, Popen, hasattr, configure, get, strftime`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def _val(combo)`
- **Línea inicial:** 2419 | **Línea final:** 2421
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2466 | **Línea final:** 2468
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2551 | **Línea final:** 2553
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2602 | **Línea final:** 2604
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2756 | **Línea final:** 2758
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, split, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(self, msg, level)`
- **Línea inicial:** 3187 | **Línea final:** 3202
- **Firma completa:** `def _log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `see, dumps, insert, evaluate_js, hasattr, configure, str, strftime`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _append_stock_log(self, msg)`
- **Línea inicial:** 3204 | **Línea final:** 3219
- **Firma completa:** `def _append_stock_log(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `see, dumps, insert, evaluate_js, hasattr, configure, str, strftime`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def __getattr__(self, name)`
- **Línea inicial:** 3221 | **Línea final:** 3224
- **Firma completa:** `def __getattr__(self, name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_DummyWidget, setattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

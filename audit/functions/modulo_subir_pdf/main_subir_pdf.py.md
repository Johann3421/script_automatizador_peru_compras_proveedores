# Auditoría de Funciones: `modulo_subir_pdf/main_subir_pdf.py`

- **Lenguaje:** `python`
- **Líneas de código:** 3375
- **Hash SHA256:** `a1a44c3ec495`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _make_stock_log(append_fn)`
- **Línea inicial:** 171 | **Línea final:** 179
- **Firma completa:** `def _make_stock_log(append_fn)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn, _StockLog, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def run_app()`
- **Línea inicial:** 3234 | **Línea final:** 3369
- **Firma completa:** `def run_app()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_Backend, insert, Event, SubirPdfWebApi, setattr, hasattr, _load_dropdown_json, isfile, getattr, create_window`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 19)

### `def __init__(self, parent)`
- **Línea inicial:** 81 | **Línea final:** 142
- **Firma completa:** `def __init__(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `attributes, CTkLabel, place, winfo_screenheight, configure, pack, __init__, overrideredirect, after, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _step(self)`
- **Línea inicial:** 144 | **Línea final:** 152
- **Firma completa:** `def _step(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, after, set, len`
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
- **Dependencias / Invocaciones:** `Lock, Event`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def request(self, img)`
- **Línea inicial:** 207 | **Línea final:** 219
- **Firma completa:** `def request(self, img)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, is_set, wait, set`
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
- **Dependencias / Invocaciones:** `_load_dropdown_json, Event, poll_queue, __init__, CaptchaBridge, SplashScreen, geometry, withdraw, title, set_default_color_theme`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _load_dropdown_json(self)`
- **Línea inicial:** 301 | **Línea final:** 325
- **Firma completa:** `def _load_dropdown_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `dirname, resource_path, insert, isfile, abspath, load, open`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _setup_styles(self)`
- **Línea inicial:** 365 | **Línea final:** 391
- **Firma completa:** `def _setup_styles(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, map, Style, theme_use`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _set_taskbar_icon(self)`
- **Línea inicial:** 393 | **Línea final:** 402
- **Firma completa:** `def _set_taskbar_icon(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `GetParent, GetWindowLongW, winfo_id, ShowWindow, SetWindowLongW`
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
- **Dependencias / Invocaciones:** `getattr, winfo_y, winfo_x, geometry`
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
- **Dependencias / Invocaciones:** `Button, insert, Checkbutton, title, resizable, winfo_screenheight, transient, Toplevel, card_sec, grab_set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _open_about_dialog(self)`
- **Línea inicial:** 505 | **Línea final:** 555
- **Firma completa:** `def _open_about_dialog(self)`
- **Propósito:** Abre la ventana modal Acerca del Sistema.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grab_set, Button, pack, winfo_screenheight, configure, transient, Frame, geometry, title, Label`
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
- **Dependencias / Invocaciones:** `overrideredirect, state, getattr, unbind, _set_taskbar_icon`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _toggle_maximize(self)`
- **Línea inicial:** 578 | **Línea final:** 598
- **Firma completa:** `def _toggle_maximize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, config, state, getattr, winfo_id, ShowWindow`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def _build_ui(self)`
- **Línea inicial:** 618 | **Línea final:** 987
- **Firma completa:** `def _build_ui(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_launch, Button, insert, Checkbutton, rowconfigure, overrideredirect, add_command, build_instructions_tab, DoubleVar, zip`
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
- **Dependencias / Invocaciones:** `hasattr, config, grid_forget, get, items, grid`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _collect_tree_rows(self)`
- **Línea inicial:** 1026 | **Línea final:** 1041
- **Firma completa:** `def _collect_tree_rows(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_children, hasattr, append, item, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _run_auditor_check(self, modulo_nombre)`
- **Línea inicial:** 1043 | **Línea final:** 1051
- **Firma completa:** `def _run_auditor_check(self, modulo_nombre)`
- **Propósito:** Ejecuta el chequeo rápido del auditor sobre las fichas procesadas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_collect_tree_rows, hasattr, audit_results, config`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _export_audit_report(self, fmt, modulo_nombre)`
- **Línea inicial:** 1053 | **Línea final:** 1089
- **Firma completa:** `def _export_audit_report(self, fmt, modulo_nombre)`
- **Propósito:** Genera y guarda el informe de auditoría en Excel (.xlsx) o PDF/HTML.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, export_pdf_report, asksaveasfilename, replace, _run_auditor_check, export_excel_report, showerror, now, showwarning, upper`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _update_tools_excel_status(self)`
- **Línea inicial:** 1091 | **Línea final:** 1105
- **Firma completa:** `def _update_tools_excel_status(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `basename, hasattr, config, getattr, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _build_advanced_tools_tab(self, parent)`
- **Línea inicial:** 1107 | **Línea final:** 1214
- **Firma completa:** `def _build_advanced_tools_tab(self, parent)`
- **Propósito:** Vista de Herramientas Avanzadas — diagnóstico y scrapers en Tkinter nativo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Button, grid_rowconfigure, make_action_btn, pack, grid_columnconfigure, configure, bbox, itemconfig, Scrollbar, create_tool_card`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _build_stock_tab(self, left_col, right_col, parent)`
- **Línea inicial:** 1218 | **Línea final:** 1472
- **Firma completa:** `def _build_stock_tab(self, left_col, right_col, parent)`
- **Propósito:** Vista de Análisis de Stock — paleta institucional light.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkLabel, insert, Event, CTkButton, CTkEntry, _on_stock_acuerdo_changed, setattr, enumerate, set, _load_stock_combos_json`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _export_stock_audit_report(self, fmt)`
- **Línea inicial:** 1489 | **Línea final:** 1523
- **Firma completa:** `def _export_stock_audit_report(self, fmt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, export_pdf_report, asksaveasfilename, getattr, export_excel_report, showerror, round, now, showwarning, upper`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_load_stock_excel(self)`
- **Línea inicial:** 1525 | **Línea final:** 1553
- **Firma completa:** `def _on_load_stock_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `analizar_excel_stock, basename, join, askopenfilename, configure, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_download_stock_template(self)`
- **Línea inicial:** 1555 | **Línea final:** 1577
- **Firma completa:** `def _on_download_stock_template(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, asksaveasfilename, Workbook, save, _append_stock_log`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _load_stock_combos_json(self)`
- **Línea inicial:** 1579 | **Línea final:** 1595
- **Firma completa:** `def _load_stock_combos_json(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `dirname, resource_path, insert, abspath, load, open, _append_stock_log`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_acuerdo_changed(self, acuerdo_text)`
- **Línea inicial:** 1597 | **Línea final:** 1617
- **Firma completa:** `def _on_stock_acuerdo_changed(self, acuerdo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sorted, configure, set, add, get, _on_stock_catalogo_changed`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_catalogo_changed(self, catalogo_text)`
- **Línea inicial:** 1619 | **Línea final:** 1640
- **Firma completa:** `def _on_stock_catalogo_changed(self, catalogo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sorted, configure, set, add, get, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_stock_start(self)`
- **Línea inicial:** 1642 | **Línea final:** 1691
- **Firma completa:** `def _on_stock_start(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, float, configure, Thread, get, strip, _append_stock_log, start`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def _on_stock_stop(self)`
- **Línea inicial:** 1693 | **Línea final:** 1707
- **Firma completa:** `def _on_stock_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, close, set, getattr, _append_stock_log`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _append_stock_log(self, msg)`
- **Línea inicial:** 1709 | **Línea final:** 1718
- **Firma completa:** `def _append_stock_log(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, configure, see, insert`
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
- **Dependencias / Invocaciones:** `clear, analizar_excel_stock, hasattr, str, configure, Thread, getattr, bool, exists, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 34)

### `def _on_audit_done(self, filas, resumen)`
- **Línea inicial:** 1817 | **Línea final:** 1878
- **Firma completa:** `def _on_audit_done(self, filas, resumen)`
- **Propósito:** Callback llamado por execute_auditor cuando termina.
Siempre se ejecuta en el hilo del auditor — usa self.after() para UI.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, hasattr, _append_stock_log, join, asksaveasfilename, Popen, configure, _ui_done, makedirs, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def _build_credentials_section(self, parent)`
- **Línea inicial:** 1879 | **Línea final:** 1931
- **Firma completa:** `def _build_credentials_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, CTkLabel, CTkButton, CTkEntry, CTkCheckBox, grid_columnconfigure, CTkFont, CTkFrame, _section_label, grid`
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
- **Dependencias / Invocaciones:** `CTkLabel, CTkButton, pack, grid_columnconfigure, CTkComboBox, CTkFont, CTkFrame, _section_label, grid`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _pick_excel(self)`
- **Línea inicial:** 2005 | **Línea final:** 2036
- **Firma completa:** `def _pick_excel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_sheet_changed, delete, basename, hasattr, insert, askopenfilename, configure, set, config, _update_tools_excel_status`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _on_sheet_changed(self, choice)`
- **Línea inicial:** 2038 | **Línea final:** 2107
- **Firma completa:** `def _on_sheet_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, parse_excel, lower, hasattr, enumerate, set, detect_columns, get, load_workbook, isdigit`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 31)

### `def _build_catalog_section(self, parent)`
- **Línea inicial:** 2111 | **Línea final:** 2169
- **Firma completa:** `def _build_catalog_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkLabel, grid_columnconfigure, dict, _opts_texts, CTkComboBox, set, _on_catalogo_changed, CTkFont, get, CTkFrame`
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
- **Dependencias / Invocaciones:** `strip, split, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _on_catalogo_changed(self, choice)`
- **Línea inicial:** 2182 | **Línea final:** 2191
- **Firma completa:** `def _on_catalogo_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_categoria_changed, _find_children, configure, _opts_texts, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _on_categoria_changed(self, choice)`
- **Línea inicial:** 2193 | **Línea final:** 2210
- **Firma completa:** `def _on_categoria_changed(self, choice)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, configure, _opts_texts, set, get, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_extract_json_portal(self)`
- **Línea inicial:** 2212 | **Línea final:** 2245
- **Firma completa:** `def _on_extract_json_portal(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `hasattr, print, basename, Thread, evaluate_js, bool, getattr, get, len, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def _build_opciones_section(self, parent)`
- **Línea inicial:** 2249 | **Línea final:** 2290
- **Firma completa:** `def _build_opciones_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkSlider, CTkLabel, grid_columnconfigure, configure, set, CTkFont, CTkFrame, _section_label, grid`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_execution_section(self, parent)`
- **Línea inicial:** 2294 | **Línea final:** 2354
- **Firma completa:** `def _build_execution_section(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_rowconfigure, CTkLabel, pack, grid_columnconfigure, configure, set, _build_captcha_panel, CTkTextbox, tag_config, CTkFont`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _make_stat(self, parent, label, color, col)`
- **Línea inicial:** 2356 | **Línea final:** 2364
- **Firma completa:** `def _make_stat(self, parent, label, color, col)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkLabel, pack, CTkFont, CTkFrame, grid`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_captcha_panel(self, parent)`
- **Línea inicial:** 2368 | **Línea final:** 2401
- **Firma completa:** `def _build_captcha_panel(self, parent)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkLabel, CTkButton, CTkEntry, grid_columnconfigure, grid_remove, CTkFont, CTkFrame, _on_captcha_submit, bind, grid`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _show_captcha(self, image_bytes)`
- **Línea inicial:** 2403 | **Línea final:** 2410
- **Firma completa:** `def _show_captcha(self, image_bytes)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `CTkImage, delete, focus_set, resize, configure, open, BytesIO, grid`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _hide_captcha_panel(self)`
- **Línea inicial:** 2412 | **Línea final:** 2413
- **Firma completa:** `def _hide_captcha_panel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid_remove`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_captcha_submit(self)`
- **Línea inicial:** 2415 | **Línea final:** 2420
- **Firma completa:** `def _on_captcha_submit(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log, _hide_captcha_panel, get, respond, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _section_label(self, parent, text, row)`
- **Línea inicial:** 2424 | **Línea final:** 2430
- **Firma completa:** `def _section_label(self, parent, text, row)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkLabel, CTkFont, grid`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(self, msg, level)`
- **Línea inicial:** 2432 | **Línea final:** 2437
- **Firma completa:** `def _log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, see, insert, append`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_test(self)`
- **Línea inicial:** 2441 | **Línea final:** 2483
- **Firma completa:** `def _on_test(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, delete, hasattr, split, configure, Thread, _val, set, _hide_captcha_panel, bool`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_certs_only(self)`
- **Línea inicial:** 2485 | **Línea final:** 2531
- **Firma completa:** `def _on_certs_only(self)`
- **Propósito:** Handler del botón 'Solo Certificaciones': entra a cada ficha y agrega ISO 9001/14001.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, delete, hasattr, split, configure, Thread, _val, set, _hide_captcha_panel, bool`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_extract(self)`
- **Línea inicial:** 2533 | **Línea final:** 2567
- **Firma completa:** `def _on_extract(self)`
- **Propósito:** Handler del botón 'Extraer Reportes': descarga reportes de Producto Ofertado.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, delete, configure, Thread, set, _hide_captcha_panel, bool, get, strip, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _execute_extract(self, usuario, password, headless)`
- **Línea inicial:** 2568 | **Línea final:** 2570
- **Firma completa:** `def _execute_extract(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_extract`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _execute_certs_only(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2571 | **Línea final:** 2573
- **Firma completa:** `def _execute_certs_only(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_certs_only`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_nro_parte(self)`
- **Línea inicial:** 2574 | **Línea final:** 2621
- **Firma completa:** `def _on_nro_parte(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, delete, split, configure, Thread, _val, set, _hide_captcha_panel, bool, get`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _execute_nro_parte(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2623 | **Línea final:** 2625
- **Firma completa:** `def _execute_nro_parte(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_nro_parte`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_compare(self)`
- **Línea inicial:** 2626 | **Línea final:** 2663
- **Firma completa:** `def _on_compare(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, delete, hasattr, split, configure, Thread, _val, set, _hide_captcha_panel, bool`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_compare(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2665 | **Línea final:** 2667
- **Firma completa:** `def _execute_compare(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_compare`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_discovery(self)`
- **Línea inicial:** 2668 | **Línea final:** 2691
- **Firma completa:** `def _on_discovery(self)`
- **Propósito:** Handler del botón 'Discovery': ejecuta el script discovery_perucompras.py.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, delete, configure, Thread, set, _hide_captcha_panel, bool, getattr, get, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_discovery(self, usuario, password, headless)`
- **Línea inicial:** 2693 | **Línea final:** 2695
- **Firma completa:** `def _execute_discovery(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_discovery`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_discovery2(self)`
- **Línea inicial:** 2696 | **Línea final:** 2719
- **Firma completa:** `def _on_discovery2(self)`
- **Propósito:** Handler del botón 'Discovery v2': scraping profundo multi-técnica.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, delete, configure, Thread, set, _hide_captcha_panel, bool, getattr, get, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute_discovery2(self, usuario, password, headless)`
- **Línea inicial:** 2721 | **Línea final:** 2723
- **Firma completa:** `def _execute_discovery2(self, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_discovery2`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _execute_test(self, usuario, password, headless, pre_selected)`
- **Línea inicial:** 2724 | **Línea final:** 2726
- **Firma completa:** `def _execute_test(self, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute_test`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_launch(self)`
- **Línea inicial:** 2741 | **Línea final:** 2808
- **Firma completa:** `def _on_launch(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clear, delete, split, configure, Thread, _val, set, _hide_captcha_panel, bool, get`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)`
- **Línea inicial:** 2810 | **Línea final:** 2820
- **Firma completa:** `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `execute`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_stop(self)`
- **Línea inicial:** 2821 | **Línea final:** 2830
- **Firma completa:** `def _on_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, after, _log, set`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _reset_after_stop(self)`
- **Línea inicial:** 2832 | **Línea final:** 2842
- **Firma completa:** `def _reset_after_stop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def poll_queue(self)`
- **Línea inicial:** 2867 | **Línea final:** 2927
- **Firma completa:** `def poll_queue(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, isinstance, _log, configure, after, is_set, set, _show_captcha, get, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def __init__(self, val)`
- **Línea inicial:** 2966 | **Línea final:** 2967
- **Firma completa:** `def __init__(self, val)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def get(self)`
- **Línea inicial:** 2968 | **Línea final:** 2969
- **Firma completa:** `def get(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def set(self, val)`
- **Línea inicial:** 2970 | **Línea final:** 2972
- **Firma completa:** `def set(self, val)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def configure(self)`
- **Línea inicial:** 2973 | **Línea final:** 2973
- **Firma completa:** `def configure(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def config(self)`
- **Línea inicial:** 2974 | **Línea final:** 2974
- **Firma completa:** `def config(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def delete(self)`
- **Línea inicial:** 2975 | **Línea final:** 2975
- **Firma completa:** `def delete(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def insert(self)`
- **Línea inicial:** 2976 | **Línea final:** 2976
- **Firma completa:** `def insert(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def see(self)`
- **Línea inicial:** 2977 | **Línea final:** 2977
- **Firma completa:** `def see(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def pack(self)`
- **Línea inicial:** 2978 | **Línea final:** 2978
- **Firma completa:** `def pack(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def place(self)`
- **Línea inicial:** 2979 | **Línea final:** 2979
- **Firma completa:** `def place(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def grid(self)`
- **Línea inicial:** 2980 | **Línea final:** 2980
- **Firma completa:** `def grid(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def destroy(self)`
- **Línea inicial:** 2981 | **Línea final:** 2981
- **Firma completa:** `def destroy(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def bind(self)`
- **Línea inicial:** 2982 | **Línea final:** 2982
- **Firma completa:** `def bind(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def unbind(self)`
- **Línea inicial:** 2983 | **Línea final:** 2983
- **Firma completa:** `def unbind(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __call__(self)`
- **Línea inicial:** 2984 | **Línea final:** 2984
- **Firma completa:** `def __call__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def __init__(self, app)`
- **Línea inicial:** 2990 | **Línea final:** 2993
- **Firma completa:** `def __init__(self, app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def set_window(self, w)`
- **Línea inicial:** 2995 | **Línea final:** 2996
- **Firma completa:** `def set_window(self, w)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def get_catalog_options(self)`
- **Línea inicial:** 2998 | **Línea final:** 3000
- **Firma completa:** `def get_catalog_options(self)`
- **Propósito:** Devuelve las opciones desplegables del archivo JSON.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def minimize(self)`
- **Línea inicial:** 3003 | **Línea final:** 3004
- **Firma completa:** `def minimize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `minimize`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def maximize(self)`
- **Línea inicial:** 3006 | **Línea final:** 3007
- **Firma completa:** `def maximize(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `toggle_fullscreen`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def close(self)`
- **Línea inicial:** 3009 | **Línea final:** 3010
- **Firma completa:** `def close(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def select_file(self)`
- **Línea inicial:** 3013 | **Línea final:** 3030
- **Firma completa:** `def select_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `attributes, basename, askopenfilename, parse_excel, withdraw, detect_columns, Tk, get, destroy, get_sheets`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def select_stock_file(self)`
- **Línea inicial:** 3033 | **Línea final:** 3070
- **Firma completa:** `def select_stock_file(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `analizar_excel_stock, iterrows, attributes, basename, append, str, askopenfilename, parse_excel, withdraw, detect_columns`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def load_sheet(self, sheet_name)`
- **Línea inicial:** 3072 | **Línea final:** 3078
- **Firma completa:** `def load_sheet(self, sheet_name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `getattr, detect_columns, parse_excel, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_process(self, params)`
- **Línea inicial:** 3081 | **Línea final:** 3095
- **Firma completa:** `def start_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_launch, float, str, _DummyWidget, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def stop_process(self)`
- **Línea inicial:** 3097 | **Línea final:** 3102
- **Firma completa:** `def stop_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _on_stop`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def start_stock_process(self, params)`
- **Línea inicial:** 3105 | **Línea final:** 3135
- **Firma completa:** `def start_stock_process(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, analizar_excel_stock, _DummyWidget, getattr, _on_stock_start, get, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def start_stock_audit(self, params)`
- **Línea inicial:** 3137 | **Línea final:** 3165
- **Firma completa:** `def start_stock_audit(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `analizar_excel_stock, str, _DummyWidget, getattr, get, strip, _on_stock_audit_start`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def extract_json_portal(self, params)`
- **Línea inicial:** 3167 | **Línea final:** 3182
- **Firma completa:** `def extract_json_portal(self, params)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _DummyWidget, get, _on_extract_json_portal, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def stop_stock_process(self)`
- **Línea inicial:** 3185 | **Línea final:** 3191
- **Firma completa:** `def stop_stock_process(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, hasattr, _on_stock_stop`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def download_stock_template(self)`
- **Línea inicial:** 3193 | **Línea final:** 3200
- **Firma completa:** `def download_stock_template(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_download_stock_template, hasattr, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def export_audit(self, fmt)`
- **Línea inicial:** 3203 | **Línea final:** 3208
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
- **Dependencias / Invocaciones:** `pack, config, cmd, Label, bind`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def add_sep(titulo)`
- **Línea inicial:** 826 | **Línea final:** 832
- **Firma completa:** `def add_sep(titulo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `grid, Frame, Label, pack`
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
- **Dependencias / Invocaciones:** `Button, pack`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _ui_done()`
- **Línea inicial:** 1821 | **Línea final:** 1873
- **Firma completa:** `def _ui_done()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, hasattr, join, asksaveasfilename, Popen, configure, makedirs, get, generar_excel_auditoria, _append_stock_log`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def _log(msg)`
- **Línea inicial:** 2220 | **Línea final:** 2227
- **Firma completa:** `def _log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `hasattr, print, evaluate_js, getattr, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _on_done(fichas, filepath)`
- **Línea inicial:** 2229 | **Línea final:** 2238
- **Firma completa:** `def _on_done(fichas, filepath)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `hasattr, basename, evaluate_js, getattr, len, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _val(combo)`
- **Línea inicial:** 2454 | **Línea final:** 2456
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, split, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2501 | **Línea final:** 2503
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, split, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2586 | **Línea final:** 2588
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, split, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2637 | **Línea final:** 2639
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, split, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _val(combo)`
- **Línea inicial:** 2791 | **Línea final:** 2793
- **Firma completa:** `def _val(combo)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, split, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _log(self, msg, level)`
- **Línea inicial:** 3239 | **Línea final:** 3254
- **Firma completa:** `def _log(self, msg, level)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, str, hasattr, insert, configure, evaluate_js, see, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _append_stock_log(self, msg)`
- **Línea inicial:** 3256 | **Línea final:** 3271
- **Firma completa:** `def _append_stock_log(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, str, hasattr, insert, configure, evaluate_js, see, dumps`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def __getattr__(self, name)`
- **Línea inicial:** 3273 | **Línea final:** 3276
- **Firma completa:** `def __getattr__(self, name)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_DummyWidget, setattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

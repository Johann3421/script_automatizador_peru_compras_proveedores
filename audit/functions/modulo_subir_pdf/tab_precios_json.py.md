# Auditoría de Funciones: `modulo_subir_pdf/tab_precios_json.py`

- **Lenguaje:** `python`
- **Líneas de código:** 456
- **Hash SHA256:** `c1b90363fc20`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def build_precios_json_tab(app, parent)`
- **Línea inicial:** 7 | **Línea final:** 193
- **Firma completa:** `def build_precios_json_tab(app, parent)`
- **Propósito:** Vista de Precios JSON — paleta institucional light.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_on_extraer_menu, CTkTextbox, _on_iniciar_precios, _on_test_precios, pack, CTkLabel, CTkButton, _pick_json, CTkOptionMenu, getattr`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _export_precios_audit_report(app, fmt)`
- **Línea inicial:** 196 | **Línea final:** 226
- **Firma completa:** `def _export_precios_audit_report(app, fmt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `showinfo, upper, asksaveasfilename, export_excel_report, getattr, showwarning, showerror, export_pdf_report, now, strftime`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _load_and_populate_catalog_menu(app)`
- **Línea inicial:** 229 | **Línea final:** 305
- **Firma completa:** `def _load_and_populate_catalog_menu(app)`
- **Propósito:** Carga y puebla automáticamente los dropdowns dinámicos desde cualquier JSON disponible.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `list, join, append, isfile, isinstance, open, configure, hasattr, get_writable_path, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 22)

### `def _pick_json(app, lbl_file)`
- **Línea inicial:** 308 | **Línea final:** 323
- **Firma completa:** `def _pick_json(app, lbl_file)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `open, configure, askopenfilename, load, basename, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _log_precios(app, msg)`
- **Línea inicial:** 325 | **Línea final:** 329
- **Firma completa:** `def _log_precios(app, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `insert, see, str, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_precio_acuerdo_changed(app, selected_val)`
- **Línea inicial:** 331 | **Línea final:** 346
- **Firma completa:** `def _on_precio_acuerdo_changed(app, selected_val)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, _on_precio_catalogo_changed, configure, hasattr, set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _on_precio_catalogo_changed(app, selected_val)`
- **Línea inicial:** 348 | **Línea final:** 364
- **Firma completa:** `def _on_precio_catalogo_changed(app, selected_val)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, set, configure, hasattr`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _on_extraer_menu(app)`
- **Línea inicial:** 367 | **Línea final:** 384
- **Firma completa:** `def _on_extraer_menu(app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `bool, configure, get, strip, _log_precios, Thread, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _on_test_precios(app)`
- **Línea inicial:** 386 | **Línea final:** 420
- **Firma completa:** `def _on_test_precios(app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `bool, split, configure, get, strip, _log_precios, Thread, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _on_iniciar_precios(app)`
- **Línea inicial:** 422 | **Línea final:** 455
- **Firma completa:** `def _on_iniciar_precios(app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `bool, split, configure, get, strip, _log_precios, Thread, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _card(parent_frame, title, row)`
- **Línea inicial:** 24 | **Línea final:** 33
- **Firma completa:** `def _card(parent_frame, title, row)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `CTkFrame, grid, grid_columnconfigure, CTkLabel, CTkFont`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

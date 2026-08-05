# Documentación Técnica: `modulo_subir_pdf/main_subir_pdf.py`

- **Ruta relativa:** `modulo_subir_pdf/main_subir_pdf.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 3323
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `SplashScreen` (Línea 79)
- **Docstring:** _Pestaña/Ventana de carga inicial elegante antes de mostrar la aplicación principal._
- **Métodos:**
  - `def __init__(self, parent)` (Línea 81): Sin docstring.
  - `def _step(self)` (Línea 144): Sin docstring.
  - `def _finish(self)` (Línea 154): Sin docstring.

#### Clase `CaptchaBridge` (Línea 199)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self)` (Línea 200): Sin docstring.
  - `def request(self, img)` (Línea 207): Sin docstring.
  - `def respond(self, code)` (Línea 221): Sin docstring.

#### Clase `SubirPdfApp` (Línea 268)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self)` (Línea 269): Sin docstring.
  - `def _load_dropdown_json(self)` (Línea 301): Sin docstring.
  - `def _setup_styles(self)` (Línea 365): Sin docstring.
  - `def _set_taskbar_icon(self)` (Línea 393): Sin docstring.
  - `def _start_drag(self, event)` (Línea 404): Sin docstring.
  - `def _drag_window(self, event)` (Línea 408): Sin docstring.
  - `def _close_window(self)` (Línea 415): Sin docstring.
  - `def _open_config_dialog(self)` (Línea 420): Abre la ventana modal de Configuración y Preferencias del Sistema.
  - `def _open_about_dialog(self)` (Línea 505): Abre la ventana modal Acerca del Sistema.
  - `def _minimize_window(self)` (Línea 557): Sin docstring.
  - `def _on_window_map(self, event)` (Línea 567): Sin docstring.
  - `def _toggle_maximize(self)` (Línea 578): Sin docstring.
  - `def _build_ui(self)` (Línea 618): Sin docstring.
  - `def _clear_excel(self)` (Línea 989): Sin docstring.
  - `def _switch_view(self, view_id)` (Línea 999): Cambia la vista activa y resalta el tab horizontal correspondiente.
  - `def _collect_tree_rows(self)` (Línea 1026): Sin docstring.
  - `def _run_auditor_check(self, modulo_nombre)` (Línea 1043): Ejecuta el chequeo rápido del auditor sobre las fichas procesadas.
  - `def _export_audit_report(self, fmt, modulo_nombre)` (Línea 1053): Genera y guarda el informe de auditoría en Excel (.xlsx) o PDF/HTML.
  - `def _update_tools_excel_status(self)` (Línea 1091): Sin docstring.
  - `def _build_advanced_tools_tab(self, parent)` (Línea 1107): Vista de Herramientas Avanzadas — diagnóstico y scrapers en Tkinter nativo.
  - `def _build_stock_tab(self, left_col, right_col, parent)` (Línea 1218): Vista de Análisis de Stock — paleta institucional light.
  - `def _export_stock_audit_report(self, fmt)` (Línea 1489): Sin docstring.
  - `def _on_load_stock_excel(self)` (Línea 1525): Sin docstring.
  - `def _on_download_stock_template(self)` (Línea 1555): Sin docstring.
  - `def _load_stock_combos_json(self)` (Línea 1579): Sin docstring.
  - `def _on_stock_acuerdo_changed(self, acuerdo_text)` (Línea 1597): Sin docstring.
  - `def _on_stock_catalogo_changed(self, catalogo_text)` (Línea 1619): Sin docstring.
  - `def _on_stock_start(self)` (Línea 1642): Sin docstring.
  - `def _on_stock_stop(self)` (Línea 1693): Sin docstring.
  - `def _append_stock_log(self, msg)` (Línea 1709): Sin docstring.
  - `def _execute_stock(self, usuario, password, acuerdo, catalogo, categoria, pausa)` (Línea 1720): Sin docstring.
  - `def _on_stock_audit_start(self)` (Línea 1733): Handler del botón '🔍 Auditar Portal'.
Valida credenciales y utiliza el Excel ya subido en la aplicación (pestaña Stock u Ofertas),
luego lanza execute_auditor en un hilo en segundo plano.
  - `def _on_audit_done(self, filas, resumen)` (Línea 1817): Callback llamado por execute_auditor cuando termina.
Siempre se ejecuta en el hilo del auditor — usa self.after() para UI.
  - `def _build_credentials_section(self, parent)` (Línea 1879): Sin docstring.
  - `def _toggle_password(self)` (Línea 1933): Sin docstring.
  - `def _build_excel_section(self, parent)` (Línea 1940): Sin docstring.
  - `def _pick_excel(self)` (Línea 2005): Sin docstring.
  - `def _on_sheet_changed(self, choice)` (Línea 2038): Sin docstring.
  - `def _build_catalog_section(self, parent)` (Línea 2111): Sin docstring.
  - `def _opts_texts(self, data)` (Línea 2171): Sin docstring.
  - `def _find_children(self, combo_text)` (Línea 2174): Sin docstring.
  - `def _on_catalogo_changed(self, choice)` (Línea 2182): Sin docstring.
  - `def _on_categoria_changed(self, choice)` (Línea 2193): Sin docstring.
  - `def _build_opciones_section(self, parent)` (Línea 2214): Sin docstring.
  - `def _build_execution_section(self, parent)` (Línea 2259): Sin docstring.
  - `def _make_stat(self, parent, label, color, col)` (Línea 2321): Sin docstring.
  - `def _build_captcha_panel(self, parent)` (Línea 2333): Sin docstring.
  - `def _show_captcha(self, image_bytes)` (Línea 2368): Sin docstring.
  - `def _hide_captcha_panel(self)` (Línea 2377): Sin docstring.
  - `def _on_captcha_submit(self)` (Línea 2380): Sin docstring.
  - `def _section_label(self, parent, text, row)` (Línea 2389): Sin docstring.
  - `def _log(self, msg, level)` (Línea 2397): Sin docstring.
  - `def _on_test(self)` (Línea 2406): Sin docstring.
  - `def _on_certs_only(self)` (Línea 2450): Handler del botón 'Solo Certificaciones': entra a cada ficha y agrega ISO 9001/14001.
  - `def _on_extract(self)` (Línea 2498): Handler del botón 'Extraer Reportes': descarga reportes de Producto Ofertado.
  - `def _execute_extract(self, usuario, password, headless)` (Línea 2533): Sin docstring.
  - `def _execute_certs_only(self, usuario, password, headless, pre_selected)` (Línea 2536): Sin docstring.
  - `def _on_nro_parte(self)` (Línea 2539): Sin docstring.
  - `def _execute_nro_parte(self, usuario, password, headless, pre_selected)` (Línea 2588): Sin docstring.
  - `def _on_compare(self)` (Línea 2591): Sin docstring.
  - `def _execute_compare(self, usuario, password, headless, pre_selected)` (Línea 2630): Sin docstring.
  - `def _on_discovery(self)` (Línea 2633): Handler del botón 'Discovery': ejecuta el script discovery_perucompras.py.
  - `def _execute_discovery(self, usuario, password, headless)` (Línea 2658): Sin docstring.
  - `def _on_discovery2(self)` (Línea 2661): Handler del botón 'Discovery v2': scraping profundo multi-técnica.
  - `def _execute_discovery2(self, usuario, password, headless)` (Línea 2686): Sin docstring.
  - `def _execute_test(self, usuario, password, headless, pre_selected)` (Línea 2689): Sin docstring.
  - `def _on_launch(self)` (Línea 2706): Sin docstring.
  - `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)` (Línea 2775): Sin docstring.
  - `def _on_stop(self)` (Línea 2786): Sin docstring.
  - `def _reset_after_stop(self)` (Línea 2797): Sin docstring.
  - `def poll_queue(self)` (Línea 2832): Sin docstring.

#### Clase `_DummyWidget` (Línea 2930)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, val)` (Línea 2931): Sin docstring.
  - `def get(self)` (Línea 2933): Sin docstring.
  - `def set(self, val)` (Línea 2935): Sin docstring.
  - `def configure(self)` (Línea 2938): Sin docstring.
  - `def config(self)` (Línea 2939): Sin docstring.
  - `def delete(self)` (Línea 2940): Sin docstring.
  - `def insert(self)` (Línea 2941): Sin docstring.
  - `def see(self)` (Línea 2942): Sin docstring.
  - `def pack(self)` (Línea 2943): Sin docstring.
  - `def place(self)` (Línea 2944): Sin docstring.
  - `def grid(self)` (Línea 2945): Sin docstring.
  - `def destroy(self)` (Línea 2946): Sin docstring.
  - `def bind(self)` (Línea 2947): Sin docstring.
  - `def unbind(self)` (Línea 2948): Sin docstring.
  - `def __call__(self)` (Línea 2949): Sin docstring.

#### Clase `SubirPdfWebApi` (Línea 2952)
- **Docstring:** _Puente JS -> Python. Delega al backend SubirPdfApp._
- **Métodos:**
  - `def __init__(self, app)` (Línea 2955): Sin docstring.
  - `def set_window(self, w)` (Línea 2960): Sin docstring.
  - `def get_catalog_options(self)` (Línea 2963): Devuelve las opciones desplegables del archivo JSON.
  - `def minimize(self)` (Línea 2968): Sin docstring.
  - `def maximize(self)` (Línea 2971): Sin docstring.
  - `def close(self)` (Línea 2974): Sin docstring.
  - `def select_file(self)` (Línea 2978): Sin docstring.
  - `def select_stock_file(self)` (Línea 2998): Sin docstring.
  - `def load_sheet(self, sheet_name)` (Línea 3037): Sin docstring.
  - `def start_process(self, params)` (Línea 3046): Sin docstring.
  - `def stop_process(self)` (Línea 3062): Sin docstring.
  - `def start_stock_process(self, params)` (Línea 3070): Sin docstring.
  - `def start_stock_audit(self, params)` (Línea 3102): Sin docstring.
  - `def stop_stock_process(self)` (Línea 3133): Sin docstring.
  - `def download_stock_template(self)` (Línea 3141): Sin docstring.
  - `def export_audit(self, fmt)` (Línea 3151): Sin docstring.

### Funciones independientes:

#### `def _make_stock_log(append_fn)` (Línea 171)
- **Propósito:** Sin docstring.
- **Firma:** `def _make_stock_log(append_fn)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def run_app()` (Línea 3182)
- **Propósito:** Sin docstring.
- **Firma:** `def run_app()`
- **Retorno / Efectos:** Consulta código fuente.

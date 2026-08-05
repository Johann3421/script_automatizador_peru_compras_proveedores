# Documentación Técnica: `modulo_modificar_productos/main_modificar.py`

- **Ruta relativa:** `modulo_modificar_productos/main_modificar.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 1076
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `CaptchaBridge` (Línea 35)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self)` (Línea 36): Sin docstring.
  - `def request(self, img)` (Línea 43): Sin docstring.
  - `def respond(self, code)` (Línea 57): Sin docstring.

#### Clase `ModificarProductosApp` (Línea 68)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self)` (Línea 69): Sin docstring.
  - `def _load_dropdown_json(self)` (Línea 97): Sin docstring.
  - `def _build_ui(self)` (Línea 111): Sin docstring.
  - `def _build_credentials_section(self, parent)` (Línea 206): Sin docstring.
  - `def _toggle_password(self)` (Línea 251): Sin docstring.
  - `def _build_excel_section(self, parent)` (Línea 258): Sin docstring.
  - `def _pick_excel(self)` (Línea 315): Sin docstring.
  - `def _on_sheet_changed(self, choice)` (Línea 337): Sin docstring.
  - `def _build_catalog_section(self, parent)` (Línea 407): Sin docstring.
  - `def _opts_texts(self, data)` (Línea 459): Sin docstring.
  - `def _find_children(self, combo_text)` (Línea 462): Sin docstring.
  - `def _on_catalogo_changed(self, choice)` (Línea 470): Sin docstring.
  - `def _on_categoria_changed(self, choice)` (Línea 481): Sin docstring.
  - `def _build_opciones_section(self, parent)` (Línea 502): Sin docstring.
  - `def _build_execution_section(self, parent)` (Línea 542): Sin docstring.
  - `def _make_stat(self, parent, label, color, col)` (Línea 593): Sin docstring.
  - `def _build_captcha_panel(self, parent)` (Línea 603): Sin docstring.
  - `def _show_captcha(self, image_bytes)` (Línea 633): Sin docstring.
  - `def _hide_captcha_panel(self)` (Línea 642): Sin docstring.
  - `def _on_captcha_submit(self)` (Línea 645): Sin docstring.
  - `def _section_label(self, parent, text, row)` (Línea 654): Sin docstring.
  - `def _log(self, msg, level)` (Línea 660): Sin docstring.
  - `def _on_test(self)` (Línea 669): Sin docstring.
  - `def _execute_test(self, usuario, password, headless, pre_selected)` (Línea 713): Sin docstring.
  - `def _on_launch(self)` (Línea 836): Sin docstring.
  - `def _execute(self, usuario, password, headless, rows, pausa, pre_selected)` (Línea 915): Sin docstring.
  - `def _on_stop(self)` (Línea 992): Sin docstring.
  - `def _reset_after_stop(self)` (Línea 999): Sin docstring.
  - `def poll_queue(self)` (Línea 1007): Sin docstring.

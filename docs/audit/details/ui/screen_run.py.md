# Documentación Técnica: `ui/screen_run.py`

- **Ruta relativa:** `ui/screen_run.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 359
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `ScreenRun` (Línea 17)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, app, container)` (Línea 18): Sin docstring.
  - `def _build_captcha_panel(self)` (Línea 85): Sin docstring.
  - `def _show_captcha(self, image_bytes)` (Línea 114): Sin docstring.
  - `def _hide_captcha(self)` (Línea 124): Sin docstring.
  - `def _on_captcha_submit(self)` (Línea 127): Sin docstring.
  - `def _build_catalog_panel(self)` (Línea 136): Sin docstring.
  - `def _show_catalog_step(self, step, options)` (Línea 165): Sin docstring.
  - `def _hide_catalog(self)` (Línea 181): Sin docstring.
  - `def _on_catalog_step_submit(self)` (Línea 184): Sin docstring.
  - `def on_enter(self)` (Línea 194): Sin docstring.
  - `def _run_automation(self)` (Línea 219): Sin docstring.
  - `def poll_queue(self)` (Línea 275): Sin docstring.
  - `def _handle_item(self, item)` (Línea 300): Sin docstring.
  - `def _append_log(self, msg, level)` (Línea 330): Sin docstring.
  - `def _on_stop(self)` (Línea 336): Sin docstring.
  - `def _download_log(self)` (Línea 341): Sin docstring.
  - `def _on_new(self)` (Línea 358): Sin docstring.

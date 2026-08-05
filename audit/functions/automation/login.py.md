# Auditoría de Funciones: `automation/login.py`

- **Lenguaje:** `python`
- **Líneas de código:** 348
- **Hash SHA256:** `253252881fe5`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _find_tesseract()`
- **Línea inicial:** 29 | **Línea final:** 43
- **Firma completa:** `def _find_tesseract()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `isfile, resource_path, which`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _eliminar_modales(page)`
- **Línea inicial:** 48 | **Línea final:** 56
- **Firma completa:** `def _eliminar_modales(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, count, click, sleep, locator`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _trigger_materialize_validation(page, input_id)`
- **Línea inicial:** 58 | **Línea final:** 68
- **Firma completa:** `def _trigger_materialize_validation(page, input_id)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _ocr_captcha(image_bytes)`
- **Línea inicial:** 71 | **Línea final:** 91
- **Firma completa:** `def _ocr_captcha(image_bytes)`
- **Propósito:** OCR del CAPTCHA con preprocesamiento mejorado.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `point, resize, open, image_to_string, BytesIO, convert, sub`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _solve_captcha(page, log, stop_event, captcha_bridge)`
- **Línea inicial:** 95 | **Línea final:** 161
- **Firma completa:** `def _solve_captcha(page, log, stop_event, captcha_bridge)`
- **Propósito:** Intenta OCR con reintentos. Si falla, pide al usuario vía CaptchaBridge.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `info, range, count, request, _ocr_captcha, click, bounding_box, error, sleep, is_set`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 21)

### `def do_login(page, usuario, password, captcha_key, log, stop_event, captcha_bridge, max_retries)`
- **Línea inicial:** 164 | **Línea final:** 223
- **Firma completa:** `def do_login(page, usuario, password, captcha_key, log, stop_event, captcha_bridge, max_retries)`
- **Propósito:** Intenta login repetidamente (por defecto hasta 99 intentos) hasta ingresar o ser detenido.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `info, range, _attempt_login_once, goto, Event, error, sleep, is_set, warning, wait_for_load_state`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def _attempt_login_once(page, usuario, password, captcha_key, log, stop_event, captcha_bridge)`
- **Línea inicial:** 226 | **Línea final:** 347
- **Firma completa:** `def _attempt_login_once(page, usuario, password, captcha_key, log, stop_event, captcha_bridge)`
- **Propósito:** Un solo intento de login. Retorna (éxito: bool, es_error_credenciales_fatal: bool).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `click, is_set, info, _solve_captcha, lower, inner_text, sleep, go_back, rstrip, any`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 21)

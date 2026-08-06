# Auditoría de Funciones: `automation/login.py`

- **Lenguaje:** `python`
- **Líneas de código:** 332
- **Hash SHA256:** `270b735e4719`
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
- **Dependencias / Invocaciones:** `locator, click, count, sleep, is_visible`
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
- **Dependencias / Invocaciones:** `BytesIO, sub, convert, image_to_string, resize, open, point`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _solve_captcha(page, log, stop_event, captcha_bridge)`
- **Línea inicial:** 95 | **Línea final:** 148
- **Firma completa:** `def _solve_captcha(page, log, stop_event, captcha_bridge)`
- **Propósito:** Intenta OCR con reintentos continuos e ilimitados hasta lograr 6 caracteres válidos o ser detenido.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `locator, click, count, warning, error, sleep, info, _ocr_captcha, request, bounding_box`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 17)

### `def do_login(page, usuario, password, captcha_key, log, stop_event, captcha_bridge, max_retries)`
- **Línea inicial:** 151 | **Línea final:** 207
- **Firma completa:** `def do_login(page, usuario, password, captcha_key, log, stop_event, captcha_bridge, max_retries)`
- **Propósito:** Intenta login continuamente hasta ingresar o ser detenido por el usuario.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `Event, warning, error, sleep, _attempt_login_once, info, wait_for_load_state, is_set, goto`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def _attempt_login_once(page, usuario, password, captcha_key, log, stop_event, captcha_bridge)`
- **Línea inicial:** 210 | **Línea final:** 331
- **Firma completa:** `def _attempt_login_once(page, usuario, password, captcha_key, log, stop_event, captcha_bridge)`
- **Propósito:** Un solo intento de login. Retorna (éxito: bool, es_error_credenciales_fatal: bool).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_solve_captcha, locator, inner_text, rstrip, click, sleep, info, wait_for_load_state, lower, any`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 21)

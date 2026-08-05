# Documentación Técnica: `automation/login.py`

- **Ruta relativa:** `automation/login.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 348
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _find_tesseract()` (Línea 29)
- **Propósito:** Sin docstring.
- **Firma:** `def _find_tesseract()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _eliminar_modales(page)` (Línea 48)
- **Propósito:** Sin docstring.
- **Firma:** `def _eliminar_modales(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _trigger_materialize_validation(page, input_id)` (Línea 58)
- **Propósito:** Sin docstring.
- **Firma:** `def _trigger_materialize_validation(page, input_id)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _ocr_captcha(image_bytes)` (Línea 71)
- **Propósito:** OCR del CAPTCHA con preprocesamiento mejorado.
- **Firma:** `def _ocr_captcha(image_bytes)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _solve_captcha(page, log, stop_event, captcha_bridge)` (Línea 95)
- **Propósito:** Intenta OCR con reintentos. Si falla, pide al usuario vía CaptchaBridge.
- **Firma:** `def _solve_captcha(page, log, stop_event, captcha_bridge)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def do_login(page, usuario, password, captcha_key, log, stop_event, captcha_bridge, max_retries)` (Línea 164)
- **Propósito:** Intenta login repetidamente (por defecto hasta 99 intentos) hasta ingresar o ser detenido.
- **Firma:** `def do_login(page, usuario, password, captcha_key, log, stop_event, captcha_bridge, max_retries)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _attempt_login_once(page, usuario, password, captcha_key, log, stop_event, captcha_bridge)` (Línea 226)
- **Propósito:** Un solo intento de login. Retorna (éxito: bool, es_error_credenciales_fatal: bool).
- **Firma:** `def _attempt_login_once(page, usuario, password, captcha_key, log, stop_event, captcha_bridge)`
- **Retorno / Efectos:** Consulta código fuente.

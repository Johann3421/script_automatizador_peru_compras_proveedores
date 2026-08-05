# Auditoría de Funciones: `automation/offer_loop.py`

- **Lenguaje:** `python`
- **Líneas de código:** 137
- **Hash SHA256:** `0d1d2af7abe7`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _safe_wait_networkidle(page, log, timeout)`
- **Línea inicial:** 21 | **Línea final:** 27
- **Firma completa:** `def _safe_wait_networkidle(page, log, timeout)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `warn, wait_for_load_state`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _dismiss_confirm_modal(page)`
- **Línea inicial:** 30 | **Línea final:** 47
- **Firma completa:** `def _dismiss_confirm_modal(page)`
- **Propósito:** Cierra el modal de confirmacion tras enviar ofertas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, count, locator, click, sleep, evaluate`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _dismiss_price_modal(page)`
- **Línea inicial:** 50 | **Línea final:** 71
- **Firma completa:** `def _dismiss_price_modal(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, count, locator, click, inner_text, sleep, strip, evaluate`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def run_offer_loop(page, rows, parte_col, precio_col, log, stop_event, credentials, captcha_key, credenciales_rus, credenciales_pass, captcha_bridge, catalog_bridge, pre_selected)`
- **Línea inicial:** 74 | **Línea final:** 137
- **Firma completa:** `def run_offer_loop(page, rows, parte_col, precio_col, log, stop_event, credentials, captcha_key, credenciales_rus, credenciales_pass, captcha_bridge, catalog_bridge, pre_selected)`
- **Propósito:** Procesa ofertas en MASA vía HTTP directo (bulk upload).
Mantiene la misma firma para compatibilidad con _execute().

Returns: list[dict] con status por fila (index, status, parte, precio, ...)
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `do_login, info, process_bulk_upload, sum, done, error, get, enumerate, str, setup_catalog_search`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

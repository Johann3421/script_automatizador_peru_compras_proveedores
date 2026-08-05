# Auditoría de Funciones: `modulo_modificar_productos/automation_mod/bulk_modificar.py`

- **Lenguaje:** `python`
- **Líneas de código:** 195
- **Hash SHA256:** `dcaff7bfdb1b`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def buscar_producto_api(page, parte, catalogo, categoria, estado, log, timeout)`
- **Línea inicial:** 29 | **Línea final:** 59
- **Firma completa:** `def buscar_producto_api(page, parte, catalogo, categoria, estado, log, timeout)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `text, time, loads, get, str, findall, int, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def _is_logged_in(page)`
- **Línea inicial:** 62 | **Línea final:** 70
- **Firma completa:** `def _is_logged_in(page)`
- **Propósito:** Verifica si seguimos logueados mirando la URL actual.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _relogin(page, usuario, password, log, stop_event, captcha_bridge)`
- **Línea inicial:** 73 | **Línea final:** 87
- **Firma completa:** `def _relogin(page, usuario, password, log, stop_event, captcha_bridge)`
- **Propósito:** Re-loguea y navega a la página de gestión.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `do_login, goto, error, sleep, ok, warn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def run_bulk_modificar(page, rows, pre_selected, log, stop_event, captcha_bridge, usuario, password)`
- **Línea inicial:** 90 | **Línea final:** 195
- **Firma completa:** `def run_bulk_modificar(page, rows, pre_selected, log, stop_event, captcha_bridge, usuario, password)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `info, buscar_producto_api, guardar_cambios, _is_logged_in, join, append, goto, error, get, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 17)

# Auditoría de Funciones: `modulo_subir_pdf/automation_mod/bulk_subir_pdf.py`

- **Lenguaje:** `python`
- **Líneas de código:** 311
- **Hash SHA256:** `547f1a85ab2a`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def buscar_producto_api(page, parte, catalogo, categoria, estado, log, timeout, ficha)`
- **Línea inicial:** 27 | **Línea final:** 59
- **Firma completa:** `def buscar_producto_api(page, parte, catalogo, categoria, estado, log, timeout, ficha)`
- **Propósito:** El "FICHA N°" del Excel es el ID_CatalogoProducto de PeruCompras.
Se navega DIRECTO a la URL de edit usando la ficha como ID.
Si la página no carga (404 o "no encontrado"), se retorna None.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `info, goto, lower, ok, wait_for_selector, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def _is_logged_in(page)`
- **Línea inicial:** 62 | **Línea final:** 72
- **Firma completa:** `def _is_logged_in(page)`
- **Propósito:** Verifica si seguimos logueados mirando la URL actual.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _tiene_campos_login(page)`
- **Línea inicial:** 75 | **Línea final:** 81
- **Firma completa:** `def _tiene_campos_login(page)`
- **Propósito:** Verifica si la página actual tiene los campos de login visibles.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, locator, count`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _relogin(page, usuario, password, log, stop_event, captcha_bridge)`
- **Línea inicial:** 84 | **Línea final:** 133
- **Firma completa:** `def _relogin(page, usuario, password, log, stop_event, captcha_bridge)`
- **Propósito:** Re-loguea y navega a la página de gestión.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `do_login, info, goto, lower, error, sleep, _tiene_campos_login, ok, warn`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def run_bulk_subir_pdf(page, rows, pre_selected, log, stop_event, captcha_bridge, usuario, password)`
- **Línea inicial:** 136 | **Línea final:** 311
- **Firma completa:** `def run_bulk_subir_pdf(page, rows, pre_selected, log, stop_event, captcha_bridge, usuario, password)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `buscar_producto_api, subir_imagen_en_edicion, _is_logged_in, agregar_certificaciones_faltantes, cambiar_precio_en_edicion, is_set, eliminar_caracteristica, str, info, guardar_cambios`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 30)

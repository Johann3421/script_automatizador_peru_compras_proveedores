# Auditoría de Funciones: `modulo_modificar_productos/automation_mod/navegacion_productos.py`

- **Lenguaje:** `python`
- **Líneas de código:** 756
- **Hash SHA256:** `844142191543`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _esperar_tabla(page, log, max_ciclos, espera)`
- **Línea inicial:** 30 | **Línea final:** 39
- **Firma completa:** `def _esperar_tabla(page, log, max_ciclos, espera)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, range, count, sleep, locator`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _es_no_encontrado(page)`
- **Línea inicial:** 42 | **Línea final:** 47
- **Firma completa:** `def _es_no_encontrado(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, locator, count`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _select2_select(page, select_id, value)`
- **Línea inicial:** 52 | **Línea final:** 107
- **Firma completa:** `def _select2_select(page, select_id, value)`
- **Propósito:** Selecciona una opción en un Select2 usando el método nativo de Playwright.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, range, count, text_content, locator, select_option, click, sleep, nth, wait_for`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def apply_dropdowns_and_search(page, pre_selected, log, stop_event)`
- **Línea inicial:** 112 | **Línea final:** 318
- **Firma completa:** `def apply_dropdowns_and_search(page, pre_selected, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_esperar_tabla, click, is_set, screenshot, info, sleep, _select2_select, evaluate, warn, range`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 27)

### `def buscar_por_parte(page, parte, log, stop_event)`
- **Línea inicial:** 323 | **Línea final:** 363
- **Firma completa:** `def buscar_por_parte(page, parte, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, is_visible, range, _esperar_tabla, click, error, sleep, is_set, _es_no_encontrado`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def click_editar(page, log, stop_event)`
- **Línea inicial:** 368 | **Línea final:** 404
- **Firma completa:** `def click_editar(page, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, is_visible, click, error, sleep, is_set, wait_for_load_state, locator, get_attribute`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)`
- **Línea inicial:** 409 | **Línea final:** 430
- **Firma completa:** `def subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, set_input_files, isfile, error, sleep, is_set, ok, basename, locator`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def guardar_cambios(page, log, stop_event)`
- **Línea inicial:** 435 | **Línea final:** 451
- **Firma completa:** `def guardar_cambios(page, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, click, error, cerrar_modal_mensaje, is_set, ok, locator`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def cerrar_modal_mensaje(page, log, context)`
- **Línea inicial:** 454 | **Línea final:** 481
- **Firma completa:** `def cerrar_modal_mensaje(page, log, context)`
- **Propósito:** Espera y cierra el modal #MensajeModal que aparece tras guardar.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, is_visible, count, click, sleep, wait_for, locator, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def ensure_logged_in_and_ready(page, usuario, password, pre_selected, log, stop_event, captcha_bridge)`
- **Línea inicial:** 486 | **Línea final:** 528
- **Firma completa:** `def ensure_logged_in_and_ready(page, usuario, password, pre_selected, log, stop_event, captcha_bridge)`
- **Propósito:** Verifica que sigamos logueados y en la lista de productos.
Si no, re-loguea, navega a t_CatalogoProductoMarca, aplica dropdowns y busca.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `do_login, count, goto, lower, apply_dropdowns_and_search, error, sleep, is_set, ok, locator`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def agregar_caracteristicas(page, log, stop_event)`
- **Línea inicial:** 533 | **Línea final:** 677
- **Firma completa:** `def agregar_caracteristicas(page, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_get_select_options, click, is_set, info, sleep, evaluate, warn, range, press, select_option`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 34)

### `def _get_select_options(page, selector)`
- **Línea inicial:** 680 | **Línea final:** 688
- **Firma completa:** `def _get_select_options(page, selector)`
- **Propósito:** Retorna las opciones de un select como [{value, text}, ...].
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def volver_a_lista(page, log, stop_event)`
- **Línea inicial:** 693 | **Línea final:** 723
- **Firma completa:** `def volver_a_lista(page, log, stop_event)`
- **Propósito:** Click en #btnRegresarIndex (Retornar) para volver a la lista.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `is_visible, info, count, goto, click, sleep, is_set, wait_for_load_state, go_back, locator`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def process_single_product(page, parte, ruta_pdf, log, stop_event, pre_selected)`
- **Línea inicial:** 728 | **Línea final:** 756
- **Firma completa:** `def process_single_product(page, parte, ruta_pdf, log, stop_event, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `buscar_por_parte, guardar_cambios, apply_dropdowns_and_search, click_editar, get, agregar_caracteristicas, volver_a_lista, subir_pdf_en_edicion`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

# Auditoría de Funciones: `modulo_subir_pdf/automation_otro_bot/stock.py`

- **Lenguaje:** `python`
- **Líneas de código:** 1490
- **Hash SHA256:** `2d5aa70ace18`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _is_logged_in(page)`
- **Línea inicial:** 110 | **Línea final:** 129
- **Firma completa:** `def _is_logged_in(page)`
- **Propósito:** Verifica si seguimos logueados: URL + ausencia de formulario login visible.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, locator, wait_for`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _esta_en_mejorabasica(page)`
- **Línea inicial:** 132 | **Línea final:** 138
- **Firma completa:** `def _esta_en_mejorabasica(page)`
- **Propósito:** Verifica que estemos en la página de MejoraBasica (donde se editan productos).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _tiene_campos_login(page)`
- **Línea inicial:** 141 | **Línea final:** 147
- **Firma completa:** `def _tiene_campos_login(page)`
- **Propósito:** Verifica si la página actual tiene los campos de login visibles.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, count, locator`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _relogin(page, usuario, password, log_func, stop_event, captcha_bridge)`
- **Línea inicial:** 150 | **Línea final:** 201
- **Firma completa:** `def _relogin(page, usuario, password, log_func, stop_event, captcha_bridge)`
- **Propósito:** Vuelve a la pagina de login, se loguea de cero y navega a MejoraBasica.

Usa automation.login.do_login (la misma funcion del login inicial) porque
cierra mejor los modales del portal PeruCompras.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `do_login, insert, _LogAdapter, Event, is_set, abspath, dirname, log_func, goto, wait_for_load_state`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def log(msg)`
- **Línea inicial:** 222 | **Línea final:** 231
- **Firma completa:** `def log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `getattr, encode, now, strftime, print, decode`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def clear_modals(page)`
- **Línea inicial:** 271 | **Línea final:** 278
- **Firma completa:** `def clear_modals(page)`
- **Propósito:** Limpia todos los modales colgados.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log, evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _trigger_materialize(page, input_id)`
- **Línea inicial:** 285 | **Línea final:** 297
- **Firma completa:** `def _trigger_materialize(page, input_id)`
- **Propósito:** Dispara eventos input/change/blur en un input para Materialize CSS.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log, evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _solve_captcha(page)`
- **Línea inicial:** 300 | **Línea final:** 325
- **Firma completa:** `def _solve_captcha(page)`
- **Propósito:** OCR del CAPTCHA con 4 thresholds.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `resize, sub, log, image_to_string, BytesIO, strip, screenshot, wait_for, locator, upper`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _type_field(page, selector_list, value, materialize_id)`
- **Línea inicial:** 328 | **Línea final:** 343
- **Firma completa:** `def _type_field(page, selector_list, value, materialize_id)`
- **Propósito:** Escribe value en el primer selector que funcione.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `fill, _trigger_materialize, click, str, count, locator`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def login_with_ocr(page, usuario, password, captcha_bridge, max_intentos, skip_goto)`
- **Línea inicial:** 346 | **Línea final:** 465
- **Firma completa:** `def login_with_ocr(page, usuario, password, captcha_bridge, max_intentos, skip_goto)`
- **Propósito:** Login automático con OCR del CAPTCHA.

Si el OCR no está disponible, retorna False (caller debe caer a login manual).
skip_goto: si True, asume que ya estamos en LOGIN_URL y no navega de nuevo.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `range, _solve_captcha, _type_field, wait_for_load_state, evaluate, screenshot, is_set, go_back, click, goto`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 26)

### `def _normalizar_parte(valor)`
- **Línea inicial:** 472 | **Línea final:** 481
- **Firma completa:** `def _normalizar_parte(valor)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, strip, isnan, isinstance`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _normalizar_stock(valor)`
- **Línea inicial:** 484 | **Línea final:** 500
- **Firma completa:** `def _normalizar_stock(valor)`
- **Propósito:** Convierte a int, retorna None si es inválido.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `float, strip, int, str, isnan, isinstance`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def analizar_excel_stock(excel_path)`
- **Línea inicial:** 503 | **Línea final:** 567
- **Firma completa:** `def analizar_excel_stock(excel_path)`
- **Propósito:** Analiza el Excel de stock. Retorna {valido: bool, df: [...], errores: [...]}
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log, lower, strip, close, load_workbook, append, any, _normalizar_parte, isfile, enumerate`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 22)

### `def paso2_navegacion_stock(page)`
- **Línea inicial:** 574 | **Línea final:** 590
- **Firma completa:** `def paso2_navegacion_stock(page)`
- **Propósito:** Truco de retroceso + ir a MejoraBasica.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `log, goto, go_back, sleep`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def seleccionar_por_texto_flexible(page, select_id, texto_objetivo, retries, delay)`
- **Línea inicial:** 593 | **Línea final:** 702
- **Firma completa:** `def seleccionar_por_texto_flexible(page, select_id, texto_objetivo, retries, delay)`
- **Propósito:** Selecciona option por match flexible en Playwright disparando eventos jQuery/DOM.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, range, evaluate, lower, strip, replace, str, items, normalizar, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 24)

### `def _wait_for_select_options(page, select_id, timeout_ms)`
- **Línea inicial:** 707 | **Línea final:** 720
- **Firma completa:** `def _wait_for_select_options(page, select_id, timeout_ms)`
- **Propósito:** Espera a que un <select> tenga opciones con value no vacio.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait_for_function`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def paso3_filtros_stock(page, acuerdo, catalogo, categoria)`
- **Línea inicial:** 723 | **Línea final:** 783
- **Firma completa:** `def paso3_filtros_stock(page, acuerdo, catalogo, categoria)`
- **Propósito:** Selecciona Acuerdo > Catálogo > Categoría y espera que cargue la tabla.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log, evaluate, wait_for, _wait_for_select_options, wait_for_selector, seleccionar_por_texto_flexible, click, count, locator, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 12)

### `def clasificar_error(mensaje)`
- **Línea inicial:** 790 | **Línea final:** 804
- **Firma completa:** `def clasificar_error(mensaje)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, lower`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _browser_cerrado(mensaje)`
- **Línea inicial:** 807 | **Línea final:** 815
- **Firma completa:** `def _browser_cerrado(mensaje)`
- **Propósito:** Detecta si el error se debe a que el usuario cerró el navegador.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `any, lower, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _es_sin_resultados(mensaje)`
- **Línea inicial:** 818 | **Línea final:** 829
- **Firma completa:** `def _es_sin_resultados(mensaje)`
- **Propósito:** Detecta si la respuesta indica explicitamente que el producto no existe en el portal.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `any, lower, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _find_exact_matching_row(page, parte)`
- **Línea inicial:** 832 | **Línea final:** 875
- **Firma completa:** `def _find_exact_matching_row(page, parte)`
- **Propósito:** Busca en la tabla de productos la fila que contenga EXACTAMENTE el número de parte.
Evita seleccionar por error 'PARTE-1' cuando se busca 'PARTE'.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, all, join, strip, str, upper, compile, escape, search, inner_text`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def actualizar_producto(page, parte, stock, ficha, stop_event)`
- **Línea inicial:** 878 | **Línea final:** 1156
- **Firma completa:** `def actualizar_producto(page, parte, stock, ficha, stop_event)`
- **Propósito:** Actualiza el stock de un producto. Retorna (éxito, mensaje_error).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, all, is_visible, int, str, evaluate, strip, is_set, click, dispatch_event`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 83)

### `def _get_field(row, keys, default)`
- **Línea inicial:** 1159 | **Línea final:** 1169
- **Firma completa:** `def _get_field(row, keys, default)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, strip, items, str, isinstance`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge, acuerdo, catalogo, categoria)`
- **Línea inicial:** 1172 | **Línea final:** 1286
- **Firma completa:** `def paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge, acuerdo, catalogo, categoria)`
- **Propósito:** Itera el DataFrame y actualiza cada producto. Retorna cantidad de éxitos.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `range, time, str, strip, _get_field, is_set, _is_logged_in, round, actualizar_producto, _esta_en_mejorabasica`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 37)

### `def generar_reporte_excel(output_path, acuerdo, catalogo, categoria)`
- **Línea inicial:** 1299 | **Línea final:** 1431
- **Firma completa:** `def generar_reporte_excel(output_path, acuerdo, catalogo, categoria)`
- **Propósito:** Genera el reporte Excel con 3 hojas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `abspath, range, Reference, sum, len, sorted, items, create_sheet, makedirs, strftime`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def ejecutar_stock(page, excel_path, usuario, password, acuerdo, catalogo, categoria, pausa, captcha_bridge, log_func)`
- **Línea inicial:** 1438 | **Línea final:** 1490
- **Firma completa:** `def ejecutar_stock(page, excel_path, usuario, password, acuerdo, catalogo, categoria, pausa, captcha_bridge, log_func)`
- **Propósito:** Ejecuta el flujo completo de stock. Retorna path del reporte.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `paso4_actualizar_stock, join, login_with_ocr, dirname, paso2_navegacion_stock, paso3_filtros_stock, now, strftime, generar_reporte_excel, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def __init__(self, log_func)`
- **Línea inicial:** 84 | **Línea final:** 85
- **Firma completa:** `def __init__(self, log_func)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def info(self, msg)`
- **Línea inicial:** 87 | **Línea final:** 88
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 90 | **Línea final:** 91
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 93 | **Línea final:** 94
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, msg)`
- **Línea inicial:** 96 | **Línea final:** 97
- **Firma completa:** `def warn(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def progress(self, current, total)`
- **Línea inicial:** 99 | **Línea final:** 100
- **Firma completa:** `def progress(self, current, total)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def done(self, ok_count, error_count)`
- **Línea inicial:** 102 | **Línea final:** 103
- **Firma completa:** `def done(self, ok_count, error_count)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def normalizar(s)`
- **Línea inicial:** 595 | **Línea final:** 602
- **Firma completa:** `def normalizar(s)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, strip, replace, items, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

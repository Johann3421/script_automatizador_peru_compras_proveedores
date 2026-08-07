# Auditoría de Funciones: `modulo_subir_pdf/automation_otro_bot/stock.py`

- **Lenguaje:** `python`
- **Líneas de código:** 1486
- **Hash SHA256:** `a84c265f47cb`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _is_logged_in(page)`
- **Línea inicial:** 110 | **Línea final:** 129
- **Firma completa:** `def _is_logged_in(page)`
- **Propósito:** Verifica si seguimos logueados: URL + ausencia de formulario login visible.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait_for, locator, lower`
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
- **Dependencias / Invocaciones:** `is_visible, locator, count`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _relogin(page, usuario, password, log_func, stop_event, captcha_bridge)`
- **Línea inicial:** 150 | **Línea final:** 173
- **Firma completa:** `def _relogin(page, usuario, password, log_func, stop_event, captcha_bridge)`
- **Propósito:** Vuelve a la página de login y se loguea de cero usando la Función Padre centralizada login_automatico.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `saltar_verificacion, Event, log_func, login_automatico, is_set`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def log(msg)`
- **Línea inicial:** 194 | **Línea final:** 203
- **Firma completa:** `def log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `strftime, decode, print, encode, getattr, now`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def clear_modals(page)`
- **Línea inicial:** 243 | **Línea final:** 250
- **Firma completa:** `def clear_modals(page)`
- **Propósito:** Limpia todos los modales colgados.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate, log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _trigger_materialize(page, input_id)`
- **Línea inicial:** 257 | **Línea final:** 269
- **Firma completa:** `def _trigger_materialize(page, input_id)`
- **Propósito:** Dispara eventos input/change/blur en un input para Materialize CSS.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate, log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _solve_captcha(page)`
- **Línea inicial:** 272 | **Línea final:** 297
- **Firma completa:** `def _solve_captcha(page)`
- **Propósito:** OCR del CAPTCHA con 4 thresholds.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `sub, locator, upper, open, convert, point, strip, screenshot, image_to_string, log`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _type_field(page, selector_list, value, materialize_id)`
- **Línea inicial:** 300 | **Línea final:** 315
- **Firma completa:** `def _type_field(page, selector_list, value, materialize_id)`
- **Propósito:** Escribe value en el primer selector que funcione.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `locator, click, count, fill, str, _trigger_materialize`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def login_with_ocr(page, usuario, password, captcha_bridge, max_intentos, skip_goto)`
- **Línea inicial:** 318 | **Línea final:** 437
- **Firma completa:** `def login_with_ocr(page, usuario, password, captcha_bridge, max_intentos, skip_goto)`
- **Propósito:** Login automático con OCR del CAPTCHA.

Si el OCR no está disponible, retorna False (caller debe caer a login manual).
skip_goto: si True, asume que ya estamos en LOGIN_URL y no navega de nuevo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `locator, count, clear_modals, _solve_captcha, _type_field, screenshot, go_back, wait_for_load_state, sleep, sub`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 26)

### `def _normalizar_parte(valor)`
- **Línea inicial:** 444 | **Línea final:** 453
- **Firma completa:** `def _normalizar_parte(valor)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, isinstance, str, isnan`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _normalizar_stock(valor)`
- **Línea inicial:** 456 | **Línea final:** 472
- **Firma completa:** `def _normalizar_stock(valor)`
- **Propósito:** Convierte a int, retorna None si es inválido.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, str, isinstance, isnan, float, int`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def analizar_excel_stock(excel_path)`
- **Línea inicial:** 475 | **Línea final:** 539
- **Firma completa:** `def analizar_excel_stock(excel_path)`
- **Propósito:** Analiza el Excel de stock. Retorna {valido: bool, df: [...], errores: [...]}
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `isfile, enumerate, _normalizar_stock, list, lower, append, strip, load_workbook, _normalizar_parte, iter_rows`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 22)

### `def paso2_navegacion_stock(page)`
- **Línea inicial:** 546 | **Línea final:** 562
- **Firma completa:** `def paso2_navegacion_stock(page)`
- **Propósito:** Truco de retroceso + ir a MejoraBasica.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `goto, go_back, log, sleep`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def seleccionar_por_texto_flexible(page, select_id, texto_objetivo, retries, delay)`
- **Línea inicial:** 565 | **Línea final:** 674
- **Firma completa:** `def seleccionar_por_texto_flexible(page, select_id, texto_objetivo, retries, delay)`
- **Propósito:** Selecciona option por match flexible en Playwright disparando eventos jQuery/DOM.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `normalizar, select_option, replace, split, items, lower, strip, evaluate, str, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 24)

### `def _wait_for_select_options(page, select_id, timeout_ms)`
- **Línea inicial:** 679 | **Línea final:** 692
- **Firma completa:** `def _wait_for_select_options(page, select_id, timeout_ms)`
- **Propósito:** Espera a que un <select> tenga opciones con value no vacio.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait_for_function`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def paso3_filtros_stock(page, acuerdo, catalogo, categoria)`
- **Línea inicial:** 695 | **Línea final:** 779
- **Firma completa:** `def paso3_filtros_stock(page, acuerdo, catalogo, categoria)`
- **Propósito:** Selecciona Acuerdo > Catálogo > Categoría y espera que cargue la tabla.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `locator, click, _wait_for_select_options, count, seleccionar_por_texto_flexible, evaluate, wait_for_selector, log, wait_for, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def clasificar_error(mensaje)`
- **Línea inicial:** 786 | **Línea final:** 800
- **Firma completa:** `def clasificar_error(mensaje)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, lower`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _browser_cerrado(mensaje)`
- **Línea inicial:** 803 | **Línea final:** 811
- **Firma completa:** `def _browser_cerrado(mensaje)`
- **Propósito:** Detecta si el error se debe a que el usuario cerró el navegador.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, any, lower`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _es_sin_resultados(mensaje)`
- **Línea inicial:** 814 | **Línea final:** 825
- **Firma completa:** `def _es_sin_resultados(mensaje)`
- **Propósito:** Detecta si la respuesta indica explicitamente que el producto no existe en el portal.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, any, lower`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _find_exact_matching_row(page, parte)`
- **Línea inicial:** 828 | **Línea final:** 871
- **Firma completa:** `def _find_exact_matching_row(page, parte)`
- **Propósito:** Busca en la tabla de productos la fila que contenga EXACTAMENTE el número de parte.
Evita seleccionar por error 'PARTE-1' cuando se busca 'PARTE'.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `compile, locator, join, search, escape, upper, count, split, all, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def actualizar_producto(page, parte, stock, ficha, stop_event)`
- **Línea inicial:** 874 | **Línea final:** 1152
- **Firma completa:** `def actualizar_producto(page, parte, stock, ficha, stop_event)`
- **Propósito:** Actualiza el stock de un producto. Retorna (éxito, mensaje_error).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `locator, count, all, append, strip, float, dispatch_event, int, _find_exact_matching_row, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 83)

### `def _get_field(row, keys, default)`
- **Línea inicial:** 1155 | **Línea final:** 1165
- **Firma completa:** `def _get_field(row, keys, default)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `items, lower, strip, isinstance, str`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge, acuerdo, catalogo, categoria)`
- **Línea inicial:** 1168 | **Línea final:** 1282
- **Firma completa:** `def paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge, acuerdo, catalogo, categoria)`
- **Propósito:** Itera el DataFrame y actualiza cada producto. Retorna cantidad de éxitos.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_es_sin_resultados, paso3_filtros_stock, append, strip, actualizar_producto, _is_logged_in, len, _browser_cerrado, sleep, _get_field`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 37)

### `def generar_reporte_excel(output_path, acuerdo, catalogo, categoria)`
- **Línea inicial:** 1295 | **Línea final:** 1427
- **Firma completa:** `def generar_reporte_excel(output_path, acuerdo, catalogo, categoria)`
- **Propósito:** Genera el reporte Excel con 3 hojas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `create_sheet, add_data, BarChart, Workbook, PieChart, dirname, strftime, get_column_letter, save, add_chart`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def ejecutar_stock(page, excel_path, usuario, password, acuerdo, catalogo, categoria, pausa, captcha_bridge, log_func)`
- **Línea inicial:** 1434 | **Línea final:** 1486
- **Firma completa:** `def ejecutar_stock(page, excel_path, usuario, password, acuerdo, catalogo, categoria, pausa, captcha_bridge, log_func)`
- **Propósito:** Ejecuta el flujo completo de stock. Retorna path del reporte.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, generar_reporte_excel, strftime, dirname, login_with_ocr, now, analizar_excel_stock, paso3_filtros_stock, log_func, paso2_navegacion_stock`
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
- **Línea inicial:** 567 | **Línea final:** 574
- **Firma completa:** `def normalizar(s)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `items, lower, strip, str, replace`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

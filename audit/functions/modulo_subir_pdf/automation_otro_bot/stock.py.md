# Auditoría de Funciones: `modulo_subir_pdf/automation_otro_bot/stock.py`

- **Lenguaje:** `python`
- **Líneas de código:** 1450
- **Hash SHA256:** `8ec98635fbe0`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _is_logged_in(page)`
- **Línea inicial:** 110 | **Línea final:** 129
- **Firma completa:** `def _is_logged_in(page)`
- **Propósito:** Verifica si seguimos logueados: URL + ausencia de formulario login visible.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `locator, wait_for, lower`
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
- **Línea inicial:** 150 | **Línea final:** 201
- **Firma completa:** `def _relogin(page, usuario, password, log_func, stop_event, captcha_bridge)`
- **Propósito:** Vuelve a la pagina de login, se loguea de cero y navega a MejoraBasica.

Usa automation.login.do_login (la misma funcion del login inicial) porque
cierra mejor los modales del portal PeruCompras.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `_LogAdapter, goto, wait_for_load_state, do_login, dirname, abspath, is_set, Event, insert, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 15)

### `def log(msg)`
- **Línea inicial:** 222 | **Línea final:** 231
- **Firma completa:** `def log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `getattr, encode, print, strftime, decode, now`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def clear_modals(page)`
- **Línea inicial:** 271 | **Línea final:** 278
- **Firma completa:** `def clear_modals(page)`
- **Propósito:** Limpia todos los modales colgados.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate, log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _trigger_materialize(page, input_id)`
- **Línea inicial:** 285 | **Línea final:** 297
- **Firma completa:** `def _trigger_materialize(page, input_id)`
- **Propósito:** Dispara eventos input/change/blur en un input para Materialize CSS.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate, log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _solve_captcha(page)`
- **Línea inicial:** 300 | **Línea final:** 325
- **Firma completa:** `def _solve_captcha(page)`
- **Propósito:** OCR del CAPTCHA con 4 thresholds.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `log, resize, open, point, len, wait_for, screenshot, locator, convert, sub`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def _type_field(page, selector_list, value, materialize_id)`
- **Línea inicial:** 328 | **Línea final:** 343
- **Firma completa:** `def _type_field(page, selector_list, value, materialize_id)`
- **Propósito:** Escribe value en el primer selector que funcione.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _trigger_materialize, count, fill, locator, click`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def login_with_ocr(page, usuario, password, captcha_bridge, max_intentos, skip_goto)`
- **Línea inicial:** 346 | **Línea final:** 465
- **Firma completa:** `def login_with_ocr(page, usuario, password, captcha_bridge, max_intentos, skip_goto)`
- **Propósito:** Login automático con OCR del CAPTCHA.

Si el OCR no está disponible, retorna False (caller debe caer a login manual).
skip_goto: si True, asume que ya estamos en LOGIN_URL y no navega de nuevo.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `clear_modals, _type_field, evaluate, click, request, sub, upper, is_set, lower, goto`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 26)

### `def _normalizar_parte(valor)`
- **Línea inicial:** 472 | **Línea final:** 481
- **Firma completa:** `def _normalizar_parte(valor)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, isnan, strip, isinstance`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _normalizar_stock(valor)`
- **Línea inicial:** 484 | **Línea final:** 500
- **Firma completa:** `def _normalizar_stock(valor)`
- **Propósito:** Convierte a int, retorna None si es inválido.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, float, isnan, isinstance, int, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def analizar_excel_stock(excel_path)`
- **Línea inicial:** 503 | **Línea final:** 567
- **Firma completa:** `def analizar_excel_stock(excel_path)`
- **Propósito:** Analiza el Excel de stock. Retorna {valido: bool, df: [...], errores: [...]}
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, load_workbook, log, list, len, isfile, iter_rows, append, close, enumerate`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 22)

### `def paso2_navegacion_stock(page)`
- **Línea inicial:** 574 | **Línea final:** 590
- **Firma completa:** `def paso2_navegacion_stock(page)`
- **Propósito:** Truco de retroceso + ir a MejoraBasica.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `goto, go_back, log, sleep`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def seleccionar_por_texto_flexible(page, select_id, texto_objetivo, retries, delay)`
- **Línea inicial:** 593 | **Línea final:** 683
- **Firma completa:** `def seleccionar_por_texto_flexible(page, select_id, texto_objetivo, retries, delay)`
- **Propósito:** Selecciona option por match flexible, reintenta peticiones AJAX y dispara eventos 'change' en el DOM.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, replace, range, len, normalizar, items, evaluate, strip, sleep, lower`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def _wait_for_select_options(page, select_id, timeout_ms)`
- **Línea inicial:** 688 | **Línea final:** 701
- **Firma completa:** `def _wait_for_select_options(page, select_id, timeout_ms)`
- **Propósito:** Espera a que un <select> tenga opciones con value no vacio.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait_for_function`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def paso3_filtros_stock(page, acuerdo, catalogo, categoria)`
- **Línea inicial:** 704 | **Línea final:** 749
- **Firma completa:** `def paso3_filtros_stock(page, acuerdo, catalogo, categoria)`
- **Propósito:** Selecciona Acuerdo > Catálogo > Categoría y espera que cargue la tabla.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log, _wait_for_select_options, wait_for_selector, wait_for, locator, seleccionar_por_texto_flexible, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def clasificar_error(mensaje)`
- **Línea inicial:** 756 | **Línea final:** 770
- **Firma completa:** `def clasificar_error(mensaje)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, lower`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def _browser_cerrado(mensaje)`
- **Línea inicial:** 773 | **Línea final:** 781
- **Firma completa:** `def _browser_cerrado(mensaje)`
- **Propósito:** Detecta si el error se debe a que el usuario cerró el navegador.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, any, lower`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _find_exact_matching_row(page, parte)`
- **Línea inicial:** 784 | **Línea final:** 827
- **Firma completa:** `def _find_exact_matching_row(page, parte)`
- **Propósito:** Busca en la tabla de productos la fila que contenga EXACTAMENTE el número de parte.
Evita seleccionar por error 'PARTE-1' cuando se busca 'PARTE'.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, str, inner_text, count, split, search, locator, escape, upper, compile`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def actualizar_producto(page, parte, stock, ficha, stop_event)`
- **Línea inicial:** 830 | **Línea final:** 1123
- **Firma completa:** `def actualizar_producto(page, parte, stock, ficha, stop_event)`
- **Propósito:** Actualiza el stock de un producto. Retorna (éxito, mensaje_error).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `replace, dispatch_event, evaluate, click, all, inner_text, is_visible, press, inner_html, upper`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 84)

### `def _get_field(row, keys, default)`
- **Línea inicial:** 1126 | **Línea final:** 1136
- **Firma completa:** `def _get_field(row, keys, default)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, items, isinstance, strip, lower`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge, acuerdo, catalogo, categoria)`
- **Línea inicial:** 1139 | **Línea final:** 1246
- **Firma completa:** `def paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge, acuerdo, catalogo, categoria)`
- **Propósito:** Itera el DataFrame y actualiza cada producto. Retorna cantidad de éxitos.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `clasificar_error, _esta_en_mejorabasica, _get_field, round, paso3_filtros_stock, len, is_set, log_func, lower, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 35)

### `def generar_reporte_excel(output_path, acuerdo, catalogo, categoria)`
- **Línea inicial:** 1259 | **Línea final:** 1391
- **Firma completa:** `def generar_reporte_excel(output_path, acuerdo, catalogo, categoria)`
- **Propósito:** Genera el reporte Excel con 3 hojas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, Alignment, get_column_letter, PieChart, set_categories, makedirs, len, items, sum, cell`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def ejecutar_stock(page, excel_path, usuario, password, acuerdo, catalogo, categoria, pausa, captcha_bridge, log_func)`
- **Línea inicial:** 1398 | **Línea final:** 1450
- **Firma completa:** `def ejecutar_stock(page, excel_path, usuario, password, acuerdo, catalogo, categoria, pausa, captcha_bridge, log_func)`
- **Propósito:** Ejecuta el flujo completo de stock. Retorna path del reporte.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, login_with_ocr, len, generar_reporte_excel, analizar_excel_stock, strftime, dirname, now, paso4_actualizar_stock, paso3_filtros_stock`
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
- **Dependencias / Invocaciones:** `str, replace, items, strip, lower`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

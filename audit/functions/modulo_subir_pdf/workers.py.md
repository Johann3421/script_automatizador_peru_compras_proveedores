# Auditoría de Funciones: `modulo_subir_pdf/workers.py`

- **Lenguaje:** `python`
- **Líneas de código:** 2196
- **Hash SHA256:** `46272a44d4c9`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _make_stock_log(append_fn)`
- **Línea inicial:** 8 | **Línea final:** 15
- **Firma completa:** `def _make_stock_log(append_fn)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_StockLog, append_fn, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def execute_stock(app, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Línea inicial:** 17 | **Línea final:** 107
- **Firma completa:** `def execute_stock(app, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, str, basename, init_browser, len, _append_stock_log, paso2_navegacion_stock, join, dirname, is_set`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def execute_extract(app, usuario, password, headless)`
- **Línea inicial:** 108 | **Línea final:** 237
- **Firma completa:** `def execute_extract(app, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, get_attribute, after, warn, basename, init_browser, len, makedirs, append, join`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 32)

### `def execute_certs_only(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 238 | **Línea final:** 325
- **Firma completa:** `def execute_certs_only(app, usuario, password, headless, pre_selected)`
- **Propósito:** Ejecuta SOLO la corrección de certificaciones ISO 9001/14001 para todas las fichas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `enumerate, after, warn, init_browser, len, ok, agregar_certificaciones_faltantes, sleep, is_set, leer_certificaciones_pagina`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 23)

### `def execute_nro_parte(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 326 | **Línea final:** 383
- **Firma completa:** `def execute_nro_parte(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `next, enumerate, after, warn, init_browser, len, ok, guardar_cambios, sleep, is_set`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def execute_compare(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 384 | **Línea final:** 551
- **Firma completa:** `def execute_compare(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `upper, enumerate, str, after, warn, basename, init_browser, time, len, append`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 33)

### `def execute_discovery(app, usuario, password, headless)`
- **Línea inicial:** 552 | **Línea final:** 708
- **Firma completa:** `def execute_discovery(app, usuario, password, headless)`
- **Propósito:** Ejecuta el discovery de endpoints directamente en la app (mismo browser).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `enumerate, str, after, generar_reporte, get_text, warn, init_browser, len, makedirs, list`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 42)

### `def execute_discovery2(app, usuario, password, headless)`
- **Línea inicial:** 709 | **Línea final:** 808
- **Firma completa:** `def execute_discovery2(app, usuario, password, headless)`
- **Propósito:** Ejecuta discovery_v2_perucompras.py: 8 técnicas de scraping profundo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, init_browser, len, makedirs, list, append, join, enumerar_acciones, crawl_recursivo, sum`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 25)

### `def execute_test(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 809 | **Línea final:** 990
- **Firma completa:** `def execute_test(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `corregir_caracteristica, next, upper, enumerate, put, str, after, warn, basename, init_browser`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 46)

### `def execute(app, usuario, password, headless, rows, pausa, pre_selected)`
- **Línea inicial:** 992 | **Línea final:** 1055
- **Firma completa:** `def execute(app, usuario, password, headless, rows, pausa, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put, warn, basename, init_browser, len, sum, ok, sleep, is_set, hasattr`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 21)

### `def read_select_options_precios(page, selector)`
- **Línea inicial:** 1062 | **Línea final:** 1075
- **Firma completa:** `def read_select_options_precios(page, selector)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def wait_for_options_precios(page, selector, timeout)`
- **Línea inicial:** 1077 | **Línea final:** 1089
- **Firma completa:** `def wait_for_options_precios(page, selector, timeout)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait_for_function`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def execute_extraer_menu_precios(app, usuario, password, headless, log_func)`
- **Línea inicial:** 1091 | **Línea final:** 1183
- **Firma completa:** `def execute_extraer_menu_precios(app, usuario, password, headless, log_func)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log_func, type, enumerate, after, init_browser, list, read_select_options_precios, append, select_option, fromkeys`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def _calcular_precio_dolar(precio_max, ganancia, tc)`
- **Línea inicial:** 1190 | **Línea final:** 1192
- **Firma completa:** `def _calcular_precio_dolar(precio_max, ganancia, tc)`
- **Propósito:** (precio_max * 1.10) / 3.4 → precio en USD redondeado a 2 decimales
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `round`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _buscar_match_local(producto_pc, precios_data)`
- **Línea inicial:** 1195 | **Línea final:** 1215
- **Firma completa:** `def _buscar_match_local(producto_pc, precios_data)`
- **Propósito:** Busca en precios_data el registro que coincida con el producto de Perú Compras.
Estrategia 1: comparar C_Descripcion (PC) contra descripcin_fichaproducto (Local).
Estrategia 2: buscar nro_parte local dentro de la C_Descripcion de Perú Compras.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, upper, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def execute_test_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)`
- **Línea inicial:** 1218 | **Línea final:** 1434
- **Firma completa:** `def execute_test_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)`
- **Propósito:** TEST: navega a t_ProductoOfertadoAmp, aplica filtros, descarga TODOS los
productos mediante peticiones POST directas usando el payload interceptado
y las cookies de sesión del navegador (mucho más rápido), hace matching
y muestra qué precio se insertaría. NO escribe nada todavía.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log_func, type, str, after, init_browser, len, _buscar_match_pc, click, urlencode, re_enable`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 27)

### `def _buscar_match_pc(rec_local, all_products)`
- **Línea inicial:** 1441 | **Línea final:** 1455
- **Firma completa:** `def _buscar_match_pc(rec_local, all_products)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, upper, strip, str`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def _interpret_response_precios(text)`
- **Línea inicial:** 1457 | **Línea final:** 1465
- **Firma completa:** `def _interpret_response_precios(text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, any`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _enviar_oferta_precios(page, log_func, app)`
- **Línea inicial:** 1467 | **Línea final:** 1484
- **Firma completa:** `def _enviar_oferta_precios(page, log_func, app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `post, log_func, text`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def execute_iniciar_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val, stop_event)`
- **Línea inicial:** 1486 | **Línea final:** 1878
- **Firma completa:** `def execute_iniciar_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, log_func, enumerate, str, after, init_browser, save, len, click, urlencode`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 58)

### `def execute_auditor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Línea inicial:** 1895 | **Línea final:** 2059
- **Firma completa:** `def execute_auditor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Propósito:** Auditor del Portal Stock.

Parámetros
----------
app          : instancia de la app (para leer _stock_excel_df, _stock_stop_event)
usuario      : str — credenciales de la pestaña stock
password     : str
acuerdo      : str — texto del dropdown acuerdo (para resumen)
catalogo     : str — texto del dropdown catalogo (para resumen)
categoria    : str — texto del dropdown categoria (para resumen)
on_done      : callable(filas, resumen) — se llama al finalizar
on_log       : callable(str) — se llama para cada mensaje de log
headless     : bool — True para oculto, False para visible en pantalla
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, str, _get_id_categoria, login_automatico, init_browser, len, saltar_verificacion, append, _get_id_catalogo, _get_id_acuerdo`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def _get_id_acuerdo(combos, acuerdo_text)`
- **Línea inicial:** 2062 | **Línea final:** 2066
- **Firma completa:** `def _get_id_acuerdo(combos, acuerdo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _get_id_catalogo(combos, acuerdo_text, catalogo_text)`
- **Línea inicial:** 2068 | **Línea final:** 2074
- **Firma completa:** `def _get_id_catalogo(combos, acuerdo_text, catalogo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, _get_id_acuerdo`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _get_id_categoria(combos, acuerdo_text, catalogo_text, categoria_text)`
- **Línea inicial:** 2076 | **Línea final:** 2083
- **Firma completa:** `def _get_id_categoria(combos, acuerdo_text, catalogo_text, categoria_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, _get_id_acuerdo`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _build_portal_index(registros, on_log)`
- **Línea inicial:** 2086 | **Línea final:** 2143
- **Firma completa:** `def _build_portal_index(registros, on_log)`
- **Propósito:** Construye un índice {ficha_id: {stock_portal, estado_portal}}
a partir de los registros del portal.

El JSON puede ser:
  - Lista de dicts con claves explícitas (e.g. ID_ProductoOfertado, N_Existencias, C_Estado)
  - Lista de listas posicionales (DataTables style)
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, str, get, search, split, isinstance, startswith, len, upper, group`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def _detect_key(d, candidates)`
- **Línea inicial:** 2146 | **Línea final:** 2152
- **Firma completa:** `def _detect_key(d, candidates)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def execute_json_extractor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Línea inicial:** 2155 | **Línea final:** 2196
- **Firma completa:** `def execute_json_extractor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Propósito:** Ejecuta la extracción masiva E2E del dataset JSON del portal utilizando perucompras_core.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, join, getattr, _get_id_catalogo, _get_id_categoria, on_log, extraer_json_catalogo, on_done, len, dirname`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def re_enable()`
- **Línea inicial:** 1233 | **Línea final:** 1235
- **Firma completa:** `def re_enable()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def re_enable()`
- **Línea inicial:** 1498 | **Línea final:** 1502
- **Firma completa:** `def re_enable()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, hasattr, configure`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def info(self, msg)`
- **Línea inicial:** 10 | **Línea final:** 10
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 11 | **Línea final:** 11
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 12 | **Línea final:** 12
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 13 | **Línea final:** 13
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 14 | **Línea final:** 14
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def stock_log(msg)`
- **Línea inicial:** 58 | **Línea final:** 68
- **Firma completa:** `def stock_log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, str, set, max, _append_stock_log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _read_options(selector)`
- **Línea inicial:** 134 | **Línea final:** 142
- **Firma completa:** `def _read_options(selector)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append, strip, get_attribute, locator, inner_text, all`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _fetch(url)`
- **Línea inicial:** 598 | **Línea final:** 610
- **Firma completa:** `def _fetch(url)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def update_ui()`
- **Línea inicial:** 1158 | **Línea final:** 1173
- **Firma completa:** `def update_ui()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `configure, set, _on_precio_acuerdo_changed, fromkeys, list`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def handle_request(req)`
- **Línea inicial:** 1323 | **Línea final:** 1326
- **Firma completa:** `def handle_request(req)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def handle_response(response)`
- **Línea inicial:** 1328 | **Línea final:** 1334
- **Firma completa:** `def handle_response(response)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `json, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def handle_request(req)`
- **Línea inicial:** 1597 | **Línea final:** 1600
- **Firma completa:** `def handle_request(req)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def handle_response(response)`
- **Línea inicial:** 1602 | **Línea final:** 1608
- **Firma completa:** `def handle_response(response)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `json, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def info(self, m)`
- **Línea inicial:** 1109 | **Línea final:** 1109
- **Firma completa:** `def info(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, m)`
- **Línea inicial:** 1110 | **Línea final:** 1110
- **Firma completa:** `def ok(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, m)`
- **Línea inicial:** 1111 | **Línea final:** 1111
- **Firma completa:** `def warn(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, m)`
- **Línea inicial:** 1112 | **Línea final:** 1112
- **Firma completa:** `def error(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def info(self, m)`
- **Línea inicial:** 1246 | **Línea final:** 1246
- **Firma completa:** `def info(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, m)`
- **Línea inicial:** 1247 | **Línea final:** 1247
- **Firma completa:** `def ok(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, m)`
- **Línea inicial:** 1248 | **Línea final:** 1248
- **Firma completa:** `def warn(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, m)`
- **Línea inicial:** 1249 | **Línea final:** 1249
- **Firma completa:** `def error(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def info(self, msg)`
- **Línea inicial:** 1514 | **Línea final:** 1514
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log_func, strip, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 1515 | **Línea final:** 1515
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log_func, strip, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 1516 | **Línea final:** 1516
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log_func, strip, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 1517 | **Línea final:** 1517
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log_func, strip, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 1518 | **Línea final:** 1518
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log_func, strip, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def write(self, txt)`
- **Línea inicial:** 1519 | **Línea final:** 1521
- **Firma completa:** `def write(self, txt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `log_func, strip, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def flush(self)`
- **Línea inicial:** 1522 | **Línea final:** 1522
- **Firma completa:** `def flush(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

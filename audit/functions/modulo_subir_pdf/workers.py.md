# Auditoría de Funciones: `modulo_subir_pdf/workers.py`

- **Lenguaje:** `python`
- **Líneas de código:** 2209
- **Hash SHA256:** `2688c5aa7d32`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _make_stock_log(append_fn)`
- **Línea inicial:** 21 | **Línea final:** 28
- **Firma completa:** `def _make_stock_log(append_fn)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn, _StockLog, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def execute_stock(app, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Línea inicial:** 30 | **Línea final:** 120
- **Firma completa:** `def execute_stock(app, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, basename, len, is_set, close_browser, join, paso4_actualizar_stock, format_exc, set_viewport_size, do_login`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def execute_extract(app, usuario, password, headless)`
- **Línea inicial:** 121 | **Línea final:** 250
- **Firma completa:** `def execute_extract(app, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `finditer, evaluate, error, append, after, goto, basename, replace, len, dump`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 32)

### `def execute_certs_only(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 251 | **Línea final:** 338
- **Firma completa:** `def execute_certs_only(app, usuario, password, headless, pre_selected)`
- **Propósito:** Ejecuta SOLO la corrección de certificaciones ISO 9001/14001 para todas las fichas.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `enumerate, error, upper, after, goto, len, is_set, LogWriter, close_browser, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 23)

### `def execute_nro_parte(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 339 | **Línea final:** 396
- **Firma completa:** `def execute_nro_parte(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `leer_caracteristicas_pagina, enumerate, error, upper, after, goto, agregar_caracteristica_texto, len, is_set, LogWriter`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def execute_compare(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 397 | **Línea final:** 564
- **Firma completa:** `def execute_compare(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `leer_caracteristicas_pagina, comparar_caracteristicas, finditer, enumerate, hasattr, evaluate, str, error, append, upper`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 33)

### `def execute_discovery(app, usuario, password, headless)`
- **Línea inicial:** 565 | **Línea final:** 721
- **Firma completa:** `def execute_discovery(app, usuario, password, headless)`
- **Propósito:** Ejecuta el discovery de endpoints directamente en la app (mismo browser).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `enumerate, evaluate, str, error, clasificar_respuesta, append, after, len, dump, extract_urls_from_html`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 42)

### `def execute_discovery2(app, usuario, password, headless)`
- **Línea inicial:** 722 | **Línea final:** 821
- **Firma completa:** `def execute_discovery2(app, usuario, password, headless)`
- **Propósito:** Ejecuta discovery_v2_perucompras.py: 8 técnicas de scraping profundo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `error, append, after, generar_reporte_v2, values, len, dump, Path, is_set, LogWriter`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 25)

### `def execute_test(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 822 | **Línea final:** 1003
- **Firma completa:** `def execute_test(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `leer_caracteristicas_pagina, comparar_caracteristicas, enumerate, hasattr, str, error, append, upper, after, goto`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 46)

### `def execute(app, usuario, password, headless, rows, pausa, pre_selected)`
- **Línea inicial:** 1005 | **Línea final:** 1068
- **Firma completa:** `def execute(app, usuario, password, headless, rows, pausa, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `hasattr, error, goto, basename, len, is_set, LogWriter, close_browser, sleep, ok`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 21)

### `def read_select_options_precios(page, selector)`
- **Línea inicial:** 1075 | **Línea final:** 1088
- **Firma completa:** `def read_select_options_precios(page, selector)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def wait_for_options_precios(page, selector, timeout)`
- **Línea inicial:** 1090 | **Línea final:** 1102
- **Firma completa:** `def wait_for_options_precios(page, selector, timeout)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait_for_function`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def execute_extraer_menu_precios(app, usuario, password, headless, log_func)`
- **Línea inicial:** 1104 | **Línea final:** 1196
- **Firma completa:** `def execute_extraer_menu_precios(app, usuario, password, headless, log_func)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `enumerate, append, DummyLog, after, goto, dump, log_func, select_option, close_browser, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def _calcular_precio_dolar(precio_max, ganancia, tc)`
- **Línea inicial:** 1203 | **Línea final:** 1205
- **Firma completa:** `def _calcular_precio_dolar(precio_max, ganancia, tc)`
- **Propósito:** (precio_max * 1.10) / 3.4 → precio en USD redondeado a 2 decimales
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `round`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _buscar_match_local(producto_pc, precios_data)`
- **Línea inicial:** 1208 | **Línea final:** 1228
- **Firma completa:** `def _buscar_match_local(producto_pc, precios_data)`
- **Propósito:** Busca en precios_data el registro que coincida con el producto de Perú Compras.
Estrategia 1: comparar C_Descripcion (PC) contra descripcin_fichaproducto (Local).
Estrategia 2: buscar nro_parte local dentro de la C_Descripcion de Perú Compras.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, upper, get`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def execute_test_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)`
- **Línea inicial:** 1231 | **Línea final:** 1447
- **Firma completa:** `def execute_test_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)`
- **Propósito:** TEST: navega a t_ProductoOfertadoAmp, aplica filtros, descarga TODOS los
productos mediante peticiones POST directas usando el payload interceptado
y las cookies de sesión del navegador (mucho más rápido), hace matching
y muestra qué precio se insertaría. NO escribe nada todavía.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `evaluate, on, str, wait_for_selector, DummyLog, after, goto, len, log_func, close_browser`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 27)

### `def _buscar_match_pc(rec_local, all_products)`
- **Línea inicial:** 1454 | **Línea final:** 1468
- **Firma completa:** `def _buscar_match_pc(rec_local, all_products)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, upper, get, str`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def _interpret_response_precios(text)`
- **Línea inicial:** 1470 | **Línea final:** 1478
- **Firma completa:** `def _interpret_response_precios(text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, any`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _enviar_oferta_precios(page, log_func, app)`
- **Línea inicial:** 1480 | **Línea final:** 1497
- **Firma completa:** `def _enviar_oferta_precios(page, log_func, app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `text, post, log_func`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def execute_iniciar_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val, stop_event)`
- **Línea inicial:** 1499 | **Línea final:** 1891
- **Firma completa:** `def execute_iniciar_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `enumerate, hasattr, evaluate, Alignment, on, range, str, append, wait_for_selector, abspath`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 58)

### `def execute_auditor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Línea inicial:** 1908 | **Línea final:** 2072
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
- **Dependencias / Invocaciones:** `str, _get_id_categoria, upper, append, len, is_set, close_browser, consultar_json_productos, strip, format_exc`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def _get_id_acuerdo(combos, acuerdo_text)`
- **Línea inicial:** 2075 | **Línea final:** 2079
- **Firma completa:** `def _get_id_acuerdo(combos, acuerdo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _get_id_catalogo(combos, acuerdo_text, catalogo_text)`
- **Línea inicial:** 2081 | **Línea final:** 2087
- **Firma completa:** `def _get_id_catalogo(combos, acuerdo_text, catalogo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, _get_id_acuerdo`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _get_id_categoria(combos, acuerdo_text, catalogo_text, categoria_text)`
- **Línea inicial:** 2089 | **Línea final:** 2096
- **Firma completa:** `def _get_id_categoria(combos, acuerdo_text, catalogo_text, categoria_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, _get_id_acuerdo`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _build_portal_index(registros, on_log)`
- **Línea inicial:** 2099 | **Línea final:** 2156
- **Firma completa:** `def _build_portal_index(registros, on_log)`
- **Propósito:** Construye un índice {ficha_id: {stock_portal, estado_portal}}
a partir de los registros del portal.

El JSON puede ser:
  - Lista de dicts con claves explícitas (e.g. ID_ProductoOfertado, N_Existencias, C_Estado)
  - Lista de listas posicionales (DataTables style)
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `split, group, _detect_key, str, upper, startswith, strip, search, get, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def _detect_key(d, candidates)`
- **Línea inicial:** 2159 | **Línea final:** 2165
- **Firma completa:** `def _detect_key(d, candidates)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def execute_json_extractor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Línea inicial:** 2168 | **Línea final:** 2209
- **Firma completa:** `def execute_json_extractor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Propósito:** Ejecuta la extracción masiva E2E del dataset JSON del portal utilizando perucompras_core.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `extraer_json_catalogo, join, _get_id_categoria, on_done, _get_id_acuerdo, strftime, getattr, _get_id_catalogo, dirname, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def re_enable()`
- **Línea inicial:** 1246 | **Línea final:** 1248
- **Firma completa:** `def re_enable()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def re_enable()`
- **Línea inicial:** 1511 | **Línea final:** 1515
- **Firma completa:** `def re_enable()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, hasattr, configure`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def info(self, msg)`
- **Línea inicial:** 23 | **Línea final:** 23
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 24 | **Línea final:** 24
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 25 | **Línea final:** 25
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 26 | **Línea final:** 26
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 27 | **Línea final:** 27
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def stock_log(msg)`
- **Línea inicial:** 71 | **Línea final:** 81
- **Firma completa:** `def stock_log(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, str, _append_stock_log, max, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _read_options(selector)`
- **Línea inicial:** 147 | **Línea final:** 155
- **Firma completa:** `def _read_options(selector)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get_attribute, inner_text, locator, append, strip, all`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _fetch(url)`
- **Línea inicial:** 611 | **Línea final:** 623
- **Firma completa:** `def _fetch(url)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def update_ui()`
- **Línea inicial:** 1171 | **Línea final:** 1186
- **Firma completa:** `def update_ui()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set, fromkeys, _on_precio_acuerdo_changed, list, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def handle_request(req)`
- **Línea inicial:** 1336 | **Línea final:** 1339
- **Firma completa:** `def handle_request(req)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def handle_response(response)`
- **Línea inicial:** 1341 | **Línea final:** 1347
- **Firma completa:** `def handle_response(response)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `json, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def handle_request(req)`
- **Línea inicial:** 1610 | **Línea final:** 1613
- **Firma completa:** `def handle_request(req)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def handle_response(response)`
- **Línea inicial:** 1615 | **Línea final:** 1621
- **Firma completa:** `def handle_response(response)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `json, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def info(self, m)`
- **Línea inicial:** 1122 | **Línea final:** 1122
- **Firma completa:** `def info(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, m)`
- **Línea inicial:** 1123 | **Línea final:** 1123
- **Firma completa:** `def ok(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, m)`
- **Línea inicial:** 1124 | **Línea final:** 1124
- **Firma completa:** `def warn(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, m)`
- **Línea inicial:** 1125 | **Línea final:** 1125
- **Firma completa:** `def error(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def info(self, m)`
- **Línea inicial:** 1259 | **Línea final:** 1259
- **Firma completa:** `def info(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, m)`
- **Línea inicial:** 1260 | **Línea final:** 1260
- **Firma completa:** `def ok(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, m)`
- **Línea inicial:** 1261 | **Línea final:** 1261
- **Firma completa:** `def warn(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, m)`
- **Línea inicial:** 1262 | **Línea final:** 1262
- **Firma completa:** `def error(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def info(self, msg)`
- **Línea inicial:** 1527 | **Línea final:** 1527
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, log_func, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 1528 | **Línea final:** 1528
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, log_func, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 1529 | **Línea final:** 1529
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, log_func, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 1530 | **Línea final:** 1530
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, log_func, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 1531 | **Línea final:** 1531
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, log_func, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def write(self, txt)`
- **Línea inicial:** 1532 | **Línea final:** 1534
- **Firma completa:** `def write(self, txt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, log_func, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def flush(self)`
- **Línea inicial:** 1535 | **Línea final:** 1535
- **Firma completa:** `def flush(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

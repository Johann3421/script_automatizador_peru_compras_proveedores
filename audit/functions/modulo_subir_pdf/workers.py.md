# Auditoría de Funciones: `modulo_subir_pdf/workers.py`

- **Lenguaje:** `python`
- **Líneas de código:** 2273
- **Hash SHA256:** `54ae38939881`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _make_stock_log(append_fn)`
- **Línea inicial:** 21 | **Línea final:** 28
- **Firma completa:** `def _make_stock_log(append_fn)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_StockLog, str, append_fn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def execute_stock(app, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Línea inicial:** 30 | **Línea final:** 120
- **Firma completa:** `def execute_stock(app, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_append_stock_log, is_set, get, bool, str, _make_stock_log, len, format_exc, generar_reporte_excel, paso4_actualizar_stock`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 18)

### `def execute_extract(app, usuario, password, headless)`
- **Línea inicial:** 121 | **Línea final:** 250
- **Firma completa:** `def execute_extract(app, usuario, password, headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `after, strip, goto, append, select_option, is_set, inner_text, ok, len, format_exc`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 32)

### `def execute_certs_only(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 251 | **Línea final:** 338
- **Firma completa:** `def execute_certs_only(app, usuario, password, headless, pre_selected)`
- **Propósito:** Ejecuta SOLO la corrección de certificaciones ISO 9001/14001 para todas las fichas.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `after, goto, is_set, get, ok, len, format_exc, info, leer_certificaciones_pagina, upper`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 23)

### `def execute_nro_parte(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 339 | **Línea final:** 396
- **Firma completa:** `def execute_nro_parte(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `eliminar_caracteristica, after, strip, goto, is_set, get, agregar_caracteristica_texto, ok, len, format_exc`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def execute_compare(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 397 | **Línea final:** 564
- **Firma completa:** `def execute_compare(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `after, strip, goto, append, comparar_caracteristicas, is_set, get, ok, str, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 33)

### `def execute_discovery(app, usuario, password, headless)`
- **Línea inicial:** 565 | **Línea final:** 721
- **Firma completa:** `def execute_discovery(app, usuario, password, headless)`
- **Propósito:** Ejecuta el discovery de endpoints directamente en la app (mismo browser).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, append, analizar_js, any, Path, is_set, get, body, ok, str`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 42)

### `def execute_discovery2(app, usuario, password, headless)`
- **Línea inicial:** 722 | **Línea final:** 821
- **Firma completa:** `def execute_discovery2(app, usuario, password, headless)`
- **Propósito:** Ejecuta discovery_v2_perucompras.py: 8 técnicas de scraping profundo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, append, analizar_js_profundo, Path, is_set, get, ok, list, format_exc, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 25)

### `def execute_test(app, usuario, password, headless, pre_selected)`
- **Línea inicial:** 822 | **Línea final:** 1003
- **Firma completa:** `def execute_test(app, usuario, password, headless, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `eliminar_caracteristica, after, append, goto, strip, comparar_caracteristicas, is_set, get, ensure_logged_in_and_ready, agregar_caracteristica_texto`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 46)

### `def execute(app, usuario, password, headless, rows, pausa, pre_selected)`
- **Línea inicial:** 1005 | **Línea final:** 1068
- **Firma completa:** `def execute(app, usuario, password, headless, rows, pausa, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `goto, is_set, get, ok, len, format_exc, info, warn, sleep, put`
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
- **Efectos Secundarios:** I/O de archivos o consola, Navegación / Red HTTP
- **Dependencias / Invocaciones:** `after, DummyLog, append, goto, wait_for_options_precios, select_option, list, log_func, enumerate, open`
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
- **Dependencias / Invocaciones:** `get, strip, upper`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def execute_test_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)`
- **Línea inicial:** 1231 | **Línea final:** 1447
- **Firma completa:** `def execute_test_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)`
- **Propósito:** TEST: navega a t_ProductoOfertadoAmp, aplica filtros, descarga TODOS los
productos mediante peticiones POST directas usando el payload interceptado
y las cookies de sesión del navegador (mucho más rápido), hace matching
y muestra qué precio se insertaría. NO escribe nada todavía.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `after, DummyLog, goto, wait_for_options_precios, wait_for_selector, parse_qs, get, str, len, remove_listener`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 27)

### `def _clean_match_str(s)`
- **Línea inicial:** 1454 | **Línea final:** 1455
- **Firma completa:** `def _clean_match_str(s)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `upper, strip, sub`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _buscar_match_pc(rec_local, all_products)`
- **Línea inicial:** 1457 | **Línea final:** 1475
- **Firma completa:** `def _buscar_match_pc(rec_local, all_products)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _clean_match_str, get, str, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def _interpret_response_precios(text)`
- **Línea inicial:** 1477 | **Línea final:** 1485
- **Firma completa:** `def _interpret_response_precios(text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, any`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _enviar_oferta_precios(page, log_func, app)`
- **Línea inicial:** 1487 | **Línea final:** 1504
- **Firma completa:** `def _enviar_oferta_precios(page, log_func, app)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `text, post, log_func`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def execute_iniciar_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val, stop_event)`
- **Línea inicial:** 1506 | **Línea final:** 1955
- **Firma completa:** `def execute_iniciar_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `after, Alignment, append, goto, wait_for_options_precios, wait_for_selector, strip, parse_qs, range, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 66)

### `def execute_auditor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Línea inicial:** 1972 | **Línea final:** 2136
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
- **Dependencias / Invocaciones:** `_get_id_acuerdo, strip, consultar_json_productos, append, login_automatico, _get_id_catalogo, completar_menu_dinamico, is_set, get, str`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def _get_id_acuerdo(combos, acuerdo_text)`
- **Línea inicial:** 2139 | **Línea final:** 2143
- **Firma completa:** `def _get_id_acuerdo(combos, acuerdo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _get_id_catalogo(combos, acuerdo_text, catalogo_text)`
- **Línea inicial:** 2145 | **Línea final:** 2151
- **Firma completa:** `def _get_id_catalogo(combos, acuerdo_text, catalogo_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_get_id_acuerdo, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _get_id_categoria(combos, acuerdo_text, catalogo_text, categoria_text)`
- **Línea inicial:** 2153 | **Línea final:** 2160
- **Firma completa:** `def _get_id_categoria(combos, acuerdo_text, catalogo_text, categoria_text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_get_id_acuerdo, get`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _build_portal_index(registros, on_log)`
- **Línea inicial:** 2163 | **Línea final:** 2220
- **Firma completa:** `def _build_portal_index(registros, on_log)`
- **Propósito:** Construye un índice {ficha_id: {stock_portal, estado_portal}}
a partir de los registros del portal.

El JSON puede ser:
  - Lista de dicts con claves explícitas (e.g. ID_ProductoOfertado, N_Existencias, C_Estado)
  - Lista de listas posicionales (DataTables style)
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `search, isinstance, strip, startswith, split, upper, get, _detect_key, group, str`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def _detect_key(d, candidates)`
- **Línea inicial:** 2223 | **Línea final:** 2229
- **Firma completa:** `def _detect_key(d, candidates)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def execute_json_extractor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Línea inicial:** 2232 | **Línea final:** 2273
- **Firma completa:** `def execute_json_extractor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Propósito:** Ejecuta la extracción masiva E2E del dataset JSON del portal utilizando perucompras_core.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, _get_id_acuerdo, join, makedirs, abspath, _get_id_categoria, _get_id_catalogo, extraer_json_catalogo, getattr, on_log`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def re_enable()`
- **Línea inicial:** 1246 | **Línea final:** 1248
- **Firma completa:** `def re_enable()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def re_enable()`
- **Línea inicial:** 1518 | **Línea final:** 1522
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
- **Dependencias / Invocaciones:** `str, append_fn`
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
- **Dependencias / Invocaciones:** `configure, _append_stock_log, max, set, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _read_options(selector)`
- **Línea inicial:** 147 | **Línea final:** 155
- **Firma completa:** `def _read_options(selector)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `all, append, strip, get_attribute, locator, inner_text`
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
- **Dependencias / Invocaciones:** `configure, set, _on_precio_acuerdo_changed, list, fromkeys`
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
- **Dependencias / Invocaciones:** `get, json`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def handle_request(req)`
- **Línea inicial:** 1617 | **Línea final:** 1620
- **Firma completa:** `def handle_request(req)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def handle_response(response)`
- **Línea inicial:** 1622 | **Línea final:** 1628
- **Firma completa:** `def handle_response(response)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, json`
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
- **Línea inicial:** 1534 | **Línea final:** 1534
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, strip, log_func`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 1535 | **Línea final:** 1535
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, strip, log_func`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 1536 | **Línea final:** 1536
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, strip, log_func`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 1537 | **Línea final:** 1537
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, strip, log_func`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 1538 | **Línea final:** 1538
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, strip, log_func`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def write(self, txt)`
- **Línea inicial:** 1539 | **Línea final:** 1541
- **Firma completa:** `def write(self, txt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, strip, log_func`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def flush(self)`
- **Línea inicial:** 1542 | **Línea final:** 1542
- **Firma completa:** `def flush(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

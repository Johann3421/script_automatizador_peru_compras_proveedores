# Documentación Técnica: `modulo_subir_pdf/workers.py`

- **Ruta relativa:** `modulo_subir_pdf/workers.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 2190
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _make_stock_log(append_fn)` (Línea 8)
- **Propósito:** Sin docstring.
- **Firma:** `def _make_stock_log(append_fn)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_stock(app, usuario, password, acuerdo, catalogo, categoria, pausa)` (Línea 17)
- **Propósito:** Sin docstring.
- **Firma:** `def execute_stock(app, usuario, password, acuerdo, catalogo, categoria, pausa)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_extract(app, usuario, password, headless)` (Línea 108)
- **Propósito:** Sin docstring.
- **Firma:** `def execute_extract(app, usuario, password, headless)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_certs_only(app, usuario, password, headless, pre_selected)` (Línea 238)
- **Propósito:** Ejecuta SOLO la corrección de certificaciones ISO 9001/14001 para todas las fichas.
- **Firma:** `def execute_certs_only(app, usuario, password, headless, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_nro_parte(app, usuario, password, headless, pre_selected)` (Línea 326)
- **Propósito:** Sin docstring.
- **Firma:** `def execute_nro_parte(app, usuario, password, headless, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_compare(app, usuario, password, headless, pre_selected)` (Línea 384)
- **Propósito:** Sin docstring.
- **Firma:** `def execute_compare(app, usuario, password, headless, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_discovery(app, usuario, password, headless)` (Línea 552)
- **Propósito:** Ejecuta el discovery de endpoints directamente en la app (mismo browser).
- **Firma:** `def execute_discovery(app, usuario, password, headless)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_discovery2(app, usuario, password, headless)` (Línea 709)
- **Propósito:** Ejecuta discovery_v2_perucompras.py: 8 técnicas de scraping profundo.
- **Firma:** `def execute_discovery2(app, usuario, password, headless)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_test(app, usuario, password, headless, pre_selected)` (Línea 809)
- **Propósito:** Sin docstring.
- **Firma:** `def execute_test(app, usuario, password, headless, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute(app, usuario, password, headless, rows, pausa, pre_selected)` (Línea 992)
- **Propósito:** Sin docstring.
- **Firma:** `def execute(app, usuario, password, headless, rows, pausa, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def read_select_options_precios(page, selector)` (Línea 1062)
- **Propósito:** Sin docstring.
- **Firma:** `def read_select_options_precios(page, selector)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def wait_for_options_precios(page, selector, timeout)` (Línea 1077)
- **Propósito:** Sin docstring.
- **Firma:** `def wait_for_options_precios(page, selector, timeout)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_extraer_menu_precios(app, usuario, password, headless, log_func)` (Línea 1091)
- **Propósito:** Sin docstring.
- **Firma:** `def execute_extraer_menu_precios(app, usuario, password, headless, log_func)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _calcular_precio_dolar(precio_max, ganancia, tc)` (Línea 1190)
- **Propósito:** (precio_max * 1.10) / 3.4 → precio en USD redondeado a 2 decimales
- **Firma:** `def _calcular_precio_dolar(precio_max, ganancia, tc)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _buscar_match_local(producto_pc, precios_data)` (Línea 1195)
- **Propósito:** Busca en precios_data el registro que coincida con el producto de Perú Compras.
Estrategia 1: comparar C_Descripcion (PC) contra descripcin_fichaproducto (Local).
Estrategia 2: buscar nro_parte local dentro de la C_Descripcion de Perú Compras.
- **Firma:** `def _buscar_match_local(producto_pc, precios_data)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_test_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)` (Línea 1218)
- **Propósito:** TEST: navega a t_ProductoOfertadoAmp, aplica filtros, descarga TODOS los
productos mediante peticiones POST directas usando el payload interceptado
y las cookies de sesión del navegador (mucho más rápido), hace matching
y muestra qué precio se insertaría. NO escribe nada todavía.
- **Firma:** `def execute_test_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _buscar_match_pc(rec_local, all_products)` (Línea 1461)
- **Propósito:** Sin docstring.
- **Firma:** `def _buscar_match_pc(rec_local, all_products)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _interpret_response_precios(text)` (Línea 1473)
- **Propósito:** Sin docstring.
- **Firma:** `def _interpret_response_precios(text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _enviar_oferta_precios(page, log_func, app)` (Línea 1483)
- **Propósito:** Sin docstring.
- **Firma:** `def _enviar_oferta_precios(page, log_func, app)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_iniciar_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)` (Línea 1502)
- **Propósito:** Sin docstring.
- **Firma:** `def execute_iniciar_precios(app, usuario, password, headless, log_func, precios_data, acuerdo_val, catalogo_val, categoria_val)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def execute_auditor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)` (Línea 1893)
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
- **Firma:** `def execute_auditor(app, usuario, password, acuerdo, catalogo, categoria, on_done, on_log, headless)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_id_acuerdo(combos, acuerdo_text)` (Línea 2096)
- **Propósito:** Sin docstring.
- **Firma:** `def _get_id_acuerdo(combos, acuerdo_text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_id_catalogo(combos, acuerdo_text, catalogo_text)` (Línea 2102)
- **Propósito:** Sin docstring.
- **Firma:** `def _get_id_catalogo(combos, acuerdo_text, catalogo_text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_id_categoria(combos, acuerdo_text, catalogo_text, categoria_text)` (Línea 2110)
- **Propósito:** Sin docstring.
- **Firma:** `def _get_id_categoria(combos, acuerdo_text, catalogo_text, categoria_text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _build_portal_index(registros, on_log)` (Línea 2120)
- **Propósito:** Construye un índice {ficha_id: {stock_portal, estado_portal}}
a partir de los registros del portal.

El JSON puede ser:
  - Lista de dicts con claves explícitas (e.g. ID_ProductoOfertado, N_Existencias, C_Estado)
  - Lista de listas posicionales (DataTables style)
- **Firma:** `def _build_portal_index(registros, on_log)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _detect_key(d, candidates)` (Línea 2180)
- **Propósito:** Sin docstring.
- **Firma:** `def _detect_key(d, candidates)`
- **Retorno / Efectos:** Consulta código fuente.

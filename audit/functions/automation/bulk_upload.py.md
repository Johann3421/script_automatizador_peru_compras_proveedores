# Auditoría de Funciones: `automation/bulk_upload.py`

- **Lenguaje:** `python`
- **Líneas de código:** 411
- **Hash SHA256:** `c9ec895d7cbf`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _cookies_from_page(page)`
- **Línea inicial:** 33 | **Línea final:** 35
- **Firma completa:** `def _cookies_from_page(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `cookies`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _build_datatable_payload(N_Acuerdo, N_Catalogo, N_Categoria, start, length, search)`
- **Línea inicial:** 38 | **Línea final:** 57
- **Firma completa:** `def _build_datatable_payload(N_Acuerdo, N_Catalogo, N_Categoria, start, length, search)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, items, enumerate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def buscar_producto_por_parte(client, N_Acuerdo, N_Catalogo, N_Categoria, parte)`
- **Línea inicial:** 60 | **Línea final:** 70
- **Firma completa:** `def buscar_producto_por_parte(client, N_Acuerdo, N_Catalogo, N_Categoria, parte)`
- **Propósito:** Busca productos filtrando por parte en C_Descripcion (como el buscador del sitio).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, _build_datatable_payload, raise_for_status, post, json`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def _match_parte_in_results(parte, results)`
- **Línea inicial:** 73 | **Línea final:** 90
- **Firma completa:** `def _match_parte_in_results(parte, results)`
- **Propósito:** Busca el mejor match de un part number entre los resultados de busqueda.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, _normalize, len, sub`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def _search_and_match_one(args)`
- **Línea inicial:** 93 | **Línea final:** 140
- **Firma completa:** `def _search_and_match_one(args)`
- **Propósito:** Busca un part number y matchea. args = (row, parte_col, precio_col,
N_Acuerdo, N_Catalogo, N_Categoria, cookies_dict, log)
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, _match_parte_in_results, buscar_producto_por_parte, replace, float, get, str, strip, len, Client`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

### `def _normalize(text)`
- **Línea inicial:** 143 | **Línea final:** 144
- **Firma completa:** `def _normalize(text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sub, upper, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def fetch_catalogo_completo(client, N_Acuerdo, N_Catalogo, N_Categoria, log)`
- **Línea inicial:** 147 | **Línea final:** 172
- **Firma completa:** `def fetch_catalogo_completo(client, N_Acuerdo, N_Catalogo, N_Categoria, log)`
- **Propósito:** Descarga TODOS los productos del catalogo paginando de 500 en 500.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, get, sleep, _build_datatable_payload, raise_for_status, post, json, extend, len, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def _build_index(catalogo_rows)`
- **Línea inicial:** 176 | **Línea final:** 185
- **Firma completa:** `def _build_index(catalogo_rows)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, str, _normalize, strip`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _match_parte(parte, idx)`
- **Línea inicial:** 188 | **Línea final:** 202
- **Firma completa:** `def _match_parte(parte, idx)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_normalize, items, sub`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def match_excel_rows(excel_rows, parte_col, precio_col, catalogo_rows, log)`
- **Línea inicial:** 205 | **Línea final:** 281
- **Firma completa:** `def match_excel_rows(excel_rows, parte_col, precio_col, catalogo_rows, log)`
- **Propósito:** Cruza filas del Excel con catálogo. Retorna filas enriquecidas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_match_parte, info, keys, _build_index, append, list, replace, items, float, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 24)

### `def _interpret_response(text)`
- **Línea inicial:** 284 | **Línea final:** 292
- **Firma completa:** `def _interpret_response(text)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, any`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _insert_one(args)`
- **Línea inicial:** 295 | **Línea final:** 310
- **Firma completa:** `def _insert_one(args)`
- **Propósito:** Envía un precio. args = (row_dict, cookies_dict)
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, _interpret_response, str, post`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def insertar_precios_masivo(cookies_dict, rows_pendientes, stop_event, log, max_workers, batch_confirm)`
- **Línea inicial:** 313 | **Línea final:** 354
- **Firma completa:** `def insertar_precios_masivo(cookies_dict, rows_pendientes, stop_event, log, max_workers, batch_confirm)`
- **Propósito:** Envía precios en paralelo usando ThreadPoolExecutor.
Cada 'batch_confirm' OK, confirma la oferta vía EnviarOferta.
Retorna (ok_count, error_count).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_enviar_oferta, ThreadPoolExecutor, submit, as_completed, progress, is_set, enumerate, result, str, len`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def _enviar_oferta(client, log)`
- **Línea inicial:** 357 | **Línea final:** 369
- **Firma completa:** `def _enviar_oferta(client, log)`
- **Propósito:** Confirma la oferta (equivalente a click en #btn_enviarOferta2).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, warn, post`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def process_bulk_upload(page, rows, parte_col, precio_col, log, stop_event, pre_selected)`
- **Línea inicial:** 372 | **Línea final:** 411
- **Firma completa:** `def process_bulk_upload(page, rows, parte_col, precio_col, log, stop_event, pre_selected)`
- **Propósito:** Entry point: subida masiva via HTTP directo.
Descarga el catalogo completo y matchea en memoria.

Returns: list[dict] con status actualizado por fila.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `fetch_catalogo_completo, info, range, insertar_precios_masivo, all, error, get, _cookies_from_page, match_excel_rows, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

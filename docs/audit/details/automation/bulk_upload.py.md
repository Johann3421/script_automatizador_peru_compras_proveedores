# Documentación Técnica: `automation/bulk_upload.py`

- **Ruta relativa:** `automation/bulk_upload.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 411
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _cookies_from_page(page)` (Línea 33)
- **Propósito:** Sin docstring.
- **Firma:** `def _cookies_from_page(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _build_datatable_payload(N_Acuerdo, N_Catalogo, N_Categoria, start, length, search)` (Línea 38)
- **Propósito:** Sin docstring.
- **Firma:** `def _build_datatable_payload(N_Acuerdo, N_Catalogo, N_Categoria, start, length, search)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def buscar_producto_por_parte(client, N_Acuerdo, N_Catalogo, N_Categoria, parte)` (Línea 60)
- **Propósito:** Busca productos filtrando por parte en C_Descripcion (como el buscador del sitio).
- **Firma:** `def buscar_producto_por_parte(client, N_Acuerdo, N_Catalogo, N_Categoria, parte)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _match_parte_in_results(parte, results)` (Línea 73)
- **Propósito:** Busca el mejor match de un part number entre los resultados de busqueda.
- **Firma:** `def _match_parte_in_results(parte, results)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _search_and_match_one(args)` (Línea 93)
- **Propósito:** Busca un part number y matchea. args = (row, parte_col, precio_col,
N_Acuerdo, N_Catalogo, N_Categoria, cookies_dict, log)
- **Firma:** `def _search_and_match_one(args)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _normalize(text)` (Línea 143)
- **Propósito:** Sin docstring.
- **Firma:** `def _normalize(text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def fetch_catalogo_completo(client, N_Acuerdo, N_Catalogo, N_Categoria, log)` (Línea 147)
- **Propósito:** Descarga TODOS los productos del catalogo paginando de 500 en 500.
- **Firma:** `def fetch_catalogo_completo(client, N_Acuerdo, N_Catalogo, N_Categoria, log)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _build_index(catalogo_rows)` (Línea 176)
- **Propósito:** Sin docstring.
- **Firma:** `def _build_index(catalogo_rows)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _match_parte(parte, idx)` (Línea 188)
- **Propósito:** Sin docstring.
- **Firma:** `def _match_parte(parte, idx)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def match_excel_rows(excel_rows, parte_col, precio_col, catalogo_rows, log)` (Línea 205)
- **Propósito:** Cruza filas del Excel con catálogo. Retorna filas enriquecidas.
- **Firma:** `def match_excel_rows(excel_rows, parte_col, precio_col, catalogo_rows, log)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _interpret_response(text)` (Línea 284)
- **Propósito:** Sin docstring.
- **Firma:** `def _interpret_response(text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _insert_one(args)` (Línea 295)
- **Propósito:** Envía un precio. args = (row_dict, cookies_dict)
- **Firma:** `def _insert_one(args)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def insertar_precios_masivo(cookies_dict, rows_pendientes, stop_event, log, max_workers, batch_confirm)` (Línea 313)
- **Propósito:** Envía precios en paralelo usando ThreadPoolExecutor.
Cada 'batch_confirm' OK, confirma la oferta vía EnviarOferta.
Retorna (ok_count, error_count).
- **Firma:** `def insertar_precios_masivo(cookies_dict, rows_pendientes, stop_event, log, max_workers, batch_confirm)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _enviar_oferta(client, log)` (Línea 357)
- **Propósito:** Confirma la oferta (equivalente a click en #btn_enviarOferta2).
- **Firma:** `def _enviar_oferta(client, log)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def process_bulk_upload(page, rows, parte_col, precio_col, log, stop_event, pre_selected)` (Línea 372)
- **Propósito:** Entry point: subida masiva via HTTP directo.
Descarga el catalogo completo y matchea en memoria.

Returns: list[dict] con status actualizado por fila.
- **Firma:** `def process_bulk_upload(page, rows, parte_col, precio_col, log, stop_event, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

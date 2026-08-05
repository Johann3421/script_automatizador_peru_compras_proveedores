# Documentación Técnica: `modulo_modificar_productos/automation_mod/navegacion_productos.py`

- **Ruta relativa:** `modulo_modificar_productos/automation_mod/navegacion_productos.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 756
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _esperar_tabla(page, log, max_ciclos, espera)` (Línea 30)
- **Propósito:** Sin docstring.
- **Firma:** `def _esperar_tabla(page, log, max_ciclos, espera)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _es_no_encontrado(page)` (Línea 42)
- **Propósito:** Sin docstring.
- **Firma:** `def _es_no_encontrado(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _select2_select(page, select_id, value)` (Línea 52)
- **Propósito:** Selecciona una opción en un Select2 usando el método nativo de Playwright.
- **Firma:** `def _select2_select(page, select_id, value)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def apply_dropdowns_and_search(page, pre_selected, log, stop_event)` (Línea 112)
- **Propósito:** Sin docstring.
- **Firma:** `def apply_dropdowns_and_search(page, pre_selected, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def buscar_por_parte(page, parte, log, stop_event)` (Línea 323)
- **Propósito:** Sin docstring.
- **Firma:** `def buscar_por_parte(page, parte, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def click_editar(page, log, stop_event)` (Línea 368)
- **Propósito:** Sin docstring.
- **Firma:** `def click_editar(page, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)` (Línea 409)
- **Propósito:** Sin docstring.
- **Firma:** `def subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def guardar_cambios(page, log, stop_event)` (Línea 435)
- **Propósito:** Sin docstring.
- **Firma:** `def guardar_cambios(page, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def cerrar_modal_mensaje(page, log, context)` (Línea 454)
- **Propósito:** Espera y cierra el modal #MensajeModal que aparece tras guardar.
- **Firma:** `def cerrar_modal_mensaje(page, log, context)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def ensure_logged_in_and_ready(page, usuario, password, pre_selected, log, stop_event, captcha_bridge)` (Línea 486)
- **Propósito:** Verifica que sigamos logueados y en la lista de productos.
Si no, re-loguea, navega a t_CatalogoProductoMarca, aplica dropdowns y busca.
- **Firma:** `def ensure_logged_in_and_ready(page, usuario, password, pre_selected, log, stop_event, captcha_bridge)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def agregar_caracteristicas(page, log, stop_event)` (Línea 533)
- **Propósito:** Sin docstring.
- **Firma:** `def agregar_caracteristicas(page, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_select_options(page, selector)` (Línea 680)
- **Propósito:** Retorna las opciones de un select como [{value, text}, ...].
- **Firma:** `def _get_select_options(page, selector)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def volver_a_lista(page, log, stop_event)` (Línea 693)
- **Propósito:** Click en #btnRegresarIndex (Retornar) para volver a la lista.
- **Firma:** `def volver_a_lista(page, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def process_single_product(page, parte, ruta_pdf, log, stop_event, pre_selected)` (Línea 728)
- **Propósito:** Sin docstring.
- **Firma:** `def process_single_product(page, parte, ruta_pdf, log, stop_event, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

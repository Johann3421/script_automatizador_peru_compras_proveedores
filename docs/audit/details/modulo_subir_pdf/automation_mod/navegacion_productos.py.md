# Documentación Técnica: `modulo_subir_pdf/automation_mod/navegacion_productos.py`

- **Ruta relativa:** `modulo_subir_pdf/automation_mod/navegacion_productos.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 1464
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _esperar_tabla(page, log, max_ciclos, espera)` (Línea 31)
- **Propósito:** Sin docstring.
- **Firma:** `def _esperar_tabla(page, log, max_ciclos, espera)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _es_no_encontrado(page)` (Línea 43)
- **Propósito:** Sin docstring.
- **Firma:** `def _es_no_encontrado(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _select2_select(page, select_id, value)` (Línea 53)
- **Propósito:** Selecciona una opción en un Select2 usando el método nativo de Playwright.
- **Firma:** `def _select2_select(page, select_id, value)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def apply_dropdowns_and_search(page, pre_selected, log, stop_event)` (Línea 113)
- **Propósito:** Sin docstring.
- **Firma:** `def apply_dropdowns_and_search(page, pre_selected, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def buscar_por_parte(page, parte, log, stop_event)` (Línea 324)
- **Propósito:** Sin docstring.
- **Firma:** `def buscar_por_parte(page, parte, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def click_editar(page, log, stop_event)` (Línea 369)
- **Propósito:** Sin docstring.
- **Firma:** `def click_editar(page, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)` (Línea 410)
- **Propósito:** Sin docstring.
- **Firma:** `def subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def subir_imagen_en_edicion(page, nombre_imagen, log, stop_event)` (Línea 451)
- **Propósito:** Sube la imagen del producto. nombre_imagen es el valor de la columna
IMAGEN (PDF) del Excel (ej: "EZENT M5"). Busca en PDF_DIR con extensiones .jpg/.png/.jpeg.
- **Firma:** `def subir_imagen_en_edicion(page, nombre_imagen, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def cambiar_precio_en_edicion(page, precio, log, stop_event)` (Línea 489)
- **Propósito:** Cambia el precio en la página de edición si hay un input para él.
- **Firma:** `def cambiar_precio_en_edicion(page, precio, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _find_nro_parte_field(page)` (Línea 539)
- **Propósito:** Busca el campo N° de Parte por selectores o por label de texto.
- **Firma:** `def _find_nro_parte_field(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def actualizar_nro_parte_en_edicion(page, nueva_parte, log, stop_event)` (Línea 580)
- **Propósito:** Borra el campo N° de Parte y escribe el nuevo valor del Excel.
Usa JS para setear el valor (funciona incluso si el campo es readonly)
+ simula paste/typing para disparar eventos de validación.
- **Firma:** `def actualizar_nro_parte_en_edicion(page, nueva_parte, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def guardar_cambios(page, log, stop_event)` (Línea 630)
- **Propósito:** Click en Guardar, espera el modal de éxito y lo cierra.
Acepta múltiples selectores de modal (#MensajeModal, #modalContent, .bootbox.modal).
Si no aparece modal en 360s, asume guardado exitoso y continúa (PeruCompras es lento).
- **Firma:** `def guardar_cambios(page, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def cerrar_modal_mensaje(page, log, context)` (Línea 683)
- **Propósito:** Espera y cierra el modal #MensajeModal que aparece tras guardar. Retorna True si lo cerró.
- **Firma:** `def cerrar_modal_mensaje(page, log, context)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _tiene_campos_login(page)` (Línea 717)
- **Propósito:** Verifica si la página actual tiene los campos de login visibles.
- **Firma:** `def _tiene_campos_login(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def ensure_logged_in_and_ready(page, usuario, password, pre_selected, log, stop_event, captcha_bridge)` (Línea 726)
- **Propósito:** Verifica que sigamos logueados.
NO aplica dropdowns+Buscar (eso tarda 180s+ con miles de fichas).
Solo verifica la sesión y navega a gestión si es necesario.
- **Firma:** `def ensure_logged_in_and_ready(page, usuario, password, pre_selected, log, stop_event, captcha_bridge)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def agregar_caracteristicas(page, log, stop_event)` (Línea 768)
- **Propósito:** Sin docstring.
- **Firma:** `def agregar_caracteristicas(page, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_select_options(page, selector)` (Línea 904)
- **Propósito:** Retorna las opciones de un select como [{value, text}, ...].
- **Firma:** `def _get_select_options(page, selector)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def volver_a_lista(page, log, stop_event)` (Línea 917)
- **Propósito:** Click en #btnRegresarIndex (Retornar) para volver a la lista.
- **Firma:** `def volver_a_lista(page, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def process_single_product(page, parte, ruta_pdf, log, stop_event, pre_selected)` (Línea 952)
- **Propósito:** Sin docstring.
- **Firma:** `def process_single_product(page, parte, ruta_pdf, log, stop_event, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def leer_caracteristicas_pagina(page)` (Línea 985)
- **Propósito:** Lee la tabla de características de la página de edición.
Retorna lista de {"nombre": str, "valor": str, "id": str}.
Estructura HTML: cada característica es un .row con dos .col-md-4
(hidden inputs + nombre + valor).
- **Firma:** `def leer_caracteristicas_pagina(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def leer_certificaciones_pagina(page)` (Línea 1015)
- **Propósito:** Lee la tabla de certificaciones. Retorna lista de {"id": str, "valor": str}.
Estructura: cada cert es un .row con CERTIFICACION como texto y valor en col-md-6.
- **Firma:** `def leer_certificaciones_pagina(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _norm_value(s)` (Línea 1041)
- **Propósito:** Normaliza un valor para comparación: strip, mayúsculas, espacios colapsados.
- **Firma:** `def _norm_value(s)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def comparar_caracteristicas(page_chars, excel_chars, log)` (Línea 1047)
- **Propósito:** Compara las características de la página contra las del Excel.
Retorna {"iguales": int, "diferentes": [{"nombre", "esperado", "actual", "id"}], "faltantes_en_pagina": []}.
Si el valor de la página tiene el prefijo "NOMBRE: " (ej: "TECLADO: SI" para char TECLADO),
se ignora el prefijo antes de comparar.
- **Firma:** `def comparar_caracteristicas(page_chars, excel_chars, log)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def corregir_caracteristica(page, char_id, valor_esperado, log, stop_event, edit_url)` (Línea 1087)
- **Propósito:** Corrige UNA característica. SIEMPRE re-navega a edit_url antes para
garantizar que link_caracteristicaEdit existe (se pierde tras cada guardado).
- **Firma:** `def corregir_caracteristica(page, char_id, valor_esperado, log, stop_event, edit_url)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def agregar_certificaciones_faltantes(page, certs_esperadas, log, stop_event)` (Línea 1235)
- **Propósito:** Verifica certificaciones y agrega solo ISO 9001 / ISO 14001 si faltan.
Reutiliza agregar_caracteristicas() que abre el modal #wm_caracteristicaNueva.
Para certs no-ISO (CE, RoHS, FCC) que falten, las reporta como faltantes.
- **Firma:** `def agregar_certificaciones_faltantes(page, certs_esperadas, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def eliminar_caracteristica(page, char_id, log, stop_event)` (Línea 1270)
- **Propósito:** Elimina una característica por ID.
Flujo: click en link 'Eliminar' del row → modal ._wModal "Si/No" → click Si → listo.
NO aparece modal de éxito después (la fila simplemente desaparece).
- **Firma:** `def eliminar_caracteristica(page, char_id, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def agregar_caracteristica_texto(page, nombre_char, valor_texto, log, stop_event)` (Línea 1350)
- **Propósito:** Agrega una característica con valor de texto libre.
Flujo: click Añadir → seleccionar nombre del char → escribir valor en input de texto
→ Guardar → modal éxito → cerrar.
- **Firma:** `def agregar_caracteristica_texto(page, nombre_char, valor_texto, log, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

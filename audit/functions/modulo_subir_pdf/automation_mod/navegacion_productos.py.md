# Auditoría de Funciones: `modulo_subir_pdf/automation_mod/navegacion_productos.py`

- **Lenguaje:** `python`
- **Líneas de código:** 1464
- **Hash SHA256:** `af444aa2e230`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _esperar_tabla(page, log, max_ciclos, espera)`
- **Línea inicial:** 31 | **Línea final:** 40
- **Firma completa:** `def _esperar_tabla(page, log, max_ciclos, espera)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, range, count, sleep, locator`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def _es_no_encontrado(page)`
- **Línea inicial:** 43 | **Línea final:** 48
- **Firma completa:** `def _es_no_encontrado(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, locator, count`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _select2_select(page, select_id, value)`
- **Línea inicial:** 53 | **Línea final:** 108
- **Firma completa:** `def _select2_select(page, select_id, value)`
- **Propósito:** Selecciona una opción en un Select2 usando el método nativo de Playwright.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, range, count, text_content, locator, select_option, click, sleep, nth, wait_for`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def apply_dropdowns_and_search(page, pre_selected, log, stop_event)`
- **Línea inicial:** 113 | **Línea final:** 319
- **Firma completa:** `def apply_dropdowns_and_search(page, pre_selected, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_esperar_tabla, click, is_set, screenshot, info, sleep, _select2_select, evaluate, warn, range`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 27)

### `def buscar_por_parte(page, parte, log, stop_event)`
- **Línea inicial:** 324 | **Línea final:** 364
- **Firma completa:** `def buscar_por_parte(page, parte, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, is_visible, range, _esperar_tabla, click, error, sleep, is_set, _es_no_encontrado`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def click_editar(page, log, stop_event)`
- **Línea inicial:** 369 | **Línea final:** 405
- **Firma completa:** `def click_editar(page, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, is_visible, click, error, sleep, is_set, wait_for_load_state, locator, get_attribute`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)`
- **Línea inicial:** 410 | **Línea final:** 440
- **Firma completa:** `def subir_pdf_en_edicion(page, ruta_pdf, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, set_input_files, isfile, error, sleep, is_set, ok, basename, locator`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def subir_imagen_en_edicion(page, nombre_imagen, log, stop_event)`
- **Línea inicial:** 451 | **Línea final:** 484
- **Firma completa:** `def subir_imagen_en_edicion(page, nombre_imagen, log, stop_event)`
- **Propósito:** Sube la imagen del producto. nombre_imagen es el valor de la columna
IMAGEN (PDF) del Excel (ej: "EZENT M5"). Busca en PDF_DIR con extensiones .jpg/.png/.jpeg.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, set_input_files, join, isfile, sleep, is_set, strip, ok, basename`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def cambiar_precio_en_edicion(page, precio, log, stop_event)`
- **Línea inicial:** 489 | **Línea final:** 523
- **Firma completa:** `def cambiar_precio_en_edicion(page, precio, log, stop_event)`
- **Propósito:** Cambia el precio en la página de edición si hay un input para él.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, is_visible, count, locator, sleep, is_set, str, ok, evaluate, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def _find_nro_parte_field(page)`
- **Línea inicial:** 539 | **Línea final:** 577
- **Firma completa:** `def _find_nro_parte_field(page)`
- **Propósito:** Busca el campo N° de Parte por selectores o por label de texto.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, evaluate, count, locator`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def actualizar_nro_parte_en_edicion(page, nueva_parte, log, stop_event)`
- **Línea inicial:** 580 | **Línea final:** 625
- **Firma completa:** `def actualizar_nro_parte_en_edicion(page, nueva_parte, log, stop_event)`
- **Propósito:** Borra el campo N° de Parte y escribe el nuevo valor del Excel.
Usa JS para setear el valor (funciona incluso si el campo es readonly)
+ simula paste/typing para disparar eventos de validación.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, count, _find_nro_parte_field, click, sleep, is_set, str, ok, evaluate, warn`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def guardar_cambios(page, log, stop_event)`
- **Línea inicial:** 630 | **Línea final:** 680
- **Firma completa:** `def guardar_cambios(page, log, stop_event)`
- **Propósito:** Click en Guardar, espera el modal de éxito y lo cierra.
Acepta múltiples selectores de modal (#MensajeModal, #modalContent, .bootbox.modal).
Si no aparece modal en 360s, asume guardado exitoso y continúa (PeruCompras es lento).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `count, range, info, click, error, cerrar_modal_mensaje, is_set, ok, locator, wait_for_selector`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 12)

### `def cerrar_modal_mensaje(page, log, context)`
- **Línea inicial:** 683 | **Línea final:** 712
- **Firma completa:** `def cerrar_modal_mensaje(page, log, context)`
- **Propósito:** Espera y cierra el modal #MensajeModal que aparece tras guardar. Retorna True si lo cerró.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, is_visible, count, click, sleep, wait_for, locator, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def _tiene_campos_login(page)`
- **Línea inicial:** 717 | **Línea final:** 723
- **Firma completa:** `def _tiene_campos_login(page)`
- **Propósito:** Verifica si la página actual tiene los campos de login visibles.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `is_visible, locator, count`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def ensure_logged_in_and_ready(page, usuario, password, pre_selected, log, stop_event, captcha_bridge)`
- **Línea inicial:** 726 | **Línea final:** 763
- **Firma completa:** `def ensure_logged_in_and_ready(page, usuario, password, pre_selected, log, stop_event, captcha_bridge)`
- **Propósito:** Verifica que sigamos logueados.
NO aplica dropdowns+Buscar (eso tarda 180s+ con miles de fichas).
Solo verifica la sesión y navega a gestión si es necesario.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `do_login, info, lower, error, is_set, _tiene_campos_login, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def agregar_caracteristicas(page, log, stop_event)`
- **Línea inicial:** 768 | **Línea final:** 901
- **Firma completa:** `def agregar_caracteristicas(page, log, stop_event)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_get_select_options, click, is_set, info, sleep, evaluate, warn, range, press, select_option`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 32)

### `def _get_select_options(page, selector)`
- **Línea inicial:** 904 | **Línea final:** 912
- **Firma completa:** `def _get_select_options(page, selector)`
- **Propósito:** Retorna las opciones de un select como [{value, text}, ...].
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def volver_a_lista(page, log, stop_event)`
- **Línea inicial:** 917 | **Línea final:** 947
- **Firma completa:** `def volver_a_lista(page, log, stop_event)`
- **Propósito:** Click en #btnRegresarIndex (Retornar) para volver a la lista.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `is_visible, info, count, goto, click, sleep, is_set, wait_for_load_state, go_back, locator`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def process_single_product(page, parte, ruta_pdf, log, stop_event, pre_selected)`
- **Línea inicial:** 952 | **Línea final:** 980
- **Firma completa:** `def process_single_product(page, parte, ruta_pdf, log, stop_event, pre_selected)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `buscar_por_parte, guardar_cambios, apply_dropdowns_and_search, click_editar, get, agregar_caracteristicas, volver_a_lista, subir_pdf_en_edicion`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def leer_caracteristicas_pagina(page)`
- **Línea inicial:** 985 | **Línea final:** 1012
- **Firma completa:** `def leer_caracteristicas_pagina(page)`
- **Propósito:** Lee la tabla de características de la página de edición.
Retorna lista de {"nombre": str, "valor": str, "id": str}.
Estructura HTML: cada característica es un .row con dos .col-md-4
(hidden inputs + nombre + valor).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def leer_certificaciones_pagina(page)`
- **Línea inicial:** 1015 | **Línea final:** 1038
- **Firma completa:** `def leer_certificaciones_pagina(page)`
- **Propósito:** Lee la tabla de certificaciones. Retorna lista de {"id": str, "valor": str}.
Estructura: cada cert es un .row con CERTIFICACION como texto y valor en col-md-6.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _norm_value(s)`
- **Línea inicial:** 1041 | **Línea final:** 1044
- **Firma completa:** `def _norm_value(s)`
- **Propósito:** Normaliza un valor para comparación: strip, mayúsculas, espacios colapsados.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, sub, upper, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def comparar_caracteristicas(page_chars, excel_chars, log)`
- **Línea inicial:** 1047 | **Línea final:** 1084
- **Firma completa:** `def comparar_caracteristicas(page_chars, excel_chars, log)`
- **Propósito:** Compara las características de la página contra las del Excel.
Retorna {"iguales": int, "diferentes": [{"nombre", "esperado", "actual", "id"}], "faltantes_en_pagina": []}.
Si el valor de la página tiene el prefijo "NOMBRE: " (ej: "TECLADO: SI" para char TECLADO),
se ignora el prefijo antes de comparar.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `upper, append, items, get, startswith, _norm_value, strip, ok, len, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def corregir_caracteristica(page, char_id, valor_esperado, log, stop_event, edit_url)`
- **Línea inicial:** 1087 | **Línea final:** 1227
- **Firma completa:** `def corregir_caracteristica(page, char_id, valor_esperado, log, stop_event, edit_url)`
- **Propósito:** Corrige UNA característica. SIEMPRE re-navega a edit_url antes para
garantizar que link_caracteristicaEdit existe (se pierde tras cada guardado).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_get_select_options, click, is_set, str, info, sleep, endswith, _norm_value, evaluate, warn`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 36)

### `def agregar_certificaciones_faltantes(page, certs_esperadas, log, stop_event)`
- **Línea inicial:** 1235 | **Línea final:** 1265
- **Firma completa:** `def agregar_certificaciones_faltantes(page, certs_esperadas, log, stop_event)`
- **Propósito:** Verifica certificaciones y agrega solo ISO 9001 / ISO 14001 si faltan.
Reutiliza agregar_caracteristicas() que abre el modal #wm_caracteristicaNueva.
Para certs no-ISO (CE, RoHS, FCC) que falten, las reporta como faltantes.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, upper, ok, agregar_caracteristicas, _norm_value, is_set, leer_certificaciones_pagina, warn`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def eliminar_caracteristica(page, char_id, log, stop_event)`
- **Línea inicial:** 1270 | **Línea final:** 1347
- **Firma completa:** `def eliminar_caracteristica(page, char_id, log, stop_event)`
- **Propósito:** Elimina una característica por ID.
Flujo: click en link 'Eliminar' del row → modal ._wModal "Si/No" → click Si → listo.
NO aparece modal de éxito después (la fila simplemente desaparece).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `info, is_visible, count, locator, click, sleep, is_set, str, ok, evaluate`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def agregar_caracteristica_texto(page, nombre_char, valor_texto, log, stop_event)`
- **Línea inicial:** 1350 | **Línea final:** 1464
- **Firma completa:** `def agregar_caracteristica_texto(page, nombre_char, valor_texto, log, stop_event)`
- **Propósito:** Agrega una característica con valor de texto libre.
Flujo: click Añadir → seleccionar nombre del char → escribir valor en input de texto
→ Guardar → modal éxito → cerrar.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_get_select_options, info, count, is_visible, press, upper, locator, select_option, click, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 22)

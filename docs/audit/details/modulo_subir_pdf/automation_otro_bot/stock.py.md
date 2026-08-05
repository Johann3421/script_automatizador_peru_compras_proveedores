# Documentación Técnica: `modulo_subir_pdf/automation_otro_bot/stock.py`

- **Ruta relativa:** `modulo_subir_pdf/automation_otro_bot/stock.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 1418
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `_LogAdapter` (Línea 82)
- **Docstring:** _Adapta una función log_func() simple a la interfaz LogWriter de automation/login.py._
- **Métodos:**
  - `def __init__(self, log_func)` (Línea 84): Sin docstring.
  - `def info(self, msg)` (Línea 87): Sin docstring.
  - `def ok(self, msg)` (Línea 90): Sin docstring.
  - `def error(self, msg)` (Línea 93): Sin docstring.
  - `def warn(self, msg)` (Línea 96): Sin docstring.
  - `def progress(self, current, total)` (Línea 99): Sin docstring.
  - `def done(self, ok_count, error_count)` (Línea 102): Sin docstring.

### Funciones independientes:

#### `def _is_logged_in(page)` (Línea 110)
- **Propósito:** Verifica si seguimos logueados: URL + ausencia de formulario login visible.
- **Firma:** `def _is_logged_in(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _esta_en_mejorabasica(page)` (Línea 132)
- **Propósito:** Verifica que estemos en la página de MejoraBasica (donde se editan productos).
- **Firma:** `def _esta_en_mejorabasica(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _tiene_campos_login(page)` (Línea 141)
- **Propósito:** Verifica si la página actual tiene los campos de login visibles.
- **Firma:** `def _tiene_campos_login(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _relogin(page, usuario, password, log_func, stop_event, captcha_bridge)` (Línea 150)
- **Propósito:** Vuelve a la pagina de login, se loguea de cero y navega a MejoraBasica.

Usa automation.login.do_login (la misma funcion del login inicial) porque
cierra mejor los modales del portal PeruCompras.
- **Firma:** `def _relogin(page, usuario, password, log_func, stop_event, captcha_bridge)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def log(msg)` (Línea 222)
- **Propósito:** Sin docstring.
- **Firma:** `def log(msg)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def clear_modals(page)` (Línea 271)
- **Propósito:** Limpia todos los modales colgados.
- **Firma:** `def clear_modals(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _trigger_materialize(page, input_id)` (Línea 285)
- **Propósito:** Dispara eventos input/change/blur en un input para Materialize CSS.
- **Firma:** `def _trigger_materialize(page, input_id)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _solve_captcha(page)` (Línea 300)
- **Propósito:** OCR del CAPTCHA con 4 thresholds.
- **Firma:** `def _solve_captcha(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _type_field(page, selector_list, value, materialize_id)` (Línea 328)
- **Propósito:** Escribe value en el primer selector que funcione.
- **Firma:** `def _type_field(page, selector_list, value, materialize_id)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def login_with_ocr(page, usuario, password, captcha_bridge, max_intentos, skip_goto)` (Línea 346)
- **Propósito:** Login automático con OCR del CAPTCHA.

Si el OCR no está disponible, retorna False (caller debe caer a login manual).
skip_goto: si True, asume que ya estamos en LOGIN_URL y no navega de nuevo.
- **Firma:** `def login_with_ocr(page, usuario, password, captcha_bridge, max_intentos, skip_goto)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _normalizar_parte(valor)` (Línea 472)
- **Propósito:** Sin docstring.
- **Firma:** `def _normalizar_parte(valor)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _normalizar_stock(valor)` (Línea 484)
- **Propósito:** Convierte a int, retorna None si es inválido.
- **Firma:** `def _normalizar_stock(valor)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def analizar_excel_stock(excel_path)` (Línea 503)
- **Propósito:** Analiza el Excel de stock. Retorna {valido: bool, df: [...], errores: [...]}
- **Firma:** `def analizar_excel_stock(excel_path)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def paso2_navegacion_stock(page)` (Línea 574)
- **Propósito:** Truco de retroceso + ir a MejoraBasica.
- **Firma:** `def paso2_navegacion_stock(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def seleccionar_por_texto_flexible(page, select_id, texto_objetivo)` (Línea 593)
- **Propósito:** Selecciona option que matchea exacto, contiene, o está contenido.
- **Firma:** `def seleccionar_por_texto_flexible(page, select_id, texto_objetivo)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _wait_for_select_options(page, select_id, timeout_ms)` (Línea 656)
- **Propósito:** Espera a que un <select> tenga opciones con value no vacio.
- **Firma:** `def _wait_for_select_options(page, select_id, timeout_ms)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def paso3_filtros_stock(page, acuerdo, catalogo, categoria)` (Línea 672)
- **Propósito:** Selecciona Acuerdo > Catálogo > Categoría y espera que cargue la tabla.
- **Firma:** `def paso3_filtros_stock(page, acuerdo, catalogo, categoria)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def clasificar_error(mensaje)` (Línea 724)
- **Propósito:** Sin docstring.
- **Firma:** `def clasificar_error(mensaje)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _browser_cerrado(mensaje)` (Línea 741)
- **Propósito:** Detecta si el error se debe a que el usuario cerró el navegador.
- **Firma:** `def _browser_cerrado(mensaje)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _find_exact_matching_row(page, parte)` (Línea 752)
- **Propósito:** Busca en la tabla de productos la fila que contenga EXACTAMENTE el número de parte.
Evita seleccionar por error 'PARTE-1' cuando se busca 'PARTE'.
- **Firma:** `def _find_exact_matching_row(page, parte)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def actualizar_producto(page, parte, stock, ficha, stop_event)` (Línea 798)
- **Propósito:** Actualiza el stock de un producto. Retorna (éxito, mensaje_error).
- **Firma:** `def actualizar_producto(page, parte, stock, ficha, stop_event)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _get_field(row, keys, default)` (Línea 1094)
- **Propósito:** Sin docstring.
- **Firma:** `def _get_field(row, keys, default)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge, acuerdo, catalogo, categoria)` (Línea 1107)
- **Propósito:** Itera el DataFrame y actualiza cada producto. Retorna cantidad de éxitos.
- **Firma:** `def paso4_actualizar_stock(page, df, pausa, log_func, usuario, password, captcha_bridge, acuerdo, catalogo, categoria)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def generar_reporte_excel(output_path, acuerdo, catalogo, categoria)` (Línea 1227)
- **Propósito:** Genera el reporte Excel con 3 hojas.
- **Firma:** `def generar_reporte_excel(output_path, acuerdo, catalogo, categoria)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def ejecutar_stock(page, excel_path, usuario, password, acuerdo, catalogo, categoria, pausa, captcha_bridge, log_func)` (Línea 1366)
- **Propósito:** Ejecuta el flujo completo de stock. Retorna path del reporte.
- **Firma:** `def ejecutar_stock(page, excel_path, usuario, password, acuerdo, catalogo, categoria, pausa, captcha_bridge, log_func)`
- **Retorno / Efectos:** Consulta código fuente.

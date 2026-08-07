# Auditoría de Funciones: `automation/perucompras_core.py`

- **Lenguaje:** `python`
- **Líneas de código:** 409
- **Hash SHA256:** `9d5ed8e1af54`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _log(log_func, msg)`
- **Línea inicial:** 27 | **Línea final:** 35
- **Firma completa:** `def _log(log_func, msg)`
- **Propósito:** Envía un mensaje al logger provisto o a la consola estándar.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print, log_func`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def login_automatico(page, usuario, password, captcha_bridge, stop_event, log_func)`
- **Línea inicial:** 38 | **Línea final:** 78
- **Firma completa:** `def login_automatico(page, usuario, password, captcha_bridge, stop_event, log_func)`
- **Propósito:** FUNCION PADRE 1: Login Automático en Perú Compras.

Asegura la configuración del viewport (1920x1080), navega al portal de acceso,
rellena credenciales y resuelve el CAPTCHA numérico con OCR Tesseract.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `do_login, strip, _log, set_viewport_size, str, _LogAdapter`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def saltar_verificacion(page, log_func)`
- **Línea inicial:** 81 | **Línea final:** 108
- **Firma completa:** `def saltar_verificacion(page, log_func)`
- **Propósito:** FUNCION PADRE 2: Saltar Verificación y Navegación a MejoraBasica.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `sleep, go_back, _log, goto`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def navegar_mejora_basica(page, log_func)`
- **Línea inicial:** 111 | **Línea final:** 126
- **Firma completa:** `def navegar_mejora_basica(page, log_func)`
- **Propósito:** FUNCION PADRE 3: Navegación Garantizada a MejoraBasica.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `sleep, _log, goto`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def completar_menu_dinamico(page, acuerdo, catalogo, categoria, log_func)`
- **Línea inicial:** 129 | **Línea final:** 158
- **Firma completa:** `def completar_menu_dinamico(page, acuerdo, catalogo, categoria, log_func)`
- **Propósito:** FUNCION PADRE 4: Completar Menú Dinámico y Filtros.

Asegura que el navegador esté en MejoraBasica, selecciona los 3 dropdowns
del catálogo y hace clic explícito en 'Iniciar Búsqueda' (#btnBuscar).
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `sleep, goto, query_selector, _log, paso3_filtros_stock`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def insertar_stock_item(page, nro_parte, nuevo_stock, pausa, log_func)`
- **Línea inicial:** 161 | **Línea final:** 207
- **Firma completa:** `def insertar_stock_item(page, nro_parte, nuevo_stock, pausa, log_func)`
- **Propósito:** FUNCION PADRE 5: Insertar / Actualizar Stock de Producto.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sleep, query_selector_all, fill, wait_for_selector, query_selector, _log, press, str, click, len`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def consultar_json_productos(page, n_acuerdo, n_catalogo, n_categoria, log_func)`
- **Línea inicial:** 210 | **Línea final:** 345
- **Firma completa:** `def consultar_json_productos(page, n_acuerdo, n_catalogo, n_categoria, log_func)`
- **Propósito:** FUNCION PADRE 6: Extracción Masiva del Dataset JSON de Fichas.

Estrategia de 3 Niveles:
  1. Extracción desde la memoria DataTable/DOM en la página activa (`DataTable().rows().data()`).
  2. Consulta AJAX contextual vía jQuery (`$.ajax`) en el navegador.
  3. Petición POST DataTables nativa a `_CatalogoProductoIndexJson`.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate, get, len, strip, post, loads, text, startswith, int, _log`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 29)

### `def extraer_json_catalogo(usuario, password, n_acuerdo, n_catalogo, n_categoria, acuerdo_texto, catalogo_texto, categoria_texto, output_path, captcha_bridge, stop_event, log_func, headless)`
- **Línea inicial:** 348 | **Línea final:** 409
- **Firma completa:** `def extraer_json_catalogo(usuario, password, n_acuerdo, n_catalogo, n_categoria, acuerdo_texto, catalogo_texto, categoria_texto, output_path, captcha_bridge, stop_event, log_func, headless)`
- **Propósito:** FUNCION PADRE 7: Extracción Completa de JSON a Disco/Memoria.

Flujo E2E completo:
  1. Inicia navegador Playwright (HD 1920x1080).
  2. Ejecuta `login_automatico` con OCR Tesseract ilimitado.
  3. Ejecuta `saltar_verificacion` hacia MejoraBasica.
  4. Ejecuta `completar_menu_dinamico` + clic en #btnBuscar.
  5. Ejecuta `consultar_json_productos` para extraer el dataset completo.
  6. Guarda opcionalmente el archivo JSON en `output_path`.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `makedirs, dirname, completar_menu_dinamico, saltar_verificacion, open, login_automatico, abspath, _log, init_browser, consultar_json_productos`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def info(self, msg)`
- **Línea inicial:** 61 | **Línea final:** 61
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _log, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 62 | **Línea final:** 62
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _log, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 63 | **Línea final:** 63
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _log, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 64 | **Línea final:** 64
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _log, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 65 | **Línea final:** 65
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _log, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def write(self, txt)`
- **Línea inicial:** 66 | **Línea final:** 69
- **Firma completa:** `def write(self, txt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `str, _log, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def flush(self)`
- **Línea inicial:** 70 | **Línea final:** 70
- **Firma completa:** `def flush(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

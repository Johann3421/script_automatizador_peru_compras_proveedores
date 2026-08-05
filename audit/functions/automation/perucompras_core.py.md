# Auditoría de Funciones: `automation/perucompras_core.py`

- **Lenguaje:** `python`
- **Líneas de código:** 339
- **Hash SHA256:** `0b4367f4dd60`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _log(log_func, msg)`
- **Línea inicial:** 25 | **Línea final:** 33
- **Firma completa:** `def _log(log_func, msg)`
- **Propósito:** Envía un mensaje al logger provisto o a la consola estándar.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `print, log_func`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def login_automatico(page, usuario, password, captcha_bridge, stop_event, log_func)`
- **Línea inicial:** 36 | **Línea final:** 96
- **Firma completa:** `def login_automatico(page, usuario, password, captcha_bridge, stop_event, log_func)`
- **Propósito:** FUNCION PADRE 1: Login Automático en Perú Compras.

Asegura la configuración del viewport (1920x1080), navega al portal de acceso,
rellena credenciales y resuelve el CAPTCHA numérico con OCR Tesseract.

Parámetros
----------
page : Playwright Page
    Instancia de la página activa del navegador.
usuario : str
    Nombre de usuario del proveedor en Perú Compras.
password : str
    Contraseña de acceso.
captcha_bridge : CaptchaBridge, opcional
    Puente para resolución manual si el OCR falla.
stop_event : threading.Event, opcional
    Evento de detención provisto por la app.
log_func : Callable[[str], None], opcional
    Función para recibir logs de progreso.
    
Retorno
-------
bool
    True si el inicio de sesión fue exitoso, False si falló.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, set_viewport_size, do_login, str, _LogAdapter`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def saltar_verificacion(page, log_func)`
- **Línea inicial:** 99 | **Línea final:** 134
- **Firma completa:** `def saltar_verificacion(page, log_func)`
- **Propósito:** FUNCION PADRE 2: Saltar Verificación y Retroceso Seguro.

Ejecuta el truco de retroceso de historial de navegación en el browser
y vuelve a cargar el portal base para refrescar cookies de sesión.

Parámetros
----------
page : Playwright Page
    Instancia activa del navegador.
log_func : Callable[[str], None], opcional
    Función para recepción de logs.
    
Retorno
-------
bool
    True al completar la maniobra de retroceso.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `sleep, _log, go_back, goto`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def navegar_mejora_basica(page, log_func)`
- **Línea inicial:** 137 | **Línea final:** 164
- **Firma completa:** `def navegar_mejora_basica(page, log_func)`
- **Propósito:** FUNCION PADRE 3: Navegación Garantizada a MejoraBasica.

Navega a la sección de catálogo y actualización del portal.

Parámetros
----------
page : Playwright Page
log_func : Callable[[str], None], opcional

Retorno
-------
bool
    True si la página de MejoraBasica cargó correctamente.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `sleep, _log, goto`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def completar_menu_dinamico(page, acuerdo, catalogo, categoria, log_func)`
- **Línea inicial:** 167 | **Línea final:** 204
- **Firma completa:** `def completar_menu_dinamico(page, acuerdo, catalogo, categoria, log_func)`
- **Propósito:** FUNCION PADRE 4: Completar Menú Dinámico y Filtros.

Selecciona de forma flexible (insensible a tildes y mayúsculas) los 3 dropdowns
del catálogo electrónico (Acuerdo, Catálogo y Categoría).

Parámetros
----------
page : Playwright Page
acuerdo : str
    Nombre del Acuerdo Marco.
catalogo : str
    Nombre del Catálogo.
categoria : str
    Nombre de la Categoría.
log_func : Callable[[str], None], opcional

Retorno
-------
bool
    True si los 3 combos se seleccionaron con éxito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log, paso3_filtros_stock`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def insertar_stock_item(page, nro_parte, nuevo_stock, pausa, log_func)`
- **Línea inicial:** 207 | **Línea final:** 276
- **Firma completa:** `def insertar_stock_item(page, nro_parte, nuevo_stock, pausa, log_func)`
- **Propósito:** FUNCION PADRE 5: Insertar / Actualizar Stock de Producto.

Busca una ficha por su número de parte o código en el cuadro de búsqueda principal
del portal e inserta la nueva cantidad de existencias.

Parámetros
----------
page : Playwright Page
nro_parte : str
    Número de parte o código del producto a buscar.
nuevo_stock : int
    Cantidad de existencias a asignar.
pausa : float
    Pausa de espera en segundos tras la actualización.
log_func : Callable[[str], None], opcional

Retorno
-------
dict
    {"exito": bool, "parte": str, "stock": int, "mensaje": str}
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log, query_selector, press, len, sleep, wait_for_selector, str, click, fill, query_selector_all`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def consultar_json_productos(page, n_acuerdo, n_catalogo, n_categoria, log_func)`
- **Línea inicial:** 279 | **Línea final:** 339
- **Firma completa:** `def consultar_json_productos(page, n_acuerdo, n_catalogo, n_categoria, log_func)`
- **Propósito:** FUNCION PADRE 6: Extracción Masiva del Dataset JSON de Fichas.

Consulta el endpoint JSON crudo `_ListaProductosOfertados` mediante `fetch`
con las cookies activas de la sesión.

Parámetros
----------
page : Playwright Page
n_acuerdo : int
n_catalogo : int
n_categoria : int
log_func : Callable[[str], None], opcional

Retorno
-------
list
    Lista de diccionarios de fichas ofertadas extraídas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log, len, loads, evaluate, time, str, get, isinstance, int, startswith`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def info(self, msg)`
- **Línea inicial:** 79 | **Línea final:** 79
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 80 | **Línea final:** 80
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 81 | **Línea final:** 81
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 82 | **Línea final:** 82
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 83 | **Línea final:** 83
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def write(self, txt)`
- **Línea inicial:** 84 | **Línea final:** 87
- **Firma completa:** `def write(self, txt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_log, strip, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def flush(self)`
- **Línea inicial:** 88 | **Línea final:** 88
- **Firma completa:** `def flush(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

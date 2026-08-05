# Auditoría de Funciones: `automation/perucompras_core.py`

- **Lenguaje:** `python`
- **Líneas de código:** 334
- **Hash SHA256:** `5000417218bb`
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
- **Línea inicial:** 36 | **Línea final:** 91
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
- **Dependencias / Invocaciones:** `_log, set_viewport_size, strip, _LogAdapter, do_login`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def saltar_verificacion(page, log_func)`
- **Línea inicial:** 94 | **Línea final:** 129
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
- **Dependencias / Invocaciones:** `goto, go_back, sleep, _log`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def navegar_mejora_basica(page, log_func)`
- **Línea inicial:** 132 | **Línea final:** 159
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
- **Dependencias / Invocaciones:** `goto, sleep, _log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def completar_menu_dinamico(page, acuerdo, catalogo, categoria, log_func)`
- **Línea inicial:** 162 | **Línea final:** 199
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
- **Dependencias / Invocaciones:** `paso3_filtros_stock, _log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def insertar_stock_item(page, nro_parte, nuevo_stock, pausa, log_func)`
- **Línea inicial:** 202 | **Línea final:** 271
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
- **Dependencias / Invocaciones:** `_log, query_selector, press, query_selector_all, click, sleep, len, wait_for_selector, fill, str`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def consultar_json_productos(page, n_acuerdo, n_catalogo, n_categoria, log_func)`
- **Línea inicial:** 274 | **Línea final:** 334
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
- **Dependencias / Invocaciones:** `isinstance, evaluate, _log, get, loads, len, time, startswith, str, int`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def write(self, txt)`
- **Línea inicial:** 79 | **Línea final:** 82
- **Firma completa:** `def write(self, txt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def flush(self)`
- **Línea inicial:** 83 | **Línea final:** 83
- **Firma completa:** `def flush(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

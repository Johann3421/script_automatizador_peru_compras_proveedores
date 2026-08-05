# Auditoría de Funciones: `automation/perucompras_core.py`

- **Lenguaje:** `python`
- **Líneas de código:** 274
- **Hash SHA256:** `1cbd436931a3`
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
- **Línea inicial:** 36 | **Línea final:** 76
- **Firma completa:** `def login_automatico(page, usuario, password, captcha_bridge, stop_event, log_func)`
- **Propósito:** FUNCION PADRE 1: Login Automático en Perú Compras.

Asegura la configuración del viewport (1920x1080), navega al portal de acceso,
rellena credenciales y resuelve el CAPTCHA numérico con OCR Tesseract.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set_viewport_size, _log, do_login, str, strip, _LogAdapter`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def saltar_verificacion(page, log_func)`
- **Línea inicial:** 79 | **Línea final:** 111
- **Firma completa:** `def saltar_verificacion(page, log_func)`
- **Propósito:** FUNCION PADRE 2: Saltar Verificación y Navegación a MejoraBasica.

Ejecuta la secuencia probada de navegación:
1) Retroceso seguro de historial (go_back)
2) Recarga de BASE_URL
3) Navegación final a MEJORA_URL (sección MejoraBasica)
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `_log, goto, go_back, sleep`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def navegar_mejora_basica(page, log_func)`
- **Línea inicial:** 114 | **Línea final:** 129
- **Firma completa:** `def navegar_mejora_basica(page, log_func)`
- **Propósito:** FUNCION PADRE 3: Navegación Garantizada a MejoraBasica.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `_log, goto, sleep`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def completar_menu_dinamico(page, acuerdo, catalogo, categoria, log_func)`
- **Línea inicial:** 132 | **Línea final:** 162
- **Firma completa:** `def completar_menu_dinamico(page, acuerdo, catalogo, categoria, log_func)`
- **Propósito:** FUNCION PADRE 4: Completar Menú Dinámico y Filtros.

Asegura que el navegador esté en MejoraBasica y selecciona de forma flexible
los 3 dropdowns del catálogo electrónico (Acuerdo, Catálogo y Categoría).
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `query_selector, _log, goto, paso3_filtros_stock, sleep`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def insertar_stock_item(page, nro_parte, nuevo_stock, pausa, log_func)`
- **Línea inicial:** 165 | **Línea final:** 211
- **Firma completa:** `def insertar_stock_item(page, nro_parte, nuevo_stock, pausa, log_func)`
- **Propósito:** FUNCION PADRE 5: Insertar / Actualizar Stock de Producto.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `len, query_selector, query_selector_all, click, _log, wait_for_selector, press, fill, sleep, str`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def consultar_json_productos(page, n_acuerdo, n_catalogo, n_categoria, log_func)`
- **Línea inicial:** 214 | **Línea final:** 274
- **Firma completa:** `def consultar_json_productos(page, n_acuerdo, n_catalogo, n_categoria, log_func)`
- **Propósito:** FUNCION PADRE 6: Extracción Masiva del Dataset JSON de Fichas.

Consulta el endpoint JSON crudo `_ListaProductosOfertados` mediante `fetch`
utilizando las cookies activas de la sesión.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `len, startswith, get, time, int, isinstance, loads, type, _log, goto`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def info(self, msg)`
- **Línea inicial:** 59 | **Línea final:** 59
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warning(self, msg)`
- **Línea inicial:** 60 | **Línea final:** 60
- **Firma completa:** `def warning(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 61 | **Línea final:** 61
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def success(self, msg)`
- **Línea inicial:** 62 | **Línea final:** 62
- **Firma completa:** `def success(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 63 | **Línea final:** 63
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def write(self, txt)`
- **Línea inicial:** 64 | **Línea final:** 67
- **Firma completa:** `def write(self, txt)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strip, _log, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def flush(self)`
- **Línea inicial:** 68 | **Línea final:** 68
- **Firma completa:** `def flush(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

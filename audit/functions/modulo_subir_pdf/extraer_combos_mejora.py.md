# Auditoría de Funciones: `modulo_subir_pdf/extraer_combos_mejora.py`

- **Lenguaje:** `python`
- **Líneas de código:** 168
- **Hash SHA256:** `c9fe09655a7a`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def read_select_options(page, selector)`
- **Línea inicial:** 54 | **Línea final:** 68
- **Firma completa:** `def read_select_options(page, selector)`
- **Propósito:** Lee options de un <select>, filtra vacíos y value=0.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `evaluate`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def wait_for_options(page, selector, timeout)`
- **Línea inicial:** 71 | **Línea final:** 84
- **Firma completa:** `def wait_for_options(page, selector, timeout)`
- **Propósito:** Espera a que un <select> tenga al menos 1 option válida.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `wait_for_function`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def extraer_combos()`
- **Línea inicial:** 87 | **Línea final:** 164
- **Firma completa:** `def extraer_combos()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `read_select_options, wait_for_options, type, launch, set_viewport_size, info, isoformat, close, open, sleep`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def info(self, m)`
- **Línea inicial:** 48 | **Línea final:** 48
- **Firma completa:** `def info(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `strftime, now, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, m)`
- **Línea inicial:** 49 | **Línea final:** 49
- **Firma completa:** `def warn(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `strftime, now, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, m)`
- **Línea inicial:** 50 | **Línea final:** 50
- **Firma completa:** `def error(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `strftime, now, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, m)`
- **Línea inicial:** 51 | **Línea final:** 51
- **Firma completa:** `def ok(self, m)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `strftime, now, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

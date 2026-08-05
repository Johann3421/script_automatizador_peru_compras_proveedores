# Auditoría de Funciones: `utils/logger.py`

- **Lenguaje:** `python`
- **Líneas de código:** 24
- **Hash SHA256:** `4125dde8932e`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def __init__(self, log_queue)`
- **Línea inicial:** 5 | **Línea final:** 6
- **Firma completa:** `def __init__(self, log_queue)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Ninguna`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def info(self, msg)`
- **Línea inicial:** 8 | **Línea final:** 9
- **Firma completa:** `def info(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def ok(self, msg)`
- **Línea inicial:** 11 | **Línea final:** 12
- **Firma completa:** `def ok(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def error(self, msg)`
- **Línea inicial:** 14 | **Línea final:** 15
- **Firma completa:** `def error(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def warn(self, msg)`
- **Línea inicial:** 17 | **Línea final:** 18
- **Firma completa:** `def warn(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def progress(self, current, total)`
- **Línea inicial:** 20 | **Línea final:** 21
- **Firma completa:** `def progress(self, current, total)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def done(self, ok_count, error_count)`
- **Línea inicial:** 23 | **Línea final:** 24
- **Firma completa:** `def done(self, ok_count, error_count)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

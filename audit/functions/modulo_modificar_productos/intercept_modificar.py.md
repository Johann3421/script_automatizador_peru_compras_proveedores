# Auditoría de Funciones: `modulo_modificar_productos/intercept_modificar.py`

- **Lenguaje:** `python`
- **Líneas de código:** 238
- **Hash SHA256:** `8c42bb99fb03`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def ts()`
- **Línea inicial:** 45 | **Línea final:** 46
- **Firma completa:** `def ts()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `strftime, now`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def info(msg)`
- **Línea inicial:** 48 | **Línea final:** 49
- **Firma completa:** `def info(msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `ts, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def on_request(request)`
- **Línea inicial:** 55 | **Línea final:** 108
- **Firma completa:** `def on_request(request)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `info, isoformat, dict, print, lower, append, loads, split, items, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 20)

### `def save_results(page)`
- **Línea inicial:** 111 | **Línea final:** 124
- **Firma completa:** `def save_results(page)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `is_closed, info, isoformat, lower, open, now, dump, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def main()`
- **Línea inicial:** 129 | **Línea final:** 234
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `buscar_por_parte, init_browser, apply_dropdowns_and_search, Event, volver_a_lista, set_viewport_size, info, guardar_cambios, sleep, agregar_caracteristicas`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

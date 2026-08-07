# Auditoría de Funciones: `modulo_subir_pdf/test_extraccion_json.py`

- **Lenguaje:** `python`
- **Líneas de código:** 93
- **Hash SHA256:** `a8162bef577b`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _imprimir_resumen(data)`
- **Línea inicial:** 45 | **Línea final:** 59
- **Firma completa:** `def _imprimir_resumen(data)`
- **Propósito:** Imprime un resumen legible del JSON extraído.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `items, str, isinstance, list, len, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def ejecutar()`
- **Línea inicial:** 62 | **Línea final:** 89
- **Firma completa:** `def ejecutar()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `_imprimir_resumen, extraer_json_catalogo, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

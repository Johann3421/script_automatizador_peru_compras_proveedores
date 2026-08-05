# Auditoría de Funciones: `modulo_modificar_productos/utils_mod/excel_parser_mod.py`

- **Lenguaje:** `python`
- **Líneas de código:** 183
- **Hash SHA256:** `a5f06e0efd81`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _normalize(text)`
- **Línea inicial:** 36 | **Línea final:** 42
- **Firma completa:** `def _normalize(text)`
- **Propósito:** Normaliza texto para comparación: minúsculas, sin acentos.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, replace, items, str, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _match_col(header, aliases)`
- **Línea inicial:** 45 | **Línea final:** 47
- **Firma completa:** `def _match_col(header, aliases)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `any, _normalize`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def get_sheets(path)`
- **Línea inicial:** 50 | **Línea final:** 55
- **Firma completa:** `def get_sheets(path)`
- **Propósito:** Retorna la lista de hojas del Excel.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `close, load_workbook`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def detect_columns(path, sheet)`
- **Línea inicial:** 58 | **Línea final:** 81
- **Firma completa:** `def detect_columns(path, sheet)`
- **Propósito:** Detecta automáticamente las columnas de parte, PDF y certificaciones.
Retorna un dict con las claves 'parte_col', 'pdf_col', 'cert_col' (puede ser None).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `iter_rows, close, _match_col, str, load_workbook`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def parse_excel(path, sheet, parte_col, pdf_col, cert_col)`
- **Línea inicial:** 84 | **Línea final:** 183
- **Firma completa:** `def parse_excel(path, sheet, parte_col, pdf_col, cert_col)`
- **Propósito:** Lee el Excel y retorna una lista de dicts con:
  {
    "parte":   str,         # N° de Parte
    "pdf":     str | None,  # Ruta al PDF (o None)
    "certs":   str | None,  # Texto de certificaciones (o None)
    "_row_idx": int,        # Índice de fila (0-based, desde header+1)
  }
Filas con parte vacía son ignoradas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `all, iter_rows, list, append, close, get, _match_col, enumerate, str, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 27)

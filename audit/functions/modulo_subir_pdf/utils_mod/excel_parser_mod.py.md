# Auditoría de Funciones: `modulo_subir_pdf/utils_mod/excel_parser_mod.py`

- **Lenguaje:** `python`
- **Líneas de código:** 339
- **Hash SHA256:** `90eee74139a3`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _normalize(text)`
- **Línea inicial:** 64 | **Línea final:** 73
- **Firma completa:** `def _normalize(text)`
- **Propósito:** Normaliza texto para comparación: minúsculas, sin acentos.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, replace, items, str, strip`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def _match_col(header, aliases)`
- **Línea inicial:** 76 | **Línea final:** 85
- **Firma completa:** `def _match_col(header, aliases)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `any, _normalize, len`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 1)

### `def get_sheets(path)`
- **Línea inicial:** 88 | **Línea final:** 93
- **Firma completa:** `def get_sheets(path)`
- **Propósito:** Retorna la lista de hojas del Excel.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `close, load_workbook`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def detect_columns(path, sheet)`
- **Línea inicial:** 96 | **Línea final:** 159
- **Firma completa:** `def detect_columns(path, sheet)`
- **Propósito:** Detecta automáticamente las columnas de parte, PDF, certificaciones,
características y certificaciones esperadas.
Retorna un dict con:
  - 'parte_col'   : nombre exacto de la columna N° de Parte
  - 'ficha_col'   : nombre exacto de la columna Ficha N° (o None)
  - 'pdf_col'     : nombre exacto de la columna PDF (o None)
  - 'cert_col'    : nombre exacto de la columna Certificaciones (o None)
  - 'char_cols'   : lista de nombres de columnas de características
  - 'cert_expected_cols' : lista de nombres de columnas CERTIFICACION N
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_normalize, iter_rows, append, close, match, next, startswith, _match_col, compile, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 17)

### `def parse_excel(path, sheet, parte_col, pdf_col, cert_col)`
- **Línea inicial:** 162 | **Línea final:** 339
- **Firma completa:** `def parse_excel(path, sheet, parte_col, pdf_col, cert_col)`
- **Propósito:** Lee el Excel y retorna una lista de dicts con:
  {
    "parte":   str,         # N° de Parte
    "pdf":     str | None,  # Ruta al PDF (o None)
    "certs":   str | None,  # Texto de certificaciones (o None)
    "caracteristicas": dict,  # {nombre_caracteristica: valor_esperado, ...}
    "certs_esperadas": list,  # ['ISO 9001', 'CE O UE', ...]
    "_row_idx": int,        # Índice de fila (0-based, desde header+1)
  }
Filas con parte vacía son ignoradas.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `_normalize, all, list, iter_rows, append, close, get, match, _match_col, compile`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 66)

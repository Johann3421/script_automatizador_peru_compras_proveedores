# Documentación Técnica: `modulo_subir_pdf/utils_mod/excel_parser_mod.py`

- **Ruta relativa:** `modulo_subir_pdf/utils_mod/excel_parser_mod.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 339
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _normalize(text)` (Línea 64)
- **Propósito:** Normaliza texto para comparación: minúsculas, sin acentos.
- **Firma:** `def _normalize(text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _match_col(header, aliases)` (Línea 76)
- **Propósito:** Sin docstring.
- **Firma:** `def _match_col(header, aliases)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def get_sheets(path)` (Línea 88)
- **Propósito:** Retorna la lista de hojas del Excel.
- **Firma:** `def get_sheets(path)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def detect_columns(path, sheet)` (Línea 96)
- **Propósito:** Detecta automáticamente las columnas de parte, PDF, certificaciones,
características y certificaciones esperadas.
Retorna un dict con:
  - 'parte_col'   : nombre exacto de la columna N° de Parte
  - 'ficha_col'   : nombre exacto de la columna Ficha N° (o None)
  - 'pdf_col'     : nombre exacto de la columna PDF (o None)
  - 'cert_col'    : nombre exacto de la columna Certificaciones (o None)
  - 'char_cols'   : lista de nombres de columnas de características
  - 'cert_expected_cols' : lista de nombres de columnas CERTIFICACION N
- **Firma:** `def detect_columns(path, sheet)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def parse_excel(path, sheet, parte_col, pdf_col, cert_col)` (Línea 162)
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
- **Firma:** `def parse_excel(path, sheet, parte_col, pdf_col, cert_col)`
- **Retorno / Efectos:** Consulta código fuente.

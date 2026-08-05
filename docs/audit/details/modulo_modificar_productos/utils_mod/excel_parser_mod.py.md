# Documentación Técnica: `modulo_modificar_productos/utils_mod/excel_parser_mod.py`

- **Ruta relativa:** `modulo_modificar_productos/utils_mod/excel_parser_mod.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 183
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _normalize(text)` (Línea 36)
- **Propósito:** Normaliza texto para comparación: minúsculas, sin acentos.
- **Firma:** `def _normalize(text)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _match_col(header, aliases)` (Línea 45)
- **Propósito:** Sin docstring.
- **Firma:** `def _match_col(header, aliases)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def get_sheets(path)` (Línea 50)
- **Propósito:** Retorna la lista de hojas del Excel.
- **Firma:** `def get_sheets(path)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def detect_columns(path, sheet)` (Línea 58)
- **Propósito:** Detecta automáticamente las columnas de parte, PDF y certificaciones.
Retorna un dict con las claves 'parte_col', 'pdf_col', 'cert_col' (puede ser None).
- **Firma:** `def detect_columns(path, sheet)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def parse_excel(path, sheet, parte_col, pdf_col, cert_col)` (Línea 84)
- **Propósito:** Lee el Excel y retorna una lista de dicts con:
  {
    "parte":   str,         # N° de Parte
    "pdf":     str | None,  # Ruta al PDF (o None)
    "certs":   str | None,  # Texto de certificaciones (o None)
    "_row_idx": int,        # Índice de fila (0-based, desde header+1)
  }
Filas con parte vacía son ignoradas.
- **Firma:** `def parse_excel(path, sheet, parte_col, pdf_col, cert_col)`
- **Retorno / Efectos:** Consulta código fuente.

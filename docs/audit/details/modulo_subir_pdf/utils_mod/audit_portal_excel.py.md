# Documentación Técnica: `modulo_subir_pdf/utils_mod/audit_portal_excel.py`

- **Ruta relativa:** `modulo_subir_pdf/utils_mod/audit_portal_excel.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 251
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _header_font(bold, size, color)` (Línea 33)
- **Propósito:** Sin docstring.
- **Firma:** `def _header_font(bold, size, color)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _normal_font(bold, size, color)` (Línea 36)
- **Propósito:** Sin docstring.
- **Firma:** `def _normal_font(bold, size, color)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _fill(hex_color)` (Línea 39)
- **Propósito:** Sin docstring.
- **Firma:** `def _fill(hex_color)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _border()` (Línea 42)
- **Propósito:** Sin docstring.
- **Firma:** `def _border()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _center()` (Línea 46)
- **Propósito:** Sin docstring.
- **Firma:** `def _center()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _left()` (Línea 49)
- **Propósito:** Sin docstring.
- **Firma:** `def _left()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _build_summary_sheet(ws, resumen)` (Línea 55)
- **Propósito:** Sin docstring.
- **Firma:** `def _build_summary_sheet(ws, resumen)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _build_detail_sheet(ws, filas)` (Línea 151)
- **Propósito:** Sin docstring.
- **Firma:** `def _build_detail_sheet(ws, filas)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def generar_excel_auditoria(filas, resumen, ruta_salida)` (Línea 220)
- **Propósito:** Genera el Excel de auditoria.

filas: list[dict] — cada dict con:
    parte, descripcion, stock_excel, precio_excel, ficha,
    stock_portal, estado_portal, diferencia, resultado
    resultado in {"OK", "DIFERENCIA", "NO ENCONTRADO"}

resumen: dict — total, ok, dif, missing, tasa, acuerdo, catalogo,
    categoria, excel_file, timestamp

ruta_salida: str — path completo del .xlsx

Retorna (True, ruta_salida) | (False, mensaje_error)
- **Firma:** `def generar_excel_auditoria(filas, resumen, ruta_salida)`
- **Retorno / Efectos:** Consulta código fuente.

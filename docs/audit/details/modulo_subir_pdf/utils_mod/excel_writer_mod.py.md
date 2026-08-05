# Documentación Técnica: `modulo_subir_pdf/utils_mod/excel_writer_mod.py`

- **Ruta relativa:** `modulo_subir_pdf/utils_mod/excel_writer_mod.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 58
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def find_data_start(ws)` (Línea 12)
- **Propósito:** Encuentra la primera fila de datos (header + 1).
- **Firma:** `def find_data_start(ws)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def write_colored_results(source_path, sheet_name, results)` (Línea 21)
- **Propósito:** Colorea el Excel según los resultados.
Verde (ok) = 100% match, Amarillo (differ) = falla, Rojo (not_found) = no existe.
- **Firma:** `def write_colored_results(source_path, sheet_name, results)`
- **Retorno / Efectos:** Consulta código fuente.

# Documentación Técnica: `modulo_modificar_productos/utils_mod/excel_writer_mod.py`

- **Ruta relativa:** `modulo_modificar_productos/utils_mod/excel_writer_mod.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 57
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
- **Propósito:** Colorea el Excel según los resultados del procesamiento.
Amarillo = completado, Azul = ya tenía ISOs, Rojo = no encontrado/error.
Retorna la ruta del archivo coloreado.
- **Firma:** `def write_colored_results(source_path, sheet_name, results)`
- **Retorno / Efectos:** Consulta código fuente.

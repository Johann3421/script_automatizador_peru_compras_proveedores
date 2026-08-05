# Documentación Técnica: `demo_pywebview.py`

- **Ruta relativa:** `demo_pywebview.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 152
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `PeruComprasApi` (Línea 19)
- **Docstring:** _Clase puente JS API exponiendo métodos de backend Python a JS en el WebView._
- **Métodos:**
  - `def __init__(self)` (Línea 21): Sin docstring.
  - `def set_window(self, window)` (Línea 26): Sin docstring.
  - `def minimize(self)` (Línea 30): Sin docstring.
  - `def maximize(self)` (Línea 34): Sin docstring.
  - `def close(self)` (Línea 38): Sin docstring.
  - `def select_file(self)` (Línea 43): Sin docstring.
  - `def load_sheet(self, sheet_name)` (Línea 71): Sin docstring.
  - `def start_process(self)` (Línea 80): Sin docstring.
  - `def stop_process(self)` (Línea 84): Sin docstring.
  - `def start_stock_process(self, params)` (Línea 88): Sin docstring.
  - `def stop_stock_process(self)` (Línea 92): Sin docstring.
  - `def start_stock_audit(self, params)` (Línea 96): Sin docstring.
  - `def export_audit(self, fmt)` (Línea 102): Sin docstring.

### Funciones independientes:

#### `def main()` (Línea 130)
- **Propósito:** Sin docstring.
- **Firma:** `def main()`
- **Retorno / Efectos:** Consulta código fuente.

# Documentación Técnica: `utils/logger.py`

- **Ruta relativa:** `utils/logger.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 24
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `LogWriter` (Línea 4)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, log_queue)` (Línea 5): Sin docstring.
  - `def info(self, msg)` (Línea 8): Sin docstring.
  - `def ok(self, msg)` (Línea 11): Sin docstring.
  - `def error(self, msg)` (Línea 14): Sin docstring.
  - `def warn(self, msg)` (Línea 17): Sin docstring.
  - `def progress(self, current, total)` (Línea 20): Sin docstring.
  - `def done(self, ok_count, error_count)` (Línea 23): Sin docstring.

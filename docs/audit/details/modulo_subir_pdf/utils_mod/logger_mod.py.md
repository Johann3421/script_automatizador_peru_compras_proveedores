# Documentación Técnica: `modulo_subir_pdf/utils_mod/logger_mod.py`

- **Ruta relativa:** `modulo_subir_pdf/utils_mod/logger_mod.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 33
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `LogWriter` (Línea 9)
- **Docstring:** _Escribe mensajes en una queue thread-safe._
- **Métodos:**
  - `def __init__(self, q)` (Línea 12): Sin docstring.
  - `def _put(self, level, msg)` (Línea 16): Sin docstring.
  - `def info(self, msg)` (Línea 20): Sin docstring.
  - `def ok(self, msg)` (Línea 23): Sin docstring.
  - `def warn(self, msg)` (Línea 26): Sin docstring.
  - `def error(self, msg)` (Línea 29): Sin docstring.
  - `def done(self, ok, err)` (Línea 32): Sin docstring.

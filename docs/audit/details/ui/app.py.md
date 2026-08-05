# Documentación Técnica: `ui/app.py`

- **Ruta relativa:** `ui/app.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 101
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `CaptchaBridge` (Línea 10)
- **Docstring:** _Permite al thread de automation pedirle al usuario que resuelva el CAPTCHA._
- **Métodos:**
  - `def __init__(self)` (Línea 12): Sin docstring.
  - `def request(self, image_bytes)` (Línea 18): Sin docstring.
  - `def respond(self, code)` (Línea 27): Sin docstring.

#### Clase `CatalogBridge` (Línea 34)
- **Docstring:** _Permite al thread pedir al usuario que seleccione dropdowns en cascada._
- **Métodos:**
  - `def __init__(self)` (Línea 36): Sin docstring.
  - `def request_step(self, step, options)` (Línea 43): Bloquea hasta que el usuario seleccione un valor para este paso.
  - `def respond_step(self, value)` (Línea 54): Sin docstring.

#### Clase `App` (Línea 61)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, root)` (Línea 62): Sin docstring.
  - `def show_screen(self, name)` (Línea 93): Sin docstring.

# Documentación Técnica: `build_exe.py`

- **Ruta relativa:** `build_exe.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 192
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def run(cmd)` (Línea 18)
- **Propósito:** Sin docstring.
- **Firma:** `def run(cmd)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def find_playwright_browsers()` (Línea 23)
- **Propósito:** Encuentra la carpeta de navegadores de Playwright sin importar el módulo.
- **Firma:** `def find_playwright_browsers()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def find_tesseract_files()` (Línea 35)
- **Propósito:** Encuentra archivos de Tesseract para empaquetar.
- **Firma:** `def find_tesseract_files()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def ensure_pyinstaller()` (Línea 50)
- **Propósito:** Sin docstring.
- **Firma:** `def ensure_pyinstaller()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def build()` (Línea 59)
- **Propósito:** Sin docstring.
- **Firma:** `def build()`
- **Retorno / Efectos:** Consulta código fuente.

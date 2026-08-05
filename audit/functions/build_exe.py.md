# Auditoría de Funciones: `build_exe.py`

- **Lenguaje:** `python`
- **Líneas de código:** 192
- **Hash SHA256:** `745af021101d`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def run(cmd)`
- **Línea inicial:** 18 | **Línea final:** 20
- **Firma completa:** `def run(cmd)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `run, join, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def find_playwright_browsers()`
- **Línea inicial:** 23 | **Línea final:** 32
- **Firma completa:** `def find_playwright_browsers()`
- **Propósito:** Encuentra la carpeta de navegadores de Playwright sin importar el módulo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `get, isdir, join`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def find_tesseract_files()`
- **Línea inicial:** 35 | **Línea final:** 47
- **Firma completa:** `def find_tesseract_files()`
- **Propósito:** Encuentra archivos de Tesseract para empaquetar.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `isdir, dirname, which`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def ensure_pyinstaller()`
- **Línea inicial:** 50 | **Línea final:** 56
- **Firma completa:** `def ensure_pyinstaller()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `run, print`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def build()`
- **Línea inicial:** 59 | **Línea final:** 188
- **Firma completa:** `def build()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `find_playwright_browsers, find_tesseract_files, exists, write, join, print, isfile, rmtree, ensure_pyinstaller, run`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

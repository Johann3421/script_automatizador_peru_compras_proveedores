# Auditoría de Funciones: `build_installer.py`

- **Lenguaje:** `python`
- **Líneas de código:** 218
- **Hash SHA256:** `7030b21c2f46`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def find_usable_python()`
- **Línea inicial:** 49 | **Línea final:** 89
- **Firma completa:** `def find_usable_python()`
- **Propósito:** Encuentra un Python que tenga PyInstaller instalado.
Prioriza el Python actual. Si no tiene PyInstaller, busca otros.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `import_module, append, isfile, run, expandvars, extend`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def ensure_build_deps(python_exe)`
- **Línea inicial:** 92 | **Línea final:** 109
- **Firma completa:** `def ensure_build_deps(python_exe)`
- **Propósito:** Instala las dependencias necesarias en el Python dado.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `run, print`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 4)

### `def build()`
- **Línea inicial:** 112 | **Línea final:** 214
- **Firma completa:** `def build()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `TemporaryDirectory, print, join, makedirs, isfile, exit, run, ensure_build_deps, rmtree, getsize`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

# Documentación Técnica: `build_installer.py`

- **Ruta relativa:** `build_installer.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 218
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def find_usable_python()` (Línea 49)
- **Propósito:** Encuentra un Python que tenga PyInstaller instalado.
Prioriza el Python actual. Si no tiene PyInstaller, busca otros.
- **Firma:** `def find_usable_python()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def ensure_build_deps(python_exe)` (Línea 92)
- **Propósito:** Instala las dependencias necesarias en el Python dado.
- **Firma:** `def ensure_build_deps(python_exe)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def build()` (Línea 112)
- **Propósito:** Sin docstring.
- **Firma:** `def build()`
- **Retorno / Efectos:** Consulta código fuente.

# Auditoría de Funciones: `modulo_subir_pdf/utils_mod/config_helper.py`

- **Lenguaje:** `python`
- **Líneas de código:** 34
- **Hash SHA256:** `e1078b15f1c9`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def get_writable_path(filename, default_dir)`
- **Línea inicial:** 4 | **Línea final:** 34
- **Firma completa:** `def get_writable_path(filename, default_dir)`
- **Propósito:** Retorna una ruta de archivo que sea escribible por el usuario actual.
Si la carpeta de instalación (default_dir) es de solo lectura (por ejemplo, en Program Files),
creará y retornará una ruta en el directorio AppData/Local de Windows, copiando
el archivo pre-empaquetado si existiese.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `copy, exists, write, join, makedirs, expanduser, open, get`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

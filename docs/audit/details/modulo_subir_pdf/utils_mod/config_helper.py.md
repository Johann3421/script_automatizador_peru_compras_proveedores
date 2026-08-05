# Documentación Técnica: `modulo_subir_pdf/utils_mod/config_helper.py`

- **Ruta relativa:** `modulo_subir_pdf/utils_mod/config_helper.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 34
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def get_writable_path(filename, default_dir)` (Línea 4)
- **Propósito:** Retorna una ruta de archivo que sea escribible por el usuario actual.
Si la carpeta de instalación (default_dir) es de solo lectura (por ejemplo, en Program Files),
creará y retornará una ruta en el directorio AppData/Local de Windows, copiando
el archivo pre-empaquetado si existiese.
- **Firma:** `def get_writable_path(filename, default_dir)`
- **Retorno / Efectos:** Consulta código fuente.

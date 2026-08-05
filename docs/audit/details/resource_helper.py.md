# Documentación Técnica: `resource_helper.py`

- **Ruta relativa:** `resource_helper.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 36
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def resource_path(relative_path)` (Línea 10)
- **Propósito:** Devuelve la ruta absoluta a `relative_path`.

- Cuando la aplicación está congelada (PyInstaller) usa sys._MEIPASS o la carpeta _internal.
- En desarrollo usa la carpeta raíz del proyecto.
- **Firma:** `def resource_path(relative_path)`
- **Retorno / Efectos:** Consulta código fuente.

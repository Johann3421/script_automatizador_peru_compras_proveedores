# Auditoría de Funciones: `resource_helper.py`

- **Lenguaje:** `python`
- **Líneas de código:** 36
- **Hash SHA256:** `1b0b7cb5cd3e`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def resource_path(relative_path)`
- **Línea inicial:** 10 | **Línea final:** 30
- **Firma completa:** `def resource_path(relative_path)`
- **Propósito:** Devuelve la ruta absoluta a `relative_path`.

- Cuando la aplicación está congelada (PyInstaller) usa sys._MEIPASS o la carpeta _internal.
- En desarrollo usa la carpeta raíz del proyecto.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `exists, join, getattr, abspath, hasattr, normpath, dirname`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

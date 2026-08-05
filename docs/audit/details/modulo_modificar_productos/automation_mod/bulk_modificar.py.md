# Documentación Técnica: `modulo_modificar_productos/automation_mod/bulk_modificar.py`

- **Ruta relativa:** `modulo_modificar_productos/automation_mod/bulk_modificar.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 195
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def buscar_producto_api(page, parte, catalogo, categoria, estado, log, timeout)` (Línea 29)
- **Propósito:** Sin docstring.
- **Firma:** `def buscar_producto_api(page, parte, catalogo, categoria, estado, log, timeout)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _is_logged_in(page)` (Línea 62)
- **Propósito:** Verifica si seguimos logueados mirando la URL actual.
- **Firma:** `def _is_logged_in(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _relogin(page, usuario, password, log, stop_event, captcha_bridge)` (Línea 73)
- **Propósito:** Re-loguea y navega a la página de gestión.
- **Firma:** `def _relogin(page, usuario, password, log, stop_event, captcha_bridge)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def run_bulk_modificar(page, rows, pre_selected, log, stop_event, captcha_bridge, usuario, password)` (Línea 90)
- **Propósito:** Sin docstring.
- **Firma:** `def run_bulk_modificar(page, rows, pre_selected, log, stop_event, captcha_bridge, usuario, password)`
- **Retorno / Efectos:** Consulta código fuente.

# Documentación Técnica: `modulo_subir_pdf/tab_precios_json.py`

- **Ruta relativa:** `modulo_subir_pdf/tab_precios_json.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 456
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def build_precios_json_tab(app, parent)` (Línea 7)
- **Propósito:** Vista de Precios JSON — paleta institucional light.
- **Firma:** `def build_precios_json_tab(app, parent)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _export_precios_audit_report(app, fmt)` (Línea 196)
- **Propósito:** Sin docstring.
- **Firma:** `def _export_precios_audit_report(app, fmt)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _load_and_populate_catalog_menu(app)` (Línea 229)
- **Propósito:** Carga y puebla automáticamente los dropdowns dinámicos desde cualquier JSON disponible.
- **Firma:** `def _load_and_populate_catalog_menu(app)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _pick_json(app, lbl_file)` (Línea 308)
- **Propósito:** Sin docstring.
- **Firma:** `def _pick_json(app, lbl_file)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _log_precios(app, msg)` (Línea 325)
- **Propósito:** Sin docstring.
- **Firma:** `def _log_precios(app, msg)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _on_precio_acuerdo_changed(app, selected_val)` (Línea 331)
- **Propósito:** Sin docstring.
- **Firma:** `def _on_precio_acuerdo_changed(app, selected_val)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _on_precio_catalogo_changed(app, selected_val)` (Línea 348)
- **Propósito:** Sin docstring.
- **Firma:** `def _on_precio_catalogo_changed(app, selected_val)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _on_extraer_menu(app)` (Línea 367)
- **Propósito:** Sin docstring.
- **Firma:** `def _on_extraer_menu(app)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _on_test_precios(app)` (Línea 386)
- **Propósito:** Sin docstring.
- **Firma:** `def _on_test_precios(app)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _on_iniciar_precios(app)` (Línea 422)
- **Propósito:** Sin docstring.
- **Firma:** `def _on_iniciar_precios(app)`
- **Retorno / Efectos:** Consulta código fuente.

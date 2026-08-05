# Documentación Técnica: `modulo_modificar_productos/automation_mod/modificar_loop.py`

- **Ruta relativa:** `modulo_modificar_productos/automation_mod/modificar_loop.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 170
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def run_modificar_loop(page, rows, log, stop_event, pre_selected)` (Línea 33)
- **Propósito:** Bucle principal. Procesa cada fila del Excel.

Args:
    page: Página de Playwright (ya logueada y en la sección de gestión)
    rows: Lista de dicts con {'parte', 'pdf', 'certs', '_row_idx'}
    log: LogWriter
    stop_event: threading.Event para detener el proceso
    pre_selected: dict con los valores seleccionados en los dropdowns del catalogo

Returns:
    Lista de dicts con {'index', 'parte', 'status', 'detalle'}
    Status posibles: 'ok', 'no_encontrado', 'error_pdf', 'error_certs', 'error_guardar', 'error'
- **Firma:** `def run_modificar_loop(page, rows, log, stop_event, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

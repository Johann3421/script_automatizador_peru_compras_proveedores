# Auditoría de Funciones: `modulo_modificar_productos/automation_mod/modificar_loop.py`

- **Lenguaje:** `python`
- **Líneas de código:** 170
- **Hash SHA256:** `4e5f0c487898`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def run_modificar_loop(page, rows, log, stop_event, pre_selected)`
- **Línea inicial:** 33 | **Línea final:** 170
- **Firma completa:** `def run_modificar_loop(page, rows, log, stop_event, pre_selected)`
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
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `agregar_certificaciones, done, is_set, volver_a_lista, abrir_edicion, info, guardar_cambios, put, hasattr, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 14)

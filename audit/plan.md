# PLAN DE OPTIMIZACIÓN PRIORIZADO (FASE 4)

## Checkpoint Humano Requerido
> Este plan especifica las optimizaciones rankeadas por nivel de riesgo y beneficio.

### 🟢 Prioridad 1: Bajo Riesgo / Alto Beneficio
1. **Normalización de Handlers Web UI:** Garantizar que los métodos expuestos en `SubirPdfWebApi` y `_methods_to_bind` mantengan paridad 1:1.
2. **Limpieza de scripts auxiliares no empaquetados:** Organizar scripts de prueba aislada (`test_*.py`) dentro de `tests/` o `scripts/`.

### 🟡 Prioridad 2: Riesgo Medio (Requiere aprobación)
1. **Unificación de Parsers Excel:** Consolidar `utils/excel_parser.py` y `modulo_subir_pdf/utils_mod/excel_parser_mod.py` en un único componente reusable.

### 🔴 Prioridad 3: Riesgo Alto (Requiere suite de tests manuales)
1. Refactor de optimización en `modulo_subir_pdf/automation_otro_bot/stock.py` para desacoplar handlers de eventos visuales.

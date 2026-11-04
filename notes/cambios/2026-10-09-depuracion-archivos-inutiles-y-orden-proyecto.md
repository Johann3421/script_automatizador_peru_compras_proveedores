# 2026-10-09 — Depuración de Archivos Inútiles y Reorganización del Proyecto

- **Fecha:** 2026-10-09
- **Tipo:** Refactor / Depuración / Ordenamiento
- **Estado:** Completado
- **Autor:** Antigravity AI

---

## 1. Contexto
El usuario confirmó que el proyecto activo principal es `modulo_subir_pdf/main_subir_pdf.py` y que el resto de componentes solo son requeridos para ensamblar el instalador distribuible. Se requiere identificar con precisión todos los archivos inútiles o legados que no intervienen en la ejecución ni en la compilación del instalador para su eliminación.

---

## 2. Inventario de Archivos Inútiles / Huérfanos Identificados

### A. Raíz del Repositorio (Archivos Legados / Pruebas)
| Archivo / Carpeta | Tamaño | Motivo de Depuración |
|:---|:---:|:---|
| `demo_pywebview.py` | 5.3 KB | Script de prueba inicial descartable. |
| `extract_catalog.py` | 3.4 KB | Script aislado superado por el flujo interno. |
| `intercept_payload.py` | 8.0 KB | Script interceptor de pruebas antiguo. |
| `pagina_perucompras.html`| 140 KB | Volcado HTML estático viejo de pruebas. |
| `MONITOR_2026 (1).xlsx` | 82 KB | Archivo Excel personal de pruebas dejado en raíz. |
| `FLUJO_STOCK_COMPLETO.txt`| 19.4 KB | Nota informal de texto libre ya documentada. |
| `Instalar_PeruComprasBot_v1.1.spec` | 1.1 KB | Spec de PyInstaller de versión 1.1 obsoleto. |
| `Instalar_PeruComprasBot_v1.4.spec` | 1.1 KB | Spec generado automáticamente en builds previos. |
| `PeruComprasBot.spec` | 2.4 KB | Regenerado automáticamente por `build_exe.py`. |
| `ui/` (directorio completo)| ~27 KB | Antigua UI CustomTkinter en desuso total. |
| `modulo_modificar_productos/` | ~60 KB | Submódulo paralelo abandonado no conectado a la UI web. |
| `installer_tmp/` | ~30 MB | Residuos temporales de descarga de Inno Setup. |
| `build_installer/` | ~150 MB | Cache temporal de compilación PyInstaller. |
| `venv_build/` | ~200 MB | Entorno virtual temporal de builds anteriores. |

### B. Subcarpeta `modulo_subir_pdf/` (Bloat y Código Muerto)
| Archivo | Tamaño / Líneas | Motivo de Depuración |
|:---|:---:|:---|
| `ctk_compat.py` | 452 lín (19 KB) | Emulador CustomTkinter sin uso en PyWebView. |
| `gui_instructions_tab.py` | 105 lín (7 KB) | Pestaña Tkinter redundante con `ui_web/index.html`. |
| `tab_precios_json.py` | 468 lín (20 KB) | Pestaña Tkinter redundante con `#view-json`. Contiene un import roto (`parse_excel_precios`). |
| `test_1_ficha.py` | 132 lín (5 KB) | Script de prueba descartable. |
| `test_buscar_ficha.py` | 246 lín (9 KB) | Script de prueba descartable. |
| `test_extraccion_json.py` | 196 lín (3 KB) | Script de prueba descartable. |
| `test_ficha_endpoint.py` | 78 lín (3 KB) | Script de prueba descartable. |
| `extraer_combos_mejora.py`| 168 lín (6 KB) | Script de prueba descartable. |
| `discovery_perucompras.py`| 489 lín (24 KB) | Versión v1 deprecada por `discovery_v2_perucompras.py`. |
| `run_subir_pdf.py` | 21 lín | Redundante con `main.py`. |
| `precios_fichas_fichas_2026-07-09 (1).json` | 1.86 MB | Volcado pesado de pruebas de julio 2026. |
| `reporte_subida_precios_*.xlsx` | ~370 KB | Archivos temporales de pruebas pasadas. |
| `*.txt` (`CONTEXTO_EXTRACCION.txt`, etc.) | ~30 KB | Notas de desarrollo temporales. |

---

## 3. Componentes Críticos a Mantener para el Build
1. **Core de Ejecución:**
   - `main.py` -> delega a `modulo_subir_pdf/main_subir_pdf.py`.
   - `ui_web/index.html` + `ui_web/favicon.png`.
   - `modulo_subir_pdf/workers.py`.
   - `modulo_subir_pdf/automation_mod/` (`navegacion_productos.py`, `bulk_subir_pdf.py`).
   - `modulo_subir_pdf/automation_otro_bot/` (`stock.py`).
   - `modulo_subir_pdf/utils_mod/` (`audit_portal_excel.py`, `excel_report_designer.py`, `audit_reporter.py`, `excel_parser_mod.py`, `excel_writer_mod.py`, `logger_mod.py`).
   - `automation/browser.py` y `automation/login.py`.
   - `catalog_options.json`, `resource_helper.py`, `resources/`.
2. **Pipeline de Construcción del Instalador:**
   - `build.bat`
   - `build_exe.py`
   - `installer/setup.iss` + `installer/license.txt`
   - `requirements.txt`

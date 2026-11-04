# 2026-10-09 — Análisis Integral, Diagnóstico de Fallas y Plan de Optimización

- **Fecha:** 2026-10-09
- **Tipo:** Análisis / Diagnóstico / Arquitectura
- **Estado:** Completado
- **Autor:** Antigravity AI

---

## 1. Contexto y Objetivo
El usuario solicitó un análisis exhaustivo del proyecto, los avances logrados, las fallas técnicas actuales, los puntos críticos desorganizados y las oportunidades de optimización para formular un plan de solución definitivo.

---

## 2. Diagnóstico de Avances
1. **Interfaz Webview Moderna:** Se migró la presentación a `ui_web/index.html` con PyWebView (WebView2), logrando un diseño sobrio, institucional (`#006CA8`), libre de dependencias pesadas de navegador nativo y con controles drag/drop y CSD.
2. **Reportes Ejecutivos en Excel:** Implementación de `utils_mod/excel_report_designer.py` y `audit_portal_excel.py` generando informes de 2 hojas (Dashboard KPIs + Detalle estructurado con anchos automáticos y tiempos transcurridos).
3. **Mecanismo de Aislamiento de Navegador:** `automation/browser.py` implementa detección de Chromium aislado con fallback automático a Microsoft Edge nativo de Windows.
4. **Inserción de Precios Masiva JSON:** En `workers.py`, se integraron llamadas directas de lote para acelerar la subida de precios evitando el flujo 1x1 por DOM cuando es posible.

---

## 3. Puntos Críticos y Fallas Detectadas
1. **God-File Monolítico (`modulo_subir_pdf/main_subir_pdf.py`):**
   - 3,761 líneas.
   - Crea `_Backend` y le inyecta métodos de `SubirPdfApp` con `setattr` mientras simula widgets de Tkinter con `_DummyWidget`. Si un método lee un atributo no contemplado, arroja `AttributeError` en runtime.
2. **Conflicto de Hilos / Diálogos Tkinter dentro de PyWebView:**
   - En `SubirPdfWebApi`, métodos como `select_file()` y `select_stock_file()` inicializan `root = tk.Tk(); root.withdraw()` para abrir `filedialog`.
   - En Windows, mezclar bucles de eventos WinForms/WebView2 con Tkinter genera congelamientos y ventanas modales fantasma detrás del WebView. Debe usarse `window.create_file_dialog()` nativo de PyWebView.
3. **Credenciales en Texto Plano Hardcodeadas:**
   - `ui_web/index.html`: valores por defecto `almerco.03` / `4lm3rKenYa@#`.
   - `main_subir_pdf.py:3257`: valor por defecto `estalin.huamali01`.
4. **Duplicación Masiva de Código:**
   - 3 parsers de Excel (`utils/excel_parser.py`, `modulo_modificar_productos/utils_mod/excel_parser_mod.py`, `modulo_subir_pdf/utils_mod/excel_parser_mod.py`).
   - 3 loggers duplicados.
   - 2 submódulos paralelos de navegación.
5. **Código Muerto y Bloat Empaquetado:**
   - `ctk_compat.py` (452 lín): emulador de customtkinter innecesario en la versión PyWebView.
   - `gui_instructions_tab.py` (105 lín) y `tab_precios_json.py` (468 lín): widgets CTk redundantes.
   - Archivos temporales y volcados pesados en el repo (.xlsx, .json de 1.8 MB, html de 140 KB).
6. **Módulo Desconectado:**
   - `modulo_modificar_productos/` funciona como una app CustomTkinter paralela y aislada, nunca integrada a la UI Web `ui_web/index.html`.

---

## 4. Plan de Acción y Soluciones
- **Fase 1 (Seguridad y Estabilidad Inmediata):** Limpiar credenciales hardcodeadas y reemplazar `tk.Tk()` por `window.create_file_dialog()`.
- **Fase 2 (Desacoplamiento Estructural):** Extraer la API y controladores de `main_subir_pdf.py` a módulos limpios (`web_api.py`, `backend_controller.py`). Eliminar `_DummyWidget`.
- **Fase 3 (Consolidación):** Unificar parsers y loggers en `utils/`. Eliminar código muerto (`ctk_compat.py`, scripts de prueba huérfanos).
- **Fase 4 (Integración Completa):** Añadir la funcionalidad de `modulo_modificar_productos` en las pestañas de `ui_web/index.html`.

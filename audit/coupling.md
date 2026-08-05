# REPORTE DE ACOPLAMIENTO Y DEPENDENCIAS (FASE 3.4)

### Puntos de Acoplamiento Clave:
1. `modulo_subir_pdf/main_subir_pdf.py` ➔ `modulo_subir_pdf/workers.py` (Delegación de ejecuciones asíncronas).
2. `modulo_subir_pdf/workers.py` ➔ `automation/login.py` (Servicio de autenticación e integración Tesseract OCR).
3. `ui_web/index.html` ➔ `SubirPdfWebApi` en `main_subir_pdf.py` (Puente PyWebView JS API).

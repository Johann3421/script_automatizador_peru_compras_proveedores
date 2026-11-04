# 2026-11-04 — Control Manual de Envío y Verificación Previa de Ofertas

- **Fecha:** 2026-11-04
- **Tipo:** Feature / UX & Seguridad Operativa
- **Estado:** Implementado y Verificado
- **Módulo:** `modulo_subir_pdf` (`workers.py`, `main_subir_pdf.py`, `ui_web/index.html`)

---

## 🎯 Contexto y Objetivo
El cliente requiere que el sistema no envíe la oferta de manera automática al portal tras subir los precios temporales. Se debe permitir al usuario:
1. Subir los precios dejando la oferta en **borrador/temporal** dentro de Perú Compras para poder verificarla con tranquilidad (en la pantalla o en el reporte Excel generado).
2. Disponer de una opción en la interfaz (`chkAutoEnviar`) para decidir si enviar automáticamente o no (desmarcada por defecto para máxima seguridad).
3. Disponer de un botón visible y destacado (`btnConfirmarOferta` - `🚀 CONFIRMAR Y ENVIAR OFERTA AHORA`) para confirmar y enviar la oferta al portal con un solo clic cuando el usuario termine de verificar.

---

## 🛠️ Arquitectura y Cambios Implementados

### 1. Desacoplamiento de la Confirmación de Oferta (`modulo_subir_pdf/workers.py`)
- Se extrajo el flujo de envío de oferta a una función independiente y reutilizable: `_ejecutar_confirmacion_oferta(page, log_func, app)`.
- Se añadió el parámetro `auto_enviar` (por defecto `False`) a `execute_iniciar_precios`.
- Si `auto_enviar=False` y se insertaron precios con éxito (`oks > 0`):
  - No ejecuta `_ejecutar_confirmacion_oferta`.
  - Refresca la tabla del portal (`BuscarCatProducto()`).
  - Mantiene viva la sesión de Playwright (`app._precios_browser`, `app._precios_page`, `app._precios_pw`).
  - Genera el reporte Excel de auditoría.
  - Activa en la UI el botón de confirmación manual mediante `mostrarBotonConfirmarOferta(true)`.

### 2. Puente API Python ↔ Webview (`modulo_subir_pdf/main_subir_pdf.py`)
- En `start_json_process`: recibe `auto_enviar` desde el frontend y lo transfiere al worker de subida de precios.
- Nuevo método `confirmar_oferta_manual`:
  - Recupera la sesión activa de Playwright (`self._app._precios_page`).
  - Lanza en un hilo asíncrono la ejecución de `_ejecutar_confirmacion_oferta`.
  - Notifica a la consola UI del progreso.
  - Cierra de manera limpia el navegador y recursos al finalizar.
- En `stop_json_process`: limpia y cierra cualquier sesión de navegador retenida en espera de confirmación y oculta el botón manual.

### 3. Interfaz de Usuario y Controles (`ui_web/index.html`)
- **Checkbox de Modo:** `#chkAutoEnviar` ("Enviar oferta automáticamente (desmarcado: queda en borrador para verificar)").
- **Botón de Acción:** `#btnConfirmarOferta` ("🚀 CONFIRMAR Y ENVIAR OFERTA AHORA"), con estilo ámbar destacado (`#D97706`), inicialmente oculto y mostrado solo cuando existan ofertas listas en borrador.
- **Funciones JS:**
  - `mostrarBotonConfirmarOferta(mostrar)`: muestra/oculta y hace scroll suave al botón.
  - `confirmarOfertaManual()`: invoca `pyapi('confirmar_oferta_manual')` y maneja estados visuales de carga.

---

## 📁 Archivos Modificados
- [`modulo_subir_pdf/workers.py`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/modulo_subir_pdf/workers.py)
- [`modulo_subir_pdf/main_subir_pdf.py`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/modulo_subir_pdf/main_subir_pdf.py)
- [`ui_web/index.html`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/ui_web/index.html)
- [`dist/PeruComprasBot/ui_web/index.html`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/dist/PeruComprasBot/ui_web/index.html)
- [`notes/INDEX.md`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/notes/INDEX.md)


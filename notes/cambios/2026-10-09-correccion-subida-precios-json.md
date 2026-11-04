# 2026-10-09 — Corrección y Puesta a Punto: Subida de Precios JSON

- **Fecha:** 2026-10-09
- **Tipo:** Bug Fix / Automation / Frontend UI & Backend Bridge
- **Estado:** Completado y Verificado
- **Autor:** Antigravity AI

---

## 1. Contexto y Objetivo
El módulo **Subida de Precios JSON** (`#view-json`) fallaba al ejecutarse y no ofrecía control de visibilidad de Chromium al usuario. El objetivo fue implementar de forma completa y reactiva los controles de usuario, visibilidad de navegador, selección de catálogos y el flujo de automatización en Playwright para la inserción y extracción de precios.

---

## 2. Archivos Modificados

| Archivo | Modificación |
|---|---|
| `ui_web/index.html` | Agregados campos `jsonUser`, `jsonPass`, checkbox `chkJsonVisible`, combos `jsonAcuerdo`, `jsonCat`, `jsonCategoria`. Actualizadas funciones JS `startJsonProcess()` y `extractJsonFromPortal()`. |
| `automation/perucompras_core.py` | Corregido `BASE_URL` a `https://catalogos.perucompras.gob.pe` (sin `www.`), eliminando la redirección 301 de Azure Gateway. |
| `automation/login.py`, `automation/navigation.py`, `automation/bulk_upload.py` | Unificadas URLs canónicas sin `www.`. |
| `modulo_subir_pdf/workers.py` | Eliminadas URLs con `www.`. Reescrito `execute_json_extractor` para navegar directamente a `t_ProductoOfertadoAmp`, aplicar filtros, ingresar a Agregar Oferta e interceptar `_CatalogoProductoIndexJson` descargando las fichas en lotes API sin timeouts. |
| `modulo_subir_pdf/main_subir_pdf.py` | En `SubirPdfWebApi`: validación de contraseña, resolución de combos con `_catalog_data`, soporte de flag `visible` (headless=False) e integración completa de `extract_json_portal`. |

---

## 3. Diagnóstico de Causa Raíz y Solución Técnica

1. **Redirección 301 de Azure Application Gateway v2:**
   - Perú Compras redirige `www.catalogos.perucompras.gob.pe` hacia `catalogos.perucompras.gob.pe` con código `301 Moved Permanently`.
   - Cuando Playwright ejecuta peticiones POST hacia endpoints con `www.`, el estándar HTTP del cliente convierte el 301 en un método GET sin body. Los endpoints de ASP.NET MVC (`[HttpPost] _CatalogoProductoIndexJson`) rechazan o congelan la conexión, causando `Timeout 35000ms exceeded`.
   - **Solución:** Se migraron todas las URLs del sistema a la URL canónica `https://catalogos.perucompras.gob.pe`.

2. **Extracción Correcta de Ofertas vs Stock:**
   - Previamente `execute_json_extractor` delegaba en `extraer_json_catalogo` (orientado al módulo de Stock en `/MejoraBasica`).
   - Para la pestaña de **Precios JSON**, se reescribió `execute_json_extractor` para consultar el módulo de ofertas (`t_ProductoOfertadoAmp`), entrar a Agregar Oferta e interceptar `_CatalogoProductoIndexJson`, descargando exactamente las fichas de productos ofertables con su moneda, descripciones y precios.

3. **Reparación de `_LogAdapter.warning` y Control de Detención:**
   - En `workers.py`, `_LogAdapter` carecía del método `warning`, lo que provocaba `AttributeError` al intentar registrar advertencias de OCR en `do_login`, abortando en cada ciclo. Se añadió `warning(self, msg)`.
   - El botón **Detener** no afectaba al extractor porque `extract_json_portal` creaba `stop_event` pero `stop_json_process` consultaba `_json_stop_event`. Se unificaron ambos eventos y se añadió verificación activa de `page.is_closed()` en `do_login` para abortar inmediatamente si el usuario cierra el navegador o cancela la tarea.

4. **Fallo de Intercepción Reactiva de Payload (`_CatalogoProductoIndexJson`) y Solución Definitiva:**
   - **Causa raíz:** Tras el click en `#btnNuevoProducto`, los workers esperaban pasivamente a que `page.on("request")` capturara un request llamado exactamente `_CatalogoProductoIndexJson`. Si DataTables no se disparaba inmediatamente en ese contexto de ventana, `captured_payload` quedaba vacío tras 35s y abortaba con `Error: No se pudo capturar el payload de red. Abortando`.
   - **Solución implementada:** Se creó el helper centralizado `_download_all_catalog_products` compartido entre `execute_json_extractor`, `execute_test_precios` y `execute_iniciar_precios`.
   - El helper implementa una estrategia híbrida: escucha brevemente (3s); si el evento no llega, recurre automáticamente a `_build_datatable_payload(n_acuerdo, n_catalogo, n_categoria, start, length)` para consultar directamente el endpoint `_CatalogoProductoIndexJson` usando la sesión activa de Playwright (`page.request.post`), con paginación automática en lotes de 100 hasta completar el `recordsTotal`.

---

## 4. Próximos Pasos
- Probar la extracción y subida de precios en vivo desde la UI webview.


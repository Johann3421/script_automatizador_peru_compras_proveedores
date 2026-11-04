# 2026-11-04 — Diagnóstico y Solución de Timeout (35000ms) en Subida de Precios

- **Fecha:** 2026-11-04
- **Tipo:** Diagnóstico de Incidencia y Bugfix
- **Estado:** Resuelto y Verificado
- **Módulo:** `modulo_subir_pdf` (`workers.py`)

---

## 🎯 Contexto e Incidencia Reportada

Al ejecutar la subida o prueba de precios en el portal de Perú Compras:
```text
👉 Clic en botón 'Agregar oferta'...
ℹ️ Usando payload directo estructurado (Acuerdo [249], Catálogo [252], Categoría [11735])...
📡 Consultando catálogo en Perú Compras vía API...
❌ Error en petición inicial de catálogo: APIRequestContext.post: Timeout 35000ms exceeded.
Call log:
  - → POST https://catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp/_CatalogoProductoIndexJson
❌ No se obtuvieron fichas del catálogo
```

---

## 🔍 Análisis de Parámetros Ejecutados

1. **Parámetros enviados:**
   - **Acuerdo:** `249` (`EXT-CE-2022-5 COMPUTADORAS Y ESCÁNERES`)
   - **Catálogo:** `252` (`COMPUTADORAS DE ESCRITORIO`)
   - **Categoría:** `11735` (`COMPUTADORA DE ESCRITORIO`)
2. **Evaluación de validez:**
   - Los IDs `249 > 252 > 11735` son **completamente válidos** en Perú Compras (albergan 571 fichas técnicas de computadoras).
   - *Nota de uso:* Si el usuario carga un archivo de **Pantallas Interactivas** (`P75C00`, `P86C01`), la categoría destino en Perú Compras es `11749` (PANTALLA INTERACTIVA). No obstante, el error actual no fue de matching sino de bloqueo de red a nivel API.

---

## 🔎 Causa Raíz del Error (Timeout 35000ms)

1. **Colisión de Sesión ASP.NET (Exclusive Session Lock):**
   - Al hacer clic en `#btnNuevoProducto` ("Agregar oferta"), el navegador navega a `CatalogoProductoIndex`.
   - El script esperaba un tiempo fijo de apenas **3 segundos** (`deadline = time.time() + 3`).
   - Al cumplirse los 3 segundos, los servidores de Perú Compras aún estaban cargando los scripts y el DOM.
   - El script cancelaba los listeners y lanzaba una petición manual `page.request.post(...)` usando el payload sintético.
   - Mientras tanto, el navegador en segundo plano terminaba de inicializar jQuery/DataTables y enviaba **su propia petición AJAX con el mismo `ASP.NET_SessionId`**.
   - ASP.NET MVC bloquea concurrentemente la sesión por usuario (`SessionState Lock`), encolando las peticiones y disparando la latencia del servidor.

2. **Timeout rígido e insuficiencia de reintentos:**
   - `timeout=35000` (35s) era demasiado restrictivo para servidores públicos con alta latencia como Perú Compras (en `navigation.py` se usan 60-120s).
   - La función `_download_all_catalog_products` carecía de reintentos: ante un microcorte o demora de 36s, abortaba todo el proceso.

3. **Desperdicio de datos ya recibidos por el navegador:**
   - Cuando el navegador entraba a `CatalogoProductoIndex`, el portal ya respondía con los primeros 100 productos en `_CatalogoProductoIndexJson`.
   - `handle_response` solo extraía `recordsTotal` y descartaba el array `data`, forzando una petición POST duplicada.

4. **Cabeceras HTTP incompletas:**
   - Faltaban cabeceras requeridas por Azure Application Gateway (`Origin`, `Accept: application/json, text/javascript, */*; q=0.01`).

---

## 🛠️ Solución Implementada

1. **Reutilización del Primer Lote (Zero Redundant Calls):**
   - `handle_response` ahora intercepta y almacena `captured_initial_products` directamente de la respuesta del navegador.
   - Si el navegador ya recibió los primeros 100 productos, `_download_all_catalog_products` los reutiliza y salta directamente a la paginación a partir del registro 100, eliminando la colisión de sesión.
2. **Espera Inteligente:**
   - Ventana de intercepción ajustada a 8 segundos con **salida inmediata** (`break`) apenas se detectan productos o el payload de red.
3. **Resiliencia de Red y Reintentos Automáticos:**
   - Si no se capturaron del navegador y se requiere petición directa:
     - Timeout ampliado de 35s a **60s** para el lote inicial con **3 reintentos automáticos** y backoff.
     - Timeout ampliado a **45s** para lotes paginados con **2 reintentos** por lote.
   - Agregadas cabeceras estándar completas (`Origin`, `Accept`, `X-Requested-With`, `Referer`, `Content-Type`).
4. **Sincronización en los 3 flujos:**
   - Aplicado en `execute_iniciar_precios`, `execute_test_precios` y `execute_extraer_catalogo_json`.

---

## 📁 Archivos Modificados
- [`modulo_subir_pdf/workers.py`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/modulo_subir_pdf/workers.py)
- [`notes/INDEX.md`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/notes/INDEX.md)


# 2026-10-09 — Diagnóstico y Análisis: Módulo Subida de Precios JSON

- **Fecha:** 2026-10-09
- **Tipo:** Diagnóstico / Bug Analysis / UI & Automation
- **Estado:** Análisis Completado
- **Autor:** Antigravity AI

---

## 1. Contexto
El usuario indicó que en el módulo **Subida de Precios JSON** (`view-json`):
1. No existe control para visualizar Chromium en pantalla.
2. Al intentar ejecutar el proceso, falla.
3. Se requiere análisis exhaustivo de por qué falla y cómo implementarlo correctamente.

---

## 2. Causas de Falla Identificadas

### 🔴 A. Ausencia de Controles UI en Frontend (`ui_web/index.html`)
- El inspector de `#view-json` carece de inputs para:
  - Usuario (`jsonUser`) y Contraseña (`jsonPass`).
  - Checkbox "Mostrar navegador en pantalla" (`chkJsonVisible`).
  - Selectores de Acuerdo, Catálogo y Categoría en cascada (`jsonAcuerdo`, `jsonCat`, `jsonCategoria`).
- Actualmente, la función JavaScript `startJsonProcess()` lee los valores prestados del tab de Stock (`chkStockVisible`, `stockUser`, etc.). Si el usuario opera directamente en Precios JSON, las credenciales quedan vacías (`""`) y el login falla de inmediato.

### 🔴 B. Salto de Paso Crítico en la Navegación del Portal (`workers.py`)
- En `execute_iniciar_precios` (L1618-1647):
  - El script presiona `#btnBuscar` y espera la visibilidad de `#btnNuevoProducto` ("Agregar oferta").
  - **Fallo:** NUNCA hace click en `#btnNuevoProducto`. En su lugar, intenta saltar directamente con `page.goto(".../CatalogoProductoIndex")`.
  - En el portal de Perú Compras, si no se hace click físico/DOM en `#btnNuevoProducto`, la sesión no prepara la vista de captura. Como consecuencia, el evento de red `_CatalogoProductoIndexJson` nunca se dispara, la promesa `page.expect_response` expira tras 45s y el worker aborta con:
    `❌ Error: No se pudo capturar el payload de red. Abortando.`

### 🔴 C. IDs de Catálogo Ficticios / Hardcodeados
- En `main_subir_pdf.py` L3539-3542:
  - Intenta consultar `workers._get_id_acuerdo` y `self._app._stock_combos_data` (ambos inexistentes).
  - Como fallback, envía siempre `"249"`, `"252"`, `"11736"`. Si el usuario procesa otro catálogo o categoría, los combos no coinciden y la consulta falla.

### 🔴 D. Inconsistencia en Extracción de JSON del Portal
- El botón "EXTRAER TODOS LOS PRECIOS" invoca `execute_json_extractor`, el cual redirige a `perucompras_core.py` hacia `/MejoraBasica` (sección de Stock) en lugar de `/t_ProductoOfertadoAmp` (sección de Precios de Oferta).

---

## 3. Plan de Solución

1. **Frontend (`ui_web/index.html`):**
   - Incorporar en el panel derecho de `#view-json`:
     - Inputs de Credenciales (`jsonUser`, `jsonPass`).
     - Checkbox `chkJsonVisible` ("Mostrar navegador en pantalla").
     - Dropdowns en cascada (`jsonAcuerdo`, `jsonCat`, `jsonCategoria`).
   - Actualizar `startJsonProcess()` para leer `chkJsonVisible` y sus propios campos.
2. **Backend / Worker (`workers.py` y `main_subir_pdf.py`):**
   - Corregir el flujo en `execute_iniciar_precios`: hacer click real en `#btnNuevoProducto` y esperar el cambio de página/evento de red.
   - Conectar los combos dinámicos a `catalog_options.json` para mapear los IDs correctos.
   - Implementar extracción orientada a `t_ProductoOfertadoAmp`.

# Corrección y Blindaje de Indexación de Stock (Triple Estrategia y Sincronización Web)

- **Fecha:** 2026-11-17
- **Tipo:** Corrección de Bug / Blindaje de Rendimiento
- **Estado:** Resuelto

---

## 1. Diagnóstico del Error
En la ejecución anterior, la consola reportó:
```text
⚡ Indexando catálogo de MejoraBasica en memoria...
⚠️ Modo Clásico por UI activo (fallback)
📦 [1/200] EMU9M65020 (stock=1000, ficha=)
   ⚠ Reintento 1/3: Buscador de la tabla no disponible
   ❌ FALLO: Error inesperado
```

### Causas Raíz Detectadas:
1. **Doble Clic Prematuro en `#btnBuscar`:**
   En `paso3_filtros_stock`, se ejecutaba `btn_buscar.click(force=True)` y seguido `page.evaluate("btn.click()")`. Esto cancelaba o corrompía la petición AJAX del portal.
2. **Falsa Detección de Tabla Lista:**
   `paso3_filtros_stock` esperaba por `#TablaProductos tbody tr`. Dado que DataTables ya renderiza una fila vacía ("Ningún dato disponible en esta tabla") antes de buscar, la espera retornaba en 0.005 segundos, antes de que el servidor enviara los datos reales.
3. **Falta de Espera Activa y Fallback en `extraer_mapa_portal_stock`:**
   Al ejecutarse `extraer_mapa_portal_stock` 0.1s después de presionar buscar, `dt.data().toArray()` estaba vacío. Al no haber reintentos ni consulta directa por endpoint, caía inmediatamente al `Modo Clásico por UI` (fallback lento de 345s).
4. **Desincronización en `dist/PeruComprasBot`:**
   La carpeta compilada `dist/` mantenía versiones antiguas de HTML y scripts.

---

## 2. Solución Aplicada
1. **Espera Activa Real en `paso3_filtros_stock`:**
   - Se eliminó el doble clic sobre `#btnBuscar` (ahora hace exactamente 1 clic seguro).
   - Se implementó un bucle de espera activa (hasta 25s) que valida que `dt.data().length > 0` o que las filas del DOM contengan datos reales (descartando "Ningún dato" o "Cargando").
2. **Triple Estrategia Infalible en `extraer_mapa_portal_stock`:**
   - **Estrategia 1 (RAM):** Extrae directamente desde `window.jQuery('#TablaProductos').DataTable().data().toArray()`.
   - **Estrategia 2 (DOM Activo):** Si DataTables no devuelve array, parsea los elementos `tr` y `td` del DOM.
   - **Estrategia 3 (HTTP Directo):** Si la tabla aún no renderizó por la carga masiva (24,000 filas), realiza un `fetch` directo a `/MejoraBasica/_ListaProductosOfertados` con los parámetros seleccionados y parsea con `DOMParser()`.
   - Bucle de reintentos (hasta 4 intentos con pausas de 1s).
3. **UI Web Optimizada (`ui_web/index.html`):**
   - Botón `🧪 PROBAR 1 PRODUCTO (TEST)` colocado al inicio con color `#005A9C`.
   - Botón `🚀 INICIAR ACTUALIZACIÓN DE STOCK` en azul primario.
   - Sincronización completa de los archivos a la carpeta `dist/PeruComprasBot/` y `dist/PeruComprasBot/_internal/`.

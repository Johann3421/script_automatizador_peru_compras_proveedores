# Implementación de Motor Ultra Rápido de Stock y Botón de Test Unitario

- **Fecha:** 2026-11-16
- **Tipo:** Optimización de Rendimiento / Nueva Funcionalidad
- **Estado:** Completado

---

## 1. Contexto y Objetivo
La actualización de stock en el módulo `stock.py` presentaba una demora crítica de **345 segundos por ficha** debido a que la tabla `TablaProductos` de MejoraBasica contenía 24,137 filas en el DOM, provocando colapsos de CPU con `input[type='search']` y tiempos muertos en 4 modales consecutivos de Bootstrap (`ExistenciasModal`, `_wModal_holder`, `#MensajeModal`). Para 3,000 fichas, esto requería más de 280 horas.

El objetivo fue:
1. Reemplazar la interacción lenta del DOM por un **motor ultra rápido (~0.6s por ficha)** que indexa las 24,137 fichas en memoria RAM de JavaScript (`window.jQuery('#TablaProductos').DataTable().data().toArray()`) en 0.2s, realiza el matching en RAM y despacha un `POST /MejoraBasica/ModificarStock` directo con el token de verificación de sesión.
2. Implementar un **modo test unitario (1 producto)** accesible desde la interfaz gráfica (botón `🧪 PROBAR 1 PRODUCTO (TEST)`), que toma el primer producto del Excel cargado, lo actualiza en el portal, consulta mediante `GET /MejoraBasica/ModificarStock?ID_ProductoOfertado={id}` para verificar la persistencia real en la BD de Perú Compras, y confirma al usuario que puede proceder con el lote completo.

---

## 2. Archivos Modificados
- `modulo_subir_pdf/automation_otro_bot/stock.py`:
  - `paso4_actualizar_stock`: integra detección automática del motor rápido vía `extraer_mapa_portal_stock` y fallback al método clásico si no estuviera disponible la tabla.
  - `test_actualizar_un_producto`: función unitaria que procesa 1 producto, cronometra la petición HTTP (~0.6s), consulta la verificación GET y emite logs detallados.
- `modulo_subir_pdf/workers.py`:
  - `execute_test_stock`: worker en hilo secundario que maneja el ciclo de vida del test (navegador, login, navegación, filtros, test y reporte en consola sin afectar el Excel completo).
- `modulo_subir_pdf/main_subir_pdf.py`:
  - `btn_stock_test`: botón agregado en la interfaz CTk de escritorio.
  - `_on_stock_test_start` y `_execute_stock_test`: handlers de inicio y delegación.
  - `SubirPdfWebApi.start_stock_test`: endpoint API expuesto para la interfaz web.
  - Actualización de `_methods_to_bind` y widgets dummy.
- `ui_web/index.html`:
  - Botón `🧪 PROBAR 1 PRODUCTO (TEST)` añadido con estilo `#005A9C`.
  - Función JavaScript `startStockTest()` conectada con `pywebview.api.start_stock_test`.

---

## 3. Decisiones de Arquitectura
- **Ley de Tesler:** Toda la complejidad de indexación en RAM de 24,000 registros, resolución de IDs del portal y verificación de base de datos se mantiene en el backend. En el frontend, el usuario solo ve un botón claro: `🧪 PROBAR 1 PRODUCTO (TEST)`.
- **Verificación Bidireccional:** El test no solo asume que el POST fue exitoso por recibir HTTP 200, sino que realiza una consulta GET al modal para comprobar que el campo `N_StockAnt` en la base de datos de Perú Compras refleja el valor recién subido.
- **Transición Transparente:** Si el usuario aprueba el test, el botón `INICIAR ACTUALIZACIÓN DE STOCK` utiliza exactamente el mismo motor rápido para procesar las 3,000 fichas a un ritmo de ~0.6s por ficha.

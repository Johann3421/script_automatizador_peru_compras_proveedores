# Documentación del Problema: Extracción Completa de Productos en t_ProductoOfertadoAmp

Este documento detalla el flujo técnico, las restricciones del servidor de Perú Compras, y los intentos realizados para extraer el listado completo de productos (más de 50 registros, ej. 2592 o 5000) desde la página de visualización de la tabla.

---

## 1. Contexto del Flujo

1. El bot inicia sesión (`AccesoGeneral`) superando el CAPTCHA.
2. Navega a `t_ProductoOfertadoAmp`.
3. Selecciona Acuerdo Marco, Catálogo y Categoría en los dropdowns dinámicos.
4. Hace click en `Iniciar Búsqueda` (`#btnBuscar`).
5. Espera al botón "Agregar Oferta" (`#btnNuevoProducto`) y navega a:
   `https://www.catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp/CatalogoProductoIndex`
6. En esta última página se carga una tabla paginada con los productos.

---

## 2. El Desafío de la Paginación

La tabla utiliza **DataTables** y realiza peticiones POST asíncronas (AJAX) al endpoint:
`POST https://www.catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp/_CatalogoProductoIndexJson`

### Restricciones del Servidor
- **Seguridad (Anti-CSRF):** No se pueden hacer peticiones `fetch` directas desde JavaScript/Python a este endpoint debido a que el servidor de ASP.NET MVC requiere cabeceras y cookies de validación específicos (`__RequestVerificationToken`). Hacerlo directamente provoca respuestas con código HTML de error `403` o redirecciones.
- **Paginación Servidor:** El servidor devuelve por defecto lotes de **50 registros**. El payload del POST interceptado sigue este formato:
  ```
  draw=1
  start=0
  length=50
  columns[0][data]=C_Imagen
  ...
  ```
- **Límite de Tamaño (`length`):** Intentar cambiar el `length` de DataTables a `1000` o `500` mediante la API de DataTables (`tables.page.len(1000).draw()`) hace que el servidor retorne únicamente 50 registros (probablemente por una restricción o tope estricto en la lógica de control del backend de la entidad). Al retornar 50 cuando el cliente pidió 1000, DataTables asume que no existen más registros y deshabilita la paginación interna (detectando `info.pages = 1`).

---

## 3. Intentos de Solución y Resultados

### Intento A: Fetch Directo desde Consola
Se intentó emular la petición usando `fetch()` inyectando los parámetros en el cuerpo del mensaje POST.
- **Resultado:** Fallido. El servidor responde con error `403` por falta de tokens de seguridad (CSRF).

### Intento B: Manipulación del API de DataTables
Se ejecutó código en la consola del navegador usando Playwright (`page.evaluate`) para alterar el tamaño de página y avanzar a través de la API oficial de DataTables:
```javascript
const tables = $.fn.dataTable.tables({visible: true, api: true});
tables.page.len(100).draw(); // Cambiar a 100
tables.page('next').draw('page'); // Ir al siguiente
```
- **Resultado:** Inconsistente. Aunque `total_records` reporta el número real (ej. `2592`), las llamadas de API de DataTables no logran realizar la transición de página en este entorno o el backend ignora el cambio de `length`, limitando la lectura a la primera página de 50 ítems.

---

## 4. Solución Propuesta (Para Implementar)

En lugar de utilizar la API interna de DataTables mediante JavaScript (`$.fn.dataTable`), la forma más confiable para un navegador automatizado es **interactuar directamente con los elementos visuales del DOM**:

1. **Ajuste del Selector del Botón "Siguiente":** Localizar el botón físico "Siguiente" usando clases estándar de Bootstrap/DataTables:
   - Selector probable: `li.next a`, `a.paginate_button.next` o `#tabla_next` (o similar en el contenedor de paginación).
2. **Loop de Clics Físicos:**
   - Hacer click en el botón "Siguiente" usando Playwright: `page.click('a.next')`.
   - Esperar a que la petición de red termine (Playwright `page.wait_for_response` o una espera corta de red).
   - El interceptor de respuestas acumulará los registros automáticamente conforme cambian las páginas en pantalla.
3. **Criterio de Parada:** Continuar hasta que el botón "Siguiente" tenga la clase `disabled` (o ya no esté presente en el DOM).

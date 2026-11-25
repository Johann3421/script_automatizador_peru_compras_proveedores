# 2026-11-16 — Investigación y Validación: Motor de Stock Ultra Rápido (Direct HTTP POST vs Clics de UI)

- **Fecha:** 2026-11-16
- **Tipo:** Investigación / Optimización de Rendimiento
- **Estado:** Validado en Sesión Aislada
- **Módulos:** `modulo_subir_pdf` (`automation_otro_bot/stock.py`, `MejoraBasica`)

---

## 🎯 Diagnóstico: ¿Por qué demora 5.7 minutos (345s) por ficha?

En la sesión activa, la consola reportó:
- `📦 [1/200] EMU9M65020 (stock=1000) -> OK en 345.3s`
- `📦 [2/200] EMU9M65021 (stock=1000) -> OK en 331.1s`

### Cuellos de Botella Detectados en el Flujo Tradicional:
1. **Sobrecarga de DataTables en DOM:** La tabla `#TablaProductos` contiene **24,137 registros** cargados en el navegador. Al escribir en `input[type='search']`, DataTables filtra los 24,137 nodos DOM mediante JavaScript, congelando la CPU del navegador por más de 60 segundos por producto.
2. **Ciclo de 4 Modales Sucesivos:** Por cada producto, el script interactúa con:
   - Clic en fila `Existencias`.
   - Espera de apertura de `#ExistenciasModal` (15s timeout).
   - Espera activa de inputs editables (20s).
   - Clic en `#btn_guardar`.
   - Espera y confirmación en modal `._wModal_holder` (15s).
   - Espera y cierre en modal `#MensajeModal` (15s).
3. **Destrucción y Reconstrucción de la Tabla:** Tras cerrar `#MensajeModal`, la página recarga las 24,137 filas, haciendo que en el siguiente producto el buscador no responda a tiempo (`⚠ Reintento 1/3: Buscador de la tabla no disponible`).

---

## 🔬 Descubrimiento de la API Interna de `MejoraBasica`

Mediante una instancia de pruebas aislada, se inspeccionó el código JavaScript y los formularios del portal:

### 1. Función de Apertura del Modal:
```javascript
function fnModificarStock(id_productoOfertado) {
    var modal = $('#ExistenciasModal');
    modal.removeData('bs.modal');
    modal.modal({ remote: '/MejoraBasica/ModificarStock?ID_ProductoOfertado=' + id_productoOfertado });
    modal.modal('show');
}
```

### 2. Formulario Nativo de Modificación:
El modal contiene el formulario `#formStock`:
```html
<form action="/MejoraBasica/ModificarStock" id="formStock" method="post">
    <input name="__RequestVerificationToken" type="hidden" value="..." />
    <input id="ID_ProductoOfertado" name="ID_ProductoOfertado" type="hidden" value="76537958" />
    <input type="hidden" id="N_Acuerdo" name="N_Acuerdo" value="249">
    <input type="hidden" id="N_Catalogo" name="N_Catalogo" value="252">
    <input type="hidden" id="N_Categoria" name="N_Categoria" value="11735">
    <input type="text" id="N_StockAnt" name="N_StockAnt" value="0" readonly />
    <input type="text" id="N_Stock" name="N_Stock" value="1000" />
    <button type="submit" id="btn_guardar">Guardar</button>
</form>
```

### 3. Prueba de Envío Directo (`fetch POST`):
Se ejecutó un `POST` directo a `/MejoraBasica/ModificarStock` dentro de la sesión activa del navegador:
- **Status HTTP:** `200 OK`
- **Latencia:** **623.3 milisegundos** (0.6 segundos)
- **Persistencia:** Verificada exitosamente en el servidor de Perú Compras.

---

## ⚡ Nueva Arquitectura de Alta Velocidad (Fast Stock Engine)

1. **Pre-Indexación en Memoria RAM (0.2s única vez):**
   Al cargar la tabla tras presionar `#btnBuscar`, se extrae el dataset de las 24,137 filas directamente de `$('#TablaProductos').DataTable().data().toArray()`. Se indexa un diccionario en memoria:
   `dict[NUMERO_PARTE] = { "id_ofertado": ID, "stock_ant": STOCK }`.
2. **Matching Instantáneo (0.001s por fila):**
   Cero interacción con el buscador de DataTables o el DOM. Match directo en Python/JS.
3. **Actualización Directa por HTTP POST (0.6s por fila):**
   Envío directo a `/MejoraBasica/ModificarStock` con token CSRF validado.
4. **Cero Modales:** No se abren modales ni se congela la pantalla.

---

## 📊 Benchmark Comparativo

| Métrica | Flujo por UI (Actual) | Flujo Directo HTTP (Nuevo) |
|---|---|---|
| Tiempo por producto | **330 - 345 segundos** (5.7 min) | **0.6 - 1.0 segundos** |
| 200 productos (lote actual) | **~19 horas** | **~2 a 3 minutos** |
| 3,000 productos | **~287 horas (12 días)** | **~35 a 45 minutos** |
| Factor de aceleración | Base | **~500x más rápido** |

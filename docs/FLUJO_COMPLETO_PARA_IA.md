# FLUJO COMPLETO: Peru Compras Bot — Automatización de Subida de Precios

## 1. PROPÓSITO DEL BOT

Toma un archivo **Excel** con una lista de productos (N° de Parte + Precio), navega al sistema de **Peru Compras - Catálogo Electrónico**, busca cada producto por su N° de Parte, llena el precio en el campo correspondiente, y finalmente envía todas las ofertas agrupadas. El resultado se escribe de vuelta al Excel coloreando cada fila según su estado (verde=OK, rojo=excede rango, azul=inferior, amarillo=no encontrado).

---

## 2. ARQUITECTURA GENERAL

```
main.py (UI customtkinter)
  ├── CaptchaBridge     → comunicación UI ↔ hilo (CAPTCHA manual)
  ├── CatalogBridge     → comunicación UI ↔ hilo (selector catálogo)
  └── Thread worker ───→ _execute()
                           ├── init_browser()       → Playwright + Chromium
                           ├── do_login()           → login + CAPTCHA OCR
                           ├── setup_catalog_search() → filtros catálogo
                           └── run_offer_loop()     → el núcleo: 1x1 por fila
```

**Tecnologías:** Python 3.13, Playwright, customtkinter, openpyxl, pytesseract, Pillow.

**Archivos clave:**
| Archivo | Rol |
|---|---|
| `main.py` | UI, bridges, orquestación del hilo worker |
| `automation/browser.py` | Inicialización de Chromium, resolución de rutas Playwright |
| `automation/login.py` | Login en Peru Compras + OCR de CAPTCHA (6 chars alfanuméricos) |
| `automation/navigation.py` | Navegación, selección de catálogo en cascada (Acuerdo→Catálogo→Categoría) |
| `automation/offer_loop.py` | **Bucle principal de subida de precios (1x1)** |
| `utils/excel_parser.py` | Lectura de Excel, detección de header row, parsing a list[dict] |
| `utils/excel_writer.py` | Coloreado del Excel de salida según estado |
| `utils/logger.py` | Logger thread-safe vía queue.Queue |
| `extract_catalog.py` | Script independiente para extraer opciones de catálogo a JSON |
| `catalog_options.json` | Cache de opciones de catálogo (Acuerdo→Catálogo→Categoría) |

---

## 3. EL FLUJO COMPLETO PASO A PASO

### 3.1. Interfaz de Usuario

El usuario:
1. Ingresa credenciales (usuario + contraseña, precargadas por defecto)
2. Selecciona archivo Excel (`.xlsx`)
3. Elige pestaña (sheet) — se auto-detectan las columnas
4. Mapea columna de "N° de Parte" y columna de "Precio" (auto-detectadas por nombre)
5. Selecciona Acuerdo Marco → Catálogo → Categoría (cargados desde `catalog_options.json`)
6. Opcional: marca "Mostrar navegador en pantalla" (headless mode)
7. Click **"Iniciar Procesamiento"**

### 3.2. Lanzamiento (`_on_launch` en `main.py:500`)

```python
pre_selected = {
    "acuerdo": valor_del_combo,   # ej: "249"
    "catalogo": valor_del_combo,  # ej: "251"
    "categoria": valor_del_combo, # ej: "11737"
}
```

Se crea un **thread daemon** que ejecuta `_execute()` con:
- `creds`: usuario, password, captcha_key, headless
- `excel_data`: rows (list[dict]), parte_col, precio_col, path, sheet
- `pre_selected`: valores de catálogo elegidos en UI

### 3.3. Ejecución del Worker (`_execute` en `main.py:560`)

```
1. init_browser(headless)
   → Lanza Chromium vía Playwright
   → Configura timeout global 120s

2. do_login(usuario, password, captcha_key, log, stop_event, captcha_bridge)
   → Navega a AccesoGeneral
   → Hasta 5 reintentos
   → Por intento:
       a. Rellena usuario/password
       b. Resuelve CAPTCHA:
          - Primero: OCR con pytesseract (múltiples umbrales + votación)
          - Si OCR falla tras 4 intentos: pide captcha manual vía CaptchaBridge (UI)
       c. Click "#btnLogin"
       d. Espera networkidle
       e. Verifica que URL cambió (no sigue en /AccesoGeneral)
       f. Si está en ValidarAcceso: hace go_back()
   → Navega a t_ProductoOfertadoAmp

3. setup_catalog_search(pre_selected)
   → Si ya está en t_ProductoOfertadoAmp: ok
   → Si no: navega con _retry_goto (hasta 4 intentos, timeout exponencial)
   → Elimina modales del DOM
   → Acuerdo Marco:
       - Usa pre_selected["acuerdo"] o pide al usuario vía CatalogBridge
       - _select2_choose(page, "ajaxAcuerdo", value)
       - _wait_for_options("ajaxCatalogo") → sondea cada 500ms hasta 25s
   → Catálogo:
       - Usa pre_selected["catalogo"] o pide al usuario
       - Valida que el valor exista entre las opciones cargadas
       - _select_native(page, "ajaxCatalogo", value)
       - _wait_for_options("ajaxCategoria")
   → Categoría:
       - Usa pre_selected["categoria"] o pide al usuario
       - Valida que el valor exista entre las opciones cargadas
       - _select_native(page, "ajaxCategoria", value)
   → Click "#btnBuscar" (con wait_for_selector timeout 10s)
   → Espera networkidle 60s
   → Espera "#btnNuevoProducto" hasta 30s, click
   → Espera networkidle 60s
   → Verifica URL contiene "CatalogoProductoIndex"
   → Retorna dict con acuerdo/catalogo/categoria

4. run_offer_loop(rows, parte_col, precio_col, ...) → [results]
   → VER DETALLE EN SECCIÓN 4
   → Retorna list[dict] con estado de cada fila

5. write_results(excel_path, sheet, results)
   → Carga el Excel original
   → Colorea cada fila según status: GREEN/YELLOW/RED/BLUE
   → Guarda como "nombre_procesado_YYYYMMDD_HHMMSS.xlsx"
```

### 3.4. CAPTCHA OCR (`_solve_captcha` en `login.py`)

El CAPTCHA de Peru Compras tiene **6 caracteres alfanuméricos en mayúsculas**.

Estrategia OCR:
- Escalar imagen 4x con LANCZOS
- Convertir a escala de grises
- Aplicar 7 estrategias de umbralización (thresholds 140/120/100/80, contraste, invertido, raw)
- Para cada estrategia, aplicar 3 configuraciones de Tesseract (PSM 7, 8, 13)
- Whitelist: solo A-Z + 0-9
- **Votación ponderada**: cada resultado de 6 chars = 1 voto, 4-5 chars = 0.5 voto
- Retorna el más votado

Si OCR falla tras 4 intentos → solicita CAPTCHA manual vía `CaptchaBridge` (aparece panel en UI).

---

## 4. EL NÚCLEO: `run_offer_loop` — PROCESAMIENTO 1x1 (offer_loop.py)

### 4.1. Flujo por cada fila del Excel

```
POR CADA FILA i EN rows:
  │
  ├── ¿Sesión expirada? (URL contiene "AccesoGeneral")
  │   → Re-autenticar (login + setup_catalog_search)
  │
  ├── Extraer parte_val de row[parte_col], precio_val de row[precio_col]
  │
  ├── 1. BUSCAR PRODUCTO
  │   input#C_Descripcion → click → fill(parte_val)
  │
  ├── 2. CLICK "Buscar"
  │   #btnBuscar.click() → wait networkidle 90s
  │
  ├── 3. ESPERAR DATATABLES
  │   Sonda .dataTables_processing hasta 75s (30 ciclos × 2.5s)
  │
  ├── 4. VERIFICAR "NO ENCONTRADO"
  │   Busca .dataTables_empty o td:"No se encontraron"
  │   Si encontrado → marca "no_encontrado", CONTINUE
  │
  ├── 5. ENCONTRAR INPUT DE PRECIO (con reintentos)
  │   Hasta 5 intentos:
  │   - Busca input.cls_txtMonto
  │   - Si visible → click, guardar referencia
  │   - Si no: espera 2s, reintenta
  │   - Si reaparece dataTables_empty → marca not_found
  │
  ├── 6. LLENAR PRECIO
  │   price_input.fill(precio_val)
  │
  ├── 7. VALIDACIÓN (Tab)
  │   page.keyboard.press("Tab")
  │   Espera 2.5s
  │   _dismiss_price_modal():
  │     - ¿Apareció #MensajeModal2?
  │     - Si sí: extrae texto de #Msg, descarta modal
  │     - Clasifica: "excede"/"supera" → ROJO
  │                  "inferior"/"menor"/"minimo" → AZUL
  │                  >50000 → ROJO, <5 → AZUL, else → fuera_rango
  │     - Limpia el input de precio
  │   Si NO modal → OK
  │
  ├── 8. ENVIAR LOTE CADA 50
  │   batch_ok ≥ 50 → _submit_offer():
  │     - click #btn_enviarOferta2
  │     - wait networkidle 90s
  │     - _dismiss_confirm_modal() → cierra modal post-envío
  │     - Re-ejecuta setup_catalog_search() (vuelve al listado)
  │   → batch_ok = 0
  │
  └── sleep(1.5)

AL FINALIZAR:
  Si batch_ok > 0 → _submit_offer() (envía pendientes)
  log.done(ok_count, error_count)
```

### 4.2. Tiempos típicos por fila

| Paso | Tiempo |
|---|---|
| Buscar producto (fill + click) | ~1-2s |
| Esperar DataTable processing | ~3-30s (puede ser >60s en días de cierre) |
| Encontrar input precio (reintentos) | ~0-12s |
| Llenar precio + Tab + validación | ~4s |
| Sleep entre filas | 1.5s |
| **Total por fila (promedio)** | **~10-50s** |

Para 200 filas: **~30-180 minutos** (sin contar lotes).

### 4.3. Envío de lote (`_submit_offer`)

Cada 50 ofertas OK se hace clic en `#btn_enviarOferta2`. Esto:
1. Envía un request HTTP (probablemente POST con JSON) al servidor con todas las ofertas pendientes
2. Muestra un modal de confirmación
3. Se cierra el modal con `_dismiss_confirm_modal()` (múltiples estrategias: JS nativo + click en botones + limpieza DOM)
4. Se vuelve al catálogo vía `setup_catalog_search()` para seguir procesando

**Este es el punto crítico**: el botón `#btn_enviarOferta2` probablemente dispara un **fetch/XHR con payload JSON** que contiene todos los precios ingresados. Si interceptamos ese request, sabríamos el formato exacto.

---

## 5. ESTRUCTURA DEL SITIO WEB PERU COMPRAS

### URLs relevantes
```
https://www.catalogos.perucompras.gob.pe/
  ├── /AccesoGeneral                      → Login
  ├── /t_ProductoOfertadoAmp              → Búsqueda en catálogo
  └── /t_ProductoOfertadoAmp/CatalogoProductoIndex  → Listado de productos + precios
```

### Elementos DOM clave en CatalogoProductoIndex

```html
<!-- Búsqueda -->
<input id="C_Descripcion" ...>            <!-- N° de Parte -->

<!-- Botones -->
<button id="btnBuscar">Buscar</button>
<button id="btnNuevoProducto">Agregar oferta</button>
<button id="btn_enviarOferta2">Enviar oferta</button>

<!-- Tabla de resultados (DataTables) -->
<table id="tablaProductos" ...>
  <tr>
    <td>N° Parte</td>
    <td>Descripción</td>
    <td><input class="cls_txtMonto" ...></td>  <!-- ← input de precio -->
  </tr>
  ...
</table>
<div class="dataTables_processing">Procesando...</div>
<div class="dataTables_empty">No se encontraron registros</div>

<!-- Modales -->
<div id="MensajeModal2">                  <!-- Validación de precio -->
  <span id="Msg">El precio ingresado excede...</span>
</div>
<div id="_wModal">                        <!-- Confirmación de envío -->
  <button class="_wModal_btn_ok">Aceptar</button>
</div>
```

### Mecanismo de cascada de catálogo

El formulario de búsqueda usa:
- **`#ajaxAcuerdo`**: Select2 (dropdown con búsqueda). Al cambiar, dispara AJAX que carga opciones en `#ajaxCatalogo`.
- **`#ajaxCatalogo`**: `<select>` nativo. Al cambiar, dispara AJAX que carga opciones en `#ajaxCategoria`.
- **`#ajaxCategoria`**: `<select>` nativo.

Los valores se envía como parámetros GET/POST al backend al hacer clic en "Iniciar Búsqueda".

---

## 6. OPORTUNIDAD: SUBIDA MASIVA VÍA JSON (NO 1x1)

### 6.1. El problema actual

El flujo 1x1 es **extremadamente lento** porque por cada producto:
1. Navega a la página de búsqueda (o ya está allí)
2. Busca el producto
3. Espera DataTables
4. Localiza el input de precio entre reintentos
5. Llena el precio
6. Presiona Tab y espera validación
7. Repite

Para 500 productos, puede tomar **4-8 horas**.

### 6.2. La oportunidad

El botón **`#btn_enviarOferta2`** envía un request HTTP (probablemente POST) con un **payload JSON** que contiene los precios ingresados. En lugar de:

1. Llenar inputs 1x1 con Playwright
2. Hacer click en Enviar cada 50

Podríamos:

1. **Hacer login** con Playwright (necesario por CAPTCHA)
2. Obtener cookies/session token
3. **Hacer llamadas HTTP directas** (requests, httpx) para:
   - Buscar productos y obtener sus IDs internos
   - Enviar todos los precios en una sola llamada JSON

### 6.3. Lo que necesitamos descubrir

1. **Formato del JSON**: cuando se hace click en `#btn_enviarOferta2`, ¿qué payload se envía? Necesitamos interceptar el request con Playwright (usando `page.route()` o escuchando `request` events) o con herramientas de desarrollo (Chrome DevTools → Network → XHR).

2. **IDs internos**: el sistema probablemente asigna un ID interno a cada producto dentro del catálogo. ¿Cómo se obtiene? Probablemente está en las celdas de la tabla o en atributos `data-*` del `<tr>`.

3. **Tokens CSRF / ANTIFORGERY**: el sitio puede tener tokens de seguridad que rotan. ¿Dónde se obtienen? ¿En el HTML o en cookies?

4. **Endpoint de precio**: ¿cuál es la URL exacta del endpoint que recibe los precios? ¿`/GuardarPrecios`, `/ActualizarOferta`, `/EnviarOferta`?

### 6.4. Plan de acción sugerido

**Fase 1 — Descubrimiento:**
1. Usar Playwright para navegar normalmente, pero habilitar `page.on("request")` y `page.on("response")` para loguear TODOS los requests XHR
2. Especial atención al request que se dispara al hacer click en `#btn_enviarOferta2`
3. Guardar el payload completo (request body) y los headers, especialmente `Content-Type`, cookies, tokens
4. Identificar el endpoint que recibe la oferta

**Fase 2 — Prototipo:**
1. Extraer la session cookie de Playwright
2. Hacer una petición HTTP directa replicando el request de `#btn_enviarOferta2`
3. Verificar que el servidor lo acepta

**Fase 3 — Refactor:**
1. Reemplazar `run_offer_loop()` por:
   - Una llamada que primero obtiene IDs de productos (quizás vía búsqueda)
   - Una segunda llamada que envía todos los precios en un solo JSON
2. Mantener el login y CAPTCHA con Playwright (es la parte más compleja de reemplazar)
3. Mantener la UI y bridges igual

### 6.5. Consideraciones técnicas

- **Session management**: Playwright mantiene cookies automáticamente. Si usamos requests HTTP directas, debemos extraer las cookies del contexto de Playwright (`page.context.cookies()`) y pasarlas manualmente.
- **Playwright no bloqueante**: podemos usar `page.evaluate()` para ejecutar JS arbitrario que haga fetch directo al backend. Esto evita tener que manejar cookies manualmente.
- **Velocidad potencial**: una llamada HTTP directa toma ~100-500ms vs ~10-50s por producto con Playwright. Para 500 productos: **~1-2 minutos vs 4-8 horas**.

---

## 7. RESUMEN TÉCNICO PARA OTRA IA

```
STACK:
  Python 3.13 + Playwright + customtkinter + openpyxl + pytesseract

SITIO:
  https://www.catalogos.perucompras.gob.pe
  Login con CAPTCHA (6 chars, OCR vía pytesseract con votación multi-estrategia)
  Catálogo en cascada: Select2 (acuerdo) → <select> (catálogo) → <select> (categoría)

FLUJO ACTUAL (lento):
  Excel → login → setup_catalog_search → [buscar producto → llenar precio → validar] × N → enviar lote cada 50

OPORTUNIDAD (rápido):
  Excel → login → extraer session → llamadas HTTP directas con JSON → enviar todo en 1 request

LO QUE FALTA DESCUBRIR:
  - Endpoint de precios y formato JSON del payload
  - IDs internos de productos en la tabla
  - Tokens CSRF si existen
  - Ruta exacta del request de #btn_enviarOferta2

HERRAMIENTA SUGERIDA:
  page.on("request", handler) en Playwright para interceptar y loguear
  el request de envío de ofertas.

ARCHIVOS A MODIFICAR:
  - automation/offer_loop.py (reemplazar el loop 1x1)
  - automation/navigation.py (quizás agregar funciones HTTP directas)
  - automation/api_client.py (NUEVO: cliente HTTP con session cookies)
```

---

## 8. FLUJO DE DATOS: EXCEL → RESULTS

```
Excel (.xlsx)
  │
  ├── get_sheets() → [nombre_sheets]
  ├── get_columns() → [nombre_columnas]
  └── parse_excel() → [{"Col1": val1, "Col2": val2}, ...]
                        ↑ list[dict], una por fila
  │
  ├── parte_col (ej: "CÓDIGO ÚNICO")
  └── precio_col (ej: "PRECIO DE LISTA")
        │
        ▼
  run_offer_loop() devuelve:
  [
    {"index": 0, "status": "ok", "parte": "ABC123", "precio": "150.00"},
    {"index": 1, "status": "no_encontrado", "parte": "XYZ789", "precio": "200.00"},
    {"index": 2, "status": "excede", ...},
    ...
  ]
        │
        ▼
  write_results() → "original_procesado_20260609_123456.xlsx"
    Colorea cada fila según status:
      ok            → VERDE  (#C6EFCE)
      no_encontrado → AMARILLO (#FFEB9C)
      sin_part_number→ AMARILLO
      excede        → ROJO   (#FFC7CE)
      inferior      → AZUL   (#BDD7EE)
      error         → AMARILLO
```

## 9. UBICACIÓN DE ARCHIVOS

```
D:\SISTEMAS 02\Desktop\Proyectos_generales\script_automatizador_peru_comproveedores\
├── main.py                    → Entry point + UI
├── build_installer.py          → Compila .exe con PyInstaller
├── install_perucombras.py      → Instalador (descarga dependencias)
├── extract_catalog.py          → Extrae opciones de catálogo a JSON
├── catalog_options.json        → Cache de opciones de catálogo
├── requirements.txt            → Dependencias Python
├── automation/
│   ├── browser.py             → Chromium + Playwright init
│   ├── login.py               → Login + OCR CAPTCHA
│   ├── navigation.py          → Catálogo + navegación
│   └── offer_loop.py          → ★ Bucle de subida de precios
├── utils/
│   ├── logger.py              → Log thread-safe
│   ├── excel_parser.py        → Lectura de Excel
│   └── excel_writer.py        → Coloreado de Excel
├── dist/
│   └── Instalar_PeruComprasBot_v10.1.exe  → Último build
└── docs/
    └── FLUJO_COMPLETO_PARA_IA.md  → ★ Este documento
```

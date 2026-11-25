# 2026-11-16 — Corrección de Extracción de Stock (stock=0) y Detención Inmediata de Proceso

- **Fecha:** 2026-11-16
- **Tipo:** Bugfix & Resiliencia
- **Estado:** Implementado y Verificado
- **Módulos:** `modulo_subir_pdf` (`main_subir_pdf.py`, `workers.py`, `automation_otro_bot/stock.py`)

---

## 🎯 Contexto del Problema

El usuario reportó dos fallas críticas en el módulo de actualización de stock:
1. **Stock en 0 persistente:** A pesar de que el Excel contenía cantidades válidas, el sistema procesaba `stock=0` en cada producto (`📦 [1/200] EMU9M65020 (stock=0, ficha=)`).
2. **Botón Detener inoperante:** Al presionar "Detener", la UI mostraba `⏹ Detención solicitada`, pero el hilo continuaba ejecutando reintentos (1/3, 2/3, 3/3) y bloqueando la interfaz.

---

## 🔍 Causas Raíz Identificadas

1. **Crash silencioso por `.iterrows()` en `select_stock_file`:**
   - En `main_subir_pdf.py`, al cargar el archivo de stock, `analizar_excel_stock` devolvía `res["df"]` como una `list` de diccionarios.
   - El código ejecutaba `for _, r in df.iterrows():`, lanzando un `AttributeError: 'list' object has no attribute 'iterrows'`.
   - El `except Exception:` capturaba el error y llamaba a `parse_excel(path, first, parte_col=...)` (el parser de ofertas PDF), el cual **no extrae columnas de stock**.
   - `self._app._stock_excel_df` quedaba guardado con filas sin campo `Stock`, por lo que `paso4_actualizar_stock` recurría al valor por defecto: `0`.

2. **Falso positivo en detección de columna 'id' vs 'cantidad':**
   - El alias de búsqueda `"id"` para ficha coincidía como subcadena dentro de la palabra `"cant-id-ad"`, asignando incorrectamente la columna de cantidad a la columna de ficha técnica.

3. **Desconexión de `STOP_EVENT` entre módulos de Python:**
   - En `workers.py`, `from automation_otro_bot.stock import STOP_EVENT; STOP_EVENT = app._stock_stop_event` creaba una variable local en `workers.py` sin mutar el `STOP_EVENT` dentro de `automation_otro_bot.stock`.
   - `paso4_actualizar_stock` no recibía `stop_event` en su firma, por lo que dentro de `stock.py`, `STOP_EVENT` permanecía como `None`.
   - Las condiciones `if STOP_EVENT and STOP_EVENT.is_set():` nunca se cumplían durante los reintentos.

---

## 🛠️ Soluciones Implementadas

1. **Manejo Correcto de Estructuras en `select_stock_file` (`main_subir_pdf.py`):**
   - Se itera `df_data` directamente como lista de diccionarios (`for r in df_data:`), extrayendo `Parte`, `Stock` y `Ficha`.
   - Se implementó `_parse_stock_excel_fallback` exclusivo para stock (usando `openpyxl`), garantizando que jamás se recurra al parser de PDFs ni se pierda la columna de stock.

2. **Detección Flexible y Robusta de Columnas (`stock.py` y `main_subir_pdf.py`):**
   - Nueva función `_match_alias` con validación de límites de palabra para alias cortos (ej. `"id"`, `"pn"`, `"cod"`), eliminando falsos positivos en palabras compuestas como `"cantidad"`.
   - Soporte amplio para sinónimos: `["stock", "cant", "cantidad", "unidades", "existencias", "disponible", "inventario", "total"]`.

3. **Propagación Real del `STOP_EVENT` y Cancelación Inmediata:**
   - En `workers.py`: se asigna explícitamente `stock_mod.STOP_EVENT = app._stock_stop_event` y se inyecta `stop_event=app._stock_stop_event` como parámetro a `paso4_actualizar_stock`.
   - En `stock.py`: `paso4_actualizar_stock` utiliza `current_stop = stop_event or STOP_EVENT`. En cada reintento, ante `current_stop.is_set()` o mensaje `"Detenido por usuario"`, rompe el bucle de inmediato sin esperar timeouts.
   - En `_browser_cerrado()`: se agregaron patrones de detención explícita (`"detenido por usuario"`, `"detención solicitada"`).
   - En `stop_stock_process`: activa el evento de parada y cierra forzosamente el navegador Playwright para liberar bloqueos síncronos de red.

---

## 📁 Archivos Modificados
- [`modulo_subir_pdf/automation_otro_bot/stock.py`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/modulo_subir_pdf/automation_otro_bot/stock.py)
- [`modulo_subir_pdf/main_subir_pdf.py`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/modulo_subir_pdf/main_subir_pdf.py)
- [`modulo_subir_pdf/workers.py`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/modulo_subir_pdf/workers.py)
- [`notes/INDEX.md`](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/notes/INDEX.md)

# 2026-10-09 — Subida de Precios por Excel con Matching Exacto por Número de Parte

- **Fecha:** 2026-10-09
- **Tipo:** Feature / Mejora de Precisión
- **Estado:** Completado y Verificado
- **Módulo:** `modulo_subir_pdf` (Subida de Precios Excel / JSON)

---

## 🎯 Contexto y Objetivo
El usuario solicitó habilitar la carga de precios mediante hojas de cálculo Excel (`.xlsx`) a través de una plantilla estándar (`plantilla_precios.xlsx`), permitiendo ingresar directamente el número de parte y el precio a ofertar.
Requisito crítico: **Matching 100% exacto por número de parte**, sin tolerar coincidencias parciales, sub-cadenas ambiguas ni falsos positivos con otros modelos del catálogo.

---

## 🛠️ Cambios Implementados

### 1. Interfaz de Usuario Web (`ui_web/index.html`)
- Renombrado el encabezado a `Subida de Precios (EXCEL / JSON)`.
- Añadido botón `📋 PLANTILLA EXCEL` para generar y descargar la plantilla oficial con un clic.
- Actualizada la función `selectJsonFile()` para admitir filtros `.xlsx`, `.xls` y `.json`, detectando las filas y actualizando el badge y la grilla con los precios cargados.
- Adaptada la visualización en tabla (`renderJsonTable`) para renderizar directamente precios ingresados por Excel.

### 2. Backend Bridge (`modulo_subir_pdf/main_subir_pdf.py`)
- Implementada la función `_parse_precios_excel(path)`:
  - Detección inteligente de cabeceras (`Numero_Parte`, `Parte`, `Precio`, `Monto`, `Descripcion`) o fallback posicional.
  - Conversión segura y saneamiento de precios numéricos.
- Implementada `download_precios_template()`:
  - Generación de libro Excel institucional con cabecera `Numero_Parte`, `Precio`, `Descripcion` estilizada en azul corporativo y filas de ejemplo.
- Actualizada `select_json_file()` en el API bridge para procesar de forma unificada tanto `.json` como `.xlsx`.

### 3. Algoritmo de Matching Exacto (`modulo_subir_pdf/workers.py`)
- Implementado `_buscar_match_exacto(rec_local, all_products)`:
  - Búsqueda estricta por token delimitado con regex `(?<![A-Za-z0-9])` + `(?![A-Za-z0-9])`.
  - Coincidencia exacta con `N_CatalogoProducto`.
  - Eliminación del fuzzy matching / substring que provocaba falsos positivos entre modelos con prefijos comunes.
- Modificado `execute_iniciar_precios()`:
  - Priorización de precio numérico directo ingresado (`Precio` / `precio` / `N_PrecioOfertado`).
  - Fallback a fórmula histórica de ganancia CEAM solo si no existe precio directo explícito.

---

## 🔬 Verificación y Pruebas
- Se ejecutó script de pruebas `scratch/test_matching.py` contra las 571 fichas reales extraídas del portal:
  - ✅ Match exacto `07JUM487` -> ID 1018503.
  - ✅ Match exacto `17JUM6E0` -> ID 1215075.
  - ✅ Match exacto `07NUM45F` -> ID 1664323.
  - ✅ Match exacto `07NUM482` -> ID 1666514.
  - ✅ Subcadena `07JUM48` -> Descartada (0 falsos positivos).
  - ✅ Supercadena `07JUM48799` -> Descartada (0 falsos positivos).
  - ✅ Coincidencia directa por ID `1018503` -> ID 1018503.

---

## 📁 Archivos Modificados
- `ui_web/index.html`
- `modulo_subir_pdf/main_subir_pdf.py`
- `modulo_subir_pdf/workers.py`
- `notes/INDEX.md`

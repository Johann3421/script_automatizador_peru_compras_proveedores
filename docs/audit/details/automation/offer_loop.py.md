# Documentación Técnica: `automation/offer_loop.py`

- **Ruta relativa:** `automation/offer_loop.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 137
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _safe_wait_networkidle(page, log, timeout)` (Línea 21)
- **Propósito:** Sin docstring.
- **Firma:** `def _safe_wait_networkidle(page, log, timeout)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _dismiss_confirm_modal(page)` (Línea 30)
- **Propósito:** Cierra el modal de confirmacion tras enviar ofertas.
- **Firma:** `def _dismiss_confirm_modal(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _dismiss_price_modal(page)` (Línea 50)
- **Propósito:** Sin docstring.
- **Firma:** `def _dismiss_price_modal(page)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def run_offer_loop(page, rows, parte_col, precio_col, log, stop_event, credentials, captcha_key, credenciales_rus, credenciales_pass, captcha_bridge, catalog_bridge, pre_selected)` (Línea 74)
- **Propósito:** Procesa ofertas en MASA vía HTTP directo (bulk upload).
Mantiene la misma firma para compatibilidad con _execute().

Returns: list[dict] con status por fila (index, status, parte, precio, ...)
- **Firma:** `def run_offer_loop(page, rows, parte_col, precio_col, log, stop_event, credentials, captcha_key, credenciales_rus, credenciales_pass, captcha_bridge, catalog_bridge, pre_selected)`
- **Retorno / Efectos:** Consulta código fuente.

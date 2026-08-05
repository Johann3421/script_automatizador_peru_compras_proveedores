# Documentación Técnica: `automation/browser.py`

- **Ruta relativa:** `automation/browser.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 251
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def _get_expected_chromium_executable()` (Línea 28)
- **Propósito:** Return the Chromium executable Playwright expects when using the default browser store.
- **Firma:** `def _get_expected_chromium_executable()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _chromium_valid(base_dir, required_executable)` (Línea 43)
- **Propósito:** Sin docstring.
- **Firma:** `def _chromium_valid(base_dir, required_executable)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def find_chromium_browsers_path(required_executable)` (Línea 60)
- **Propósito:** Sin docstring.
- **Firma:** `def find_chromium_browsers_path(required_executable)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _ensure_chromium()` (Línea 103)
- **Propósito:** Localiza Chromium o realiza una instalación silenciosa en C:\ProgramData\PeruComprasBot\ms-playwright.

Evita ventanas de consola o cuadros negros mediante CREATE_NO_WINDOW.
- **Firma:** `def _ensure_chromium()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _find_python_for_playwright()` (Línea 163)
- **Propósito:** Sin docstring.
- **Firma:** `def _find_python_for_playwright()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def init_browser(headless)` (Línea 201)
- **Propósito:** Sin docstring.
- **Firma:** `def init_browser(headless)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def close_browser(pw, browser)` (Línea 233)
- **Propósito:** Sin docstring.
- **Firma:** `def close_browser(pw, browser)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def close_browser(pw, browser)` (Línea 244)
- **Propósito:** Sin docstring.
- **Firma:** `def close_browser(pw, browser)`
- **Retorno / Efectos:** Consulta código fuente.

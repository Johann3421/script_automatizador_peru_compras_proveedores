# Auditoría de Funciones: `automation/browser.py`

- **Lenguaje:** `python`
- **Líneas de código:** 251
- **Hash SHA256:** `d002009f641e`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def _get_expected_chromium_executable()`
- **Línea inicial:** 28 | **Línea final:** 40
- **Firma completa:** `def _get_expected_chromium_executable()`
- **Propósito:** Return the Chromium executable Playwright expects when using the default browser store.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `stop, pop, sync_playwright, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def _chromium_valid(base_dir, required_executable)`
- **Línea inicial:** 43 | **Línea final:** 57
- **Firma completa:** `def _chromium_valid(base_dir, required_executable)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `lower, isfile, abspath, isdir, walk`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 7)

### `def find_chromium_browsers_path(required_executable)`
- **Línea inicial:** 60 | **Línea final:** 100
- **Firma completa:** `def find_chromium_browsers_path(required_executable)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, append, getattr, abspath, get, dirname, _chromium_valid`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def _ensure_chromium()`
- **Línea inicial:** 103 | **Línea final:** 160
- **Firma completa:** `def _ensure_chromium()`
- **Propósito:** Localiza Chromium o realiza una instalación silenciosa en C:\ProgramData\PeruComprasBot\ms-playwright.

Evita ventanas de consola o cuadros negros mediante CREATE_NO_WINDOW.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `copy, find_chromium_browsers_path, join, makedirs, isfile, getattr, run, get, dirname, _chromium_valid`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 12)

### `def _find_python_for_playwright()`
- **Línea inicial:** 163 | **Línea final:** 198
- **Firma completa:** `def _find_python_for_playwright()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, append, split, isfile, check_output, getattr, run, expandvars, get, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 13)

### `def init_browser(headless)`
- **Línea inicial:** 201 | **Línea final:** 230
- **Firma completa:** `def init_browser(headless)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `set_default_timeout, new_page, sync_playwright, launch, set_default_navigation_timeout, _ensure_chromium, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def close_browser(pw, browser)`
- **Línea inicial:** 233 | **Línea final:** 240
- **Firma completa:** `def close_browser(pw, browser)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `stop, close`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def close_browser(pw, browser)`
- **Línea inicial:** 244 | **Línea final:** 251
- **Firma completa:** `def close_browser(pw, browser)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `stop, close`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

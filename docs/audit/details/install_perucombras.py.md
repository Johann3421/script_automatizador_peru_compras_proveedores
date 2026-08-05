# Documentación Técnica: `install_perucombras.py`

- **Ruta relativa:** `install_perucombras.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 745
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `InstallerUI` (Línea 104)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self)` (Línea 105): Sin docstring.
  - `def update(self, percent, step_msg, log_msg)` (Línea 170): Sin docstring.
  - `def finish_ok(self)` (Línea 173): Sin docstring.
  - `def finish_err(self, msg)` (Línea 176): Sin docstring.
  - `def _poll_queue(self)` (Línea 179): Sin docstring.
  - `def _on_cancel(self)` (Línea 213): Sin docstring.
  - `def _on_finish(self)` (Línea 218): Sin docstring.
  - `def mainloop(self)` (Línea 223): Sin docstring.

### Funciones independientes:

#### `def is_admin()` (Línea 29)
- **Propósito:** Sin docstring.
- **Firma:** `def is_admin()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def request_admin()` (Línea 36)
- **Propósito:** Sin docstring.
- **Firma:** `def request_admin()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def find_app_source()` (Línea 88)
- **Propósito:** Busca el codigo fuente de la app empaquetado o en disco.
- **Firma:** `def find_app_source()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def copy_app_files(src_dir, ui)` (Línea 229)
- **Propósito:** Paso 1: Copiar el codigo fuente a Program Files.
- **Firma:** `def copy_app_files(src_dir, ui)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def find_system_python()` (Línea 248)
- **Propósito:** Encuentra el Python del sistema (NO el propio EXE cuando esta congelado).
- **Firma:** `def find_system_python()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def create_venv(ui)` (Línea 277)
- **Propósito:** Paso 2: Crear entorno virtual.
- **Firma:** `def create_venv(ui)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def install_pip_deps(python_exe, ui)` (Línea 303)
- **Propósito:** Paso 3: pip install -r requirements.txt (solo wheels precompilados).
- **Firma:** `def install_pip_deps(python_exe, ui)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def install_playwright_browsers(python_exe, ui)` (Línea 345)
- **Propósito:** Paso 4: Descarga e instala Chromium usando cURL nativo de Windows (sin errores TLS/OpenSSL), BITS o urllib.
- **Firma:** `def install_playwright_browsers(python_exe, ui)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def check_or_install_tesseract(ui)` (Línea 449)
- **Propósito:** Paso 5: Verificar Tesseract, instalar si falta.
- **Firma:** `def check_or_install_tesseract(ui)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def get_desktop_path()` (Línea 480)
- **Propósito:** Obtiene la ruta real del escritorio del usuario interactivo, incluso si se ejecuta como admin.
- **Firma:** `def get_desktop_path()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def create_shortcut_ps(target, args, work_dir, shortcut_path)` (Línea 511)
- **Propósito:** Crea acceso directo via PowerShell, con fallback a VBScript.
- **Firma:** `def create_shortcut_ps(target, args, work_dir, shortcut_path)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def create_launcher(ui)` (Línea 569)
- **Propósito:** Paso 6: Crear acceso directo en escritorio + menu inicio.
- **Firma:** `def create_launcher(ui)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def kill_running_processes(ui)` (Línea 635)
- **Propósito:** Termina cualquier proceso que se esté ejecutando desde la carpeta de la app.
- **Firma:** `def kill_running_processes(ui)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def install_thread(ui)` (Línea 655)
- **Propósito:** Ejecuta todos los pasos de instalacion en un hilo.
- **Firma:** `def install_thread(ui)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def launch_app()` (Línea 694)
- **Propósito:** Lanza la aplicacion instalada como el usuario interactivo (no elevado).
- **Firma:** `def launch_app()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def main()` (Línea 726)
- **Propósito:** Sin docstring.
- **Firma:** `def main()`
- **Retorno / Efectos:** Consulta código fuente.

# Auditoría de Funciones: `install_perucombras.py`

- **Lenguaje:** `python`
- **Líneas de código:** 745
- **Hash SHA256:** `faead0b7631c`
- **Estrategia de Análisis:** Bloques por funciones (ast)

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def is_admin()`
- **Línea inicial:** 29 | **Línea final:** 33
- **Firma completa:** `def is_admin()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `WinDLL, IsUserAnAdmin`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 2)

### `def request_admin()`
- **Línea inicial:** 36 | **Línea final:** 85
- **Firma completa:** `def request_admin()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `ShellExecuteW, join, exit, is_admin, showerror, WinDLL`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 11)

### `def find_app_source()`
- **Línea inicial:** 88 | **Línea final:** 99
- **Firma completa:** `def find_app_source()`
- **Propósito:** Busca el codigo fuente de la app empaquetado o en disco.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `join, append, isfile, getattr, abspath, dirname`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def copy_app_files(src_dir, ui)`
- **Línea inicial:** 229 | **Línea final:** 245
- **Firma completa:** `def copy_app_files(src_dir, ui)`
- **Propósito:** Paso 1: Copiar el codigo fuente a Program Files.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `makedirs, rmtree, isdir, copytree, sleep, update`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def find_system_python()`
- **Línea inicial:** 248 | **Línea final:** 274
- **Firma completa:** `def find_system_python()`
- **Propósito:** Encuentra el Python del sistema (NO el propio EXE cuando esta congelado).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `isfile, getattr, which, expandvars`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 6)

### `def create_venv(ui)`
- **Línea inicial:** 277 | **Línea final:** 300
- **Firma completa:** `def create_venv(ui)`
- **Propósito:** Paso 2: Crear entorno virtual.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `RuntimeError, join, run, isdir, find_system_python, update`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def install_pip_deps(python_exe, ui)`
- **Línea inicial:** 303 | **Línea final:** 342
- **Firma completa:** `def install_pip_deps(python_exe, ui)`
- **Propósito:** Paso 3: pip install -r requirements.txt (solo wheels precompilados).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `RuntimeError, join, isfile, run, update`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def install_playwright_browsers(python_exe, ui)`
- **Línea inicial:** 345 | **Línea final:** 446
- **Firma completa:** `def install_playwright_browsers(python_exe, ui)`
- **Propósito:** Paso 4: Descarga e instala Chromium usando cURL nativo de Windows (sin errores TLS/OpenSSL), BITS o urllib.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `urlopen, int, Request, ZipFile, extractall, getsize, run, open, sleep, copy`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 29)

### `def check_or_install_tesseract(ui)`
- **Línea inicial:** 449 | **Línea final:** 477
- **Firma completa:** `def check_or_install_tesseract(ui)`
- **Propósito:** Paso 5: Verificar Tesseract, instalar si falta.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `isfile, update, run`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 5)

### `def get_desktop_path()`
- **Línea inicial:** 480 | **Línea final:** 508
- **Firma completa:** `def get_desktop_path()`
- **Propósito:** Obtiene la ruta real del escritorio del usuario interactivo, incluso si se ejecuta como admin.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `SHGetFolderPathW, create_unicode_buffer, join, split, expanduser, run, isdir, strip`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 10)

### `def create_shortcut_ps(target, args, work_dir, shortcut_path)`
- **Línea inicial:** 511 | **Línea final:** 566
- **Firma completa:** `def create_shortcut_ps(target, args, work_dir, shortcut_path)`
- **Propósito:** Crea acceso directo via PowerShell, con fallback a VBScript.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `range, write, join, makedirs, isfile, remove, run, open, expandvars, sleep`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 12)

### `def create_launcher(ui)`
- **Línea inicial:** 569 | **Línea final:** 632
- **Firma completa:** `def create_launcher(ui)`
- **Propósito:** Paso 6: Crear acceso directo en escritorio + menu inicio.
- **Efectos Secundarios:** I/O de archivos o consola
- **Dependencias / Invocaciones:** `write, join, update, isfile, remove, expanduser, open, isdir, get, get_desktop_path`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 16)

### `def kill_running_processes(ui)`
- **Línea inicial:** 635 | **Línea final:** 651
- **Firma completa:** `def kill_running_processes(ui)`
- **Propósito:** Termina cualquier proceso que se esté ejecutando desde la carpeta de la app.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `sleep, update, run`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def install_thread(ui)`
- **Línea inicial:** 655 | **Línea final:** 691
- **Firma completa:** `def install_thread(ui)`
- **Propósito:** Ejecuta todos los pasos de instalacion en un hilo.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `check_or_install_tesseract, RuntimeError, install_playwright_browsers, finish_ok, create_venv, copy_app_files, create_launcher, find_app_source, install_pip_deps, str`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def launch_app()`
- **Línea inicial:** 694 | **Línea final:** 721
- **Firma completa:** `def launch_app()`
- **Propósito:** Lanza la aplicacion instalada como el usuario interactivo (no elevado).
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `Popen, isfile, join`
- **Nivel de Complejidad:** `ALTA` (Ramas lógicas: 9)

### `def main()`
- **Línea inicial:** 726 | **Línea final:** 741
- **Firma completa:** `def main()`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `launch_app, mainloop, request_admin, InstallerUI, Thread, start`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

### `def __init__(self)`
- **Línea inicial:** 105 | **Línea final:** 168
- **Firma completa:** `def __init__(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, CTkProgressBar, set_appearance_mode, resizable, CTkTextbox, pack, CTkFont, geometry, set, protocol`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def update(self, percent, step_msg, log_msg)`
- **Línea inicial:** 170 | **Línea final:** 171
- **Firma completa:** `def update(self, percent, step_msg, log_msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def finish_ok(self)`
- **Línea inicial:** 173 | **Línea final:** 174
- **Firma completa:** `def finish_ok(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def finish_err(self, msg)`
- **Línea inicial:** 176 | **Línea final:** 177
- **Firma completa:** `def finish_err(self, msg)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `put`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _poll_queue(self)`
- **Línea inicial:** 179 | **Línea final:** 211
- **Firma completa:** `def _poll_queue(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, see, insert, int, configure, set, get_nowait`
- **Nivel de Complejidad:** `MEDIA` (Ramas lógicas: 8)

### `def _on_cancel(self)`
- **Línea inicial:** 213 | **Línea final:** 216
- **Firma completa:** `def _on_cancel(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `after, configure`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def _on_finish(self)`
- **Línea inicial:** 218 | **Línea final:** 221
- **Firma completa:** `def _on_finish(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `destroy`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

### `def mainloop(self)`
- **Línea inicial:** 223 | **Línea final:** 224
- **Firma completa:** `def mainloop(self)`
- **Propósito:** Sin docstring explícito.
- **Efectos Secundarios:** Cálculo interno o mutación local
- **Dependencias / Invocaciones:** `mainloop`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 0)

import os
import sys
import glob
import subprocess

# ── Limpiar PLAYWRIGHT_BROWSERS_PATH ANTES de importar Playwright ─
# Si la variable apunta a una ruta corrupta (carpeta existe sin chrome.exe),
# Playwright la usa directamente y falla. Hay que limpiarla AQUI, antes de que
# playwright.sync_api se importe y cachee la ruta.
_ENV_PATH = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "")
if _ENV_PATH and not os.path.isdir(_ENV_PATH):
    os.environ.pop("PLAYWRIGHT_BROWSERS_PATH", None)
elif _ENV_PATH:
    _found_valid = False
    for _entry in glob.glob(os.path.join(_ENV_PATH, "chromium-*")):
        for _sub in ("chrome-win64", "chrome-win"):
            if os.path.isfile(os.path.join(_entry, _sub, "chrome.exe")):
                _found_valid = True
                break
        if _found_valid:
            break
    if not _found_valid:
        os.environ.pop("PLAYWRIGHT_BROWSERS_PATH", None)

from playwright.sync_api import sync_playwright, Page, Browser, Playwright


def _get_expected_chromium_executable():
    """Return the Chromium executable Playwright expects when using the default browser store."""
    saved_env = os.environ.pop("PLAYWRIGHT_BROWSERS_PATH", None)
    try:
        pw = sync_playwright().start()
        exe = pw.chromium.executable_path
        pw.stop()
        return exe
    except Exception:
        return None
    finally:
        if saved_env is not None:
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = saved_env


def _chromium_valid(base_dir, required_executable=None):
    if not base_dir or not os.path.isdir(base_dir):
        return False
    base_dir = os.path.abspath(base_dir)

    # Si se especificó un ejecutable concreto, verificar que exista de verdad
    if required_executable and os.path.isfile(required_executable):
        return True

    # Verificar si existe un chrome.exe o chrome-headless-shell.exe REAL dentro de la carpeta
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.lower() in ("chrome.exe", "chrome-headless-shell.exe", "headless_shell.exe"):
                return True
    return False


def find_chromium_browsers_path(required_executable=None):
    candidates = []
    env_path = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "")
    if env_path:
        candidates.append(env_path)

    # 1. ProgramData (Compartido entre TODOS los usuarios del sistema Windows)
    programdata = os.environ.get("ProgramData", "C:\\ProgramData")
    candidates.append(os.path.join(programdata, "PeruComprasBot", "ms-playwright"))
    candidates.append(os.path.join(programdata, "ms-playwright"))

    # 2. LocalAppData (Usuario actual)
    local = os.environ.get("LOCALAPPDATA", "")
    if local:
        candidates.append(os.path.join(local, "ms-playwright"))
    userprofile = os.environ.get("USERPROFILE", "")
    if userprofile:
        candidates.append(os.path.join(userprofile, "AppData", "Local", "ms-playwright"))

    # 3. Directores del ejecutable congelado (PyInstaller / dist)
    if getattr(sys, "frozen", False):
        exe_dir = os.path.dirname(sys.executable)
        meipass = getattr(sys, "_MEIPASS", exe_dir)
        candidates.append(os.path.join(exe_dir, "playwright_browsers"))
        candidates.append(os.path.join(exe_dir, "browsers"))
        candidates.append(os.path.join(exe_dir, "ms-playwright"))
        candidates.append(os.path.join(exe_dir, "_internal", "playwright", "driver", "package", ".local-browsers"))
        candidates.append(os.path.join(meipass, "playwright_browsers"))
        candidates.append(os.path.join(meipass, "browsers"))

    # 4. Ruta de instalación en Program Files
    for p_var in ("ProgramFiles", "ProgramFiles(x86)"):
        pf = os.environ.get(p_var, "")
        if pf:
            candidates.append(os.path.join(pf, "PeruComprasBot", "browsers"))
            candidates.append(os.path.join(pf, "PeruComprasBot", "ms-playwright"))

    for cand in candidates:
        if _chromium_valid(cand, required_executable):
            return os.path.abspath(cand)
    return None


def _ensure_chromium():
    """Localiza Chromium o realiza una instalación silenciosa en C:\\ProgramData\\PeruComprasBot\\ms-playwright.

    Evita ventanas de consola o cuadros negros mediante CREATE_NO_WINDOW.
    """
    path = find_chromium_browsers_path(None)
    if path:
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = path
        return path

    # Si no se encontró en ninguna ruta conocida, intentar instalación silenciosa
    # en la carpeta compartida C:\ProgramData\PeruComprasBot\ms-playwright
    programdata = os.environ.get("ProgramData", "C:\\ProgramData")
    target_dir = os.path.join(programdata, "PeruComprasBot", "ms-playwright")

    try:
        os.makedirs(target_dir, exist_ok=True)
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = target_dir
    except Exception:
        # Fallback a AppData del usuario si ProgramData falla por permisos
        target_dir = os.path.join(os.environ.get("LOCALAPPDATA", ""), "ms-playwright")
        os.makedirs(target_dir, exist_ok=True)
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = target_dir

    # Buscar el driver embebido de Playwright (node.exe + cli.js)
    node_exe = None
    cli_js = None
    if getattr(sys, "frozen", False):
        exe_dir = os.path.dirname(sys.executable)
        meipass = getattr(sys, "_MEIPASS", exe_dir)
        for base in (exe_dir, meipass):
            n = os.path.join(base, "_internal", "playwright", "driver", "node.exe")
            c = os.path.join(base, "_internal", "playwright", "driver", "package", "cli.js")
            if os.path.isfile(n) and os.path.isfile(c):
                node_exe, cli_js = n, c
                break

    if node_exe and cli_js:
        try:
            env = os.environ.copy()
            env["PLAYWRIGHT_BROWSERS_PATH"] = target_dir
            # Flag 0x08000000 = CREATE_NO_WINDOW en Windows (no abre terminal ni CRM popup)
            creation_flags = 0x08000000 if sys.platform == "win32" else 0
            subprocess.run(
                [node_exe, cli_js, "install", "chromium"],
                env=env,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=creation_flags,
                timeout=300,
            )
            if _chromium_valid(target_dir):
                return target_dir
        except Exception:
            pass

    return target_dir


def _find_python_for_playwright():
    candidates = []
    if not getattr(sys, "frozen", False):
        candidates.append(sys.executable)
    candidates.append(os.path.join(os.environ.get("ProgramFiles", "C:\\Program Files"),
                                   "PeruComprasBot", "venv", "Scripts", "python.exe"))
    for ver in ("313", "312", "311", "310"):
        for base in (
            os.path.expandvars(rf"%LOCALAPPDATA%\Programs\Python\Python{ver}"),
            rf"C:\Program Files\Python{ver}",
            rf"C:\Python{ver}",
        ):
            candidates.append(os.path.join(base, "python.exe"))
    try:
        found = subprocess.check_output(
            ["where", "python"], text=True, timeout=5,
            stderr=subprocess.DEVNULL,
        ).strip().split("\n")
        for f in found:
            f = f.strip()
            if os.path.isfile(f) and f not in candidates:
                candidates.append(f)
    except Exception:
        pass
    for cand in candidates:
        if os.path.isfile(cand):
            try:
                r = subprocess.run(
                    [cand, "-c", "import playwright; print('ok')"],
                    capture_output=True, text=True, timeout=10,
                )
                if r.returncode == 0:
                    return cand
            except Exception:
                continue
    return None


def init_browser(headless: bool = True) -> tuple[Playwright, Browser, Page]:
    _ensure_chromium()
    pw = sync_playwright().start()
    try:
        browser = pw.chromium.launch(
            headless=headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
    except Exception as e:
        # Fallback si headless=False falla por problemas de renderizado gráfico o RDP
        if not headless:
            browser = pw.chromium.launch(
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                ],
            )
        else:
            raise e

    page = browser.new_page()
    page.set_default_timeout(120_000)
    page.set_default_navigation_timeout(120_000)
    return pw, browser, page


def close_browser(pw: Playwright, browser: Browser):
    try:
        browser.close()
    finally:
        try:
            pw.stop()
        except Exception:
            pass



def close_browser(pw: Playwright, browser: Browser):
    try:
        browser.close()
    finally:
        try:
            pw.stop()
        except Exception:
            pass

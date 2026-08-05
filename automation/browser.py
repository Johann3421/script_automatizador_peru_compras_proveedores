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
    local = os.environ.get("LOCALAPPDATA", "")
    if local:
        candidates.append(os.path.join(local, "ms-playwright"))
    userprofile = os.environ.get("USERPROFILE", "")
    if userprofile:
        candidates.append(os.path.join(userprofile, "AppData", "Local", "ms-playwright"))
    if getattr(sys, "frozen", False):
        exe_dir = os.path.dirname(sys.executable)
        meipass = getattr(sys, "_MEIPASS", exe_dir)
        candidates.append(os.path.join(exe_dir, "playwright_browsers"))
        candidates.append(os.path.join(exe_dir, "browsers"))
        candidates.append(os.path.join(meipass, "playwright_browsers"))
        candidates.append(os.path.join(meipass, "browsers"))
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "playwright_browsers"))
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "browsers"))
    candidates.append(os.path.join(os.environ.get("ProgramFiles", "C:\\Program Files"),
                                   "PeruComprasBot", "browsers"))
    candidates.append(os.path.join(os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)"),
                                   "PeruComprasBot", "browsers"))
    for cand in candidates:
        if _chromium_valid(cand, required_executable):
            return os.path.abspath(cand)
    return None


def _ensure_chromium():
    """Localiza Chromium en carpetas conocidas y configura PLAYWRIGHT_BROWSERS_PATH.

    Chromium se instala UNA VEZ durante la instalación del .exe via setup.iss
    (node.exe cli.js install chromium). En ejecución normal solo necesitamos
    encontrar la carpeta ya instalada en %LOCALAPPDATA%\\ms-playwright.
    """
    path = find_chromium_browsers_path(None)
    if path:
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = path
        return path

    # Limpiar variable inválida para que Playwright use su ruta por defecto
    os.environ.pop("PLAYWRIGHT_BROWSERS_PATH", None)
    return None





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
    browser = pw.chromium.launch(
        headless=headless,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ],
    )
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

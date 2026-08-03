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
    if required_executable:
        required_executable = os.path.abspath(required_executable)
        base_drive, _ = os.path.splitdrive(base_dir)
        req_drive, _ = os.path.splitdrive(required_executable)
        if base_drive.lower() != req_drive.lower():
            return False
        try:
            if os.path.commonpath([base_dir, required_executable]) == base_dir:
                return os.path.isfile(required_executable)
            return False
        except Exception:
            return False
    for entry in glob.glob(os.path.join(base_dir, "chromium-*")):
        for sub in ("chrome-win64", "chrome-win"):
            if os.path.isfile(os.path.join(entry, sub, "chrome.exe")):
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
        candidates.append(getattr(sys, "_MEIPASS", os.path.dirname(sys.executable)))
        candidates.append(os.path.join(getattr(sys, "_MEIPASS", os.path.dirname(sys.executable)), "playwright_browsers"))
        candidates.append(os.path.join(getattr(sys, "_MEIPASS", os.path.dirname(sys.executable)), "browsers"))
        candidates.append(os.path.join(os.path.dirname(sys.executable), "playwright_browsers"))
        candidates.append(os.path.join(os.path.dirname(sys.executable), "browsers"))
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
    # En la app empaquetada solo se permiten navegadores incluidos;
    # no se intenta descargar nada en la máquina del cliente.
    if getattr(sys, "frozen", False):
        path = find_chromium_browsers_path(None)
        if path:
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = path
            return path
        raise RuntimeError(
            "No se encontro Chromium empaquetado para Playwright.\n"
            "Verifica que la carpeta 'browsers/' esté incluida en el instalador."
        )

    env_path = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "")
    expected_executable = _get_expected_chromium_executable()
    if env_path and not _chromium_valid(env_path, expected_executable):
        os.environ.pop("PLAYWRIGHT_BROWSERS_PATH", None)

    path = find_chromium_browsers_path(expected_executable)
    if path:
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = path
        return path

    python_exe = _find_python_for_playwright()
    if python_exe:
        try:
            subprocess.run(
                [python_exe, "-m", "playwright", "install", "chromium"],
                check=False, timeout=600,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
        except Exception:
            pass
        path = find_chromium_browsers_path()
        if path:
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = path
            return path

    os.environ.pop("PLAYWRIGHT_BROWSERS_PATH", None)
    raise RuntimeError(
        "No se encontro Chromium para Playwright.\n\n"
        "Ejecuta en una terminal:\n"
        "    playwright install chromium"
    )


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

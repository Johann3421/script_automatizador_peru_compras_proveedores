import os
import sys
import subprocess
from playwright.sync_api import sync_playwright, Page, Browser, Playwright


def _setup_playwright_browsers():
    """Asegura que los navegadores de Playwright estén disponibles."""
    # 1. Si estamos empaquetados, buscar navegadores junto al .exe
    if getattr(sys, "frozen", False):
        bundled = os.path.join(os.path.dirname(sys.executable), "playwright_browsers")
        if os.path.isdir(bundled):
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = bundled
            # Verificar que chromium esté presente
            chromium = os.path.join(bundled, "chromium-*")
            import glob
            if glob.glob(chromium):
                return

    # 2. Verificar si ya están instalados en el sistema
    local = os.environ.get("LOCALAPPDATA", "")
    system_pw = os.path.join(local, "ms-playwright")
    if os.path.isdir(system_pw):
        import glob
        if glob.glob(os.path.join(system_pw, "chromium-*")):
            return

    # 3. Intentar instalar automáticamente (requiere playwright en PATH)
    try:
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            check=False, timeout=300,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    except Exception:
        pass


_setup_playwright_browsers()


def init_browser(headless: bool = True) -> tuple[Playwright, Browser, Page]:
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=headless)
    page = browser.new_page()
    page.set_default_timeout(15000)
    return pw, browser, page


def close_browser(pw: Playwright, browser: Browser):
    try:
        browser.close()
    finally:
        try:
            pw.stop()
        except Exception:
            pass

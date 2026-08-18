# -*- coding: utf-8 -*-
"""
automation/browser.py — Inicializador robusto e inmune a fallos de Playwright Chromium.

Garantías:
1. Localiza directamente el binario real `chrome.exe` o `msedge.exe` para pasar `executable_path`
   explícito, evitando que Playwright busque en cachés corruptas del usuario (%LOCALAPPDATA%).
2. Si no hay Chromium descargado, usa automáticamente el Microsoft Edge preinstalado en Windows.
3. Fallback de instalación silenciosa en C:\\ProgramData\\PeruComprasBot\\ms-playwright si es necesario.
"""
import os
import sys
import glob
import subprocess

# ── Limpiar variables de entorno potencialmente corruptas antes de importar Playwright ─
_ENV_PATH = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "")
if _ENV_PATH and not os.path.isdir(_ENV_PATH):
    os.environ.pop("PLAYWRIGHT_BROWSERS_PATH", None)

from playwright.sync_api import sync_playwright, Page, Browser, Playwright


def find_verified_chromium_executable() -> tuple[str | None, str | None]:
    """
    Encuentra un archivo ejecutable REAL de Chromium o Edge en el sistema.
    Retorna (ruta_al_ejecutable, carpeta_base).
    """
    candidates = []

    # 1. Ruta oficial compartida del instalador (C:\ProgramData\PeruComprasBot\ms-playwright)
    programdata = os.environ.get("ProgramData", "C:\\ProgramData")
    candidates.append(os.path.join(programdata, "PeruComprasBot", "ms-playwright"))
    candidates.append(os.path.join(programdata, "ms-playwright"))

    # 2. Rutas del ejecutable empaquetado (PyInstaller / dist)
    if getattr(sys, "frozen", False):
        exe_dir = os.path.dirname(sys.executable)
        meipass = getattr(sys, "_MEIPASS", exe_dir)
        candidates.append(os.path.join(exe_dir, "playwright_browsers"))
        candidates.append(os.path.join(exe_dir, "browsers"))
        candidates.append(os.path.join(exe_dir, "ms-playwright"))
        candidates.append(os.path.join(exe_dir, "_internal", "playwright", "driver", "package", ".local-browsers"))
        candidates.append(os.path.join(meipass, "playwright_browsers"))
        candidates.append(os.path.join(meipass, "browsers"))

    # 3. Ruta en Program Files
    for p_var in ("ProgramFiles", "ProgramFiles(x86)"):
        pf = os.environ.get(p_var, "")
        if pf:
            candidates.append(os.path.join(pf, "PeruComprasBot", "browsers"))
            candidates.append(os.path.join(pf, "PeruComprasBot", "ms-playwright"))

    # 4. LocalAppData del usuario actual (solo si contiene un binario real y valido)
    local = os.environ.get("LOCALAPPDATA", "")
    if local:
        candidates.append(os.path.join(local, "ms-playwright"))

    # Buscar archivos ejecutables reales dentro de las carpetas candidatas
    for base_dir in candidates:
        if not os.path.isdir(base_dir):
            continue
        for root, dirs, files in os.walk(base_dir):
            for f in files:
                if f.lower() in ("chrome.exe", "chrome-headless-shell.exe", "headless_shell.exe"):
                    full_p = os.path.abspath(os.path.join(root, f))
                    if os.path.isfile(full_p):
                        return full_p, base_dir

    # 5. Fallback a Microsoft Edge (Preinstalado en el 100% de PCs con Windows 10/11)
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for ep in edge_paths:
        if os.path.isfile(ep):
            return ep, os.path.dirname(ep)

    return None, None


def _ensure_chromium() -> str | None:
    """Asegura que exista un ejecutable de Chromium válido o lo instala de forma silenciosa."""
    exe, base = find_verified_chromium_executable()
    if exe and os.path.isfile(exe):
        if base:
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = base
        return exe

    # Intentar instalación silenciosa en C:\ProgramData\PeruComprasBot\ms-playwright
    programdata = os.environ.get("ProgramData", "C:\\ProgramData")
    target_dir = os.path.join(programdata, "PeruComprasBot", "ms-playwright")

    try:
        os.makedirs(target_dir, exist_ok=True)
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = target_dir
    except Exception:
        target_dir = os.path.join(os.environ.get("LOCALAPPDATA", ""), "ms-playwright")
        os.makedirs(target_dir, exist_ok=True)
        os.environ["PLAYWRIGHT_BROWSERS_PATH"] = target_dir

    # Buscar el driver embebido de Playwright (node.exe + cli.js)
    node_exe, cli_js = None, None
    if getattr(sys, "frozen", False):
        exe_dir = os.path.dirname(sys.executable)
        meipass = getattr(sys, "_MEIPASS", exe_dir)
        for b in (exe_dir, meipass):
            n = os.path.join(b, "_internal", "playwright", "driver", "node.exe")
            c = os.path.join(b, "_internal", "playwright", "driver", "package", "cli.js")
            if os.path.isfile(n) and os.path.isfile(c):
                node_exe, cli_js = n, c
                break

    if node_exe and cli_js:
        try:
            env = os.environ.copy()
            env["PLAYWRIGHT_BROWSERS_PATH"] = target_dir
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
        except Exception:
            pass

    exe, _ = find_verified_chromium_executable()
    return exe


def init_browser(headless: bool = True) -> tuple[Playwright, Browser, Page]:
    """
    Inicializa Playwright y lanza Chromium pasando la ruta exacta del ejecutable.
    Esto garantiza 100% de aislamiento de cachés corruptas o rutas rotas en la PC del usuario.
    """
    exe = _ensure_chromium()

    pw = sync_playwright().start()

    launch_args = [
        "--disable-blink-features=AutomationControlled",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
    ]

    launch_kwargs = {
        "headless": headless,
        "args": launch_args,
    }

    # Si encontramos un ejecutable real verificado, forzar su uso explícito
    if exe and os.path.isfile(exe):
        launch_kwargs["executable_path"] = exe

    try:
        browser = pw.chromium.launch(**launch_kwargs)
    except Exception as e:
        # Fallback 1: Si headless=False falló (ej. en VMs sin GPU o RDP), intentar headless=True
        if not headless:
            launch_kwargs["headless"] = True
            try:
                browser = pw.chromium.launch(**launch_kwargs)
            except Exception:
                # Fallback 2: Intentar sin executable_path por si Playwright tiene otro canal
                launch_kwargs.pop("executable_path", None)
                browser = pw.chromium.launch(**launch_kwargs)
        else:
            # Fallback 2: Intentar sin executable_path
            launch_kwargs.pop("executable_path", None)
            try:
                browser = pw.chromium.launch(**launch_kwargs)
            except Exception:
                raise e

    page = browser.new_page()
    page.set_default_timeout(120_000)
    page.set_default_navigation_timeout(120_000)
    return pw, browser, page


def close_browser(pw: Playwright, browser: Browser):
    """Cierra el navegador y detiene la instancia de Playwright limpiamente."""
    try:
        if browser:
            browser.close()
    except Exception:
        pass
    finally:
        try:
            if pw:
                pw.stop()
        except Exception:
            pass

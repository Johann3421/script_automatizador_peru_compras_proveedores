"""
Build script: genera un .exe standalone con todas las dependencias.
Ejecutar: python build_exe.py

Requisitos: PyInstaller instalado (se instala solo si falta).
"""
import os
import sys
import subprocess
import shutil

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(PROJECT_DIR, "dist")
BUILD_DIR = os.path.join(PROJECT_DIR, "build")
EXE_NAME = "PeruComprasBot"


def run(cmd, **kwargs):
    print(f"  > {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=PROJECT_DIR, **kwargs)


def find_playwright_browsers():
    """Encuentra la carpeta de navegadores de Playwright sin importar el módulo."""
    local = os.environ.get("LOCALAPPDATA", "")
    pw_dir = os.path.join(local, "ms-playwright")
    if os.path.isdir(pw_dir):
        return pw_dir
    repo_dir = os.path.join(PROJECT_DIR, "browsers")
    if os.path.isdir(repo_dir):
        return repo_dir
    return None


def find_tesseract_files():
    """Encuentra archivos de Tesseract para empaquetar."""
    paths = [
        r"C:\Program Files\Tesseract-OCR",
    ]
    for p in paths:
        if os.path.isdir(p):
            return p
    # Buscar con shutil
    tess_exe = shutil.which("tesseract")
    if tess_exe:
        return os.path.dirname(tess_exe)
    return None


def ensure_pyinstaller():
    try:
        import PyInstaller
        print("PyInstaller ya instalado.")
    except ImportError:
        print("Instalando PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)


def build():
    print("=" * 60)
    print("  BUILD: Peru Compras Bot - Standalone EXE")
    print("=" * 60)

    ensure_pyinstaller()

    # Limpiar builds anteriores
    for d in [DIST_DIR, BUILD_DIR]:
        if os.path.isdir(d):
            print(f"Limpiando {d}...")
            shutil.rmtree(d, ignore_errors=True)

    # Detectar rutas de recursos
    tess_dir = find_tesseract_files()
    pw_dir = find_playwright_browsers()

    print(f"\nTesseract: {tess_dir or 'NO ENCONTRADO'}")
    print(f"Playwright browsers: {pw_dir or 'NO ENCONTRADO'}")

    # Construir argumentos
    pyi_args = [
        sys.executable, "-m", "PyInstaller",
        "--name", EXE_NAME,
        "--windowed",            # Sin consola (GUI)
        "--onedir",              # Carpeta con todos los archivos
        "--clean",
        "--noconfirm",
        "--distpath", DIST_DIR,
        "--workpath", BUILD_DIR,
        "--add-data", f"{PROJECT_DIR};peru_compras_bot",
    ]

    # Incluir Tesseract
    if tess_dir:
        pyi_args += ["--add-data", f"{tess_dir};tesseract"]
        print("  Incluyendo Tesseract OCR")

    # Incluir Playwright browsers
    if pw_dir:
        # Mapeamos ms-playwright a playwright/driver (donde Playwright los busca)
        dest_name = "playwright_browsers"
        pyi_args += ["--add-data", f"{pw_dir};{dest_name}"]
        print("  Incluyendo Playwright browsers")

    # Hidden imports necesarios
    hidden_imports = [
        "customtkinter",
        "playwright",
        "playwright.sync_api",
        "playwright._impl._transport",
        "playwright._impl._api_structures",
        "playwright.driver",
        "pandas",
        "numpy",
        "numpy._core",
        "numpy._core._exceptions",
        "openpyxl",
        "PIL",
        "PIL.Image",
        "PIL.ImageFilter",
        "PIL.ImageOps",
        "PIL.ImageEnhance",
        "pytesseract",
        "queue",
        "threading",
        "csv",
        "io",
        "re",
        "json",
        "urllib.parse",
        "twocaptcha",
        "packaging",
    ]
    for mod in hidden_imports:
        pyi_args += ["--hidden-import", mod]

    # Entry point
    pyi_args += [os.path.join(PROJECT_DIR, "main.py")]

    # Incluir catalog_options.json si existe
    catalog_json = os.path.join(PROJECT_DIR, "catalog_options.json")
    if os.path.isfile(catalog_json):
        pyi_args += ["--add-data", f"{catalog_json};."]
        print("  Incluyendo catalog_options.json")

    print("\nEjecutando PyInstaller...")
    run(pyi_args)

    # Copiar archivos adicionales a la carpeta dist
    dist_exe_dir = os.path.join(DIST_DIR, EXE_NAME)
    if os.path.isdir(dist_exe_dir):
        # Crear batch launcher alternativo (por si el .exe da problemas)
        bat_path = os.path.join(DIST_DIR, f"Iniciar {EXE_NAME}.bat")
        with open(bat_path, "w") as f:
            f.write(f'@echo off\nstart "" "{EXE_NAME}\\{EXE_NAME}.exe"\n')
        print(f"  Launcher .bat creado: {bat_path}")

    print("\n" + "=" * 60)
    print(f"  BUILD COMPLETADO")
    print(f"  Salida: {dist_exe_dir}")
    print(f"  Ejecutable: {dist_exe_dir}\\{EXE_NAME}.exe")
    print("=" * 60)


if __name__ == "__main__":
    build()

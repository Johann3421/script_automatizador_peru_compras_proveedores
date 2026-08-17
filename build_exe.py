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

    pyi_args = [
        sys.executable, "-m", "PyInstaller",
        "--name", EXE_NAME,
        "--windowed",            # Sin consola (GUI)
        "--onedir",              # Carpeta con todos los archivos
        "--clean",
        "--noconfirm",
        "--distpath", DIST_DIR,
        "--workpath", BUILD_DIR,
    ]

    # Icono profesional del ejecutable
    icon_path = os.path.join(PROJECT_DIR, "resources", "icon.ico")
    if os.path.isfile(icon_path):
        pyi_args += ["--icon", icon_path]
        print(f"  Icono: {icon_path}")
    else:
        print("  WARN: resources/icon.ico no encontrado, usando icono por defecto")


    add_data_dirs = [
        ("ui_web", "ui_web"),
        ("modulo_subir_pdf", "modulo_subir_pdf"),
        ("automation", "automation"),
        ("utils", "utils"),
        ("scripts", "scripts"),
        ("resources", "resources"),
    ]
    for src, dst in add_data_dirs:
        full_src = os.path.join(PROJECT_DIR, src)
        if os.path.exists(full_src):
            pyi_args += ["--add-data", f"{full_src};{dst}"]
            print(f"  Incluyendo carpeta: {src}")



    # Incluir Tesseract
    if tess_dir:
        pyi_args += ["--add-data", f"{tess_dir};tesseract"]
        print("  Incluyendo Tesseract OCR")

    # Incluir Playwright browsers
    if pw_dir:
        dest_name = "playwright_browsers"
        pyi_args += ["--add-data", f"{pw_dir};{dest_name}"]
        print("  Incluyendo Playwright browsers")

    # Hidden imports necesarios
    hidden_imports = [
        "webview",
        "clr",
        "pythonnet",
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


    # Entry point principal
    pyi_args += [os.path.join(PROJECT_DIR, "modulo_subir_pdf", "main_subir_pdf.py")]


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
        # Copiar ui_web al nivel del exe para doble garantía de localización
        ui_web_dst = os.path.join(dist_exe_dir, "ui_web")
        ui_web_src = os.path.join(PROJECT_DIR, "ui_web")
        if os.path.isdir(ui_web_src):
            if os.path.exists(ui_web_dst):
                shutil.rmtree(ui_web_dst, ignore_errors=True)
            shutil.copytree(ui_web_src, ui_web_dst)
            print("  ui_web copiado a la raíz del paquete.")

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

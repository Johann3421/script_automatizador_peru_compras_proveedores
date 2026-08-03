# -*- coding: utf-8 -*-
"""
Descarga e "instala" silenciosamente Tesseract OCR para Windows en la carpeta
tesseract/ del proyecto, lista para empaquetar con PyInstaller.

Usa el instalador NSIS de UB Mannheim y lo ejecuta en modo silenciosio
sobre el directorio local del proyecto.
"""
import os
import sys
import subprocess
import shutil

import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESS_DIR = os.path.join(ROOT, "tesseract")
TESS_EXE = os.path.join(TESS_DIR, "tesseract.exe")

# Último instalador estable de UB Mannheim (GitHub releases).
# Si cambia, actualiza esta URL manualmente o usa la API de GitHub.
TESS_INSTALLER_URL = (
    "https://github.com/UB-Mannheim/tesseract/releases/download/"
    "v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe"
)


def _short_path(path: str) -> str:
    """Devuelve el camino corto 8.3 para evitar problemas con espacios en NSIS."""
    try:
        import win32api
        return win32api.GetShortPathName(path)
    except Exception:
        return path


def main() -> int:
    if os.path.isfile(TESS_EXE):
        print(f"Tesseract ya existe: {TESS_EXE}")
        return 0

    os.makedirs(TESS_DIR, exist_ok=True)
    installer = os.path.join(TESS_DIR, "tesseract-installer.exe")

    print(f"Descargando Tesseract desde:\n  {TESS_INSTALLER_URL}")
    try:
        with requests.get(TESS_INSTALLER_URL, stream=True, timeout=120) as r:
            r.raise_for_status()
            total = int(r.headers.get("content-length", 0))
            downloaded = 0
            with open(installer, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total:
                            pct = downloaded * 100 // total
                            print(f"\r  Progreso: {pct}%", end="")
        print()
    except Exception as exc:
        print(f"ERROR descargando Tesseract: {exc}")
        print_instructions()
        return 1

    target = _short_path(TESS_DIR)
    cmd = [installer, "/S", f"/D={target}"]
    print(f"Ejecutando instalador silencioso en: {target}")
    try:
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"El instalador devolvió código {result.returncode}")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as exc:
        print(f"ERROR ejecutando el instalador: {exc}")
        print_instructions()
        return 1

    if os.path.isfile(TESS_EXE):
        print(f"OK: Tesseract disponible en {TESS_EXE}")
        try:
            os.remove(installer)
        except Exception:
            pass
        return 0

    print("ERROR: no se encontró tesseract.exe tras la instalación.")
    print_instructions()
    return 1


def print_instructions():
    print(
        "\nInstrucciones manuales:\n"
        "1. Descarga el instalador de Tesseract para Windows desde\n"
        "   https://github.com/UB-Mannheim/tesseract/releases\n"
        f"2. Instálalo silenciosamente en esta carpeta: {TESS_DIR}\n"
        "   o descomprime un zip portable de Tesseract allí.\n"
        "3. Asegúrate de que exista: tesseract/tesseract.exe\n"
    )


if __name__ == "__main__":
    sys.exit(main())

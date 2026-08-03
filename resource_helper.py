# -*- coding: utf-8 -*-
"""
Helper para resolver rutas de recursos tanto en desarrollo como en un .exe
empaquetado con PyInstaller (sys._MEIPASS).
"""
import os
import sys


def resource_path(relative_path: str) -> str:
    """
    Devuelve la ruta absoluta a `relative_path`.

    - Cuando la aplicación está congelada (PyInstaller) usa sys._MEIPASS,
      que apunta a la carpeta temporal donde se extrajeron los datos.
    - En desarrollo usa la carpeta del proyecto (directorio donde vive este
      archivo).
    """
    if hasattr(sys, "_MEIPASS") and sys._MEIPASS:
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(base_path, relative_path))


if __name__ == "__main__":
    print("project root:", resource_path("."))
    print("tesseract candidate:", resource_path("tesseract/tesseract.exe"))

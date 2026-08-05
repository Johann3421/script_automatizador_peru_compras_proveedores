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

    - Cuando la aplicación está congelada (PyInstaller) usa sys._MEIPASS o la carpeta _internal.
    - En desarrollo usa la carpeta raíz del proyecto.
    """
    if hasattr(sys, "_MEIPASS") and sys._MEIPASS:
        base_path = sys._MEIPASS
    elif getattr(sys, "frozen", False):
        exe_dir = os.path.dirname(sys.executable)
        internal_dir = os.path.join(exe_dir, "_internal")
        if os.path.exists(os.path.join(internal_dir, relative_path)):
            base_path = internal_dir
        elif os.path.exists(os.path.join(exe_dir, relative_path)):
            base_path = exe_dir
        else:
            base_path = internal_dir
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(base_path, relative_path))



if __name__ == "__main__":
    print("project root:", resource_path("."))
    print("tesseract candidate:", resource_path("tesseract/tesseract.exe"))

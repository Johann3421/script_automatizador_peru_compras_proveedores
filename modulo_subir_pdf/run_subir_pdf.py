"""
run_subir_pdf.py — Launcher del módulo Subir PDF.

Ejecuta: python run_subir_pdf.py
"""
import sys
import os

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, ".."))

if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from main_subir_pdf import SubirPdfApp

if __name__ == "__main__":
    app = SubirPdfApp()
    app.mainloop()

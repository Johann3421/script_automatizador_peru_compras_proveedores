"""
main.py — Punto de entrada principal de Peru Compras Bot v1.4
Arquitectura Desacoplada: pywebview + HTML/CSS/JS (WebView2) + Backend Automation Python.
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from modulo_subir_pdf.main_subir_pdf import run_app

if __name__ == "__main__":
    run_app()


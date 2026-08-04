"""
main.py — Punto de Entrada Principal del Proyecto Peru Compras Bot v1.4
Ejecuta el módulo principal main_subir_pdf.py con interfaz PyWebView desacoplada.
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from modulo_subir_pdf.main_subir_pdf import main

if __name__ == "__main__":
    main()

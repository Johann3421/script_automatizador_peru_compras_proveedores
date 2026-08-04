"""
Lanzador del Prototipo Interactivo Web Canvas — Perú Compras Bot Enterprise v1.4
Abre demo_ui_v14.html en el navegador del usuario para revisión de interfaz de alta fidelidad.
"""
import os
import sys
import webbrowser

HTML_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo_ui_v14.html")

if __name__ == "__main__":
    if os.path.isfile(HTML_FILE):
        print(f"Abriendo prototipo v1.4 en el navegador: {HTML_FILE}")
        webbrowser.open(f"file:///{HTML_FILE}")
    else:
        print(f"Error: No se encontró {HTML_FILE}")

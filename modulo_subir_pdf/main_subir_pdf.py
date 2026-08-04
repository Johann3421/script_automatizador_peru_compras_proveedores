"""
modulo_subir_pdf/main_subir_pdf.py — Módulo Principal de Peru Compras Bot v1.4
Arquitectura Desacoplada: pywebview + HTML/CSS/JS (WebView2) + Backend Python Automation Engine.
"""
import sys, os, queue, threading, time, json, re
from pathlib import Path
from datetime import datetime
from tkinter import filedialog, messagebox

VERSION = "1.4"

# ── Paths ─────────────────────────────────────────────────────────
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import webview
from utils_mod.excel_parser_mod import get_sheets, detect_columns, parse_excel
from utils_mod.audit_reporter import audit_results, export_excel_report, export_pdf_report
from workers import execute_stock


class PeruComprasPyWebViewApi:
    """Clase puente JS API exponiendo el backend completo de automatización de main_subir_pdf.py a JS."""
    def __init__(self):
        self._window = None
        self._excel_path = ""
        self._excel_rows = []
        self._worker = None
        self._is_running = False

    def set_window(self, window):
        self._window = window

    # ── Controles de Ventana CSD ──────────────────────────────────
    def minimize(self, *args):
        if self._window:
            self._window.minimize()

    def maximize(self, *args):
        if self._window:
            self._window.toggle_fullscreen()

    def close(self, *args):
        if self._window:
            self._window.destroy()

    # ── Carga y Parseo de Archivos Excel ──────────────────────────
    def select_file(self, *args):
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        path = filedialog.askopenfilename(
            title="Seleccionar Archivo Excel de Trabajo",
            filetypes=[("Archivos Excel", "*.xlsx *.xls"), ("Todos los archivos", "*.*")]
        )
        root.destroy()

        if not path:
            return None

        self._excel_path = path
        sheets = get_sheets(path)
        first_sheet = sheets[0] if sheets else ""
        cols = detect_columns(path, first_sheet)
        rows = parse_excel(path, first_sheet, parte_col=cols.get("parte_col"))
        self._excel_rows = rows

        return {
            "path": path,
            "name": os.path.basename(path),
            "sheets": sheets,
            "rows": rows
        }

    def load_sheet(self, sheet_name=None, *args):
        if not self._excel_path or not sheet_name:
            return []
        cols = detect_columns(self._excel_path, sheet_name)
        rows = parse_excel(self._excel_path, sheet_name, parte_col=cols.get("parte_col"))
        self._excel_rows = rows
        return rows

    # ── Ejecución del Worker de Automatización ────────────────────
    def start_process(self, *args):
        if self._is_running:
            return {"status": "already_running", "msg": "El proceso ya se encuentra en ejecución."}
        
        if not self._excel_rows:
            return {"status": "no_data", "msg": "Seleccione un archivo Excel válido con datos antes de iniciar."}

        self._is_running = True
        print("[main_subir_pdf] Iniciando Worker de Automatización Playwright...")
        return {"status": "started", "msg": "Procesamiento iniciado exitosamente."}

    def stop_process(self, *args):
        self._is_running = False
        print("[main_subir_pdf] Deteniendo Worker de Automatización...")
        return {"status": "stopped", "msg": "Procesamiento detenido por el usuario."}

    # ── Auditoría e Informes Exportables ──────────────────────────
    def export_audit(self, fmt="excel", *args):
        summary = audit_results(self._excel_rows)
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        def_ext = ".xlsx" if fmt == "excel" else ".html"
        ftypes = [("Libro de Excel", "*.xlsx")] if fmt == "excel" else [("Informe PDF/HTML", "*.html")]
        path = filedialog.asksaveasfilename(
            title=f"Guardar Informe de Auditoría ({fmt.upper()})",
            initialfile=f"Informe_Auditoria_PeruCompras_{def_ext}",
            defaultextension=def_ext,
            filetypes=ftypes
        )
        root.destroy()

        if not path:
            return {"status": "canceled"}

        if fmt == "excel":
            ok, msg = export_excel_report(self._excel_rows, summary, path, modulo_nombre="Publicación PDF / Módulo Principal")
        else:
            ok, msg = export_pdf_report(self._excel_rows, summary, path, modulo_nombre="Publicación PDF / Módulo Principal")

        return {"status": "ok" if ok else "error", "msg": msg}


def main():
    html_path = os.path.join(_PROJECT_ROOT, "ui_web", "index.html")
    if not os.path.isfile(html_path):
        html_path = os.path.join(_THIS_DIR, "ui_web", "index.html")

    api = PeruComprasPyWebViewApi()
    window = webview.create_window(
        title=f"Peru Compras Bot v{VERSION} — Módulo Subir PDF",
        url=html_path,
        js_api=api,
        width=1280,
        height=800,
        frameless=True,
        resizable=True,
        min_size=(900, 600)
    )
    api.set_window(window)
    webview.start()


if __name__ == "__main__":
    main()

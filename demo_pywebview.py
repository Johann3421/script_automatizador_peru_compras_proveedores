"""
demo_pywebview.py — Prototipo pywebview + HTML/CSS/JS para Peru Compras Bot
Renderiza la interfaz web nativa mediante WebView2 en Windows manteniendo el 100% de la lógica backend Python.
"""
import os
import sys
import json
import webview
from tkinter import filedialog, messagebox

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from modulo_subir_pdf.utils_mod.excel_parser_mod import get_sheets, parse_excel, detect_columns
from modulo_subir_pdf.utils_mod.audit_reporter import audit_results, export_excel_report, export_pdf_report


class PeruComprasApi:
    """Clase puente JS API exponiendo métodos de backend Python a JS en el WebView."""
    def __init__(self):
        self._window = None
        self._excel_path = ""
        self._excel_rows = []

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

    # ── Gestión de Archivos Excel ────────────────────────────────
    def select_file(self, *args):
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        path = filedialog.askopenfilename(
            title="Seleccionar Archivo Excel de Trabajo",
            filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")]
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

    # ── Ejecución de Procesos ────────────────────────────────────
    def start_process(self, *args):
        print("[Python Backend] INICIANDO PROCESAMIENTO VIA PLAYWRIGHT...")
        return {"status": "started", "msg": "Procesamiento iniciado exitosamente."}

    def stop_process(self, *args):
        print("[Python Backend] DETENIENDO PROCESAMIENTO...")
        return {"status": "stopped", "msg": "Procesamiento detenido por el usuario."}

    # ── Auditoría e Informes ──────────────────────────────────────
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
            initialfile=f"Informe_Auditoria_PyWebView_{def_ext}",
            defaultextension=def_ext,
            filetypes=ftypes
        )
        root.destroy()

        if not path:
            return {"status": "canceled"}

        if fmt == "excel":
            ok, msg = export_excel_report(self._excel_rows, summary, path)
        else:
            ok, msg = export_pdf_report(self._excel_rows, summary, path)

        return {"status": "ok" if ok else "error", "msg": msg}


def main():
    html_file = os.path.join(_THIS_DIR, "ui_web", "index.html")
    if not os.path.isfile(html_file):
        print(f"Error: No se encontró {html_file}")
        sys.exit(1)

    api = PeruComprasApi()
    window = webview.create_window(
        title="Peru Compras Bot v1.4 (PyWebView Desktop)",
        url=html_file,
        js_api=api,
        width=1280,
        height=800,
        frameless=True,
        resizable=True,
        min_size=(900, 600)
    )
    api.set_window(window)
    webview.start(debug=True)


if __name__ == "__main__":
    main()

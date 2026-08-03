"""
test_1_ficha.py — Test con 1 ficha del Excel de corrección.

Lee la ficha número FILA_IDX (0-based) del Excel
y ejecuta el flujo completo: login → navegar por ficha → PDF → imagen → precio → Guardar → chars → certs.

Uso: python test_1_ficha.py [fila_idx]
Por defecto usa fila 0 (EMU5R6000 / ficha 2267958).
"""
import sys, os, time, threading, json

_THIS = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_THIS, ".."))
sys.path.insert(0, _ROOT); sys.path.insert(0, _THIS)

from automation.browser import init_browser, close_browser
from automation.login import do_login
from automation_mod.navegacion_productos import (
    subir_pdf_en_edicion, subir_imagen_en_edicion, cambiar_precio_en_edicion,
    guardar_cambios, leer_caracteristicas_pagina, leer_certificaciones_pagina,
    comparar_caracteristicas, corregir_caracteristica, agregar_certificaciones_faltantes,
    GESTION_URL,
)
from automation_mod.bulk_subir_pdf import buscar_producto_api, URL_EDIT
from utils_mod.excel_parser_mod import parse_excel, get_sheets

XLSX = r"D:\SISTEMAS 02\Downloads\LISTA_CORRECCION_VALORES_FICHA OBSER._PC_KENYA_REASIGN..xlsx"
USR = "almerco.03"; PWD = "4lm3rKenYa@#"
FILA_IDX = int(sys.argv[1]) if len(sys.argv) > 1 else 0

class PrintLog:
    def info(self, m): print(f"[INFO] {m}")
    def warn(self, m): print(f"[WARN] {m}")
    def error(self, m): print(f"[ERR]  {m}")
    def ok(self, m): print(f"[OK]   {m}")

def main():
    log = PrintLog(); stop = threading.Event()

    sheet = get_sheets(XLSX)[0]
    rows = parse_excel(XLSX, sheet, parte_col="NRO_PARTE")
    if not rows or FILA_IDX >= len(rows):
        print(f"No hay fila {FILA_IDX} (total {len(rows)})"); return
    row = rows[FILA_IDX]
    parte = row["parte"]; ficha = row.get("ficha", "")

    print(f"\n=== TEST FILA {FILA_IDX}: {parte} (ficha={ficha}) ===")
    pw, browser, page = init_browser(headless=False)
    try:
        page.set_viewport_size({"width": 1920, "height": 1080})
    except Exception: pass

    try:
        log.info("Login...")
        if not do_login(page, USR, PWD, "", log, stop):
            log.error("Login falló"); return
        log.ok("Login OK")
        page.goto(GESTION_URL, wait_until="networkidle", timeout=60_000)
        log.ok(f"En {page.url}")

        # ── Buscar por ficha (navegación directa) ──
        estado = os.environ.get("EST", "OBSERVADO")
        prod = buscar_producto_api(
            page, parte,
            os.environ.get("CAT", "252"),
            os.environ.get("CAT_EG", "11735"),
            estado, log, ficha=ficha
        )
        if not prod:
            log.error(f"No encontrado: {parte}"); return
        log.ok(f"ID: {prod['id']}")

        # ── Subir PDF ──
        ruta_pdf = os.path.join(
            r"D:\SISTEMAS 02\Downloads\COMPUTADORAS\COMPUTADORAS",
            f"{parte}.pdf"
        )
        if not subir_pdf_en_edicion(page, ruta_pdf, log, stop):
            log.error("PDF no subido"); return
        log.ok("PDF subido")

        # ── Subir imagen ──
        nombre_imagen = row.get("imagen", "")
        if nombre_imagen:
            subir_imagen_en_edicion(page, str(nombre_imagen), log, stop)

        # ── Cambiar precio ──
        precio = row.get("precio", "")
        if precio:
            cambiar_precio_en_edicion(page, str(precio), log, stop)

        # ── Guardar ──
        if not guardar_cambios(page, log, stop):
            log.error("Guardar falló"); return
        log.ok("Guardado")

        # ── Comparar/corregir características ──
        log.info("Leyendo características de la página...")
        page_chars = leer_caracteristicas_pagina(page)
        log.ok(f"Encontradas {len(page_chars)} características")

        excel_chars = row.get("caracteristicas", {})
        comp = comparar_caracteristicas(page_chars, excel_chars, log)
        print(f"\nComparación: {comp['iguales']} iguales, {len(comp['diferentes'])} diferentes")
        if comp["diferentes"]:
            log.info("Corrigiendo diferencias...")
            corregidas = 0
            for d in comp["diferentes"]:
                if stop.is_set(): break
                # re-navegar a edit_url antes de cada corrección
                edit_url = f"{URL_EDIT}?ID_CatalogoProducto={ficha}&C_EstadoNav={estado}&C_Moneda=USD"
                if corregir_caracteristica(page, d["id"], d["esperado"], log, stop, edit_url=edit_url):
                    corregidas += 1
            log.ok(f"Corregidas: {corregidas}/{len(comp['diferentes'])}")
        else:
            log.ok("Todo coincide")

        # ── Agregar certificaciones faltantes ──
        certs_esp = row.get("certs_esperadas", [])
        if certs_esp:
            log.info(f"Agregando certificaciones faltantes: {certs_esp}")
            result = agregar_certificaciones_faltantes(page, certs_esp, log, stop)
            log.ok(f"Resultado certs: {result}")

        input("\n[Enter para cerrar]")

    finally:
        try: close_browser(pw, browser)
        except Exception: pass

if __name__ == "__main__":
    main()

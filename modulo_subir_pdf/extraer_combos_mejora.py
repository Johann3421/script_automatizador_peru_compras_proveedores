"""
extraer_combos_mejora.py — Extrae combinaciones del módulo MejoraBasica
========================================================================
Usa el login robusto de automation/login.py (que ya cierra modales, dispara
eventos Materialize, hace OCR y maneja ValidarAcceso).

Navega a /MejoraBasica, extrae los dropdowns de filtros
(Acuerdo, Catálogo, Categoría, Región, Provincia) y guarda en JSON.

Uso: python extraer_combos_mejora.py
"""
import json
import time
import sys
from datetime import datetime
from pathlib import Path

# Add parent dirs to path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

# Localizar Tesseract (si no está en PATH)
import os
TESSERACT_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]
for tp in TESSERACT_PATHS:
    if os.path.isfile(tp):
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = tp
        break

from playwright.sync_api import sync_playwright
from automation.browser import init_browser, close_browser
from automation.login import do_login
from utils.logger import LogWriter

OUTPUT_FILE = Path(__file__).parent / "dropdowns_mejora_basica.json"
URL = "https://www.catalogos.perucompras.gob.pe/MejoraBasica"

# Credenciales por defecto (las que puso el usuario)
USUARIO = "fernando.trinidad"
PASSWORD = "po!tLKB#8^r4e"


class PrintLog:
    def info(self, m): print(f"[{datetime.now().strftime('%H:%M:%S')}] {m}")
    def warn(self, m): print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚠ {m}")
    def error(self, m): print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ {m}")
    def ok(self, m): print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ {m}")


def read_select_options(page, selector):
    """Lee options de un <select>, filtra vacíos y value=0."""
    try:
        opts = page.evaluate(f"""
            () => {{
                const sel = document.querySelector('{selector}');
                if (!sel) return [];
                return Array.from(sel.options)
                    .map(o => ({{value: o.value, text: o.text}}))
                    .filter(o => o.value && o.value !== '0' && o.text.trim());
            }}
        """)
        return opts
    except Exception:
        return []


def wait_for_options(page, selector, timeout=20):
    """Espera a que un <select> tenga al menos 1 option válida."""
    try:
        page.wait_for_function(
            f"""() => {{
                const sel = document.querySelector('{selector}');
                if (!sel) return false;
                return Array.from(sel.options).filter(o => o.value && o.value !== '0').length >= 1;
            }}""",
            timeout=timeout * 1000,
        )
        return True
    except Exception:
        return False


def extraer_combos():
    log = PrintLog()
    stop = type('S', (), {'is_set': lambda s: False})()  # dummy stop event

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})

        # 1. Login robusto (igual al de la app principal)
        log.info("Iniciando login con credenciales del nuevo usuario...")
        if not do_login(page, USUARIO, PASSWORD, "", log, stop, None):
            log.error("Login falló, saliendo")
            browser.close()
            return

        log.ok(f"Login exitoso, navegando a {URL}...")

        # 2. Navegar a MejoraBasica
        page.goto(URL, wait_until="networkidle", timeout=60_000)
        time.sleep(3)

        # 3. Leer Acuerdos
        log.info("Leyendo Acuerdos...")
        acuerdos = read_select_options(page, "#ajaxAcuerdo")
        log.info(f"  {len(acuerdos)} acuerdos encontrados")

        combinaciones = []

        for ac_idx, acuerdo in enumerate(acuerdos):
            log.info(f"Acuerdo [{ac_idx+1}/{len(acuerdos)}]: {acuerdo['text'][:60]}")
            page.select_option("#ajaxAcuerdo", value=acuerdo["value"])
            time.sleep(2)
            wait_for_options(page, "#ajaxCatalogo", timeout=15)

            catalogos = read_select_options(page, "#ajaxCatalogo")
            log.info(f"  {len(catalogos)} catalogos")

            for cat in catalogos:
                page.select_option("#ajaxCatalogo", value=cat["value"])
                time.sleep(2)
                wait_for_options(page, "#ajaxCategoria", timeout=15)

                categorias = read_select_options(page, "#ajaxCategoria")
                log.info(f"    {len(categorias)} categorias en {cat['text'][:40]}")

                for cg in categorias:
                    page.select_option("#ajaxCategoria", value=cg["value"])
                    time.sleep(2)

                    # Leer Región y Provincia si existen
                    regiones = read_select_options(page, "#ajaxRegion, #ajaxDepartamento")
                    provincias = read_select_options(page, "#ajaxProvincia")

                    combinaciones.append({
                        "acuerdo": acuerdo,
                        "catalogo": cat,
                        "categoria": cg,
                        "regiones": regiones,
                        "provincias": provincias,
                    })
                    log.info(f"      OK {cg['text'][:40]} ({len(regiones)} regiones, {len(provincias)} provincias)")

        # 4. Guardar
        output = {
            "url": URL,
            "extracted_at": datetime.now().isoformat(),
            "total_combinaciones": len(combinaciones),
            "acuerdos": [{"value": a["value"], "text": a["text"]} for a in acuerdos],
            "combinaciones": combinaciones,
        }

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        log.ok(f"Guardado en {OUTPUT_FILE}")
        log.ok(f"   {len(combinaciones)} combinaciones extraídas")

        browser.close()


if __name__ == "__main__":
    extraer_combos()

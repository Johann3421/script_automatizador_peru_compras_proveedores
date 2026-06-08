"""
Extrae TODAS las opciones de los dropdowns en cascada del catalogo.
Genera catalog_options.json con la estructura completa.
"""
import json, time, threading, queue, os
from utils.logger import LogWriter
from automation.browser import init_browser, close_browser
from automation.login import do_login
from automation.navigation import _get_select_options, _select2_choose, _select_native

URL = "https://www.catalogos.perucompras.gob.pe/t_ProductoOfertadoAmp"
USUARIO = "estalin.huamali01"
PASSWORD = "PE/CyG6c&1R4T="


def extract_catalog(output_path="catalog_options.json"):
    log_queue = queue.Queue()
    log = LogWriter(log_queue)
    stop = threading.Event()
    pw, browser, page = init_browser(headless=False)

    try:
        print("=== Login ===")
        ok = do_login(page, USUARIO, PASSWORD, None, log, stop, max_retries=5)
        while not log_queue.empty():
            item = log_queue.get_nowait()
            print("  [%s] %s" % (item.get('level','?'), item.get('msg','')[:100]))

        if not ok:
            print("FALLO LOGIN. Abortando.")
            return None

        print("\n=== Navegando al catalogo ===")
        page.goto(URL, wait_until="networkidle")
        page.wait_for_load_state("domcontentloaded")
        time.sleep(3)

        page.evaluate("""
            document.querySelectorAll('.modal-backdrop, .modal.open, .modal.show, .swal2-container')
                .forEach(el => el.remove());
            document.body.style.overflow = '';
            document.body.classList.remove('modal-open');
        """)
        time.sleep(1)

        print("\n=== Extrayendo Acuerdos Marco ===")
        acuerdos = _get_select_options(page, "ajaxAcuerdo")
        acuerdos = [o for o in acuerdos if o["value"] != "0"]
        print("  Encontrados: %d" % len(acuerdos))
        for a in acuerdos:
            print("    %s: %s" % (a['value'], a['text'][:70]))

        catalogos_map = {}
        categorias_map = {}

        for acuerdo in acuerdos:
            val = acuerdo["value"]
            print("\n--- Acuerdo %s ---" % val)

            _select2_choose(page, "ajaxAcuerdo", val)
            time.sleep(3)

            catalogos = _get_select_options(page, "ajaxCatalogo")
            catalogos = [o for o in catalogos if o["value"] != "0"]
            catalogos_map[val] = catalogos
            print("  Catalogos: %d" % len(catalogos))

            for catalogo in catalogos:
                cval = catalogo["value"]
                print("    -> Catalogo %s: %s" % (cval, catalogo['text'][:40]))

                _select_native(page, "ajaxCatalogo", cval)
                time.sleep(3)

                categorias = _get_select_options(page, "ajaxCategoria")
                categorias = [o for o in categorias if o["value"] != "0"]
                categorias_map[cval] = categorias
                print("       %d categorias" % len(categorias))

        data = {
            "acuerdos": acuerdos,
            "catalogos": catalogos_map,
            "categorias": categorias_map,
        }
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("\n=== Guardado en %s ===" % output_path)
        return data

    finally:
        close_browser(pw, browser)


if __name__ == "__main__":
    extract_catalog()
    print("\nListo.")

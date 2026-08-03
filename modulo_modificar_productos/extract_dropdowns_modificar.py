"""
extract_dropdowns_modificar.py — Extrae TODAS las combinaciones de dropdowns
de t_CatalogoProductoMarca y las guarda en un JSON para la UI.

Ejecutar:  python extract_dropdowns_modificar.py

El script:
  1. Abre el browser y hace login
  2. Navega a t_CatalogoProductoMarca
  3. Detecta TODOS los <select> del DOM
  4. Extrae opciones de cada nivel
  5. Selecciona la primera opción y espera que carguen las opciones hijas
  6. Explora recursivamente (opción por opción) solo el primer nivel
  7. Guarda dropdown_options_modificar.json con la estructura:

     {
       "url": "...",
       "selects": {
         "id_del_select": {
           "name": "label visible si existe",
           "options": [{"value": "...", "text": "..."}, ...],
           "children": {
             "id_hijo": {
               "options": [...],
               "children": { ... }
             }
           }
         }
       }
     }
"""
import sys
import os
import json
import time
import re

from playwright.sync_api import TimeoutError as PlaywrightTimeout

_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_MODULE_DIR, ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from automation.browser import init_browser, close_browser
from automation.login import do_login
from utils.logger import LogWriter
import queue
import threading

# ── CONFIG ────────────────────────────────────────────────────────────────────
USUARIO  = "almerco.01"
PASSWORD = "KY300582@$"
TARGET_URL = "https://www.catalogos.perucompras.gob.pe/t_CatalogoProductoMarca"
OUTPUT_FILE = os.path.join(_MODULE_DIR, "dropdown_options_modificar.json")

MAX_LEVELS = 5     # Máxima profundidad de cascada
WAIT_OPTIONS = 20  # Segundos máximos esperando que carguen opciones hijas
MAX_PARENT_TRIES = 5  # Cuántas opciones del primer nivel probar si no cargan hijos

log_queue = queue.Queue()
log = LogWriter(log_queue)


def ts():
    return time.strftime("%H:%M:%S")


def info(msg):
    print(f"[{ts()}] {msg}")


def _get_select_ids(page) -> list[str]:
    """Retorna todos los IDs de <select> visibles en la página."""
    return page.evaluate("""
        (() => {
            const ids = [];
            document.querySelectorAll('select[id]').forEach(sel => {
                if (sel.offsetParent !== null) ids.push(sel.id);
            });
            return ids;
        })()
    """)


def _get_options(page, select_id: str) -> list[dict]:
    """Extrae opciones de un select, filtrando valores vacíos y placeholders."""
    options = page.evaluate(f"""
        (() => {{
            var sel = document.getElementById('{select_id}');
            if (!sel) return [];
            return Array.from(sel.options).map(o => ({{value: o.value, text: (o.text || '').trim()}}));
        }})()
    """)
    return [o for o in (options or []) if o["value"] and o["value"] != "0"]


def _select_option(page, select_id: str, value: str):
    """Selecciona una opción en un select (Select2-aware)."""
    # Método 1: JS directo + eventos
    page.evaluate(f"""
        var sel = document.getElementById('{select_id}');
        if (sel) {{
            sel.value = '{value}';
            sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
            sel.dispatchEvent(new Event('input', {{ bubbles: true }}));
            if (typeof $ !== 'undefined' && $(sel).data('select2')) {{
                $(sel).trigger('change.select2');
                $(sel).trigger('select2:select');
            }}
        }}
    """)
    time.sleep(2)

    # Método 2: Click en el widget Select2 y seleccionar de la lista desplegable
    try:
        # Hacer click en el contenedor para abrir el dropdown
        page.click(f"#{select_id}", force=True, timeout=3000)
        time.sleep(1)
        page.locator("#select2-" + select_id + "-container").first.click(force=True, timeout=2000)
        time.sleep(0.5)
        # Buscar y clickear la opcion en el dropdown de Select2
        options_list = page.locator("li.select2-results__option")
        count = options_list.count()
        if count > 0:
            for i in range(min(count, 50)):
                opt = options_list.nth(i)
                if opt.is_visible():
                    opt_text = opt.text_content().strip()
                    if value in opt.get_attribute("id") or opt.get_attribute("id") == f"{select_id}-{value}":
                        opt.click(force=True, timeout=2000)
                        break
            else:
                # Si no encontro por ID, hacer click en la primera visible
                for i in range(min(count, 5)):
                    if options_list.nth(i).is_visible():
                        options_list.nth(i).click(force=True, timeout=2000)
                        break
    except Exception:
        pass

    time.sleep(2)


def _wait_for_child_options(page, child_id: str, timeout: int = WAIT_OPTIONS) -> list[dict]:
    """Espera hasta que el select hijo tenga opciones reales."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        opts = _get_options(page, child_id)
        if opts:
            return opts
        time.sleep(0.8)
    return []


def explore_level(page, select_ids: list[str], depth: int, parent_value: str = "") -> dict:
    """
    Dado un nivel, extrae TODAS las opciones del select actual.
    Para la PRIMERA opción, explora recursivamente el siguiente nivel.
    Solo profundiza con la primera opción de cada nivel (para que sea rápido).
    """
    if depth >= len(select_ids):
        return {}

    current_id = select_ids[depth]
    info(f"  {'  ' * depth}Nivel {depth+1}: select #{current_id}")

    options = _get_options(page, current_id)
    if not options:
        options = _wait_for_child_options(page, current_id)
    if not options:
        info(f"  {'  ' * depth}  → sin opciones")
        return {}

    info(f"  {'  ' * depth}  → {len(options)} opciones")

    # Construir el label del select (buscar un <label> asociado)
    label = page.evaluate(f"""
        (() => {{
            var sel = document.getElementById('{current_id}');
            if (!sel) return '';
            var label = document.querySelector("label[for='{current_id}']");
            if (label) return (label.textContent || '').trim();
            var prev = sel.previousElementSibling;
            if (prev && prev.tagName === 'LABEL') return (prev.textContent || '').trim();
            return '';
        }})()
    """)

    result = {
        "id": current_id,
        "label": label,
        "options": options,
        "children": {},
    }

    # Explorar siguiente nivel con algunas opciones del nivel actual
    if depth + 1 < len(select_ids) and options:
        child_id = select_ids[depth + 1]
        tries = min(MAX_PARENT_TRIES, len(options))

        for t in range(tries):
            opt = options[t]
            info(f"  {'  ' * depth}  → Probando opcion {t+1}/{tries}: '{opt['text'][:50]}'...")
            _select_option(page, current_id, opt["value"])
            time.sleep(3)

            child_opts = _wait_for_child_options(page, child_id, timeout=WAIT_OPTIONS)
            if child_opts:
                info(f"  {'  ' * depth}  → {len(child_opts)} opciones hijas cargadas!")
                result["children"] = explore_level(page, select_ids, depth + 1, opt["value"])
                break
            else:
                info(f"  {'  ' * depth}  → Sin opciones hijas con esta opcion, probando siguiente...")
        else:
            info(f"  {'  ' * depth}  → Ninguna de las {tries} opciones cargo hijos.")

    return result


def _retry_goto(page, url, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            info(f"[goto] intento {attempt}/{max_retries} → {url[:80]}...")
            page.goto(url, wait_until="domcontentloaded", timeout=60_000 * attempt)
            page.wait_for_selector("body", timeout=30_000)
            info("[goto] OK")
            return True
        except PlaywrightTimeout:
            info(f"[goto] Timeout intento {attempt}")
            if attempt < max_retries:
                time.sleep(3 * attempt)
    return False


def main():
    info("=" * 60)
    info("  EXTRACTOR DE DROPDOWNS — t_CatalogoProductoMarca")
    info("=" * 60)

    info("Iniciando browser...")
    pw, browser, page = init_browser(headless=False)
    stop_event = threading.Event()

    try:
        info("Login...")
        ok = do_login(page, USUARIO, PASSWORD, "", log, stop_event, captcha_bridge=None)
        if not ok:
            info("ERROR: Login fallido")
            return

        info("Navegando a t_CatalogoProductoMarca...")
        if not _retry_goto(page, TARGET_URL):
            info("ERROR: No se pudo cargar la página")
            return

        time.sleep(3)

        # ── Cerrar modales colgados ──
        page.evaluate("""
            document.querySelectorAll(
                '.modal-backdrop, .modal.open, .modal.show, '
                + '.swal2-container, #_wModal_bg'
            ).forEach(el => el.remove());
            document.body.style.overflow = '';
            document.body.classList.remove('modal-open');
        """)
        time.sleep(1)

        # ── Detectar selects ──
        select_ids = _get_select_ids(page)
        info(f"\nSelects detectados: {len(select_ids)}")
        for sid in select_ids:
            info(f"  → #{sid}")

        if not select_ids:
            info("No se detectaron selects. ¿Está cargada la página correcta?")
            return

        # ── Extraer recursivamente ──
        info("\nExtrayendo opciones (explorando cascada con primera opción)...")
        structure = {
            "url": TARGET_URL,
            "select_ids_order": select_ids,
            "levels": {},
        }

        result = explore_level(page, select_ids, 0)
        structure["levels"][result["id"]] = result

        # ── Guardar ──
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(structure, f, indent=2, ensure_ascii=False)
        info(f"\nGuardado en: {OUTPUT_FILE}")
        info(f"Total opciones extraídas por nivel:")
        for sid, lvl in structure["levels"].items():
            info(f"  {sid}: {len(lvl.get('options',[]))} opciones")

    except Exception as e:
        info(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

    finally:
        info("\nCerrando browser...")
        try:
            page.wait_for_timeout(2000)
        except Exception:
            pass
        close_browser(pw, browser)
        info("Listo.")


if __name__ == "__main__":
    main()

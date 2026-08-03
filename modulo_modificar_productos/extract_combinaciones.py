"""
extract_combinaciones.py — Extrae TODAS las combinaciones de dropdowns
para un Acuerdo Marco específico: EXT-CE-2022-5.

Recorre exhaustivamente:
  Acuerdo → cada Catálogo → cada Categoría → cada Estado

Guarda en: combinaciones_computadoras.json
"""
import sys
import os
import json
import time

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
TARGET_ACUERDO = "EXT-CE-2022-5"
OUTPUT_FILE = os.path.join(_MODULE_DIR, "combinaciones_computadoras.json")

WAIT_TIMEOUT = 20  # segundos max esperando opciones hijas

log_queue = queue.Queue()
log = LogWriter(log_queue)


def ts():
    return time.strftime("%H:%M:%S")


def info(msg):
    print(f"[{ts()}] {msg}")


def _get_options(page, select_id: str) -> list[dict]:
    options = page.evaluate(f"""
        (() => {{
            var sel = document.getElementById('{select_id}');
            if (!sel) return [];
            return Array.from(sel.options).map(o => ({{value: o.value, text: (o.text || '').trim()}}));
        }})()
    """)
    return [o for o in (options or []) if o["value"] and o["value"] != "0"]


def _select_value(page, select_id: str, value: str):
    """Selecciona opcion (Select2-aware)."""
    # JS directo
    page.evaluate(f"""
        var sel = document.getElementById('{select_id}');
        if (sel) {{
            sel.value = '{value}';
            sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
            sel.dispatchEvent(new Event('input', {{ bubbles: true }}));
            if (typeof $ !== 'undefined' && $(sel).data('select2')) {{
                $(sel).trigger('change.select2');
            }}
        }}
    """)
    time.sleep(2)

    # Click en Select2 widget
    try:
        page.click(f"#{select_id}", force=True, timeout=3000)
        time.sleep(0.8)
        container = f"#select2-{select_id}-container"
        page.locator(container).first.click(force=True, timeout=3000)
        time.sleep(0.5)
        options_list = page.locator("li.select2-results__option")
        count = options_list.count()
        for i in range(min(count, 100)):
            opt = options_list.nth(i)
            if opt.is_visible():
                opt_id = opt.get_attribute("id") or ""
                if value in opt_id or opt_id.endswith(f"-{value}"):
                    opt.click(force=True, timeout=2000)
                    break
    except Exception:
        pass
    time.sleep(2)


def _wait_options(page, select_id: str, timeout: int = WAIT_TIMEOUT) -> list[dict]:
    deadline = time.time() + timeout
    while time.time() < deadline:
        opts = _get_options(page, select_id)
        if opts:
            return opts
        time.sleep(0.8)
    return []


def explore_level(page, select_order: list[str], depth: int,
                 options: list[dict]) -> list[dict]:
    """
    Recorre exhaustivamente. Para CADA opcion en el nivel actual:
      - la selecciona
      - espera que carguen opciones en el SIGUIENTE nivel
      - llama recursivamente
    select_order: lista ordenada de IDs (ej. ['ajaxCatalogo','ajaxCategoria','ajaxEstado'])
    depth: indice actual dentro de select_order
    """
    results = []
    current_id = select_order[depth]
    total = len(options)
    indent = "  " * depth

    for i, opt in enumerate(options):
        text = opt["text"][:70]
        info(f"{indent}[{current_id}] {i+1}/{total}: '{text}'")

        _select_value(page, current_id, opt["value"])

        node = {"value": opt["value"], "text": opt["text"]}

        # Hay siguiente nivel?
        if depth + 1 < len(select_order):
            next_id = select_order[depth + 1]
            child_opts = _wait_options(page, next_id)
            if child_opts:
                info(f"{indent}  → {len(child_opts)} opciones en {next_id}")
                node["children"] = explore_level(page, select_order, depth + 1, child_opts)
            else:
                info(f"{indent}  → sin opciones en {next_id}")

        results.append(node)
    return results


def _get_select_ids(page) -> list[str]:
    return page.evaluate("""
        (() => {
            const ids = [];
            document.querySelectorAll('select[id]').forEach(sel => {
                if (sel.offsetParent !== null) ids.push(sel.id);
            });
            return ids;
        })()
    """)


def _retry_goto(page, url, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            info(f"[goto] intento {attempt}/{max_retries}...")
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
    info(f"  EXTRACTOR DE COMBINACIONES — {TARGET_ACUERDO}")
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

        info("Navegando...")
        if not _retry_goto(page, TARGET_URL):
            info("ERROR: No se pudo cargar")
            return

        time.sleep(2)
        page.evaluate("""
            document.querySelectorAll('.modal-backdrop,.modal.open,.modal.show,.swal2-container,#_wModal_bg')
            .forEach(el => el.remove());
            document.body.classList.remove('modal-open');
        """)
        time.sleep(1)

        # ── Buscar el Acuerdo objetivo ──
        all_selects = _get_select_ids(page)
        info(f"Selects detectados: {all_selects}")

        acuerdo_opts = _get_options(page, "ajaxAcuerdo")
        info(f"Acuerdos disponibles: {len(acuerdo_opts)}")

        target = None
        for opt in acuerdo_opts:
            if TARGET_ACUERDO in opt["text"]:
                target = opt
                break

        if not target:
            info(f"ERROR: No se encontro '{TARGET_ACUERDO}' entre los acuerdos")
            info(f"Primeros 5: {[o['text'][:60] for o in acuerdo_opts[:5]]}")
            return

        info(f"Acuerdo encontrado: {target['text'][:80]} (value={target['value']})")

        # ── Seleccionar y esperar hijos ──
        _select_value(page, "ajaxAcuerdo", target["value"])
        time.sleep(3)

        remaining = _get_select_ids(page)
        info(f"Selects post-acuerdo: {remaining}")

        # Determinar orden de los selects restantes
        next_ids = [s for s in remaining if s != "ajaxAcuerdo"]
        info(f"Orden de exploracion: {next_ids}")

        if not next_ids:
            info("ERROR: No hay selects hijos")
            return

        catalog_opts = _wait_options(page, next_ids[0])
        if not catalog_opts:
            info("ERROR: No cargaron catalogos")
            return

        info(f"\nExplorando {len(catalog_opts)} catalogos en cascada completa...")
        tree = explore_level(page, next_ids, 0, catalog_opts)

        # ── Guardar ──
        output = {
            "acuerdo": {"value": target["value"], "text": target["text"]},
            "selects_order": next_ids,
            "combinaciones": tree,
            "total_catalogos": len(catalog_opts),
        }
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        info(f"\nGuardado en: {OUTPUT_FILE}")
        info(f"Total catalogos explorados: {len(tree)}")

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

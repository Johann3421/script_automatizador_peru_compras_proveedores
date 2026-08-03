"""
intercept_modificar.py — Captura automática de endpoints HTTP
Ejecuta el flujo completo automáticamente y captura todos los POST requests.
Genera captured_modificar.json con los endpoints descubiertos.
"""
import sys
import os
import json
import time
import threading
import queue
from datetime import datetime
from urllib.parse import parse_qs

_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_MODULE_DIR, ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from automation.browser import init_browser, close_browser
from automation.login import do_login
from utils.logger import LogWriter

# ── CONFIG ───────────────────────────────────────────────────────
USUARIO  = "almerco.03"
PASSWORD = "4lm3rKenYa@#"

GESTION_URL = "https://www.catalogos.perucompras.gob.pe/t_CatalogoProductoMarca"
OUTPUT_FILE = os.path.join(_MODULE_DIR, "captured_modificar.json")

FILTROS = {
    "acuerdo":   "249",
    "catalogo":  "252",
    "categoria": "11735",
    "estado":    "OBSERVADO",
}

PARTE_PRUEBA = "GMC9M6S034V4"
PDF_DIR = r"D:\SISTEMAS 02\Downloads\COMPUTADORAS\COMPUTADORAS"

# ── Log ──────────────────────────────────────────────────────────
log_queue = queue.Queue()
log = LogWriter(log_queue)

def ts():
    return datetime.now().strftime("%H:%M:%S")

def info(msg):
    print(f"[{ts()}] {msg}")

# ── Interceptor ──────────────────────────────────────────────────
all_requests = []
target_requests = []

def on_request(request):
    url = request.url
    method = request.method
    if "perucompras" not in url.lower():
        return

    try:
        post_data = request.post_data
    except Exception:
        post_data = None

    entry = {
        "timestamp": datetime.now().isoformat(),
        "method": method,
        "url": url,
        "headers": dict(request.headers),
        "post_data_raw": post_data,
        "post_data_parsed": None,
        "post_data_format": None,
        "category": None,
    }

    if post_data:
        try:
            entry["post_data_parsed"] = json.loads(post_data)
            entry["post_data_format"] = "json"
        except Exception:
            try:
                parsed = parse_qs(post_data)
                entry["post_data_parsed"] = {k: v[0] if len(v) == 1 else v for k, v in parsed.items()}
                entry["post_data_format"] = "form-encoded"
            except Exception:
                entry["post_data_format"] = "raw"

    url_low = url.lower()
    if "upload" in url_low or "adjfile" in url_low or "pdf" in url_low or "archivo" in url_low:
        entry["category"] = "UPLOAD_PDF"
    elif "guardar" in url_low or "save" in url_low or "/edit" in url_low.split("?")[0]:
        entry["category"] = "GUARDAR"
    elif "caracteristica" in url_low or "cert" in url_low or "homolog" in url_low:
        entry["category"] = "CERTIFICACIONES"
    elif "buscar" in url_low or "lista" in url_low or "json" in url_low:
        entry["category"] = "BUSQUEDA_TABLA"

    if method == "POST" and post_data:
        target_requests.append(entry)
        info(f"🎯 POST [{entry['category'] or 'OTHER'}] {method} {url[:120]}")
        ct = request.headers.get("content-type", "")
        if "multipart" in ct.lower():
            info(f"   Content-Type: MULTIPART/FORM-DATA")
        info(f"   Body preview: {post_data[:400]}")
        print()

    all_requests.append(entry)


def save_results(page):
    output = {
        "captured_at": datetime.now().isoformat(),
        "current_url": page.url if not page.is_closed() else "N/A",
        "summary": {
            "total_requests": len(all_requests),
            "post_requests": len(target_requests),
        },
        "POST_REQUESTS": target_requests,
        "GET_REQUESTS": [r for r in all_requests if r["method"] == "GET" and "catalogoproducto" in r["url"].lower()],
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    info(f"💾 {len(target_requests)} POSTs capturados → {OUTPUT_FILE}")


# ── Flujo automático ─────────────────────────────────────────────

def main():
    info("=" * 60)
    info("  INTERCEPTOR AUTOMÁTICO — Modificar Productos")
    info("=" * 60)

    pw = browser = None
    stop = threading.Event()

    try:
        info("Iniciando browser...")
        pw, browser, page = init_browser(headless=False)

        page.on("request", on_request)
        page.set_viewport_size({"width": 1920, "height": 1080})

        # ── Login ──
        info("Login...")
        ok = do_login(page, USUARIO, PASSWORD, "", log, stop, captcha_bridge=None)
        if not ok:
            info("✗ Login fallido")
            save_results(page)
            return
        info("✓ Login OK")

        # ── Navegar a gestión ──
        info(f"Navegando a t_CatalogoProductoMarca...")
        page.goto(GESTION_URL, wait_until="networkidle", timeout=60_000)
        time.sleep(3)

        # ── Importar funciones del flujo ──
        from automation_mod.navegacion_productos import (
            apply_dropdowns_and_search,
            buscar_por_parte, click_editar,
            subir_pdf_en_edicion, guardar_cambios,
            agregar_caracteristicas, volver_a_lista,
        )

        # ── Aplicar dropdowns + Buscar ──
        info("Aplicando dropdowns y Buscar...")
        result = apply_dropdowns_and_search(page, FILTROS, log, stop)
        info(f"Resultado búsqueda: {result}")

        # ── Buscar producto ──
        parte = PARTE_PRUEBA
        ruta_pdf = os.path.join(PDF_DIR, f"{parte}.pdf")
        info(f"Buscando: {parte}")
        ok = buscar_por_parte(page, parte, log, stop)
        if not ok:
            info("✗ Producto no encontrado")
            save_results(page)
            return

        # ── Editar ──
        info("Click Editar...")
        ok = click_editar(page, log, stop)
        if not ok:
            info("✗ No se pudo abrir edición")
            save_results(page)
            return

        # ── Subir PDF ──
        info(f"Subiendo PDF: {ruta_pdf}")
        ok = subir_pdf_en_edicion(page, ruta_pdf, log, stop)
        if not ok:
            info("✗ No se pudo subir PDF")
            save_results(page)
            return

        # ── Guardar ──
        info("Click Guardar...")
        ok = guardar_cambios(page, log, stop)
        if not ok:
            info("✗ Error al guardar")
            save_results(page)
            return

        # ── Certificaciones ──
        info("Añadiendo ISO 9001 + ISO 14001...")
        cert_result = agregar_caracteristicas(page, log, stop)
        info(f"Certs: añadidas={cert_result.get('added')} saltadas={cert_result.get('skipped')}")

        # ── Retornar ──
        info("Click Retornar...")
        volver_a_lista(page, log, stop)

        info("\n✓ FLUJO COMPLETO EJECUTADO")
        info("Revisá captured_modificar.json")

        time.sleep(3)
        save_results(page)

    except Exception as e:
        info(f"Error: {e}")
        import traceback
        traceback.print_exc()
        try:
            save_results(page)
        except Exception:
            pass
    finally:
        if browser and pw:
            try:
                close_browser(pw, browser)
            except Exception:
                pass
        info("Listo.")


if __name__ == "__main__":
    main()

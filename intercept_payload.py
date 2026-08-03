"""
INTERCEPT PAYLOAD — Peru Compras
=================================
Usa la automatización existente para llegar hasta la página de edición de ofertas,
luego intercepta el request XHR que se dispara al hacer click en "Enviar oferta"
(#btn_enviarOferta2) para capturar el payload JSON exacto.

ASÍ se descubre el formato que necesitamos para la subida masiva.

USO:
    1. Editar USUARIO / PASSWORD líneas 37-38 si son distintas
    2. python intercept_payload.py
    3. Cuando se abra el browser, el script hará login y catálogo automáticamente
    4. Aparecerá el catálogo de productos — ingresá MANUALMENTE 2-3 precios
    5. Hacé click en "Enviar oferta"
    6. El payload se captura automáticamente y se guarda en captured_payload.json

Basado en: automation/browser.py, automation/login.py, automation/navigation.py
"""
import sys, os, json, time, re
from datetime import datetime
from urllib.parse import parse_qs

# ── Asegurar imports desde el proyecto ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from automation.browser import init_browser, close_browser
from automation.login import do_login
from automation.navigation import setup_catalog_search, _retry_goto, CATALOGO_INDEX_URL
from utils.logger import LogWriter
import queue, threading

# ── EDITAR AQUÍ si las credenciales son diferentes ──
USUARIO  = "estalin.huamali01"
PASSWORD = "PE/CyG6c&1R4T="

OUTPUT_FILE = "captured_payload.json"

# ── Patrones de URL que nos interesan ──
TARGET_PATTERNS = [
    "EnviarOferta", "GuardarOferta", "ActualizarOferta",
    "SaveOferta", "RegistrarOferta", "Oferta",
    "Precio", "GuardarPrecio", "ActualizarPrecio",
    "btn_enviarOferta",
]

captured_requests = []
all_xhr = []
log_queue = queue.Queue()
log = LogWriter(log_queue)


def log_msg(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")


def is_interesting(url: str, method: str, post_data: str | None) -> bool:
    if method != "POST" or not post_data:
        return False
    url_lower = url.lower()
    for pat in TARGET_PATTERNS:
        if re.search(pat, url_lower, re.IGNORECASE):
            return True
    if "perucompras" in url_lower:
        return True
    return False


def save_results():
    output = {
        "captured_at": datetime.now().isoformat(),
        "summary": {
            "total_xhr_requests": len(all_xhr),
            "target_requests_captured": len(captured_requests),
        },
        "TARGET_REQUESTS": captured_requests,
        "all_perucompras_post_requests": [
            r for r in all_xhr
            if r["method"] == "POST" and r.get("post_data_raw")
        ],
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    log_msg(f"  💾 Guardado en '{OUTPUT_FILE}'")
    log_msg(f"     → {len(captured_requests)} requests objetivo")
    log_msg(f"     → {len(output['all_perucompras_post_requests'])} POST totales")


def main():
    log_msg("=" * 60)
    log_msg("  INTERCEPTOR DE PAYLOAD — Peru Compras")
    log_msg("  Basado en la automatización existente")
    log_msg("=" * 60)
    log_msg(f"  Output: {OUTPUT_FILE}")
    log_msg("=" * 60)

    # ── 1. Inicializar browser ──
    log_msg("Iniciando browser...")
    pw, browser, page = init_browser(headless=False)

    # ── 2. Setup del interceptor de requests ──
    def on_request(request):
        url = request.url
        method = request.method
        if "perucompras" not in url.lower():
            return
        try:
            post_data = request.post_data
        except:
            post_data = None

        entry = {
            "timestamp": datetime.now().isoformat(),
            "method": method,
            "url": url,
            "headers": dict(request.headers),
            "post_data_raw": post_data,
            "post_data_parsed": None,
            "is_target": False,
        }

        if post_data:
            try:
                entry["post_data_parsed"] = json.loads(post_data)
                entry["post_data_format"] = "json"
            except:
                try:
                    entry["post_data_parsed"] = parse_qs(post_data)
                    entry["post_data_format"] = "form-encoded"
                except:
                    entry["post_data_format"] = "raw"

        if is_interesting(url, method, post_data):
            entry["is_target"] = True
            captured_requests.append(entry)
            log_msg(f"\n{'='*50}")
            log_msg(f"  🎯 REQUEST OBJETIVO CAPTURADO!")
            log_msg(f"     URL: {url}")
            log_msg(f"     Method: {method}")
            ct = request.headers.get("content-type", "N/A")
            log_msg(f"     Content-Type: {ct}")
            if post_data:
                log_msg(f"     Body ({len(post_data)} chars):")
                log_msg(f"     {post_data[:1000]}")
            log_msg(f"{'='*50}\n")
            save_results()

        if method in ("POST", "PUT", "PATCH"):
            log_msg(f"  [XHR] {method} {url[:100]}")

        all_xhr.append(entry)

    page.on("request", on_request)

    # ── 3. Login ──
    log_msg("Haciendo login en Peru Compras...")
    stop_event = threading.Event()
    ok = do_login(page, USUARIO, PASSWORD, "", log, stop_event, captcha_bridge=None)
    if not ok:
        log_msg("✗ Login fallido. Abortando.")
        close_browser(pw, browser)
        sys.exit(1)
    log_msg("✓ Login exitoso!")

    # ── 4. Setup catálogo (con valores por defecto del JSON) ──
    #     Cargar catalog_options.json para obtener los valores pre-seleccionados
    json_path = os.path.join(BASE_DIR, "catalog_options.json")
    if os.path.isfile(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            catalog_data = json.load(f)
        acuerdos = catalog_data.get("acuerdos", [])
        if acuerdos:
            acuerdo_val = acuerdos[0]["value"]
            catalogos = catalog_data.get("catalogos", {}).get(acuerdo_val, [])
            catalogo_val = catalogos[0]["value"] if catalogos else ""
            categorias = catalog_data.get("categorias", {}).get(catalogo_val, [])
            categoria_val = categorias[0]["value"] if categorias else ""
            pre_selected = {
                "acuerdo": acuerdo_val,
                "catalogo": catalogo_val,
                "categoria": categoria_val,
            }
            log_msg(f"Usando pre-seleccionados del JSON: {pre_selected}")
        else:
            pre_selected = {}
    else:
        log_msg("⚠  No se encontró catalog_options.json, se usará el bridge")
        pre_selected = {}

    result = setup_catalog_search(page, log, catalog_bridge=None, pre_selected=pre_selected)
    if not result:
        log_msg("✗ Configuración de catálogo fallida. Abortando.")
        close_browser(pw, browser)
        sys.exit(1)
    log_msg(f"✓ Catálogo configurado: {result}")

    # ── 5. Instrucciones al usuario ──
    log_msg("\n" + "=" * 60)
    log_msg("  BROWSER LISTO — PASOS MANUALES:")
    log_msg("=" * 60)
    log_msg("  1. En la tabla de productos, ingresá 2-3 precios")
    log_msg("     (buscá productos si es necesario con #C_Descripcion)")
    log_msg("  2. Hacé click en 'Enviar oferta' (#btn_enviarOferta2)")
    log_msg("  3. El payload se capturará AUTOMÁTICAMENTE")
    log_msg("  4. Ctrl+C para salir después de capturar")
    log_msg("=" * 60)
    log_msg("  Esperando interacción...\n")

    # ── 6. Loop de espera (el browser está visible) ──
    try:
        while not page.is_closed():
            time.sleep(1)
    except KeyboardInterrupt:
        log_msg("\nCtrl+C — guardando y saliendo...")
    except Exception as e:
        log_msg(f"Error: {e}")
    finally:
        save_results()
        try:
            close_browser(pw, browser)
        except:
            pass


if __name__ == "__main__":
    main()

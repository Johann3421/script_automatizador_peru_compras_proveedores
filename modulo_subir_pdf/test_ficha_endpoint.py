"""
test_ficha_endpoint.py — Descubre de dónde se extraen las fichas en t_CatalogoProductoMarca
"""
import sys, time, threading, json
sys.path.insert(0, '.')
sys.path.insert(0, 'modulo_subir_pdf')

from automation.browser import init_browser, close_browser
from automation.login import do_login
from utils.logger import LogWriter

class PrintLog:
    def info(self, m): print(f"[INFO] {m}")
    def warn(self, m): print(f"[WARN] {m}")
    def error(self, m): print(f"[ERR]  {m}")
    def ok(self, m): print(f"[OK]   {m}")

def main():
    log = PrintLog()
    stop = threading.Event()
    pw, browser, page = init_browser(headless=False)
    try: page.set_viewport_size({"width": 1920, "height": 1080})
    except Exception: pass
    try:
        if not do_login(page, "almerco.03", "4lm3rKenYa@#", "", log, stop):
            log.error("Login falló"); return
        log.ok("Login OK")

        # Capturar TODAS las requests/responses
        captured = []
        def on_request(req):
            if "catalogos.perucompras" in req.url and "cdn" not in req.url:
                captured.append({
                    "type": "request", "method": req.method, "url": req.url,
                    "resource": req.resource_type,
                    "post_data": (req.post_data or "")[:500] if req.post_data else ""
                })
        def on_response(res):
            url = res.url
            if "catalogos.perucompras" in url and "cdn" not in url and res.request.resource_type in ("xhr", "fetch"):
                try:
                    body = res.text() if res.status == 200 else ""
                except Exception:
                    body = "<no body>"
                captured.append({
                    "type": "response", "method": res.request.method, "url": url,
                    "status": res.status, "content_type": res.headers.get("content-type", ""),
                    "body_preview": body[:500]
                })
        page.on("request", on_request)
        page.on("response", on_response)

        # Navegar a la ruta objetivo
        url = "https://www.catalogos.perucompras.gob.pe/t_CatalogoProductoMarca?N_Acuerdo=249&N_Catalogo=252&N_Categoria=11735&C_EstadoNav=OBSERVADO"
        log.info(f"Navegando a {url}")
        page.goto(url, wait_until="networkidle", timeout=60_000)
        time.sleep(5)

        # Imprimir las requests/responses interesantes
        print(f"\n=== CAPTURADAS {len(captured)} requests/responses ===")
        for c in captured:
            if c["type"] == "response":
                print(f"\n[{c['type']}] {c['method']} {c['url']}")
                print(f"  status: {c['status']}, content-type: {c['content_type']}")
                print(f"  body_preview: {c['body_preview'][:400]}")
            else:
                if c["resource"] in ("xhr", "fetch", "document"):
                    print(f"\n[{c['type']}] {c['method']} {c['url']}")
                    if c.get("post_data"):
                        print(f"  post: {c['post_data'][:300]}")

        input("\n[Enter para cerrar]")
    finally:
        try: close_browser(pw, browser)
        except Exception: pass

if __name__ == "__main__":
    main()

"""
test_buscar_ficha.py — Explorar cómo PeruCompras busca por N° de ficha.

Probar varios métodos:
1. API _CatalogoProductoIndex con C_Descripcion=ficha
2. API _CatalogoProductoIndex con C_ID_Producto=ficha
3. API _CatalogoProductoIndex con C_Ficha=ficha
4. API con N_ID_Producto=ficha
5. POST a la página de gestión con form-encoded data
6. Interceptar la URL que usa la UI cuando busca por N° de parte y replicar con ficha
"""
import sys
import os
import re
import time
import threading
import json

_THIS = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_THIS, ".."))
sys.path.insert(0, _ROOT)
sys.path.insert(0, _THIS)

from automation.browser import init_browser, close_browser
from automation.login import do_login

BASE = "https://www.catalogos.perucompras.gob.pe"
URL_TABLA = f"{BASE}/t_CatalogoProductoMarca/_CatalogoProductoIndex"
URL_GESTION = f"{BASE}/t_CatalogoProductoMarca"

# Una ficha conocida del Excel
FICHA_TEST = "2267958"
PARTE_TEST = "EMU5R6000"


class PrintLog:
    def info(self, m): print(f"[INFO] {m}")
    def warn(self, m): print(f"[WARN] {m}")
    def error(self, m): print(f"[ERR]  {m}")
    def ok(self, m): print(f"[OK]   {m}")


def probar_api_con_param(page, nombre, params, log):
    """Probar el API con un set de params y reportar resultado."""
    log.info(f"\n=== Test: {nombre} ===")
    log.info(f"  Params: {params}")
    try:
        url = URL_TABLA
        sep = "?"
        for k, v in params.items():
            url += f"{sep}{k}={v}"
            sep = "&"
        url += f"&_={int(time.time()*1000)}"
        resp = page.request.get(url, timeout=30_000)
        html = resp.text()
        log.info(f"  Status: {resp.status}, bytes: {len(html)}")
        # Buscar IDs
        ids = re.findall(r"ID_CatalogoProducto=(\d+)", html)
        log.info(f"  IDs encontrados: {ids[:3] if ids else 'NINGUNO'}")
        # Buscar JSON
        try:
            data = json.loads(html)
            if isinstance(data, dict):
                log.info(f"  JSON keys: {list(data.keys())[:5]}")
                if "data" in data or "aaData" in data:
                    records = data.get("data", data.get("aaData", []))
                    log.info(f"  Records: {len(records)}")
                    if records:
                        log.info(f"  Primer record: {records[0]}")
        except Exception:
            pass
        # Mostrar primeros 300 chars
        preview = html[:300].replace("\n", " ").replace("\r", " ")
        log.info(f"  Preview: {preview}")
        return len(ids) > 0
    except Exception as e:
        log.warn(f"  Error: {e}")
        return False


def interceptar_busqueda_real(page, log):
    """Interceptar la búsqueda real que hace la UI cuando se busca por N° de parte."""
    log.info("\n=== Interceptando búsqueda real de la UI ===")
    # Ir a la página de gestión
    page.goto(URL_GESTION, wait_until="networkidle", timeout=60_000)
    time.sleep(2)

    # Aplicar dropdowns mínimos
    from automation_mod.navegacion_productos import _select2_select
    try:
        _select2_select(page, "ajaxAcuerdo", "249")
        time.sleep(1.5)
        _select2_select(page, "ajaxCatalogo", "252")
        time.sleep(1.5)
        _select2_select(page, "ajaxCategoria", "11735")
        time.sleep(1.5)
        _select2_select(page, "ajaxEstado", "OBSERVADO")
        time.sleep(1.5)
    except Exception as e:
        log.warn(f"  Dropdowns: {e}")

    # Capturar requests de la página
    requests_captured = []
    def on_request(req):
        if "_CatalogoProductoIndex" in req.url or "CatalogoProducto" in req.url:
            requests_captured.append({
                "url": req.url,
                "method": req.method,
                "post_data": req.post_data,
                "headers": dict(req.headers),
            })
    page.on("request", on_request)

    # Llenar campo con N° de parte y buscar
    campo = page.locator("#C_Descripcion").first
    campo.fill(PARTE_TEST)
    time.sleep(1)
    btn = page.locator("#btnBuscar").first
    btn.click()

    # Esperar un poco para capturar el request
    time.sleep(5)

    log.info(f"  Requests capturados: {len(requests_captured)}")
    for r in requests_captured:
        log.info(f"    {r['method']} {r['url']}")
        if r['post_data']:
            log.info(f"    POST data: {r['post_data']}")
        if 'x-requested-with' in r['headers']:
            log.info(f"    X-Requested-With: {r['headers']['x-requested-with']}")

    return requests_captured


def main():
    log = PrintLog()
    stop = threading.Event()

    log.info(f"Iniciando navegador (visible)...")
    pw, browser, page = init_browser(headless=False)
    try:
        page.set_viewport_size({"width": 1920, "height": 1080})
    except Exception:
        pass

    try:
        log.info(f"Login...")
        if not do_login(page, "almerco.03", "4lm3rKenYa@#", "", log, stop):
            log.error("Login falló")
            return
        log.ok("Login OK")

        # Probar varios métodos de API
        params_base = {
            "N_Catalogo": "252",
            "N_Categoria": "11735",
            "C_EstadoNav": "OBSERVADO",
        }

        # 1. C_Descripcion=ficha
        probar_api_con_param(page, "API con C_Descripcion=FICHA",
                             {**params_base, "C_Descripcion": FICHA_TEST}, log)

        # 2. C_ID_Producto=ficha
        probar_api_con_param(page, "API con C_ID_Producto=FICHA",
                             {**params_base, "C_ID_Producto": FICHA_TEST}, log)

        # 3. N_ID_Producto=ficha
        probar_api_con_param(page, "API con N_ID_Producto=FICHA",
                             {**params_base, "N_ID_Producto": FICHA_TEST}, log)

        # 4. C_Ficha=ficha
        probar_api_con_param(page, "API con C_Ficha=FICHA",
                             {**params_base, "C_Ficha": FICHA_TEST}, log)

        # 5. C_Descripcion=ficha + draw (DataTables)
        probar_api_con_param(page, "API DataTables con C_Descripcion=FICHA",
                             {**params_base, "C_Descripcion": FICHA_TEST, "draw": "1", "start": "0", "length": "10"}, log)

        # 6. POST a _CatalogoProductoIndex con form-encoded
        log.info("\n=== Test: POST form-encoded con ficha ===")
        try:
            resp = page.request.post(URL_TABLA,
                form={**params_base, "C_Descripcion": FICHA_TEST, "draw": "1", "start": "0", "length": "10"},
                headers={"X-Requested-With": "XMLHttpRequest"},
                timeout=30_000)
            html = resp.text()
            log.info(f"  Status: {resp.status}, bytes: {len(html)}")
            ids = re.findall(r"ID_CatalogoProducto=(\d+)", html)
            log.info(f"  IDs encontrados: {ids[:3] if ids else 'NINGUNO'}")
            preview = html[:300].replace("\n", " ").replace("\r", " ")
            log.info(f"  Preview: {preview}")
        except Exception as e:
            log.warn(f"  Error: {e}")

        # 7. POST con ficha en otros campos
        log.info("\n=== Test: POST con N_ID_CatalogoProducto ===")
        try:
            resp = page.request.post(URL_TABLA,
                form={**params_base, "N_ID_CatalogoProducto": FICHA_TEST, "draw": "1"},
                headers={"X-Requested-With": "XMLHttpRequest"},
                timeout=30_000)
            html = resp.text()
            log.info(f"  Status: {resp.status}, bytes: {len(html)}")
            ids = re.findall(r"ID_CatalogoProducto=(\d+)", html)
            log.info(f"  IDs encontrados: {ids[:3] if ids else 'NINGUNO'}")
        except Exception as e:
            log.warn(f"  Error: {e}")

        # 8. Interceptar la búsqueda real
        requests = interceptar_busqueda_real(page, log)
        if requests:
            log.info("\n=== Replicar request con ficha ===")
            for r in requests:
                # Tomar el primer request a _CatalogoProductoIndex y replicar con ficha
                if "_CatalogoProductoIndex" in r["url"] and r["post_data"]:
                    log.info(f"  Replicando {r['url']} con ficha en lugar de parte...")
                    # Reemplazar C_Descripcion={parte} con C_Descripcion={ficha}
                    new_post = r["post_data"].replace(f"C_Descripcion={PARTE_TEST}", f"C_Descripcion={FICHA_TEST}")
                    new_post = new_post.replace(f"C_Descripcion={PARTE_TEST}", f"C_Descripcion={FICHA_TEST}")
                    if new_post != r["post_data"]:
                        try:
                            resp = page.request.post(r["url"].split("?")[0],
                                form=dict(item.split("=") for item in new_post.split("&") if "=" in item),
                                headers={k: v for k, v in r["headers"].items() if k.startswith("x-") or k == "content-type"},
                                timeout=30_000)
                            html = resp.text()
                            ids = re.findall(r"ID_CatalogoProducto=(\d+)", html)
                            log.info(f"  IDs con ficha: {ids[:3] if ids else 'NINGUNO'}")
                            preview = html[:300].replace("\n", " ").replace("\r", " ")
                            log.info(f"  Preview: {preview}")
                        except Exception as e:
                            log.warn(f"  Error: {e}")
                    break

        input("\n[Enter para cerrar]")

    finally:
        try:
            close_browser(pw, browser)
        except Exception:
            pass


if __name__ == "__main__":
    main()

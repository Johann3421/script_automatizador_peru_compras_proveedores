"""
discovery_v2_perucompras.py — Scraping profundo multi-técnica
================================================================================
Técnicas adicionales sobre v1:
  T1. Archivos de reconocimiento (robots.txt, sitemap, .axd, etc.)
  T2. Análisis profundo de JS (incluye versión exacta del bundle)
  T3. Enumeración de acciones por controlador
  T4. POST a endpoints que dieron 500
  T5. Fuerza bruta de IDs en rutas (/Reportes/Index/N)
  T6. Headers de tecnología
  T7. Crawling recursivo
  T8. Rutas JS nuevas no probadas

USO (standalone):
  python discovery_v2_perucompras.py [usuario] [password]
"""

import json
import re
import sys
import os
import time
import threading
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
from bs4 import BeautifulSoup

# ══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════════════════════

USUARIO  = sys.argv[1] if len(sys.argv) > 1 else "almerco.03"
PASSWORD = sys.argv[2] if len(sys.argv) > 2 else "4lm3rKenYa@#"

BASE       = "https://www.catalogos.perucompras.gob.pe"
OUTPUT_DIR = Path("discovery_v2_output")
DELAY      = 0.15

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,*/*;q=0.9",
    "accept-language": "es-PE,es;q=0.9",
}

ACCIONES_MVC = [
    "Index", "Create", "Edit", "Delete", "Details", "List",
    "Json", "Data", "_Index", "_List", "_Data", "_Json",
    "Export", "ExportExcel", "Download", "Print", "Report",
    "Search", "Buscar", "Filter", "Filtrar",
    "Save", "Guardar", "Update", "Actualizar",
    "Activate", "Deactivate", "Activar", "Inactivar",
    "Upload", "Preview",
    "GetById", "GetAll", "GetList",
    "Modal", "Popup", "Detalle", "Resumen",
]

CONTROLADORES_BASE = [
    "Home", "t_CatalogoProductoMarca", "t_ProductoOfertado",
    "t_ProductoOfertadoAmp", "t_Proforma", "t_Usuario",
    "Reportes", "General", "Accesos", "AccesoGeneral",
    "MejoraBasica", "MejoraCobertura", "MejoraPlazo",
    "DescuentoVolumen", "DescuentoVolumenAmp",
    "AcuerdoSuscripcion", "OrdenCompra", "ProformaSinOrdenCompra",
    "Notificacion", "ConsultaValoresCreados",
    "t_Catalogo", "t_Categoria", "t_Acuerdo", "t_Marca",
    "t_Proveedor", "t_Empresa", "t_Rol", "t_Evaluacion",
    "t_Adjudicacion", "t_Homologacion", "t_Certificacion",
    "t_OrdenCompra", "t_Notificacion", "t_Configuracion",
    "t_Parametro", "t_Contrato", "t_Entidad", "t_Ficha",
    "t_FichaProducto", "t_Caracteristica", "t_Cobertura",
    "t_MarcaProducto", "t_CatalogoProducto", "t_Comprador",
    "t_Auditoria", "t_SolicitudIncorporacion", "t_Subsanacion",
    "t_Observacion", "t_HistorialPrecio", "t_Penalidad",
    "t_Imagen", "t_ArchivoAdjunto", "t_Reporte",
    "Evaluacion", "Adjudicacion", "Homologacion", "Incorporacion",
    "Subsanacion", "Marca", "Proveedor", "Comprador",
    "Entidad", "Catalogo", "Dashboard", "Admin",
    "Administracion", "Supervisor", "Evaluador",
    "AdmisionEvaluacion", "GestionProducto", "GestionMarca",
    "Inicio",
]

POST_CANDIDATOS = [
    "/General/ListaJ_CatalogoAcuerdo",
    "/General/ListaJ_CategoriaCatalogo",
    "/General/ListaJ_AcuerdoActivo",
    "/General/ListaJ_MarcaCatalogo",
    "/General/ListaJ_ProveedorAcuerdo",
    "/General/ListaJ_Caracteristica",
    "/General/ListaJ_ValorCaracteristica",
    "/General/ListaJ_Certificacion",
    "/General/ListaJ_EstadoFicha",
    "/General/ListaJ_Moneda",
    "/General/ListaJ_Region",
    "/General/ListaJ_TipoDocumento",
    "/General/ListaJ_Rol",
    "/General/ListaJ_Entidad",
    "/General/ListaJ_Comprador",
    "/General/ListaJ_Evaluador",
    "/Home/getDatosPopup",
    "/Home/validarEncuestas",
    "/Inicio",
]

ID_RANGOS = list(range(1, 50)) + [100, 107, 108, 150, 200, 249, 250, 251, 252]

RECON_FILES = [
    "/robots.txt", "/sitemap.xml", "/web.config", "/Web.config",
    "/.htaccess", "/app_offline.htm",
    "/elmah.axd", "/trace.axd",
    "/ScriptResource.axd", "/WebResource.axd",
    "/bundles", "/Content/Site.css",
    "/Scripts/General.js",
    "/favicon.ico",
    "/api", "/api/swagger",
    "/swagger", "/swagger/index.html", "/swagger/ui",
    "/health", "/status", "/ping", "/version",
]


def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


# ─────────────────────────────────────────────────────────────────────────────
# LOGIN (reusa el patrón de la app, con OCR + bridge)
# ─────────────────────────────────────────────────────────────────────────────

def do_login(page, stop_event=None) -> bool:
    log(f"Login como '{USUARIO}'...")
    for intento in range(1, 6):
        if stop_event and stop_event.is_set(): return False
        log(f"  Intento {intento}/5...")
        try:
            page.goto(f"{BASE}/AccesoGeneral", wait_until="domcontentloaded", timeout=30_000)
            page.fill('#UserName, input[name="ID_Usuario"]', USUARIO)
            page.fill('#Password, input[name="Contrasena"]', PASSWORD)
            captcha_text = ""
            try:
                import pytesseract
                from PIL import Image
                import io
                img_el = page.locator('#imgCaptcha, img[src*="aptcha"]').first
                img_el.wait_for(timeout=5000)
                img_bytes = img_el.screenshot()
                img = Image.open(io.BytesIO(img_bytes))
                img = img.resize((img.width*4, img.height*4), Image.LANCZOS).convert("L")
                for th in [140, 120, 100, 80]:
                    binary = img.point(lambda p: 255 if p > th else 0)
                    text = pytesseract.image_to_string(
                        binary,
                        config="--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                    ).strip().upper()
                    text = re.sub(r"[^A-Z0-9]", "", text)
                    if len(text) == 6:
                        captcha_text = text
                        log(f"  OCR: {captcha_text}"); break
            except Exception as e:
                log(f"  OCR no disp.: {e}")
            if not captcha_text:
                log("  CAPTCHA manual:")
                captcha_text = input("  > ").strip().upper()
            if not captcha_text: continue
            page.fill('#txtCaptcha, input[name="CodigoCaptcha"]', captcha_text)
            page.click('#btnLogin, button[type="submit"]')
            page.wait_for_load_state("networkidle", timeout=30_000)
            if "AccesoGeneral" not in page.url:
                log(f"  ✓ Login OK → {page.url}")
                return True
            log(f"  ✗ Falló, reintentando...")
        except Exception as e:
            log(f"  Error: {e}")
    return False


# ─────────────────────────────────────────────────────────────────────────────
# UTILIDADES
# ─────────────────────────────────────────────────────────────────────────────

def extract_all_urls(text):
    patterns = [
        r'["\'](/[\w\-/_]{2,120})["\']',
        r'url\s*[=:]\s*["\'](/[^"\'?#]{2,120})',
        r'href\s*=\s*["\'](/[^"\'?#]{2,120})',
        r'action\s*=\s*["\'](/[^"\'?#]{2,120})',
        r'\.ajax\s*\(\s*["\']?(/[^"\'?#\s]{2,120})',
        r'fetch\s*\(\s*["\'](/[^"\'?#]{2,120})',
    ]
    found = set()
    for p in patterns:
        for m in re.findall(p, text, re.IGNORECASE):
            m = m.strip().split("?")[0].split("#")[0]
            if (m.startswith("/") and not m.startswith("//") and len(m) > 2
                    and not any(ext in m.lower() for ext in
                                ['.jpg','.png','.gif','.ico','.woff','.svg','.map','.min.js','.min.css'])):
                found.add(m)
    return found


def probe(page, path, method="GET", data=None, log_func=None) -> dict:
    """Hace una request y devuelve metadata de la respuesta.
    Usa fetch() desde JS para garantizar cookies y timeout correcto."""
    url = BASE + path if path.startswith("/") else path
    if method == "GET":
        result = page.evaluate("""
            async (u) => {
                try {
                    const r = await fetch(u, { method: 'GET', redirect: 'manual',
                        headers: { 'X-Requested-With': 'XMLHttpRequest' } });
                    let text = '';
                    try { text = await r.text(); } catch(e) { text = ''; }
                    return { ok: true, status: r.status, url: r.url, type: r.type, text: text.substring(0, 2000) };
                } catch (e) { return { ok: false, error: String(e) }; }
            }
        """, url)
    elif method == "POST_JSON":
        result = page.evaluate("""
            async ([u, body]) => {
                try {
                    const r = await fetch(u, { method: 'POST', redirect: 'manual',
                        headers: { 'Content-Type': 'application/json', 'X-Requested-With': 'XMLHttpRequest' },
                        body: JSON.stringify(body) });
                    let text = '';
                    try { text = await r.text(); } catch(e) { text = ''; }
                    return { ok: true, status: r.status, url: r.url, type: r.type, text: text.substring(0, 2000) };
                } catch (e) { return { ok: false, error: String(e) }; }
            }
        """, [url, data or {}])
    else:
        result = page.evaluate("""
            async (u) => {
                try {
                    const r = await fetch(u, { method: 'POST', redirect: 'manual',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' } });
                    let text = '';
                    try { text = await r.text(); } catch(e) { text = ''; }
                    return { ok: true, status: r.status, url: r.url, type: r.type, text: text.substring(0, 2000) };
                } catch (e) { return { ok: false, error: String(e) }; }
            }
        """, url)

    if not result.get("ok"):
        return {"path": path, "method": method, "status": -1,
                "categoria": "connection_error", "error_detail": result.get("error",""),
                "title": "", "size": 0, "sub_urls": []}

    status = result.get("status", 0)
    url_final = result.get("url", url)
    text = result.get("text", "")

    soup = BeautifulSoup(text[:5000], "lxml") if "<html" in text[:200].lower() else None
    is_home = ("AccesoGeneral" in url_final
               or (soup and bool(soup.find("input", {"name": "CodigoCaptcha"}))))

    title = ""
    if soup:
        t = soup.find("title")
        h = soup.find("h5") or soup.find("h4") or soup.find("h3")
        title = (t.get_text(strip=True) if t else
                 h.get_text(strip=True) if h else "")

    error_detail = ""
    if status == 500:
        m = re.search(r'(?:Exception|Error|at\s+\w+\.\w+\(|System\.|Microsoft\.)', text[:3000])
        if m:
            error_detail = text[max(0, m.start()-50):m.start()+300]

    if is_home: cat = "silently_redirected"
    elif status == 200: cat = "accessible"
    elif status == 500: cat = "error_500"
    elif status in (301, 302, 307, 308): cat = "redirect"
    elif status == 403: cat = "forbidden"
    elif status == 401: cat = "unauthorized"
    elif status == 404: cat = "not_found"
    else: cat = f"http_{status}"

    sub_urls = set()
    if status == 200 and not is_home:
        sub_urls = extract_all_urls(text)

    return {
        "path": path, "method": method, "status": status,
        "url_final": url_final, "categoria": cat, "title": title,
        "size": len(text), "error_detail": error_detail[:500] if error_detail else "",
        "sub_urls": sorted(sub_urls),
    }


# ─────────────────────────────────────────────────────────────────────────────
# TÉCNICAS
# ─────────────────────────────────────────────────────────────────────────────

def recon_files(page):
    log("\nT1: Archivos de reconocimiento...")
    results = []
    for path in RECON_FILES:
        r = probe(page, path)
        if r["categoria"] not in ("not_found", "silently_redirected", "connection_error"):
            log(f"  {'✅' if r['status']==200 else '⚠'} {path} → {r['status']} {r['categoria']}")
            results.append(r)
        time.sleep(0.1)
    return results


def analizar_js_profundo(page):
    log("\nT2: Análisis profundo de JS...")
    todas_rutas = set()
    detalles = []
    js_urls = [
        f"{BASE}/Scripts/General.js",
        f"{BASE}/Scripts/General.js?v=202606171607517966",
        f"{BASE}/Scripts/select2.js",
        f"{BASE}/Scripts/jquery.inputmask.min.js",
        f"{BASE}/bundles/jquery",
        f"{BASE}/bundles/bootstrap",
        f"{BASE}/bundles/modalj",
        f"{BASE}/bundles/numeros",
        f"{BASE}/bundles/fancybox",
    ]
    for p in ["/", "/Home", "/Reportes/ProductoOfertadoIndex",
              "/t_CatalogoProductoMarca", "/t_ProductoOfertadoAmp"]:
        try:
            r = page.request.get(BASE + p, headers=HEADERS, timeout=15_000)
            if r.status == 200:
                soup = BeautifulSoup(r.text(), "lxml")
                for s in soup.find_all("script", src=True):
                    src = s["src"]
                    if src.startswith("/") and not src.startswith("//"):
                        full = BASE + src
                        if full not in js_urls:
                            js_urls.append(full)
                todas_rutas |= extract_all_urls(r.text())
        except Exception: pass

    js_urls = list(dict.fromkeys(js_urls))
    for js_url in js_urls:
        try:
            r = page.request.get(js_url, headers=HEADERS, timeout=20_000)
            if r.status == 200:
                rutas = extract_all_urls(r.text())
                rutas_filtradas = {ru for ru in rutas
                    if ru.startswith("/") and not any(ext in ru for ext in ['.js','.css','.png','.gif'])}
                todas_rutas |= rutas_filtradas
                log(f"  ✓ {js_url.replace(BASE,'').split('?')[0]} → {len(rutas_filtradas)} rutas")
                detalles.append({"url": js_url, "size_kb": len(r.body())//1024,
                                 "rutas": sorted(rutas_filtradas)})
        except Exception as e:
            log(f"  ✗ {js_url}: {e}")

    log(f"  → {len(todas_rutas)} rutas únicas de JS")
    return sorted(todas_rutas), detalles


def enumerar_acciones(page):
    log(f"\nT3: Enumerando {len(CONTROLADORES_BASE)} ctrl × {len(ACCIONES_MVC)} acciones...")
    results = []
    encontrados = 0
    total = len(CONTROLADORES_BASE) * len(ACCIONES_MVC)
    for ctrl in CONTROLADORES_BASE:
        for accion in ACCIONES_MVC:
            path = f"/{ctrl}/{accion}"
            r = probe(page, path)
            if r["categoria"] not in ("not_found", "silently_redirected", "connection_error"):
                encontrados += 1
                log(f"  ✅ {path} → {r['status']} | {r['title'][:40]}")
                results.append(r)
            time.sleep(DELAY)
    log(f"  → {encontrados}/{total} acciones no-404")
    return results


def probar_post(page):
    log(f"\nT4: POST a {len(POST_CANDIDATOS)} endpoints...")
    results = []
    payloads = [
        {}, {"N_Acuerdo": "249"}, {"N_Acuerdo": "249", "C_Estado": "ACTIVO"},
        {"N_Catalogo": "252"},
        {"N_Catalogo": "252", "N_CategoriaParent": 0, "C_Estado": "ACTIVO^IMPLEMENTACION", "N_Nivel": "1"},
        {"id": 1}, {"Id": 1},
    ]
    for path in POST_CANDIDATOS:
        for payload in payloads:
            r = probe(page, path, "POST_JSON", data=payload)
            if r["categoria"] not in ("not_found", "silently_redirected", "connection_error"):
                log(f"  ✅ POST {path} → {r['status']} | {r['title'][:30]}")
                r["post_payload"] = payload
                results.append(r)
                break
            time.sleep(0.1)
        time.sleep(DELAY)
    return results


def bruteforce_ids(page):
    log("\nT5: Fuerza bruta de IDs en /Reportes/Index/N...")
    results = []
    for id_val in ID_RANGOS:
        path = f"/Reportes/Index/{id_val}"
        r = probe(page, path)
        if r["categoria"] not in ("not_found", "silently_redirected", "connection_error"):
            log(f"  ✅ {path} → {r['status']} | {r['title'][:40]}")
            r["id_value"] = id_val
            results.append(r)
        time.sleep(DELAY)
    return results


def analizar_headers_tecnologia(page):
    log("\nT6: Headers de tecnología...")
    # Usar fetch() desde JS para evitar el bug de timeout en ms
    r = page.evaluate("""
        async (u) => {
            try {
                const resp = await fetch(u, { method: 'GET', redirect: 'manual' });
                const headers = {};
                resp.headers.forEach((v, k) => { headers[k.toLowerCase()] = v; });
                return { ok: true, status: resp.status, headers: headers };
            } catch (e) { return { ok: false, error: String(e) }; }
        }
    """, BASE)
    if not r.get("ok"):
        log(f"  Error: {r.get('error', 'unknown')}")
        return {}
    headers = r.get("headers", {})
    interes = ["server", "x-powered-by", "x-aspnet-version", "x-aspnetmvc-version",
               "x-frame-options", "x-content-type-options", "strict-transport-security",
               "content-security-policy"]
    result = {}
    for h in interes:
        if h in headers:
            result[h] = headers[h]
            log(f"  {h}: {headers[h][:100]}")
    log(f"  status: {r.get('status')}")
    return result


def crawl_recursivo(page, seeds, max_depth=2):
    log(f"\nT7: Crawling recursivo (depth {max_depth}, {len(seeds)} seeds)...")
    visitados = set()
    cola = [(s, 0) for s in seeds]
    results = []
    while cola:
        path, depth = cola.pop(0)
        if path in visitados or depth > max_depth: continue
        visitados.add(path)
        r = probe(page, path)
        if r["categoria"] == "accessible":
            results.append(r)
            if depth < max_depth:
                for sub in r.get("sub_urls", []):
                    if sub not in visitados and sub.startswith("/") \
                       and not any(ext in sub for ext in ['.js','.css','.png','.jpg','.gif']):
                        cola.append((sub, depth + 1))
            log(f"  {'  '*depth}✅ {path} → {r['title'][:40]}")
        time.sleep(DELAY)
    log(f"  → {len(results)} páginas accesibles")
    return results


# ─────────────────────────────────────────────────────────────────────────────
# REPORTE
# ─────────────────────────────────────────────────────────────────────────────

def generar_reporte_v2(all_results, output_dir):
    lineas = [f"# Mapa Completo de Endpoints v2 — Peru Compras",
              f"Cuenta: `{USUARIO}` | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "", "---", ""]
    todos = []
    for items in all_results.values():
        if isinstance(items, list):
            for it in items:
                if isinstance(it, dict) and "categoria" in it:
                    todos.append(it)
    seen = {}
    for r in todos:
        k = f"{r.get('method','GET')}:{r.get('path','')}"
        if k not in seen: seen[k] = r
    by_cat = {}
    for r in seen.values():
        by_cat.setdefault(r.get("categoria","unknown"), []).append(r)

    lineas += ["## Resumen", "| Categoría | Cantidad |", "|---|---|"]
    emojis = {"accessible":"✅","error_500":"💥","requires_auth":"🔒",
               "forbidden":"❌","silently_redirected":"🫥","not_found":"—"}
    for cat, items in sorted(by_cat.items(), key=lambda x: -len(x[1])):
        e = emojis.get(cat, "⚠")
        lineas.append(f"| {e} {cat} | {len(items)} |")

    for cat in ["accessible", "error_500", "requires_auth", "forbidden"]:
        items = by_cat.get(cat, [])
        if not items: continue
        e = emojis.get(cat, "⚠")
        lineas += ["", f"---", "", f"## {e} {cat.upper()} ({len(items)})"]
        for r in sorted(items, key=lambda x: x.get("path","")):
            method = r.get("method","GET")
            path = r.get("path","")
            title = r.get("title","")
            status = r.get("status","")
            lineas.append(f"- `[{method}] {path}` ({status}) — {title[:60]}")
            if r.get("error_detail"):
                lineas.append(f"  ```\n  {r['error_detail'][:200]}\n  ```")
            if r.get("sub_urls"):
                for su in r["sub_urls"][:8]:
                    lineas.append(f"  → `{su}`")

    if "tech_headers" in all_results and all_results["tech_headers"]:
        lineas += ["", "---", "", "## 🔧 Tecnología"]
        for k, v in all_results["tech_headers"].items():
            lineas.append(f"- `{k}`: `{v[:100]}`")

    if "brute_ids" in all_results and all_results["brute_ids"]:
        lineas += ["", "---", "", "## 🔢 IDs de Reportes"]
        for r in all_results["brute_ids"]:
            lineas.append(f"- `/Reportes/Index/{r['id_value']}` — {r.get('title','')[:60]}")

    if "js_rutas" in all_results:
        lineas += ["", "---", "", "## 📜 Rutas en JS"]
        for ruta in all_results["js_rutas"]:
            lineas.append(f"- `{ruta}`")

    path = output_dir / "mapa_v2.md"
    path.write_text("\n".join(lineas), encoding="utf-8")
    log(f"  → Reporte: {path}")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print(f"  PERU COMPRAS — DISCOVERY v2 | Cuenta: {USUARIO}")
    print("=" * 65)

    OUTPUT_DIR.mkdir(exist_ok=True)
    all_results = {}

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(user_agent=HEADERS["user-agent"])
        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})

        if not do_login(page):
            log("✗ Login fallido"); sys.exit(1)

        all_results["recon"] = recon_files(page)
        js_rutas, js_detalles = analizar_js_profundo(page)
        all_results["js_rutas"]    = js_rutas
        all_results["js_detalles"] = js_detalles
        all_results["acciones"]    = enumerar_acciones(page)
        all_results["post_results"] = probar_post(page)
        all_results["brute_ids"]    = bruteforce_ids(page)
        all_results["tech_headers"] = analizar_headers_tecnologia(page)

        seeds = [r["path"] for r in (all_results["recon"] + all_results["acciones"]
                                      + all_results["post_results"])
                 if r.get("categoria") == "accessible"]
        seeds += ["/Home", "/t_CatalogoProductoMarca", "/ConsultaValoresCreados",
                  "/ProformaSinOrdenCompra"]
        seeds = list(dict.fromkeys(seeds))
        all_results["crawl"] = crawl_recursivo(page, seeds, max_depth=2)

        # Rutas JS nuevas
        ya_probadas = set(r["path"] for results in all_results.values()
                           if isinstance(results, list) for r in results
                           if isinstance(r, dict) and "path" in r)
        js_nuevas = [p for p in js_rutas if p not in ya_probadas and p.startswith("/")]
        if js_nuevas:
            log(f"\nProbando {len(js_nuevas)} rutas nuevas del JS...")
            js_probe_results = []
            for path in js_nuevas:
                r = probe(page, path)
                if r["categoria"] not in ("not_found", "silently_redirected"):
                    log(f"  {'✅' if r['status']==200 else '⚠'} {path} → {r['status']}")
                    js_probe_results.append(r)
                time.sleep(DELAY)
            all_results["js_probed"] = js_probe_results

        browser.close()

    for key, data in all_results.items():
        path = OUTPUT_DIR / f"{key}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    generar_reporte_v2(all_results, OUTPUT_DIR)

    total = sum(
        1 for items in all_results.values()
        if isinstance(items, list)
        for it in items
        if isinstance(it, dict) and "categoria" in it
    )
    print()
    print("=" * 65)
    print(f"  DISCOVERY v2 COMPLETO")
    print(f"  Endpoints no-404: {total}")
    print(f"  Archivos: {OUTPUT_DIR}/")
    print("=" * 65)


if __name__ == "__main__":
    main()

"""
discovery_perucompras.py — Mapa completo de endpoints ocultos de PeruCompras
=================================================================================
Estrategia en 4 capas (misma lógica que el original, pero sync Playwright):
  1. Análisis estático de JS
  2. Fuzzing por naming convention (~200 candidatos)
  3. Clasificación de respuestas (200/302/403/404/500)
  4. Crawling de páginas accesibles

USO:
  python discovery_perucompras.py
  python discovery_perucompras.py "almerco.03" "4lm3rKenYa@#"

SALIDA:
  discovery_output/
  ├── endpoints_accesibles.json
  ├── endpoints_otro_rol.json
  ├── endpoints_error.json
  ├── endpoints_todos.json
  ├── js_analisis.json
  └── mapa_completo.md
"""

import re
import os
import sys
import json
import time
import threading
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
from bs4 import BeautifulSoup

# ══════════════════════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════════════════════

USUARIO  = sys.argv[1] if len(sys.argv) > 1 else "almerco.03"
PASSWORD = sys.argv[2] if len(sys.argv) > 2 else "4lm3rKenYa@#"

BASE       = "https://www.catalogos.perucompras.gob.pe"
OUTPUT_DIR = Path("discovery_output")
DELAY      = 0.2

HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/145.0.0.0 Safari/537.36"
    ),
    "accept": "text/html,application/xhtml+xml,*/*;q=0.9",
    "accept-language": "es-PE,es;q=0.9",
}

# Candidatos a probar (lista maestra del discovery)
CANDIDATOS = [
    # t_* conocidos
    "/t_ProductoOfertado", "/t_ProductoOfertadoAmp", "/t_CatalogoProductoMarca",
    "/t_Proforma", "/t_Usuario", "/t_Usuario/Index", "/t_Usuario/Create", "/t_Usuario/ListaUsuarios",
    # t_* a descubrir
    "/t_CatalogoProducto", "/t_CatalogoProducto/Index", "/t_CatalogoProductoAmp",
    "/t_Catalogo", "/t_Catalogo/Index", "/t_Categoria", "/t_Categoria/Index",
    "/t_Acuerdo", "/t_Acuerdo/Index", "/t_Marca", "/t_Marca/Index", "/t_MarcaProducto",
    "/t_MarcaProducto/Index", "/t_Proveedor", "/t_Proveedor/Index", "/t_Empresa",
    "/t_Empresa/Index", "/t_Rol", "/t_Rol/Index", "/t_Evaluacion", "/t_Evaluacion/Index",
    "/t_Adjudicacion", "/t_Adjudicacion/Index", "/t_Homologacion", "/t_Homologacion/Index",
    "/t_Certificacion", "/t_Certificacion/Index", "/t_OrdenCompra", "/t_OrdenCompra/Index",
    "/t_Notificacion", "/t_Notificacion/Index", "/t_Configuracion", "/t_Configuracion/Index",
    "/t_Parametro", "/t_Parametro/Index", "/t_Contrato", "/t_Contrato/Index", "/t_Penalidad",
    "/t_Penalidad/Index", "/t_Reporte", "/t_Reporte/Index", "/t_Auditoria", "/t_Auditoria/Index",
    "/t_Log", "/t_Log/Index", "/t_Entidad", "/t_Entidad/Index", "/t_Comprador",
    "/t_Comprador/Index", "/t_Ficha", "/t_Ficha/Index", "/t_FichaProducto", "/t_FichaProducto/Index",
    "/t_CaracteristicaValor", "/t_Caracteristica", "/t_Caracteristica/Index", "/t_ValorCaracteristica",
    "/t_Cobertura", "/t_Cobertura/Index", "/t_PlazoEntrega", "/t_DescuentoVolumen",
    "/t_Imagen", "/t_ImagenProducto", "/t_ArchivoAdjunto", "/t_SolicitudIncorporacion",
    "/t_SolicitudIncorporacion/Index", "/t_SolicitudMejora", "/t_Subsanacion", "/t_Subsanacion/Index",
    "/t_Observacion", "/t_Observacion/Index", "/t_HistorialPrecio", "/t_HistorialPrecio/Index",
    # Reportes
    "/Reportes/Index", "/Reportes/Index/107", "/Reportes/ProductoOfertadoIndex",
    "/Reportes/_detProductoOfertadoIndex",
    "/Reportes/EvaluacionIndex", "/Reportes/AdjudicacionIndex", "/Reportes/ProveedorIndex",
    "/Reportes/MarcaIndex", "/Reportes/CatalogoIndex", "/Reportes/HomologacionIndex",
    "/Reportes/OrdenCompraIndex", "/Reportes/ProformaIndex", "/Reportes/NotificacionIndex",
    "/Reportes/CompradoresIndex", "/Reportes/EntidadIndex", "/Reportes/FichaIndex",
    "/Reportes/PrecioIndex", "/Reportes/HistorialIndex", "/Reportes/ContratoIndex",
    "/Reportes/PenalidadIndex", "/Reportes/DescuentoIndex", "/Reportes/CoberturaIndex",
    "/Reportes/SubsanacionIndex", "/Reportes/ObservacionIndex", "/Reportes/AuditoriaIndex",
    "/Reportes/Estadisticas", "/Reportes/Dashboard",
    # General/ListaJ_*
    "/General/ListaJ_CatalogoAcuerdo", "/General/ListaJ_CategoriaCatalogo",
    "/General/ListaJ_AcuerdoActivo", "/General/ListaJ_AcuerdoAll",
    "/General/ListaJ_MarcaCatalogo", "/General/ListaJ_ProveedorAcuerdo",
    "/General/ListaJ_EstadoOferta", "/General/ListaJ_Rol", "/General/ListaJ_Entidad",
    "/General/ListaJ_Region", "/General/ListaJ_Departamento", "/General/ListaJ_Provincia",
    "/General/ListaJ_Distrito", "/General/ListaJ_TipoDocumento", "/General/ListaJ_Moneda",
    "/General/ListaJ_UnidadMedida", "/General/ListaJ_Categoria", "/General/ListaJ_SubCategoria",
    "/General/ListaJ_Caracteristica", "/General/ListaJ_ValorCaracteristica",
    "/General/ListaJ_Certificacion", "/General/ListaJ_EstadoFicha", "/General/ListaJ_EstadoCatalogo",
    "/General/ListaJ_TipoProveedor", "/General/ListaJ_Cobertura", "/General/ListaJ_PlazoEntrega",
    "/General/ListaJ_Evaluador", "/General/ListaJ_Comprador",
    # Módulos sin prefijo
    "/AcuerdoSuscripcion", "/MejoraBasica", "/MejoraCobertura", "/MejoraPlazo/IndexMejora",
    "/DescuentoVolumen", "/DescuentoVolumenAmp", "/OrdenCompra", "/ProformaSinOrdenCompra",
    "/Notificacion", "/Evaluacion", "/Evaluacion/Index", "/Adjudicacion", "/Adjudicacion/Index",
    "/Homologacion", "/Homologacion/Index", "/Incorporacion", "/Incorporacion/Index",
    "/Subsanacion", "/Subsanacion/Index", "/Marca", "/Marca/Index", "/MarcaProducto",
    "/MarcaProducto/Index", "/Proveedor", "/Proveedor/Index", "/Comprador", "/Comprador/Index",
    "/Entidad", "/Entidad/Index", "/Catalogo", "/Catalogo/Index", "/Dashboard", "/Inicio",
    "/Home", "/Home/Index", "/AdmisionEvaluacion", "/AdmisionEvaluacion/Index",
    "/GestionProducto", "/GestionProducto/Index", "/GestionMarca", "/GestionMarca/Index",
    "/GestionProveedor", "/GestionProveedor/Index",
    # Admin
    "/Admin", "/Admin/Index", "/Admin/Dashboard", "/Admin/Usuarios", "/Admin/Roles",
    "/Admin/Configuracion", "/Administracion", "/Administracion/Index",
    "/Gestion", "/Gestion/Index", "/Supervisor", "/Supervisor/Index",
    "/Evaluador", "/Evaluador/Index",
    # Auth
    "/Accesos", "/Accesos/Method", "/Accesos/ObtenerIndicadorSemaforoProveedor",
    "/Accesos/Perfil", "/Accesos/CambiarPassword",
    # APIs JSON
    "/api/catalogo", "/api/producto", "/api/proveedor", "/api/marca",
    "/api/evaluacion", "/api/reporte", "/Api/Catalogo", "/Api/Producto",
    # Sub-actions
    "/MejoraCobertura/Index", "/MejoraCobertura/Create", "/MejoraCobertura/Edit",
    "/MejoraPlazo/Index", "/MejoraPlazo/Create", "/DescuentoVolumen/Index",
    "/DescuentoVolumen/Create", "/DescuentoVolumenAmp/Index",
    # Marca
    "/t_CatalogoProductoMarca/Index", "/t_CatalogoProductoMarca/Create",
    "/t_CatalogoProductoMarca/ListarProductos", "/t_CatalogoProductoMarca/_CatalogoProductoIndex",
    # Comprador
    "/Compra", "/Compra/Index", "/PlanAnual", "/PlanAnual/Index",
    "/Requerimiento", "/Requerimiento/Index",
]

JS_SCRIPTS = [
    "/Scripts/General.js", "/Scripts/select2.js",
    "/Scripts/jquery.inputmask.min.js",
    "/Scripts/admin2/datatables/jquery.dataTables.min.js",
]

URL_PATTERNS = [
    r'(?:url|href|action|src)\s*[=:]\s*["\']([/][^"\'?#\s]{3,100})["\']',
    r'["\'](/(?:t_|Reportes|General|Admin|Accesos|Api|api)[^"\'?#\s]{2,100})["\']',
    r'(?:ajax|fetch|get|post|put)\s*\(\s*["\']([/][^"\'?#\s]{3,100})["\']',
    r'url\s*:\s*["\']([/][^"\'?#\s]{3,100})["\']',
    r'location\s*=\s*["\']([/][^"\'?#\s]{3,100})["\']',
]


def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


# ─────────────────────────────────────────────────────────────────────────────
# LOGIN (OCR + manual fallback)
# ─────────────────────────────────────────────────────────────────────────────

def do_login(page) -> bool:
    log("Login...")
    for intento in range(1, 6):
        log(f"  Intento {intento}/5...")
        try:
            page.goto(f"{BASE}/AccesoGeneral", wait_until="domcontentloaded", timeout=30_000)
            page.fill('#UserName, input[name="ID_Usuario"]', USUARIO)
            page.fill('#Password, input[name="Contrasena"]', PASSWORD)
            # CAPTCHA: intentar OCR, fallback input
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
                        log(f"  OCR: {captcha_text}")
                        break
            except Exception as e:
                log(f"  OCR no disponible: {e}")

            if not captcha_text:
                captcha_text = input("  CAPTCHA > ").strip().upper()
            if not captcha_text:
                continue

            page.fill('#txtCaptcha, input[name="CodigoCaptcha"]', captcha_text)
            page.click('#btnLogin, button[type="submit"]')
            page.wait_for_load_state("networkidle", timeout=30_000)
            if "AccesoGeneral" not in page.url:
                log(f"  ✓ Login OK")
                return True
            log(f"  ✗ Falló, reintentando...")
        except Exception as e:
            log(f"  Error: {e}")
    return False


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def extract_urls_from_js(js_text: str) -> set:
    found = set()
    for pattern in URL_PATTERNS:
        for m in re.findall(pattern, js_text, re.IGNORECASE):
            m = m.strip()
            if (m.startswith("/") and not m.startswith("//") and len(m) > 2
                    and not any(ext in m for ext in ['.css', '.png', '.jpg', '.gif', '.ico', '.woff', '.svg'])):
                found.add(m)
    return found


def extract_urls_from_html(html_text: str) -> set:
    found = set()
    soup = BeautifulSoup(html_text, "lxml")
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/") and not href.startswith("//"):
            found.add(href.split("?")[0])
    for form in soup.find_all("form", action=True):
        action = form["action"]
        if action.startswith("/"):
            found.add(action.split("?")[0])
    for script in soup.find_all("script"):
        if script.string:
            found |= extract_urls_from_js(script.string)
    for script in soup.find_all("script", src=True):
        src = script["src"]
        if src.startswith("/"):
            found.add(src.split("?")[0])
    return found


# ─────────────────────────────────────────────────────────────────────────────
# CAPA 1: JS ESTÁTICO
# ─────────────────────────────────────────────────────────────────────────────

def analizar_js(page) -> dict:
    log("Capa 1: Analizando JS estático...")
    todas_las_rutas = set()
    scripts_analizados = []

    # Página principal
    resp_html = page.evaluate("() => document.documentElement.outerHTML")
    rutas_html = extract_urls_from_html(resp_html)
    todas_las_rutas |= rutas_html

    # Scripts conocidos + los descubiertos
    scripts_a_analizar = list(JS_SCRIPTS)
    soup = BeautifulSoup(resp_html, "lxml")
    for script in soup.find_all("script", src=True):
        src = script["src"]
        if src.startswith("/Scripts") or "/bundles/" in src:
            scripts_a_analizar.append(src.split("?")[0])
    scripts_a_analizar = list(set(scripts_a_analizar))

    for script_path in scripts_a_analizar:
        url = BASE + script_path
        try:
            r = page.request.get(url, headers=HEADERS, timeout=15)
            if r.status == 200:
                js_text = r.text()
                rutas = extract_urls_from_js(js_text)
                todas_las_rutas |= rutas
                scripts_analizados.append({
                    "script": script_path, "size_kb": len(r.body()) // 1024,
                    "rutas_encontradas": len(rutas), "rutas": sorted(rutas),
                })
                log(f"  ✓ {script_path} → {len(rutas)} rutas")
        except Exception as e:
            log(f"  ✗ {script_path} → {e}")
        time.sleep(0.1)

    rutas_filtradas = {
        r for r in todas_las_rutas
        if not any(ext in r for ext in ['.js', '.css', '.png', '.jpg', '.gif',
                                         '.ico', '.woff', '.svg', '.map', '.min'])
        and len(r) > 2
    }
    log(f"  → {len(rutas_filtradas)} rutas únicas de JS/HTML")

    return {
        "rutas_descubiertas": sorted(rutas_filtradas),
        "scripts_analizados": scripts_analizados,
        "total": len(rutas_filtradas),
    }


# ─────────────────────────────────────────────────────────────────────────────
# CAPA 2+3: FUZZING + CLASIFICACIÓN
# ─────────────────────────────────────────────────────────────────────────────

def clasificar_respuesta(status, url_final_str, html_text):
    url_final_str = str(url_final_str).lower()
    if status == 404: return "not_found"
    if status == 500: return "error_500"
    if status == 403: return "forbidden"
    if status in (401, 302):
        if "accesogeneral" in url_final_str or "login" in url_final_str:
            return "requires_auth"
        return "redirect"
    if status == 200:
        if "accesogeneral" in url_final_str: return "requires_auth"
        if html_text and ("AccesoGeneral" in html_text[:500] or "Iniciar Sesión" in html_text[:500]):
            return "requires_auth"
        return "accessible"
    return f"http_{status}"


def fuzz_endpoints(page, candidatos: list) -> dict:
    log(f"\nCapa 2+3: Fuzzing {len(candidatos)} endpoints...")
    resultados = {
        "accessible": [], "requires_auth": [], "forbidden": [],
        "error_500": [], "redirect": [], "not_found": [],
    }
    for i, path in enumerate(candidatos, 1):
        url = BASE + path
        try:
            r = page.request.get(url, headers=HEADERS, timeout=15, max_redirects=0)
            cat = clasificar_respuesta(r.status, r.url, r.text()[:500] if r.status == 200 else "")
            entry = {
                "path": path, "url": url, "status": r.status,
                "url_final": str(r.url), "size_bytes": len(r.body()),
                "categoria": cat,
            }
            if cat == "accessible":
                html = r.text()
                soup = BeautifulSoup(html, "lxml")
                title = soup.find("title")
                h5 = soup.find("h5")
                entry["titulo"] = (title.get_text(strip=True) if title
                                   else h5.get_text(strip=True) if h5 else "")
                sub = extract_urls_from_html(html)
                entry["sub_rutas"] = sorted([s for s in sub
                    if not any(ext in s for ext in ['.js', '.css', '.png'])])
                log(f"  [{i}/{len(candidatos)}] ✅ {path} → {r.status_code if hasattr(r, 'status_code') else r.status} | {entry['titulo'][:40]}")
            elif cat in ("requires_auth", "forbidden", "error_500"):
                log(f"  [{i}/{len(candidatos)}] 🔒 {path} → {r.status} ({cat})")
            else:
                if i % 20 == 0:
                    log(f"  [{i}/{len(candidatos)}] ... procesando ...")
            resultados[cat].append(entry)
        except Exception as e:
            log(f"  [{i}/{len(candidatos)}] ✗ {path} → {e}")
        time.sleep(DELAY)
    return resultados


# ─────────────────────────────────────────────────────────────────────────────
# CAPA 4: CRAWLING
# ─────────────────────────────────────────────────────────────────────────────

def crawl_accesibles(accesibles, ya_visitados):
    log(f"\nCapa 4: Crawling de {len(accesibles)} páginas accesibles...")
    nuevas = set()
    for entry in accesibles:
        for sub in entry.get("sub_rutas", []):
            if sub not in ya_visitados and sub.startswith("/"):
                nuevas.add(sub)
    nuevas -= ya_visitados
    log(f"  {len(nuevas)} rutas nuevas a probar desde crawling")
    return list(nuevas)


# ─────────────────────────────────────────────────────────────────────────────
# REPORTE
# ─────────────────────────────────────────────────────────────────────────────

def generar_reporte(js_info, resultados, output_dir):
    lineas = [
        "# Mapa de Endpoints — Peru Compras",
        f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "", "---", "",
        "## Resumen",
        "| Categoría | Cantidad |",
        "|-----------|---------|",
    ]
    emojis = {"accessible": "✅", "requires_auth": "🔒", "forbidden": "❌",
              "error_500": "💥", "redirect": "↪️", "not_found": "404"}
    for cat, items in resultados.items():
        lineas.append(f"| {emojis.get(cat, '?')} {cat} | {len(items)} |")

    lineas += ["", "---", "", "## ✅ Endpoints Accesibles"]
    for e in resultados.get("accessible", []):
        lineas.append(f"- `{e['path']}` — {e.get('titulo', '')}")
        for sr in e.get("sub_rutas", [])[:5]:
            lineas.append(f"  - `{sr}`")

    lineas += ["", "---", "", "## 🔒 Endpoints que Requieren Otro Rol",
               "> Existen en el servidor pero redirigen a login con la cuenta actual.",
               "> Probablemente accesibles con cuentas de: MARCA, EVALUADOR, ADMIN, COMPRADOR"]
    for e in resultados.get("requires_auth", []) + resultados.get("forbidden", []):
        lineas.append(f"- `{e['path']}` (HTTP {e['status']})")

    lineas += ["", "---", "", "## 💥 Endpoints con Error 500",
               "> Existen pero tienen bug del lado del servidor.",
               "> Son endpoints reales — pueden funcionar con parámetros correctos."]
    for e in resultados.get("error_500", []):
        lineas.append(f"- `{e['path']}`")

    lineas += ["", "---", "", "## 📜 Rutas encontradas en JS estático"]
    for r in js_info.get("rutas_descubiertas", []):
        lineas.append(f"- `{r}`")

    path = output_dir / "mapa_completo.md"
    path.write_text("\n".join(lineas), encoding="utf-8")
    log(f"  Reporte: {path}")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("  PERU COMPRAS — DISCOVERY DE ENDPOINTS OCULTOS")
    print(f"  Base: {BASE}")
    print(f"  Usuario: {USUARIO}")
    print("=" * 65)

    OUTPUT_DIR.mkdir(exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(user_agent=HEADERS["user-agent"])
        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})

        if not do_login(page):
            log("✗ Login fallido"); sys.exit(1)

        js_info = analizar_js(page)
        with open(OUTPUT_DIR / "js_analisis.json", "w", encoding="utf-8") as f:
            json.dump(js_info, f, ensure_ascii=False, indent=2)

        todos_candidatos = list(set(CANDIDATOS + js_info["rutas_descubiertas"]))
        todos_candidatos.sort()
        log(f"\n  Total candidatos a probar: {len(todos_candidatos)}")

        resultados = fuzz_endpoints(page, todos_candidatos)

        # Capa 4
        visitados = set(todos_candidatos)
        nuevas = crawl_accesibles(resultados["accessible"], visitados)
        if nuevas:
            log(f"  Probando {len(nuevas)} rutas adicionales del crawling...")
            r2 = fuzz_endpoints(page, nuevas)
            for cat in resultados:
                resultados[cat].extend(r2.get(cat, []))

        with open(OUTPUT_DIR / "endpoints_accesibles.json", "w", encoding="utf-8") as f:
            json.dump(resultados["accessible"], f, ensure_ascii=False, indent=2)
        with open(OUTPUT_DIR / "endpoints_otro_rol.json", "w", encoding="utf-8") as f:
            json.dump(resultados["requires_auth"] + resultados["forbidden"],
                      f, ensure_ascii=False, indent=2)
        with open(OUTPUT_DIR / "endpoints_error.json", "w", encoding="utf-8") as f:
            json.dump(resultados["error_500"], f, ensure_ascii=False, indent=2)
        with open(OUTPUT_DIR / "endpoints_todos.json", "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

        generar_reporte(js_info, resultados, OUTPUT_DIR)

        browser.close()

    print()
    print("=" * 65)
    print(f"  DISCOVERY COMPLETO")
    print(f"  ✅ Accesibles:       {len(resultados['accessible'])}")
    print(f"  🔒 Otro rol:         {len(resultados['requires_auth']) + len(resultados['forbidden'])}")
    print(f"  💥 Error 500:        {len(resultados['error_500'])}")
    print(f"  Archivos en:         {OUTPUT_DIR}/")
    print("=" * 65)


if __name__ == "__main__":
    main()

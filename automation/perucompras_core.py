"""
automation/perucompras_core.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Módulo de Funciones Padre Reutilizables de Automatización Perú Compras.

Este módulo centraliza todas las operaciones atómicas y compuestas
con el portal de Perú Compras, desacopladas al 100% de la interfaz de usuario (UI):
  1. `login_automatico`: Inicio de sesión robusto con OCR Tesseract.
  2. `saltar_verificacion`: Maniobra de retroceso y navegación a MejoraBasica.
  3. `navegar_mejora_basica`: Navegación garantizada a la sección MejoraBasica.
  4. `completar_menu_dinamico`: Selección flexible de combos de catálogo.
  5. `insertar_stock_item`: Actualización atómica de stock de un producto.
  6. `consultar_json_productos`: Extracción del dataset JSON crudo.
  7. `extraer_json_catalogo`: Extracción E2E completa del catálogo JSON a disco/memoria.
"""

import os
import time
import json
from typing import Callable, Optional, Dict, Any, List


BASE_URL = "https://www.catalogos.perucompras.gob.pe"
MEJORA_URL = f"{BASE_URL}/MejoraBasica"


def _log(log_func: Optional[Callable[[str], None]], msg: str) -> None:
    """Envía un mensaje al logger provisto o a la consola estándar."""
    if log_func:
        try:
            log_func(msg)
        except Exception:
            print(msg)
    else:
        print(msg)


def login_automatico(
    page,
    usuario: str,
    password: str,
    captcha_bridge=None,
    stop_event=None,
    log_func: Optional[Callable[[str], None]] = None
) -> bool:
    """
    FUNCION PADRE 1: Login Automático en Perú Compras.
    
    Asegura la configuración del viewport (1920x1080), navega al portal de acceso,
    rellena credenciales y resuelve el CAPTCHA numérico con OCR Tesseract.
    """
    from automation.login import do_login
    
    _log(log_func, "🔐 Configurando viewport HD 1920x1080 para login...")
    try:
        page.set_viewport_size({"width": 1920, "height": 1080})
    except Exception as e:
        _log(log_func, f"⚠️ No se pudo fijar viewport HD: {e}")

    class _LogAdapter:
        def info(self, msg): _log(log_func, str(msg).strip())
        def warning(self, msg): _log(log_func, f"⚠️ {str(msg).strip()}")
        def error(self, msg): _log(log_func, f"❌ {str(msg).strip()}")
        def success(self, msg): _log(log_func, f"✅ {str(msg).strip()}")
        def ok(self, msg): _log(log_func, f"✅ {str(msg).strip()}")
        def write(self, txt):
            clean = str(txt).strip()
            if clean:
                _log(log_func, clean)
        def flush(self): pass

    log_adapter = _LogAdapter()
    ok = do_login(page, usuario, password, "", log_adapter, stop_event, captcha_bridge)
    if ok:
        _log(log_func, "✅ Sesión iniciada correctamente.")
    else:
        _log(log_func, "❌ Inicio de sesión falló.")
    return ok


def saltar_verificacion(
    page,
    log_func: Optional[Callable[[str], None]] = None
) -> bool:
    """
    FUNCION PADRE 2: Saltar Verificación y Navegación a MejoraBasica.
    """
    _log(log_func, "🔄 Ejecutando maniobra de retroceso seguro y evasión...")
    try:
        page.go_back()
        time.sleep(2)
    except Exception:
        pass

    try:
        page.goto(BASE_URL, wait_until="networkidle", timeout=60_000)
        time.sleep(2)
    except Exception:
        pass

    try:
        page.goto(MEJORA_URL, wait_until="networkidle", timeout=60_000)
        time.sleep(3)
        _log(log_func, "📍 Navegación a MejoraBasica completada exitosamente.")
        return True
    except Exception as e:
        _log(log_func, f"⚠️ Error en navegación a MejoraBasica: {e}")
        return False


def navegar_mejora_basica(
    page,
    log_func: Optional[Callable[[str], None]] = None
) -> bool:
    """
    FUNCION PADRE 3: Navegación Garantizada a MejoraBasica.
    """
    _log(log_func, "📍 Navegando a la sección MejoraBasica...")
    try:
        page.goto(MEJORA_URL, wait_until="networkidle", timeout=60_000)
        time.sleep(3)
        _log(log_func, "✅ Sección MejoraBasica lista.")
        return True
    except Exception as e:
        _log(log_func, f"❌ Error navegando a MejoraBasica: {e}")
        return False


def completar_menu_dinamico(
    page,
    acuerdo: str,
    catalogo: str,
    categoria: str,
    log_func: Optional[Callable[[str], None]] = None
) -> bool:
    """
    FUNCION PADRE 4: Completar Menú Dinámico y Filtros.
    
    Asegura que el navegador esté en MejoraBasica, selecciona los 3 dropdowns
    del catálogo y hace clic explícito en 'Iniciar Búsqueda' (#btnBuscar).
    """
    from modulo_subir_pdf.automation_otro_bot.stock import paso3_filtros_stock
    
    if "MejoraBasica" not in page.url or not page.query_selector("#N_Acuerdo, #ajaxAcuerdo"):
        _log(log_func, "📍 Redirigiendo a MejoraBasica antes de aplicar filtros...")
        try:
            page.goto(MEJORA_URL, wait_until="networkidle", timeout=60_000)
            time.sleep(3)
        except Exception as e:
            _log(log_func, f"⚠️ Advertencia en redirección: {e}")

    _log(log_func, f"📋 Aplicando filtros en menú dinámico: {acuerdo} > {catalogo} > {categoria}")
    ok = paso3_filtros_stock(page, acuerdo, catalogo, categoria)
    if ok:
        _log(log_func, "✅ Menú dinámico configurado y búsqueda iniciada correctamente.")
    else:
        _log(log_func, "❌ Error al seleccionar opciones en el menú dinámico.")
    return ok


def insertar_stock_item(
    page,
    nro_parte: str,
    nuevo_stock: int,
    pausa: float = 2.0,
    log_func: Optional[Callable[[str], None]] = None
) -> Dict[str, Any]:
    """
    FUNCION PADRE 5: Insertar / Actualizar Stock de Producto.
    """
    _log(log_func, f"🔍 Buscando producto '{nro_parte}' para asignar stock={nuevo_stock}...")
    try:
        page.wait_for_selector("#txtBuscar", timeout=15_000)
        page.fill("#txtBuscar", str(nro_parte))
        page.keyboard.press("Enter")
        time.sleep(2)

        filas = page.query_selector_all("#tbProductos tbody tr")
        if not filas or len(filas) == 0:
            msg = f"❌ Producto '{nro_parte}' no hallado en el portal."
            _log(log_func, msg)
            return {"exito": False, "parte": nro_parte, "stock": nuevo_stock, "mensaje": msg}

        input_stock = page.query_selector("#tbProductos tbody tr:first-child input[name*='Existencias']")
        if not input_stock:
            input_stock = page.query_selector("#tbProductos tbody tr:first-child input.txt-stock")

        if not input_stock:
            msg = f"❌ Campo de stock no editable para '{nro_parte}'."
            _log(log_func, msg)
            return {"exito": False, "parte": nro_parte, "stock": nuevo_stock, "mensaje": msg}

        input_stock.fill(str(nuevo_stock))
        
        btn_guardar = page.query_selector("#tbProductos tbody tr:first-child button.btn-guardar-stock")
        if btn_guardar:
            btn_guardar.click()
            time.sleep(pausa)

        msg = f"✅ Stock actualizado a {nuevo_stock} para '{nro_parte}'."
        _log(log_func, msg)
        return {"exito": True, "parte": nro_parte, "stock": nuevo_stock, "mensaje": msg}

    except Exception as e:
        msg = f"❌ Error insertando stock para '{nro_parte}': {e}"
        _log(log_func, msg)
        return {"exito": False, "parte": nro_parte, "stock": nuevo_stock, "mensaje": msg}


def consultar_json_productos(
    page,
    n_acuerdo: Optional[int] = None,
    n_catalogo: Optional[int] = None,
    n_categoria: Optional[int] = None,
    log_func: Optional[Callable[[str], None]] = None
) -> List[Dict[str, Any]]:
    """
    FUNCION PADRE 6: Extracción Masiva del Dataset JSON de Fichas.
    
    Extrae y parsea el dataset de productos/fichas desde la tabla `#TablaProductos`
    del portal Perú Compras (MejoraBasica) convirtiendo las filas HTML en objetos JSON.
    """
    _log(log_func, "📡 Solicitando dataset JSON crudo del portal...")

    # ── ESTRATEGIA 1: Extraer y parsear directamente la tabla #TablaProductos del DOM activo
    try:
        data_dom = page.evaluate("""() => {
            try {
                let rows = [];
                if (window.jQuery && window.jQuery.fn.DataTable && window.jQuery('#TablaProductos').length) {
                    const dt = window.jQuery('#TablaProductos').DataTable();
                    if (dt && dt.rows().nodes().length > 0) {
                        rows = Array.from(dt.rows().nodes());
                    }
                }
                if (!rows || rows.length === 0) {
                    rows = Array.from(document.querySelectorAll('#TablaProductos tbody tr'));
                }

                const items = [];
                rows.forEach(tr => {
                    const tds = tr.querySelectorAll('td');
                    if (tds.length < 5) return;

                    const desc = tds[1] ? tds[1].innerText.trim() : "";
                    if (!desc || desc.includes("No se encontraron")) return;

                    const estado = tds[2] ? tds[2].innerText.trim() : "";
                    const moneda = tds[3] ? tds[3].innerText.trim() : "";
                    const precioTxt = tds[4] ? tds[4].innerText.trim().replace(/,/g, '') : "0";
                    const precioPubTxt = tds[5] ? tds[5].innerText.trim().replace(/,/g, '') : "0";
                    const stockTxt = tds[6] ? tds[6].innerText.trim().replace(/,/g, '') : "0";
                    const stockPubTxt = tds[7] ? tds[7].innerText.trim().replace(/,/g, '') : "0";
                    
                    const htmlTd8 = tds[8] ? tds[8].innerHTML : "";
                    const htmlTd9 = tds[9] ? tds[9].innerHTML : "";
                    
                    let idOfertado = "";
                    let idCatalogo = "";
                    
                    const matchOfertado = htmlTd9.match(/fnReducirPrecio\((\d+)\)/) || htmlTd9.match(/fnModificarStock\((\d+)\)/);
                    if (matchOfertado) idOfertado = matchOfertado[1];

                    const matchCatalogo = htmlTd8.match(/fnDetalleRegistro\((\d+)\)/);
                    if (matchCatalogo) idCatalogo = matchCatalogo[1];

                    items.push({
                        "ID_ProductoOfertado": idOfertado,
                        "ID_CatalogoProducto": idCatalogo,
                        "C_Descripcion": desc,
                        "C_Estado": estado,
                        "C_MonedaOfertada": moneda,
                        "N_PrecioOfertado": parseFloat(precioTxt) || 0.0,
                        "N_PrecioOfertadoPorPublicar": parseFloat(precioPubTxt) || 0.0,
                        "N_Stock": parseInt(stockTxt) || 0,
                        "N_StockPorPublicar": parseInt(stockPubTxt) || 0
                    });
                });

                return items;
            } catch(e) {
                return null;
            }
        }""")

        if isinstance(data_dom, list) and len(data_dom) > 0:
            _log(log_func, f"✅ Dataset extraído exitosamente desde la tabla en pantalla ({len(data_dom)} fichas).")
            return data_dom
    except Exception as e:
        _log(log_func, f"ℹ️ Extracción directa del DOM omitida: {e}")

    # Extraer IDs dinámicos del DOM si están disponibles
    try:
        dom_ids = page.evaluate("""() => {
            const ac = document.querySelector('#ajaxAcuerdo, #N_Acuerdo, select[name*="cuerdo"]')?.value;
            const cat = document.querySelector('#ajaxCatalogo, #N_Catalogo, select[name*="atalogo"]')?.value;
            const catg = document.querySelector('#ajaxCategoria, #N_Categoria, select[name*="ategoria"]')?.value;
            return { ac: ac || null, cat: cat || null, catg: catg || null };
        }""")
        if dom_ids.get("ac") and str(dom_ids["ac"]).isdigit():
            n_acuerdo = int(dom_ids["ac"])
        if dom_ids.get("cat") and str(dom_ids["cat"]).isdigit():
            n_catalogo = int(dom_ids["cat"])
        if dom_ids.get("catg") and str(dom_ids["catg"]).isdigit():
            n_categoria = int(dom_ids["catg"])
    except Exception:
        pass

    n_acuerdo = n_acuerdo or 249
    n_catalogo = n_catalogo or 252
    n_categoria = n_categoria or 11736

    _log(log_func, f"  🔍 Parámetros de consulta: Acuerdo={n_acuerdo}, Catálogo={n_catalogo}, Categoría={n_categoria}")

    # ── ESTRATEGIA 2: Fetch HTTP de _ListaProductosOfertados y parseo de HTML a JSON
    ts = int(time.time() * 1000)
    endpoint_get = (
        f"{BASE_URL}/MejoraBasica/_ListaProductosOfertados"
        f"?N_Acuerdo={n_acuerdo}&N_Catalogo={n_catalogo}"
        f"&N_Categoria={n_categoria}&C_Descripcion=&_={ts}"
    )

    try:
        resp = page.request.get(
            endpoint_get,
            headers={
                "X-Requested-With": "XMLHttpRequest",
                "Referer": f"{BASE_URL}/MejoraBasica",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            },
            timeout=35000
        )

        if resp.status == 200:
            html_text = resp.text()
            data_parsed = page.evaluate("""(html) => {
                try {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const rows = doc.querySelectorAll('#TablaProductos tbody tr, table tbody tr');
                    const items = [];

                    rows.forEach(tr => {
                        const tds = tr.querySelectorAll('td');
                        if (tds.length < 5) return;

                        const desc = tds[1] ? tds[1].innerText.trim() : "";
                        if (!desc || desc.includes("No se encontraron")) return;

                        const estado = tds[2] ? tds[2].innerText.trim() : "";
                        const moneda = tds[3] ? tds[3].innerText.trim() : "";
                        const precioTxt = tds[4] ? tds[4].innerText.trim().replace(/,/g, '') : "0";
                        const precioPubTxt = tds[5] ? tds[5].innerText.trim().replace(/,/g, '') : "0";
                        const stockTxt = tds[6] ? tds[6].innerText.trim().replace(/,/g, '') : "0";
                        const stockPubTxt = tds[7] ? tds[7].innerText.trim().replace(/,/g, '') : "0";

                        const htmlTd8 = tds[8] ? tds[8].innerHTML : "";
                        const htmlTd9 = tds[9] ? tds[9].innerHTML : "";
                        
                        let idOfertado = "";
                        let idCatalogo = "";
                        
                        const matchOfertado = htmlTd9.match(/fnReducirPrecio\((\d+)\)/) || htmlTd9.match(/fnModificarStock\((\d+)\)/);
                        if (matchOfertado) idOfertado = matchOfertado[1];

                        const matchCatalogo = htmlTd8.match(/fnDetalleRegistro\((\d+)\)/);
                        if (matchCatalogo) idCatalogo = matchCatalogo[1];

                        items.push({
                            "ID_ProductoOfertado": idOfertado,
                            "ID_CatalogoProducto": idCatalogo,
                            "C_Descripcion": desc,
                            "C_Estado": estado,
                            "C_MonedaOfertada": moneda,
                            "N_PrecioOfertado": parseFloat(precioTxt) || 0.0,
                            "N_PrecioOfertadoPorPublicar": parseFloat(precioPubTxt) || 0.0,
                            "N_Stock": parseInt(stockTxt) || 0,
                            "N_StockPorPublicar": parseInt(stockPubTxt) || 0
                        });
                    });

                    return items;
                } catch(e) {
                    return [];
                }
            }""", html_text)

            if isinstance(data_parsed, list) and len(data_parsed) > 0:
                _log(log_func, f"✅ Dataset extraído y parseado exitosamente vía HTML Endpoint ({len(data_parsed)} fichas).")
                return data_parsed

    except Exception as e:
        _log(log_func, f"⚠️ Error en Estrategia HTML Endpoint: {e}")

    # ── ESTRATEGIA 3: POST Endpoint DataTables _CatalogoProductoIndexJson
    endpoint_post = f"{BASE_URL}/t_ProductoOfertadoAmp/_CatalogoProductoIndexJson"
    payload = {
        "draw": "1", "start": "0", "length": "5000",
        "search[value]": "", "search[regex]": "false",
        "N_Acuerdo": str(n_acuerdo), "N_Catalogo": str(n_catalogo), "N_Categoria": str(n_categoria)
    }

    try:
        resp_post = page.request.post(
            endpoint_post,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": f"{BASE_URL}/t_ProductoOfertadoAmp/CatalogoProductoIndex"
            },
            data=payload,
            timeout=35000
        )

        if resp_post.status == 200:
            text_post = resp_post.text().strip().lstrip('\ufeff')
            if text_post and text_post.startswith('{'):
                parsed_post = json.loads(text_post)
                data_post = parsed_post.get("data", []) if isinstance(parsed_post, dict) else parsed_post
                if isinstance(data_post, list) and len(data_post) > 0:
                    _log(log_func, f"✅ Dataset extraído exitosamente vía POST DataTables ({len(data_post)} fichas).")
                    return data_post

    except Exception as e:
        _log(log_func, f"❌ Error en Estrategia POST: {e}")

    _log(log_func, "❌ No se pudieron extraer fichas del portal.")
    return []


def extraer_json_catalogo(
    usuario: str = "estalin.huamali01",
    password: str = "",
    n_acuerdo: int = 249,
    n_catalogo: int = 252,
    n_categoria: int = 11736,
    acuerdo_texto: str = "EXT-CE-2022-5 COMPUTADORAS Y ESCÁNERES",
    catalogo_texto: str = "COMPUTADORAS DE ESCRITORIO",
    categoria_texto: str = "COMPUTADORA TODO EN UNO",
    output_path: Optional[str] = None,
    captcha_bridge = None,
    stop_event = None,
    log_func: Optional[Callable[[str], None]] = None,
    headless: bool = True
) -> List[Dict[str, Any]]:
    """
    FUNCION PADRE 7: Extracción Completa de JSON a Disco/Memoria.
    
    Flujo E2E completo:
      1. Inicia navegador Playwright (HD 1920x1080).
      2. Ejecuta `login_automatico` con OCR Tesseract ilimitado.
      3. Ejecuta `saltar_verificacion` hacia MejoraBasica.
      4. Ejecuta `completar_menu_dinamico` + clic en #btnBuscar.
      5. Ejecuta `consultar_json_productos` para extraer el dataset completo.
      6. Guarda opcionalmente el archivo JSON en `output_path`.
    """
    from automation.browser import init_browser, close_browser

    _log(log_func, f"🚀 [PADRE 7] Iniciando extracción masiva de JSON (Usuario: {usuario})...")
    pw = browser = page = None
    data = []

    try:
        pw, browser, page = init_browser(headless=headless)

        if not login_automatico(page, usuario, password, captcha_bridge, stop_event, log_func):
            _log(log_func, "❌ Login falló. Extracción JSON cancelada.")
            return []

        saltar_verificacion(page, log_func)
        completar_menu_dinamico(page, acuerdo_texto, catalogo_texto, categoria_texto, log_func)
        data = consultar_json_productos(page, n_acuerdo, n_catalogo, n_categoria, log_func)

        if output_path and data:
            try:
                folder = os.path.dirname(os.path.abspath(output_path))
                os.makedirs(folder, exist_ok=True)
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                _log(log_func, f"💾 Dataset guardado exitosamente en: {output_path}")
            except Exception as e:
                _log(log_func, f"⚠️ Error guardando archivo JSON: {e}")

        return data

    except Exception as e:
        _log(log_func, f"❌ Error en extraer_json_catalogo: {e}")
        return []

    finally:
        if pw and browser:
            close_browser(pw, browser)

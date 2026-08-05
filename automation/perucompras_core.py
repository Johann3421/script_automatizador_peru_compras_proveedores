"""
automation/perucompras_core.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Módulo de Funciones Padre Reutilizables de Automatización Perú Compras.

Este módulo centraliza todas las operaciones atómicas y compuestas
con el portal de Perú Compras, desacopladas al 100% de la interfaz de usuario (UI):
  1. `login_automatico`: Inicio de sesión robusto con OCR Tesseract.
  2. `saltar_verificacion`: Maniobra de retroceso y evasion de verificaciones.
  3. `navegar_mejora_basica`: Navegación garantizada a la sección MejoraBasica.
  4. `completar_menu_dinamico`: Selección flexible de combos de catálogo.
  5. `insertar_stock_item`: Actualización atómica de stock de un producto.
  6. `consultar_json_productos`: Extracción del dataset JSON crudo.
"""

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
    
    Parámetros
    ----------
    page : Playwright Page
        Instancia de la página activa del navegador.
    usuario : str
        Nombre de usuario del proveedor en Perú Compras.
    password : str
        Contraseña de acceso.
    captcha_bridge : CaptchaBridge, opcional
        Puente para resolución manual si el OCR falla.
    stop_event : threading.Event, opcional
        Evento de detención provisto por la app.
    log_func : Callable[[str], None], opcional
        Función para recibir logs de progreso.
        
    Retorno
    -------
    bool
        True si el inicio de sesión fue exitoso, False si falló.
    """
    from automation.login import do_login
    
    _log(log_func, "🔐 [PADRE] Iniciando login automático en Perú Compras...")
    try:
        page.set_viewport_size({"width": 1920, "height": 1080})
    except Exception as e:
        _log(log_func, f"⚠️ No se pudo fijar viewport HD: {e}")

    class _LogAdapter:
        def write(self, txt):
            clean = txt.strip()
            if clean:
                _log(log_func, clean)
        def flush(self): pass

    log_adapter = _LogAdapter()
    ok = do_login(page, usuario, password, "", log_adapter, stop_event, captcha_bridge)
    if ok:
        _log(log_func, "✅ [PADRE] Login automático exitoso.")
    else:
        _log(log_func, "❌ [PADRE] Login automático falló.")
    return ok


def saltar_verificacion(
    page,
    log_func: Optional[Callable[[str], None]] = None
) -> bool:
    """
    FUNCION PADRE 2: Saltar Verificación y Retroceso Seguro.
    
    Ejecuta el truco de retroceso de historial de navegación en el browser
    y vuelve a cargar el portal base para refrescar cookies de sesión.
    
    Parámetros
    ----------
    page : Playwright Page
        Instancia activa del navegador.
    log_func : Callable[[str], None], opcional
        Función para recepción de logs.
        
    Retorno
    -------
    bool
        True al completar la maniobra de retroceso.
    """
    _log(log_func, "🔄 [PADRE] Ejecutando maniobra de retroceso seguro y evasión...")
    try:
        page.go_back()
        time.sleep(1.5)
    except Exception as e:
        _log(log_func, f"ℹ️ go_back omitido: {e}")

    try:
        page.goto(BASE_URL, wait_until="networkidle", timeout=60_000)
        time.sleep(1.5)
        return True
    except Exception as e:
        _log(log_func, f"⚠️ Error navegando a BASE_URL: {e}")
        return False


def navegar_mejora_basica(
    page,
    log_func: Optional[Callable[[str], None]] = None
) -> bool:
    """
    FUNCION PADRE 3: Navegación Garantizada a MejoraBasica.
    
    Navega a la sección de catálogo y actualización del portal.
    
    Parámetros
    ----------
    page : Playwright Page
    log_func : Callable[[str], None], opcional
    
    Retorno
    -------
    bool
        True si la página de MejoraBasica cargó correctamente.
    """
    _log(log_func, "📍 [PADRE] Navegando a la sección MejoraBasica...")
    try:
        page.goto(MEJORA_URL, wait_until="networkidle", timeout=60_000)
        time.sleep(2)
        _log(log_func, "✅ [PADRE] Sección MejoraBasica cargada.")
        return True
    except Exception as e:
        _log(log_func, f"❌ [PADRE] Error navegando a MejoraBasica: {e}")
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
    
    Selecciona de forma flexible (insensible a tildes y mayúsculas) los 3 dropdowns
    del catálogo electrónico (Acuerdo, Catálogo y Categoría).
    
    Parámetros
    ----------
    page : Playwright Page
    acuerdo : str
        Nombre del Acuerdo Marco.
    catalogo : str
        Nombre del Catálogo.
    categoria : str
        Nombre de la Categoría.
    log_func : Callable[[str], None], opcional
    
    Retorno
    -------
    bool
        True si los 3 combos se seleccionaron con éxito.
    """
    from modulo_subir_pdf.automation_otro_bot.stock import paso3_filtros_stock
    
    _log(log_func, f"📋 [PADRE] Completando menú dinámico: {acuerdo} > {catalogo} > {categoria}")
    ok = paso3_filtros_stock(page, acuerdo, catalogo, categoria)
    if ok:
        _log(log_func, "✅ [PADRE] Menú dinámico configurado correctamente.")
    else:
        _log(log_func, "❌ [PADRE] Error al seleccionar opciones en el menú dinámico.")
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
    
    Busca una ficha por su número de parte o código en el cuadro de búsqueda principal
    del portal e inserta la nueva cantidad de existencias.
    
    Parámetros
    ----------
    page : Playwright Page
    nro_parte : str
        Número de parte o código del producto a buscar.
    nuevo_stock : int
        Cantidad de existencias a asignar.
    pausa : float
        Pausa de espera en segundos tras la actualización.
    log_func : Callable[[str], None], opcional
    
    Retorno
    -------
    dict
        {"exito": bool, "parte": str, "stock": int, "mensaje": str}
    """
    _log(log_func, f"🔍 [PADRE] Buscando producto '{nro_parte}' para asignar stock={nuevo_stock}...")
    try:
        # Esperar cuadro de búsqueda principal
        page.wait_for_selector("#txtBuscar", timeout=15_000)
        page.fill("#txtBuscar", str(nro_parte))
        page.keyboard.press("Enter")
        time.sleep(2)

        # Verificar si encontró filas en la tabla
        filas = page.query_selector_all("#tbProductos tbody tr")
        if not filas or len(filas) == 0:
            msg = f"❌ Producto '{nro_parte}' no hallado en el portal."
            _log(log_func, msg)
            return {"exito": False, "parte": nro_parte, "stock": nuevo_stock, "mensaje": msg}

        # Seleccionar primer campo de stock e ingresar nuevo valor
        input_stock = page.query_selector("#tbProductos tbody tr:first-child input[name*='Existencias']")
        if not input_stock:
            input_stock = page.query_selector("#tbProductos tbody tr:first-child input.txt-stock")

        if not input_stock:
            msg = f"❌ Campo de stock no editable para '{nro_parte}'."
            _log(log_func, msg)
            return {"exito": False, "parte": nro_parte, "stock": nuevo_stock, "mensaje": msg}

        input_stock.fill(str(nuevo_stock))
        
        # Guardar cambios
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
    n_acuerdo: int,
    n_catalogo: int,
    n_categoria: int,
    log_func: Optional[Callable[[str], None]] = None
) -> List[Dict[str, Any]]:
    """
    FUNCION PADRE 6: Extracción Masiva del Dataset JSON de Fichas.
    
    Consulta el endpoint JSON crudo `_ListaProductosOfertados` mediante `fetch`
    con las cookies activas de la sesión.
    
    Parámetros
    ----------
    page : Playwright Page
    n_acuerdo : int
    n_catalogo : int
    n_categoria : int
    log_func : Callable[[str], None], opcional
    
    Retorno
    -------
    list
        Lista de diccionarios de fichas ofertadas extraídas.
    """
    _log(log_func, f"📡 [PADRE] Extrayendo dataset JSON crudo (Acuerdo:{n_acuerdo}, Cat:{n_catalogo}, Catg:{n_categoria})...")
    ts = int(time.time() * 1000)
    endpoint = (
        f"{BASE_URL}/MejoraBasica/_ListaProductosOfertados"
        f"?N_Acuerdo={n_acuerdo}&N_Catalogo={n_catalogo}"
        f"&N_Categoria={n_categoria}&C_Descripcion=&_={ts}"
    )

    try:
        raw = page.evaluate(f"""
            async () => {{
                try {{
                    const r = await fetch('{endpoint}', {{
                        method: 'GET', credentials: 'include'
                    }});
                    if (!r.ok) return '__HTTP_' + r.status;
                    return await r.text();
                }} catch(e) {{
                    return '__ERR_' + e.toString();
                }}
            }}
        """)

        if not raw or str(raw).startswith("__"):
            _log(log_func, f"❌ [PADRE] Error al consultar endpoint: {raw}")
            return []

        parsed = json.loads(raw)
        data = parsed.get("data", []) if isinstance(parsed, dict) else parsed
        _log(log_func, f"✅ [PADRE] Dataset extraído exitosamente ({len(data)} fichas).")
        return data if isinstance(data, list) else []

    except Exception as e:
        _log(log_func, f"❌ [PADRE] Error parseando JSON de productos: {e}")
        return []

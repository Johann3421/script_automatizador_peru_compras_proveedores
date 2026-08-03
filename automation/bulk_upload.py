"""
Bulk Upload — Subida masiva de precios vía HTTP directo.

Reemplaza el bucle 1x1 (playwright) por llamadas HTTP paralelas.
Velocidad estimada: ~30-60 productos/minuto (busqueda individual por parte).

Flujo:
  1. Extrae cookies de sesión del Browser (Playwright ya autenticado)
  2. Para CADA fila del Excel, busca el part number via _CatalogoProductoIndexJson
     (mismo filtro que el buscador del sitio: C_Descripcion={parte})
  3. Matchea el part number dentro de los 1-3 resultados
  4. Envía los precios en paralelo con httpx (Inserta_ProductoOfertadoTMP)
  5. Confirma el envío (EnviarOferta)
"""

import time, re, concurrent.futures, threading
import httpx

BASE_URL = "https://www.catalogos.perucompras.gob.pe"
URL_TABLA = f"{BASE_URL}/t_ProductoOfertadoAmp/_CatalogoProductoIndexJson"
URL_INSERTA = f"{BASE_URL}/t_ProductoOfertadoAmp/Inserta_ProductoOfertadoTMP"

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "origin": BASE_URL,
    "referer": f"{BASE_URL}/t_ProductoOfertadoAmp/CatalogoProductoIndex",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "accept": "application/json, text/javascript, */*; q=0.01",
}


def _cookies_from_page(page) -> dict[str, str]:
    raw = page.context.cookies()
    return {c["name"]: c["value"] for c in raw}


def _build_datatable_payload(N_Acuerdo, N_Catalogo, N_Categoria, start=0, length=500, search=""):
    cols = ["C_Imagen", "C_Descripcion", "C_ArchivoDescriptivo",
            "C_MonedaOfertada", "N_PrecioOfertado", "N_CatalogoProducto", "C_Estado"]
    params = {
        "draw": "1", "order[0][column]": "0", "order[0][dir]": "asc",
        "start": str(start), "length": str(length),
        "search[value]": search, "search[regex]": "false",
        "N_Acuerdo": str(N_Acuerdo), "N_Catalogo": str(N_Catalogo),
        "N_Categoria": str(N_Categoria), "C_Descripcion": search,
    }
    for i, col in enumerate(cols):
        for key, val in {
            f"columns[{i}][data]": col, f"columns[{i}][name]": col,
            f"columns[{i}][searchable]": "true",
            f"columns[{i}][orderable]": "true",
            f"columns[{i}][search][value]": "",
            f"columns[{i}][search][regex]": "false",
        }.items():
            params[key] = val
    return params


def buscar_producto_por_parte(client: httpx.Client, N_Acuerdo, N_Catalogo, N_Categoria,
                              parte: str) -> list[dict]:
    """Busca productos filtrando por parte en C_Descripcion (como el buscador del sitio)."""
    payload = _build_datatable_payload(N_Acuerdo, N_Catalogo, N_Categoria,
                                       start=0, length=10, search=parte)
    try:
        resp = client.post(URL_TABLA, data=payload, headers=HEADERS, timeout=60)
        resp.raise_for_status()
        return resp.json().get("data", [])
    except Exception:
        return []


def _match_parte_in_results(parte: str, results: list[dict]) -> dict | None:
    """Busca el mejor match de un part number entre los resultados de busqueda."""
    key = _normalize(parte)
    if not key or not results:
        return None
    # 1) Exact substring
    for r in results:
        desc = _normalize(r.get("C_Descripcion") or "")
        if key in desc:
            return r
    # 2) Alphanumeric-only
    clean = re.sub(r"[^A-Z0-9]", "", key)
    if clean and len(clean) >= 3:
        for r in results:
            desc_clean = re.sub(r"[^A-Z0-9]", "", _normalize(r.get("C_Descripcion") or ""))
            if clean in desc_clean:
                return r
    return None


def _search_and_match_one(args) -> dict:
    """Busca un part number y matchea. args = (row, parte_col, precio_col,
       N_Acuerdo, N_Catalogo, N_Categoria, cookies_dict, log)"""
    row, parte_col, precio_col, N_Acuerdo, N_Catalogo, N_Categoria, cookies_dict, log = args

    parte = str(row.get(parte_col) or "").strip()
    precio_raw = str(row.get(precio_col) or "").strip()
    try:
        precio_num = float(precio_raw.replace(",", ".").replace(" ", ""))
    except (ValueError, TypeError):
        precio_num = None

    result = {**row, "parte": parte, "precio_raw": precio_raw,
              "precio": precio_num, "status": "pendiente"}

    if not parte:
        result["status"] = "sin_part_number"
        return result
    if precio_num is None:
        result["status"] = "sin_precio"
        return result

    result["N_CatalogoProducto"] = ""
    result["moneda"] = "USD"

    try:
        with httpx.Client(cookies=cookies_dict, follow_redirects=True, timeout=60) as client:
            search_results = buscar_producto_por_parte(
                client, N_Acuerdo, N_Catalogo, N_Categoria, parte)
    except Exception as e:
        result["status"] = "error"
        result["resp"] = str(e)
        return result

    if not search_results:
        result["status"] = "no_encontrado"
        return result

    cat = _match_parte_in_results(parte, search_results)
    if cat:
        result["N_CatalogoProducto"] = str(cat.get("N_CatalogoProducto") or "")
        result["moneda"] = str(cat.get("C_MonedaOfertada") or "USD")
        if len(search_results) > 1:
            log.info(f"Parte '{parte}': {len(search_results)} coincidencias")
    else:
        result["status"] = "no_encontrado"

    return result


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").strip().upper())


def fetch_catalogo_completo(client: httpx.Client, N_Acuerdo, N_Catalogo, N_Categoria, log) -> list[dict]:
    """Descarga TODOS los productos del catalogo paginando de 500 en 500."""
    log.info("Descargando tabla completa del catálogo...")
    todos = []
    start = 0
    PAGE = 500

    while True:
        payload = _build_datatable_payload(N_Acuerdo, N_Catalogo, N_Categoria, start=start, length=PAGE)
        try:
            resp = client.post(URL_TABLA, data=payload, headers=HEADERS, timeout=60)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            log.warn(f"Error en pagina start={start}: {e}")
            break
        records = data.get("data", [])
        total = data.get("recordsTotal", 0)
        todos.extend(records)
        if start + PAGE >= total:
            break
        start += PAGE
        time.sleep(0.3)

    log.info(f"Catalogo descargado: {len(todos)} productos")
    return todos



def _build_index(catalogo_rows: list[dict]) -> dict[str, dict]:
    idx = {}
    for r in catalogo_rows:
        desc = _normalize(r.get("C_Descripcion") or "")
        nid = str(r.get("N_CatalogoProducto") or "").strip()
        if desc:
            idx[desc] = r
        if nid:
            idx[nid] = r
    return idx


def _match_parte(parte: str, idx: dict) -> dict | None:
    key = _normalize(parte)
    if not key:
        return None
    if key in idx:
        return idx[key]
    for k, v in idx.items():
        if key in k or k in key:
            return v
    clean = re.sub(r"[^A-Z0-9]", "", key)
    if clean:
        for k, v in idx.items():
            if clean in re.sub(r"[^A-Z0-9]", "", k):
                return v
    return None


def match_excel_rows(excel_rows: list[dict], parte_col: str, precio_col: str,
                     catalogo_rows: list[dict], log) -> list[dict]:
    """Cruza filas del Excel con catálogo. Retorna filas enriquecidas."""
    idx = _build_index(catalogo_rows)
    matched = []
    no_encontrados = 0

    # ── Diagnostico ──
    log.info("--- DIAGNOSTICO DE MATCHING ---")
    log.info("Filas catalogo: %d  |  Filas Excel: %d" % (len(catalogo_rows), len(excel_rows)))
    if catalogo_rows:
        log.info("Muestra catalogo (primeros 3):")
        for i, r in enumerate(catalogo_rows[:3]):
            log.info("  [%d] keys=%s" % (i, list(r.keys())[:10]))
            c_desc = str(r.get("C_Descripcion", ""))[:80]
            c_nid = r.get("N_CatalogoProducto", "")
            log.info("       C_Descripcion=%s  N_CatalogoProducto=%s" % (c_desc, c_nid))
    if excel_rows:
        log.info("Part numbers del Excel (primeros 5):")
        for i, r in enumerate(excel_rows[:5]):
            parte = str(r.get(parte_col, ""))[:80]
            precio = str(r.get(precio_col, ""))[:20]
            log.info("  [%d] parte='%s'  precio=%s" % (i, parte, precio))
    log.info("Claves del indice (primeras 10):")
    for i, k in enumerate(list(idx.keys())[:10]):
        log.info("  [%d] '%s'" % (i, str(k)[:120]))
    # ── Busqueda exhaustiva: donde aparecen los part numbers en el catalogo ──
    if excel_rows and catalogo_rows:
        log.info("Buscando part numbers del Excel en TODAS las columnas del catalogo...")
        for i, r in enumerate(excel_rows[:3]):
            parte = str(r.get(parte_col, "")).strip()
            if not parte:
                continue
            found = False
            for cat_row in catalogo_rows:
                for k, v in cat_row.items():
                    sv = str(v)
                    if parte in sv:
                        log.info(f"  PARTE '{parte}' encontrado en columna '{k}' = '{sv[:100]}'")
                        found = True
                        break
                if found:
                    break
            if not found:
                log.info(f"  PARTE '{parte}' NO encontrado en NINGUNA columna de {len(catalogo_rows)} filas")

    log.info("--- FIN DIAGNOSTICO ---")

    for row in excel_rows:
        parte = str(row.get(parte_col) or "").strip()
        precio_raw = str(row.get(precio_col) or "").strip()
        try:
            precio_num = float(precio_raw.replace(",", ".").replace(" ", ""))
        except (ValueError, TypeError):
            precio_num = None

        result = {
            **row,
            "parte": parte, "precio_raw": precio_raw,
            "precio": precio_num, "status": "pendiente",
        }
        if not parte:
            result["status"] = "sin_part_number"
        elif precio_num is None:
            result["status"] = "sin_precio"
        else:
            cat = _match_parte(parte, idx)
            if not cat:
                result["status"] = "no_encontrado"
                no_encontrados += 1
            else:
                result["N_CatalogoProducto"] = str(cat.get("N_CatalogoProducto") or "")
                result["moneda"] = str(cat.get("C_MonedaOfertada") or "USD")
        matched.append(result)

    log.info(f"Match: {len(matched)} filas ({no_encontrados} no encontrados)")
    return matched


def _interpret_response(text: str) -> str:
    t = text.lower()
    if any(w in t for w in ["excede", "supera", "máximo", "maximo", "mayor"]):
        return "excede"
    if any(w in t for w in ["inferior", "menor", "mínimo", "minimo"]):
        return "inferior"
    if "error" in t:
        return "error"
    return "ok"


def _insert_one(args) -> dict:
    """Envía un precio. args = (row_dict, cookies_dict)"""
    row, cookies = args
    payload = {
        "N_CatalogoProducto": row["N_CatalogoProducto"],
        "C_MonedaOfertada": row.get("moneda", "USD"),
        "N_PrecioOfertado": str(row["precio"]),
    }
    try:
        resp = httpx.post(URL_INSERTA, data=payload, headers=HEADERS, cookies=cookies, timeout=30)
        row["status"] = _interpret_response(resp.text)
        row["resp"] = resp.text[:200]
    except Exception as e:
        row["status"] = "error"
        row["resp"] = str(e)
    return row


def insertar_precios_masivo(cookies_dict: dict, rows_pendientes: list[dict],
                            stop_event: threading.Event, log,
                            max_workers: int = 10, batch_confirm: int = 200) -> tuple[int, int]:
    """
    Envía precios en paralelo usando ThreadPoolExecutor.
    Cada 'batch_confirm' OK, confirma la oferta vía EnviarOferta.
    Retorna (ok_count, error_count).
    """
    total = len(rows_pendientes)
    ok_count = 0
    error_count = 0
    args_list = [(r, cookies_dict) for r in rows_pendientes]

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as pool:
        fut_to_row = {pool.submit(_insert_one, args): i for i, args in enumerate(args_list)}
        done = 0
        for future in concurrent.futures.as_completed(fut_to_row):
            if stop_event and stop_event.is_set():
                break
            idx = fut_to_row[future]
            try:
                row = future.result()
                rows_pendientes[idx] = row
                if row["status"] == "ok":
                    ok_count += 1
                else:
                    error_count += 1
            except Exception as e:
                rows_pendientes[idx]["status"] = "error"
                rows_pendientes[idx]["resp"] = str(e)
                error_count += 1

            done += 1
            if done % 20 == 0 or done == total:
                log.progress(done, total)

    # Confirmacion final (fuera del pool)
    if ok_count > 0:
        with httpx.Client(cookies=cookies_dict, follow_redirects=True, timeout=30) as client:
            _enviar_oferta(client, log)

    return ok_count, error_count


def _enviar_oferta(client: httpx.Client, log) -> bool:
    """Confirma la oferta (equivalente a click en #btn_enviarOferta2)."""
    for suffix in ["/EnviarOferta", "/Enviar_Oferta", "/ConfirmarOferta"]:
        url = f"{BASE_URL}/t_ProductoOfertadoAmp{suffix}"
        try:
            resp = client.post(url, headers={**HEADERS, "content-type": ""}, timeout=30)
            if resp.status_code == 200:
                log.info(f"Oferta confirmada → {suffix}")
                return True
        except Exception:
            continue
    log.warn("No se pudo confirmar oferta automaticamente")
    return False


def process_bulk_upload(page, rows: list[dict], parte_col: str, precio_col: str,
                        log, stop_event, pre_selected: dict = None) -> list[dict]:
    """
    Entry point: subida masiva via HTTP directo.
    Descarga el catalogo completo y matchea en memoria.

    Returns: list[dict] con status actualizado por fila.
    """
    N_Acuerdo = (pre_selected or {}).get("acuerdo", "")
    N_Catalogo = (pre_selected or {}).get("catalogo", "")
    N_Categoria = (pre_selected or {}).get("categoria", "")

    if not all([N_Acuerdo, N_Catalogo, N_Categoria]):
        log.error("Faltan valores del catalogo (acuerdo/catalogo/categoria)")
        return [{"index": i, "status": "error", "parte": "", "precio": ""} for i in range(len(rows))]

    cookies_dict = _cookies_from_page(page)
    if not cookies_dict:
        log.error("No se pudieron extraer cookies de sesion")
        return [{"index": i, "status": "error"} for i in range(len(rows))]

    with httpx.Client(cookies=cookies_dict, follow_redirects=True, timeout=60) as client:
        catalogo_rows = fetch_catalogo_completo(client, N_Acuerdo, N_Catalogo, N_Categoria, log)
        if not catalogo_rows:
            log.error("Catalogo vacio — no se pueden enviar precios")
            return [{"index": i, "status": "error"} for i in range(len(rows))]

        matched = match_excel_rows(rows, parte_col, precio_col, catalogo_rows, log)

    pendientes = [r for r in matched if r["status"] == "pendiente"]
    if pendientes:
        log.info(f"Enviando {len(pendientes)} precios en paralelo...")
        ok_count, error_count = insertar_precios_masivo(
            cookies_dict, pendientes, stop_event, log
        )
        log.info(f"Bulk upload: {ok_count} OK, {error_count} errores")
    else:
        log.info("No hay productos pendientes para enviar")

    return matched

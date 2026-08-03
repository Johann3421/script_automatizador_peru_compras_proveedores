"""
modificar_loop.py — Bucle principal de modificación de productos.

Por cada fila del Excel:
  1. Busca el producto por N° de Parte
  2. Abre la ficha de edición
  3. Sube el PDF desde D:\\SISTEMAS 02\\Downloads\\COMPUTADORAS\\COMPUTADORAS
  4. Agrega certificaciones: ISO 9001 + ISO 14001
  5. Guarda los cambios
  6. Vuelve a la lista para el siguiente producto

Retorna una lista de resultados con el estado de cada fila.
"""
import os
import time
import threading
from playwright.sync_api import Page

from .navegacion_productos import (
    buscar_producto,
    abrir_edicion,
    subir_pdf,
    agregar_certificaciones,
    guardar_cambios,
    volver_a_lista,
    GESTION_URL,
)

PDF_DIR = r"D:\SISTEMAS 02\Downloads\COMPUTADORAS\COMPUTADORAS"
CERTS = ["ISO 9001", "ISO 14001"]


def run_modificar_loop(
    page: Page,
    rows: list[dict],
    log,
    stop_event: threading.Event,
    pre_selected: dict = None,
) -> list[dict]:
    """
    Bucle principal. Procesa cada fila del Excel.

    Args:
        page: Página de Playwright (ya logueada y en la sección de gestión)
        rows: Lista de dicts con {'parte', 'pdf', 'certs', '_row_idx'}
        log: LogWriter
        stop_event: threading.Event para detener el proceso
        pre_selected: dict con los valores seleccionados en los dropdowns del catalogo

    Returns:
        Lista de dicts con {'index', 'parte', 'status', 'detalle'}
        Status posibles: 'ok', 'no_encontrado', 'error_pdf', 'error_certs', 'error_guardar', 'error'
    """
    results = []
    total = len(rows)
    ok_count = 0
    err_count = 0

    log.info(f"Iniciando modificación de {total} productos...")

    for i, row in enumerate(rows):
        if stop_event.is_set():
            log.warn("Proceso detenido por el usuario.")
            break

        parte = row.get("parte", "")
        pdf_path = os.path.join(PDF_DIR, f"{parte}.pdf") if parte else ""
        certs = CERTS

        log.info(f"[{i+1}/{total}] Procesando: {parte}")

        # Si el log posee una cola, enviamos el progreso
        if hasattr(log, "queue") and log.queue:
            log.queue.put({
                "type": "progress",
                "current": i + 1,
                "total": total,
            })
        elif hasattr(log, "log_queue") and log.log_queue:
            log.log_queue.put({
                "type": "progress",
                "current": i + 1,
                "total": total,
            })

        result = {
            "index":  row.get("_row_idx", i),
            "parte":  parte,
            "status": "error",
            "detalle": "",
        }

        # ── 1. Verificar si la sesión expiró ──────────────────────────────
        if "AccesoGeneral" in page.url:
            log.error("  Sesión expirada. Se requiere re-login manual.")
            result["detalle"] = "sesion_expirada"
            results.append(result)
            err_count += 1
            break

        # ── 2. Buscar producto ────────────────────────────────────────────
        encontrado = buscar_producto(page, parte, log, stop_event)
        if not encontrado:
            result["status"] = "no_encontrado"
            result["detalle"] = "Producto no encontrado en la tabla"
            results.append(result)
            err_count += 1
            time.sleep(1)
            continue

        # ── 3. Abrir edición ──────────────────────────────────────────────
        if not abrir_edicion(page, log):
            result["detalle"] = "No se pudo abrir la ficha de edición"
            results.append(result)
            err_count += 1
            # Volver a la lista para continuar
            volver_a_lista(page, log)
            time.sleep(1)
            continue

        # ── 4. Subir PDF ──────────────────────────────────────────────────
        pdf_ruta = os.path.join(PDF_DIR, f"{parte}.pdf")
        if not subir_pdf(page, pdf_ruta, log):
            result["status"] = "error_pdf"
            result["detalle"] = f"Error subiendo PDF: {pdf_ruta}"
            results.append(result)
            err_count += 1
            volver_a_lista(page, log)
            time.sleep(1)
            continue

        # ── 5. Agregar certificaciones ────────────────────────────────────
        certs_failed = False
        for cert in CERTS:
            if not agregar_certificaciones(page, cert, log):
                result["status"] = "error_certs"
                result["detalle"] = f"Error agregando certificacion: {cert}"
                results.append(result)
                err_count += 1
                volver_a_lista(page, log)
                time.sleep(1)
                certs_failed = True
                break
        if certs_failed:
            continue

        # ── 6. Guardar ────────────────────────────────────────────────────
        if not guardar_cambios(page, log):
            result["status"] = "error_guardar"
            result["detalle"] = "Error al guardar los cambios"
            results.append(result)
            err_count += 1
            volver_a_lista(page, log)
            time.sleep(1)
            continue

        # ── Éxito ─────────────────────────────────────────────────────────
        result["status"] = "ok"
        result["detalle"] = f"PDF: {os.path.basename(pdf_path)} | Certs: ISO 9001 + ISO 14001"
        results.append(result)
        ok_count += 1

        log.ok(f"  ✓ {parte} modificado correctamente")

        # Volver a la lista para el siguiente
        volver_a_lista(page, log)
        time.sleep(1.5)

    log.done(ok_count, err_count)
    return results

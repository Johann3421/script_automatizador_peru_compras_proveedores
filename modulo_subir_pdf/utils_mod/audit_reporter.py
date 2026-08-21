# -*- coding: utf-8 -*-
"""
audit_reporter.py — Módulo Auditor de Resultados e Informe de Auditoría (Excel / PDF)
Permite verificar rápidamente el estado de subidas y generar informes corporativos en Excel o PDF.
"""

import os
import time
from datetime import datetime
from utils_mod.excel_report_designer import build_executive_excel_report, format_elapsed_time


def audit_results(rows_data: list[dict], elapsed_seconds: float | None = None) -> dict:
    """
    Analiza una lista de dicts con la información del proceso.
    Retorna un diccionario summary con métricas completas de auditoría.
    """
    total = len(rows_data)
    ok_cnt = 0
    warn_cnt = 0
    err_cnt = 0

    for r in rows_data:
        st = str(r.get("estado", r.get("resultado", ""))).lower()
        if any(w in st for w in ("éxito", "exito", "ok", "✓", "correcto", "coincide")):
            ok_cnt += 1
        elif any(w in st for w in ("no hallado", "no encontrado", "advertencia", "⚠️", "diferencia", "!=")):
            warn_cnt += 1
        elif any(w in st for w in ("error", "fallo", "✕", "x")):
            err_cnt += 1

    rate = (ok_cnt / total * 100.0) if total > 0 else 0.0
    elapsed_txt = format_elapsed_time(elapsed_seconds) if elapsed_seconds is not None else "—"

    return {
        "total": total,
        "ok": ok_cnt,
        "warn": warn_cnt,
        "err": err_cnt,
        "pending": max(0, total - (ok_cnt + warn_cnt + err_cnt)),
        "rate": round(rate, 1),
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "elapsed_time": elapsed_txt,
        "elapsed_seconds": elapsed_seconds or 0.0,
    }


def export_excel_report(rows_data, summary, output_path, modulo_nombre="Publicación PDF"):
    """
    Genera un informe completo de auditoría en formato Excel (.xlsx) con diseño ejecutivo y dashboards.
    """
    headers = [
        ("idx",         "N°",                    "center", 6),
        ("parte",       "N° de Parte",           "center", 18),
        ("ficha",       "Ficha Técnica",         "center", 16),
        ("descripcion", "Descripción / Marca",   "left",   42),
        ("precio",      "Precio S/",             "right",  16),
        ("stock",       "Stock",                 "center", 12),
        ("estado",      "Resultado de Auditoría","center", 20),
        ("obs",         "Observaciones / Detalle","left",  30),
    ]

    return build_executive_excel_report(
        rows_data=rows_data,
        summary=summary,
        output_path=output_path,
        modulo_nombre=modulo_nombre,
        headers_config=headers
    )


def export_pdf_report(rows_data, summary, output_path, modulo_nombre="Publicación PDF"):
    """
    Genera un informe detallado de auditoría en formato PDF/HTML estructurado.
    """
    try:
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Informe de Auditoría — Perú Compras Bot</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; color: #1A1A1A; margin: 20px; background: #FFF; }}
        .header {{ background: #003366; color: white; padding: 16px; text-align: center; border-radius: 4px; }}
        .header h1 {{ margin: 0; font-size: 18px; }}
        .header p {{ margin: 4px 0 0 0; font-size: 12px; color: #E2E8F0; }}
        .resumen {{ background: #F8F9FA; border: 1px solid #C8C8C8; padding: 12px; margin: 16px 0; border-radius: 4px; }}
        .resumen h3 {{ margin-top: 0; color: #003366; border-bottom: 1px solid #C8C8C8; padding-bottom: 4px; }}
        .grid-sum {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }}
        .stat-card {{ background: white; padding: 10px; border: 1px solid #E0E0E0; border-radius: 4px; text-align: center; }}
        .stat-card .val {{ font-size: 18px; font-weight: bold; margin-top: 4px; }}
        .val.ok {{ color: #0E6251; }}
        .val.warn {{ color: #7D6608; }}
        .val.err {{ color: #78281F; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 16px; }}
        th {{ background: #0F4C81; color: white; padding: 8px; text-align: left; font-size: 11px; }}
        td {{ padding: 8px; border-bottom: 1px solid #E0E0E0; font-size: 11px; }}
        tr:nth-child(even) {{ background: #F9F9F9; }}
        .tag-ok {{ color: #0E6251; font-weight: bold; background: #D1F2EB; padding: 2px 6px; border-radius: 3px; }}
        .tag-warn {{ color: #7D6608; font-weight: bold; background: #FCF3CF; padding: 2px 6px; border-radius: 3px; }}
        .tag-err {{ color: #78281F; font-weight: bold; background: #FADBD8; padding: 2px 6px; border-radius: 3px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>INFORME DE AUDITORÍA — PERÚ COMPRAS BOT v1.4</h1>
        <p>Módulo: {modulo_nombre} | Generado: {summary.get('timestamp', '')} | Duración: {summary.get('elapsed_time', '—')}</p>
    </div>

    <div class="resumen">
        <h3>Resumen Ejecutivo de Verificación</h3>
        <div class="grid-sum">
            <div class="stat-card">
                <div>Total Procesados</div>
                <div class="val">{summary.get('total', 0)}</div>
            </div>
            <div class="stat-card">
                <div>Correctos (✓)</div>
                <div class="val ok">{summary.get('ok', 0)}</div>
            </div>
            <div class="stat-card">
                <div>Advertencias / Dif. (⚠️)</div>
                <div class="val warn">{summary.get('warn', 0)}</div>
            </div>
            <div class="stat-card">
                <div>Errores / No Hallados (✕)</div>
                <div class="val err">{summary.get('err', 0)}</div>
            </div>
        </div>
        <p style="margin-top: 10px; font-weight: bold;">Tasa de Éxito Operativa: <span class="val ok">{summary.get('rate', 0.0)}%</span></p>
    </div>

    <h3>Detalle de Registros de Productos</h3>
    <table>
        <thead>
            <tr>
                <th>N°</th>
                <th>N° de Parte</th>
                <th>Descripción / Marca</th>
                <th>Precio S/</th>
                <th>Stock</th>
                <th>Resultado de Auditoría</th>
            </tr>
        </thead>
        <tbody>
"""
        for i, r in enumerate(rows_data, 1):
            pn = str(r.get("parte", "") or r.get("nro_parte", "") or "")
            desc = str(r.get("descripcion", "") or r.get("marca", "") or "")
            precio = str(r.get("precio", "") or "")
            stock = str(r.get("stock", "") or "")
            st = str(r.get("estado", "") or "Pendiente")

            st_low = st.lower()
            if any(w in st_low for w in ("éxito", "exito", "ok", "✓", "correcto", "coincide")):
                tag_cls = "tag-ok"
            elif any(w in st_low for w in ("no hallado", "advertencia", "⚠️", "diferencia", "!=")):
                tag_cls = "tag-warn"
            elif any(w in st_low for w in ("error", "fallo", "✕", "x")):
                tag_cls = "tag-err"
            else:
                tag_cls = ""

            html_content += f"""
            <tr>
                <td>{i}</td>
                <td><strong>{pn}</strong></td>
                <td>{desc}</td>
                <td>{precio}</td>
                <td>{stock}</td>
                <td><span class="{tag_cls}">{st}</span></td>
            </tr>
"""

        html_content += """
        </tbody>
    </table>
</body>
</html>
"""
        pdf_html_path = output_path if output_path.endswith(".html") else output_path + ".html"
        with open(pdf_html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        return True, pdf_html_path
    except Exception as e:
        return False, str(e)

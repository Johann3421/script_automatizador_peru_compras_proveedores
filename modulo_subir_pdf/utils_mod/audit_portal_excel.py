# -*- coding: utf-8 -*-
"""
audit_portal_excel.py — Generador de informe Excel corporativo para la Auditoría de Stock.
"""
from __future__ import annotations
import os
from datetime import datetime
from utils_mod.excel_report_designer import build_executive_excel_report


def generar_excel_auditoria(filas: list, resumen: dict, ruta_salida: str) -> tuple[bool, str]:
    """
    Genera el informe Excel ejecutivo de auditoría de stock comparativa.
    """
    headers = [
        ("idx",           "N°",                    "center", 6),
        ("parte",         "N° de Parte",           "center", 18),
        ("ficha",         "Ficha Portal",          "center", 14),
        ("descripcion",   "Descripción del Producto", "left", 42),
        ("stock_excel",   "Stock Local",           "center", 13),
        ("stock_portal",  "Stock Portal",          "center", 13),
        ("estado_portal", "Estado Portal",         "center", 15),
        ("precio",        "Precio S/",             "right",  16),
        ("diferencia",    "Diferencia",            "center", 12),
        ("resultado",     "Resultado Auditoría",   "center", 20),
    ]

    return build_executive_excel_report(
        rows_data=filas,
        summary=resumen,
        output_path=ruta_salida,
        modulo_nombre="Auditoría de Stock — Perú Compras vs Excel",
        headers_config=headers
    )

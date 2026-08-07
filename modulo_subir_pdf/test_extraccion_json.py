"""
test_extraccion_json.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXTRACCIÓN MÁSTER DE JSON CRUDO DE PERÚ COMPRAS

Este script utiliza la Función Padre `extraer_json_catalogo` de `automation.perucompras_core`:
  1. Inicia navegador Playwright HD (1920x1080).
  2. Ejecuta inicio de sesión con OCR Tesseract ilimitado.
  3. Navega y evade bloqueos en MejoraBasica.
  4. Completa la selección en los combos del portal e inicia la búsqueda.
  5. Intercepta el dataset JSON crudo completo del endpoint `_ListaProductosOfertados`.
  6. Guarda el resultado en `output_audit/raw_mejora_basica.json` e imprime el resumen.

Uso:
  python test_extraccion_json.py
  python test_extraccion_json.py MI_CONTRASEÑA
  python test_extraccion_json.py MI_USUARIO MI_CONTRASEÑA
"""

import os
import sys
import json

# ── Añadir raíz del proyecto al path ─────────────────────────────
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from automation.perucompras_core import extraer_json_catalogo

# ── Configuración por defecto ──────────────────────────────────────
USUARIO  = os.environ.get("PC_USUARIO", "estalin.huamali01")
PASSWORD = os.environ.get("PC_PASSWORD", "")

if len(sys.argv) == 2:
    PASSWORD = sys.argv[1]
elif len(sys.argv) >= 3:
    USUARIO  = sys.argv[1]
    PASSWORD = sys.argv[2]

OUTPUT_DIR  = os.path.join(os.path.dirname(__file__), "output_audit")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "raw_mejora_basica.json")


def _imprimir_resumen(data):
    """Imprime un resumen legible del JSON extraído."""
    print("\n" + "="*60)
    print("  RESUMEN DEL JSON CRUDO EXTRAÍDO")
    print("="*60)

    registros = data if isinstance(data, list) else []
    print(f"  Total de fichas extraídas: {len(registros)}")
    if registros:
        print(f"  Muestra del primer registro:")
        primer = registros[0]
        if isinstance(primer, dict):
            for k, v in list(primer.items())[:10]:
                print(f"    {k}: {str(v)[:80]}")
    print("="*60 + "\n")


def ejecutar():
    if not PASSWORD:
        print("\n[AVISO] Setea la contraseña de alguna de estas formas:")
        print("  - python test_extraccion_json.py MI_CONTRASEÑA")
        print("  - python test_extraccion_json.py USUARIO MI_CONTRASEÑA")
        print("  - set PC_PASSWORD=MI_CLAVE  (Windows CMD)\n")
        return

    print(f"🚀 Ejecutando extracción JSON para usuario '{USUARIO}'...")
    data = extraer_json_catalogo(
        usuario=USUARIO,
        password=PASSWORD,
        n_acuerdo=249,
        n_catalogo=252,
        n_categoria=11736,
        acuerdo_texto="EXT-CE-2022-5 COMPUTADORAS Y ESCÁNERES",
        catalogo_texto="COMPUTADORAS DE ESCRITORIO",
        categoria_texto="COMPUTADORA TODO EN UNO",
        output_path=OUTPUT_FILE,
        log_func=print,
        headless=True
    )

    if data:
        _imprimir_resumen(data)
        print(f"✅ Extracción completada exitosamente. Archivo: {OUTPUT_FILE}")
    else:
        print("❌ No se pudieron extraer fichas del portal.")


if __name__ == "__main__":
    ejecutar()

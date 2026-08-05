"""
scripts/generate_code_audit.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Script determinístico de auditoría y documentación del código fuente.

Funciones principales:
  1. Escanea todos los archivos de código del proyecto (.py, .html, .js)
  2. Parsea con `ast` en Python para extraer clases, métodos, funciones y firmas.
  3. Mantiene `docs/audit/audit_progress.json` con el estado de avance.
  4. Genera `docs/audit/manifest.md` como checklist general del proyecto.
  5. Genera la documentación estructurada en `docs/audit/details/<path>.md`.
"""

import os
import sys
import ast
import json
from datetime import datetime

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Directorio raíz del proyecto
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs", "audit")
DETAILS_DIR = os.path.join(DOCS_DIR, "details")
PROGRESS_JSON = os.path.join(DOCS_DIR, "audit_progress.json")
MANIFEST_MD = os.path.join(DOCS_DIR, "manifest.md")

# Carpetas a ignorar (incluye binarios, entornos y carpetas pesadas)
EXCLUDE_DIRS = {
    "build", "dist", "installer", "__pycache__", ".git", ".agents",
    "node_modules", "venv", ".venv", "env", "brain", ".system_generated",
    "browsers", "tesseract", "venv_build", "installer_tmp", "build_installer",
    ".vscode", ".devcontainer", ".ponytail"
}

# Extensiones de archivo a auditar
AUDIT_EXTENSIONS = {".py", ".html", ".js"}


def scan_files():
    """Recorre el proyecto y devuelve una lista de dicts con info de cada archivo."""
    file_list = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Excluir directorios ignorados
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]

        for file in sorted(files):
            ext = os.path.splitext(file)[1].lower()
            if ext in AUDIT_EXTENSIONS:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, PROJECT_ROOT).replace("\\", "/")

                # Ignorar scripts auxiliares dentro de scripts/ si es el propio auditor
                if rel_path == "scripts/generate_code_audit.py":
                    continue

                try:
                    with open(abs_path, "r", encoding="utf-8", errors="replace") as f:
                        lines = f.readlines()
                    line_count = len(lines)
                except Exception:
                    line_count = 0

                file_list.append({
                    "rel_path": rel_path,
                    "abs_path": abs_path,
                    "ext": ext,
                    "lines": line_count,
                })

    return sorted(file_list, key=lambda x: x["rel_path"])


def parse_python_ast(filepath):
    """Extrae clases, funciones, firmas y docstrings usando `ast`."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            code = f.read()
        tree = ast.parse(code, filename=filepath)
    except Exception as e:
        return {"error": str(e), "classes": [], "functions": []}

    classes = []
    functions = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            c_methods = []
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    args_list = [arg.arg for arg in item.args.args]
                    c_methods.append({
                        "name": item.name,
                        "line": item.lineno,
                        "args": args_list,
                        "doc": ast.get_docstring(item) or "Sin docstring.",
                    })
            classes.append({
                "name": node.name,
                "line": node.lineno,
                "doc": ast.get_docstring(node) or "Sin docstring.",
                "methods": c_methods,
            })
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args_list = [arg.arg for arg in node.args.args]
            functions.append({
                "name": node.name,
                "line": node.lineno,
                "args": args_list,
                "doc": ast.get_docstring(node) or "Sin docstring.",
            })

    return {"classes": classes, "functions": functions}


def load_progress():
    """Carga audit_progress.json si existe."""
    if os.path.exists(PROGRESS_JSON):
        try:
            with open(PROGRESS_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "files": {}}


def save_progress(progress):
    """Guarda audit_progress.json."""
    os.makedirs(DOCS_DIR, exist_ok=True)
    progress["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(PROGRESS_JSON, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)


def generate_manifest(files, progress):
    """Genera docs/audit/manifest.md."""
    os.makedirs(DOCS_DIR, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_files = len(files)
    completed_count = sum(
        1 for f in files if progress.get("files", {}).get(f["rel_path"], {}).get("status") == "COMPLETADO"
    )
    percent = round((completed_count / total_files * 100) if total_files > 0 else 0, 1)

    lines = [
        "# MANIFEST DE AUDITORÍA Y DOCUMENTACIÓN DEL PROYECTO",
        "",
        f"**Proyecto:** Peru Compras Bot",
        f"**Última actualización:** {now}",
        f"**Progreso total:** {completed_count}/{total_files} archivos auditados ({percent}%)",
        "",
        "## Resumen de Avance",
        "",
        f"- 🟢 **Auditados / Documentados:** {completed_count}",
        f"- 🟡 **Pendientes:** {total_files - completed_count}",
        f"- 📊 **Líneas totales de código:** {sum(f['lines'] for f in files):,}",
        "",
        "## Listado de Archivos y Cola de Trabajo",
        "",
        "| Estado | Archivo | Líneas | Extensión | Detalle Doc |",
        "|:---:|:---|:---:|:---:|:---|",
    ]

    for f in files:
        rel = f["rel_path"]
        f_info = progress.get("files", {}).get(rel, {})
        status = f_info.get("status", "PENDIENTE")
        icon = "✅" if status == "COMPLETADO" else "⏳"
        doc_rel = f"details/{rel}.md"

        lines.append(
            f"| {icon} {status} | `{rel}` | {f['lines']} | `{f['ext']}` | [{rel}.md]({doc_rel}) |"
        )

    lines.extend([
        "",
        "---",
        "## Reglas de Modificación para IAs y Desarrolladores",
        "",
        "### 🔴 NO TOCAR (Core & Backend de Automatización):",
        "- `modulo_subir_pdf/workers.py` (Lógica de ejecución `execute_stock`, `execute_auditor`)",
        "- `modulo_subir_pdf/automation_otro_bot/stock.py` (Navegación en portal, formularios `paso2`, `paso3`, `paso4`)",
        "- `automation/login.py` (Resolución de CAPTCHA OCR y login)",
        "- `automation/browser.py` (Inicialización de Playwright Chromium)",
        "",
        "### 🟢 MODIFICABLE (Frontend & Reportes Visuales):",
        "- `ui_web/index.html` (Interfaz de usuario HTML/CSS/JS PyWebView)",
        "- `modulo_subir_pdf/utils_mod/audit_portal_excel.py` (Generador de reporte Excel de auditoría)",
        "- Estilos CSS, textos de etiquetas y diálogos de guardado.",
    ])

    with open(MANIFEST_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def generate_detail_doc(f_info):
    """Genera la estructura de documentación detallada para un archivo."""
    rel = f_info["rel_path"]
    abs_p = f_info["abs_path"]
    ext = f_info["ext"]

    detail_path = os.path.join(DETAILS_DIR, f"{rel}.md")
    os.makedirs(os.path.dirname(detail_path), exist_ok=True)

    lines = [
        f"# Documentación Técnica: `{rel}`",
        "",
        f"- **Ruta relativa:** `{rel}`",
        f"- **Tipo de archivo:** `{ext}`",
        f"- **Líneas de código:** {f_info['lines']}",
        f"- **Fecha de inspección:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
        "## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)",
        "",
    ]

    # Reglas específicas por carpeta/archivo
    if "workers.py" in rel or "automation" in rel or "login.py" in rel or "stock.py" in rel:
        lines.extend([
            "> [!CAUTION]",
            "> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**",
            "> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.",
            "> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.",
            "",
        ])
    else:
        lines.extend([
            "> [!NOTE]",
            "> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**",
            "> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.",
            "> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.",
            "",
        ])

    lines.append("## 📋 Estructura Interna del Archivo\n")

    if ext == ".py":
        ast_data = parse_python_ast(abs_p)
        if "error" in ast_data:
            lines.append(f"⚠️ Error parsing AST: {ast_data['error']}")
        else:
            if ast_data["classes"]:
                lines.append("### Clases definidas:\n")
                for c in ast_data["classes"]:
                    lines.append(f"#### Clase `{c['name']}` (Línea {c['line']})")
                    lines.append(f"- **Docstring:** _{c['doc']}_")
                    if c["methods"]:
                        lines.append("- **Métodos:**")
                        for m in c["methods"]:
                            args_str = ", ".join(m["args"])
                            lines.append(f"  - `def {m['name']}({args_str})` (Línea {m['line']}): {m['doc']}")
                    lines.append("")

            if ast_data["functions"]:
                lines.append("### Funciones independientes:\n")
                for fn in ast_data["functions"]:
                    args_str = ", ".join(fn["args"])
                    lines.append(f"#### `def {fn['name']}({args_str})` (Línea {fn['line']})")
                    lines.append(f"- **Propósito:** {fn['doc']}")
                    lines.append(f"- **Firma:** `def {fn['name']}({args_str})`")
                    lines.append(f"- **Retorno / Efectos:** Consulta código fuente.")
                    lines.append("")

    elif ext == ".html":
        lines.extend([
            "### Secciones principales del HTML:",
            "- **Vistas Pane:** `#view-pdf`, `#view-stock`, `#view-json`, `#view-guide`, `#view-tools`",
            "- **Puente PyWebView:** Invocaciones mediante `pyapi(cmd, params)`",
            "- **Formularios:** Credenciales, Filtros de catálogo, checkboxes de visibilidad",
            "",
        ])

    with open(detail_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    print("🔍 Iniciando escaneo determinístico del repositorio...")
    files = scan_files()
    print(f"📊 Se encontraron {len(files)} archivos de código fuente.")

    progress = load_progress()

    # Si se pasa --mark <rel_path> o --mark-all
    if len(sys.argv) > 1 and sys.argv[1] == "--mark":
        target = sys.argv[2] if len(sys.argv) > 2 else ""
        if target == "all":
            for f in files:
                progress["files"][f["rel_path"]]["status"] = "COMPLETADO"
                progress["files"][f["rel_path"]]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("✅ Todos los archivos marcados como COMPLETADOS.")
        elif target in progress.get("files", {}):
            progress["files"][target]["status"] = "COMPLETADO"
            progress["files"][target]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"✅ Archivo '{target}' marcado como COMPLETADO.")

    # Sincronizar archivos en audit_progress.json
    for f in files:
        rel = f["rel_path"]
        if rel not in progress["files"]:
            progress["files"][rel] = {
                "status": "PENDIENTE",
                "lines": f["lines"],
                "ext": f["ext"],
                "last_updated": None
            }
        else:
            progress["files"][rel]["lines"] = f["lines"]

        # Generar o refrescar doc de detalle
        generate_detail_doc(f)

    save_progress(progress)
    generate_manifest(files, progress)

    print("✅ Manifest y archivos de documentación estructurada generados exitosamente.")
    print(f"📁 Manifest: {MANIFEST_MD}")
    print(f"📁 Detalles: {DETAILS_DIR}")


if __name__ == "__main__":
    main()

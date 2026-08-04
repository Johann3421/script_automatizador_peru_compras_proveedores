import customtkinter as ctk
import threading
from tkinter import filedialog
import os
import json

def build_precios_json_tab(app, parent):
    """Vista de Precios JSON — paleta institucional light."""
    C = getattr(app, "_C", {
        "bg": "#F4F7FA", "card": "#FFFFFF", "card2": "#F0F4F8",
        "border": "#C8D6E5", "border2": "#DDE4ED",
        "txt": "#1A2332", "txt2": "#4A6080", "txt3": "#7A90A8",
        "accent": "#0D6EAA", "accent_h": "#0A5888",
        "success": "#1E6E3A", "danger": "#B91C1C", "sep": "#E2EAF3",
    })

    app._precios_json_path = ""
    app._precios_json_data = []

    parent.grid_columnconfigure(0, weight=1, minsize=360)
    parent.grid_columnconfigure(1, weight=1, minsize=360)
    parent.grid_rowconfigure(0, weight=1)

    def _card(parent_frame, title, row):
        lbl = ctk.CTkLabel(parent_frame, text=title,
                           font=ctk.CTkFont(size=12, weight="bold"),
                           text_color=C["txt"], anchor="w")
        lbl.grid(row=row, column=0, padx=0, pady=(12, 4), sticky="w")
        card = ctk.CTkFrame(parent_frame, fg_color=C["card"], corner_radius=6,
                            border_width=1, border_color=C["border"])
        card.grid(row=row+1, column=0, padx=0, pady=(0, 10), sticky="ew")
        card.grid_columnconfigure(0, weight=1)
        return card

    _entry_style = dict(height=32, fg_color=C["card2"],
                        border_color=C["border"], text_color=C["txt"])
    _cb_style = dict(
        fg_color=C["card2"], button_color=C["border"],
        button_hover_color=C["border2"], text_color=C["txt"],
        dropdown_fg_color=C["card"], dropdown_hover_color=C["card2"],
        dropdown_text_color=C["txt"],
    )

    # LEFT COLUMN
    left = ctk.CTkScrollableFrame(parent, fg_color="transparent",
                                  scrollbar_button_color=C["border"])
    left.grid(row=0, column=0, padx=(12, 6), pady=12, sticky="nsew")
    left.grid_columnconfigure(0, weight=1)

    # ── 1. Credenciales ──
    c_creds = _card(left, "Credenciales", 0)
    c_creds.grid_columnconfigure(0, weight=1)
    for ri, (lbl_txt, attr, show) in enumerate([
        ("Usuario",    "entry_precios_user", ""),
        ("Contraseña", "entry_precios_pass", "*"),
    ]):
        ctk.CTkLabel(c_creds, text=lbl_txt, font=ctk.CTkFont(size=11),
                     text_color=C["txt2"], anchor="w"
                     ).grid(row=ri*2, column=0, padx=12,
                            pady=(10 if ri==0 else 4, 1), sticky="w")
        e = ctk.CTkEntry(c_creds, show=show, **_entry_style)
        e.grid(row=ri*2+1, column=0, padx=12,
               pady=(0, 8 if ri==1 else 4), sticky="ew")
        setattr(app, attr, e)

    # ── 2. Archivo JSON ──
    c_json = _card(left, "Archivo JSON de Precios", 2)

    lbl_file = ctk.CTkLabel(c_json, text="Sin archivo", text_color=C["txt3"],
                             font=ctk.CTkFont(size=11), anchor="w")
    lbl_file.grid(row=0, column=0, padx=12, pady=(10, 4), sticky="ew")

    ctk.CTkButton(
        c_json, text="Seleccionar .json", height=32, corner_radius=4,
        font=ctk.CTkFont(size=12),
        fg_color=C["accent"], hover_color=C["accent_h"], text_color="#FFFFFF",
        command=lambda: _pick_json(app, lbl_file),
    ).grid(row=1, column=0, padx=12, pady=(0, 10), sticky="w")

    # ── 3. Filtros Dinámicos ──
    c_menu = _card(left, "Filtros del Portal (t_ProductoOfertadoAmp)", 4)
    c_menu.grid_columnconfigure(0, weight=1)

    ctk.CTkButton(
        c_menu, text="Extraer Menu Dinamico", height=32, corner_radius=4,
        font=ctk.CTkFont(size=12),
        fg_color=C["card2"], hover_color=C["border"],
        text_color=C["txt"], border_width=1, border_color=C["border"],
        command=lambda: _on_extraer_menu(app),
    ).grid(row=0, column=0, columnspan=2, padx=12, pady=(10, 8), sticky="ew")

    for ri, (lbl_txt, attr, cmd) in enumerate([
        ("Acuerdo",   "option_precio_acuerdo",   lambda v: _on_precio_acuerdo_changed(app, v)),
        ("Catalogo",  "option_precio_catalogo",  lambda v: _on_precio_catalogo_changed(app, v)),
        ("Categoria", "option_precio_categoria", None),
    ]):
        ctk.CTkLabel(c_menu, text=lbl_txt, font=ctk.CTkFont(size=11),
                     text_color=C["txt2"], anchor="w"
                     ).grid(row=ri*2+1, column=0, padx=12,
                            pady=(4 if ri>0 else 0, 1), sticky="w")
        kw = dict(**_cb_style, values=["-- Extraer menu primero --"], width=300)
        if cmd:
            kw["command"] = cmd
        om = ctk.CTkOptionMenu(c_menu, **kw)
        om.grid(row=ri*2+2, column=0, padx=12,
                pady=(0, 4 if ri<2 else 10), sticky="ew")
        setattr(app, attr, om)

    app.check_precios_visible = ctk.CTkCheckBox(
        c_menu, text="Mostrar navegador en pantalla",
        font=ctk.CTkFont(size=12), text_color=C["txt"],
        border_color=C["border"], fg_color=C["accent"],
    )
    app.check_precios_visible.grid(row=7, column=0, padx=12, pady=(2, 12), sticky="w")

    # RIGHT COLUMN
    right = ctk.CTkFrame(parent, fg_color=C["card"], corner_radius=8,
                         border_width=1, border_color=C["border"])
    right.grid(row=0, column=1, padx=(6, 12), pady=12, sticky="nsew")
    right.grid_columnconfigure(0, weight=1)
    right.grid_rowconfigure(2, weight=1)

    ctk.CTkLabel(
        right, text="Panel de Ejecucion",
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color=C["txt"], anchor="w",
    ).grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")

    status_row = ctk.CTkFrame(right, fg_color=C["card2"], corner_radius=6,
                              border_width=1, border_color=C["border"])
    status_row.grid(row=1, column=0, padx=12, pady=(0, 8), sticky="ew")
    app.lbl_precios_status = ctk.CTkLabel(
        status_row, text="Listo para extraer o iniciar",
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color=C["txt"],
    )
    app.lbl_precios_status.pack(side="left", padx=12, pady=8)

    app.log_box_precios = ctk.CTkTextbox(
        right, wrap="word", font=ctk.CTkFont(family="Courier New", size=11),
        fg_color=C["card"], border_width=1, border_color=C["border"],
        text_color=C["txt"],
    )
    app.log_box_precios.grid(row=2, column=0, padx=12, pady=(0, 8), sticky="nsew")
    app.log_box_precios.configure(state="disabled")

    # Botones de acción
    app.btn_test_precios = ctk.CTkButton(
        right, text="Prueba (1 producto)", height=34,
        font=ctk.CTkFont(size=12, weight="bold"), corner_radius=6,
        fg_color=C["card2"], hover_color=C["border"],
        text_color=C["txt"], border_width=1, border_color=C["border"],
        command=lambda: _on_test_precios(app),
    )
    app.btn_test_precios.grid(row=3, column=0, padx=12, pady=(0, 6), sticky="ew")

    app.btn_iniciar_precios = ctk.CTkButton(
        right, text="Iniciar Subida de Precios", height=36,
        font=ctk.CTkFont(size=13, weight="bold"), corner_radius=6,
        fg_color=C["accent"], hover_color=C["accent_h"], text_color="#FFFFFF",
        command=lambda: _on_iniciar_precios(app),
    )
    app.btn_iniciar_precios.grid(row=4, column=0, padx=12, pady=(0, 6), sticky="ew")

    # Auditor de Precios JSON
    audit_card = _card(right, "🔍 Auditor de Resultados — Precios JSON", 5)
    audit_body = ctk.CTkFrame(audit_card, fg_color="transparent")
    audit_body.pack(fill="x", padx=10, pady=8)

    app.lbl_audit_precios_summary = ctk.CTkLabel(
        audit_body, text="Cargue o ejecute precios para auditar...",
        font=ctk.CTkFont(size=11), text_color=C["txt2"], anchor="w"
    )
    app.lbl_audit_precios_summary.pack(fill="x", pady=(0, 6))

    btn_row_p = ctk.CTkFrame(audit_body, fg_color="transparent")
    btn_row_p.pack(fill="x")

    ctk.CTkButton(
        btn_row_p, text="📊 Informe Excel", height=32,
        font=ctk.CTkFont(size=11, weight="bold"),
        fg_color="#1B6B1B", hover_color="#145214", text_color="#FFFFFF",
        command=lambda: _export_precios_audit_report(app, fmt="excel")
    ).pack(side="left", padx=(0, 4), fill="x", expand=True)

    ctk.CTkButton(
        btn_row_p, text="📄 Informe PDF", height=32,
        font=ctk.CTkFont(size=11, weight="bold"),
        fg_color="#006CA8", hover_color="#00507E", text_color="#FFFFFF",
        command=lambda: _export_precios_audit_report(app, fmt="pdf")
    ).pack(side="left", fill="x", expand=True)

    _load_and_populate_catalog_menu(app)


def _export_precios_audit_report(app, fmt="excel"):
    from utils_mod.audit_reporter import audit_results, export_excel_report, export_pdf_report
    from tkinter import filedialog, messagebox
    from datetime import datetime

    rows = getattr(app, "_precios_json_data", []) or []
    summary = audit_results(rows)
    if not rows:
        messagebox.showwarning("Auditor Precios JSON", "No hay datos de precios cargados en el archivo JSON para auditar.")
        return

    def_ext = ".xlsx" if fmt == "excel" else ".html"
    ftypes = [("Libro de Excel", "*.xlsx")] if fmt == "excel" else [("Informe de Auditoría PDF/HTML", "*.html")]
    path = filedialog.asksaveasfilename(
        title=f"Guardar Informe de Auditoría Precios JSON ({fmt.upper()})",
        initialfile=f"Informe_Auditoria_Precios_JSON_{datetime.now().strftime('%Y%m%d_%H%M%S')}{def_ext}",
        defaultextension=def_ext,
        filetypes=ftypes
    )
    if not path:
        return

    if fmt == "excel":
        ok, msg = export_excel_report(rows, summary, path, modulo_nombre="Subida de Precios JSON")
    else:
        ok, msg = export_pdf_report(rows, summary, path, modulo_nombre="Subida de Precios JSON")

    if ok:
        messagebox.showinfo("Auditor Precios JSON", f"¡Informe de Auditoría de Precios generado exitosamente!\n\nUbicación:\n{msg}")
    else:
        messagebox.showerror("Error en Auditoría", f"Ocurrió un error al generar el informe:\n{msg}")


def _load_and_populate_catalog_menu(app):
    """Carga y puebla automáticamente los dropdowns dinámicos desde cualquier JSON disponible."""
    import utils_mod.config_helper as ch
    base_dir = os.path.dirname(__file__)
    root_dir = os.path.dirname(base_dir)
    
    candidates = [
        ch.get_writable_path("dropdowns_precios.json", base_dir),
        os.path.join(base_dir, "dropdowns_precios.json"),
        os.path.join(root_dir, "dropdowns_precios.json"),
        os.path.join(base_dir, "combinaciones_computadoras.json"),
        os.path.join(root_dir, "combinaciones_computadoras.json"),
        os.path.join(base_dir, "catalog_options.json"),
        os.path.join(root_dir, "catalog_options.json"),
    ]
    
    combinaciones = []
    
    for path in candidates:
        if os.path.isfile(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    raw = json.load(f)
                
                # Formato 1: dropdowns_precios.json (lista de objetos con acuerdo, catalogo, categorias)
                if isinstance(raw, list) and len(raw) > 0 and "acuerdo" in raw[0]:
                    combinaciones = raw
                    break
                
                # Formato 2: combinaciones_computadoras.json (objeto con acuerdo y combinaciones)
                if isinstance(raw, dict) and "acuerdo" in raw and "combinaciones" in raw:
                    acuerdo_obj = raw["acuerdo"]
                    for cat_item in raw["combinaciones"]:
                        cats_arr = []
                        for sub in cat_item.get("children", []):
                            cats_arr.append({"value": str(sub.get("value", "")), "text": str(sub.get("text", ""))})
                        combinaciones.append({
                            "acuerdo": acuerdo_obj,
                            "catalogo": {"value": str(cat_item.get("value", "")), "text": str(cat_item.get("text", ""))},
                            "categorias": cats_arr
                        })
                    if combinaciones:
                        break

                # Formato 3: catalog_options.json (acuerdos, catalogos, categorias)
                if isinstance(raw, dict) and "acuerdos" in raw:
                    for ac in raw.get("acuerdos", []):
                        ac_id = str(ac.get("value"))
                        cats_for_ac = raw.get("catalogos", {}).get(ac_id, [])
                        for cat in cats_for_ac:
                            cat_id = str(cat.get("value"))
                            subcats = raw.get("categorias", {}).get(cat_id, [])
                            combinaciones.append({
                                "acuerdo": ac,
                                "catalogo": cat,
                                "categorias": subcats
                            })
                    if combinaciones:
                        break
            except Exception:
                continue

    if combinaciones:
        app._precios_combinaciones = combinaciones
        acuerdos_str = [f"{c['acuerdo']['value']} - {c['acuerdo']['text']}" for c in combinaciones if "acuerdo" in c]
        acuerdos_str = list(dict.fromkeys(acuerdos_str))
        if acuerdos_str:
            app.option_precio_acuerdo.configure(values=acuerdos_str)
            app.option_precio_acuerdo.set(acuerdos_str[0])
            try:
                _on_precio_acuerdo_changed(app, acuerdos_str[0])
            except Exception:
                pass
            if hasattr(app, "btn_iniciar_precios"):
                app.btn_iniciar_precios.configure(state="normal")
            return True
    return False


def _pick_json(app, lbl_file):
    path = filedialog.askopenfilename(
        title="Seleccionar archivo JSON",
        filetypes=[("JSON", "*.json"), ("Todos", "*.*")],
    )
    if not path:
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        app._precios_json_path = path
        app._precios_json_data = data
        name = os.path.basename(path)
        lbl_file.configure(text=f"{name} ({len(data)} registros)", text_color="#2ecc71")
    except Exception as e:
        lbl_file.configure(text=f"Error: {e}", text_color="#e74c3c")

def _log_precios(app, msg):
    app.log_box_precios.configure(state="normal")
    app.log_box_precios.insert("end", str(msg) + "\n")
    app.log_box_precios.see("end")
    app.log_box_precios.configure(state="disabled")

def _on_precio_acuerdo_changed(app, selected_val):
    if not hasattr(app, "_precios_combinaciones"): return
    cat_list = []
    for c in app._precios_combinaciones:
        if f"{c['acuerdo']['value']} - {c['acuerdo']['text']}" == selected_val:
            cat_str = f"{c['catalogo']['value']} - {c['catalogo']['text']}"
            if cat_str not in cat_list:
                cat_list.append(cat_str)
                
    if cat_list:
        app.option_precio_catalogo.configure(values=cat_list)
        app.option_precio_catalogo.set(cat_list[0])
        _on_precio_catalogo_changed(app, cat_list[0])
    else:
        app.option_precio_catalogo.configure(values=["-- Sin datos --"])
        app.option_precio_catalogo.set("-- Sin datos --")

def _on_precio_catalogo_changed(app, selected_val):
    if not hasattr(app, "_precios_combinaciones"): return
    cg_list = []
    for c in app._precios_combinaciones:
        cat_str = f"{c['catalogo']['value']} - {c['catalogo']['text']}"
        if cat_str == selected_val:
            for catg in c["categorias"]:
                cg_str = f"{catg['value']} - {catg['text']}"
                if cg_str not in cg_list:
                    cg_list.append(cg_str)
                    
    if cg_list:
        app.option_precio_categoria.configure(values=cg_list)
        app.option_precio_categoria.set(cg_list[0])
    else:
        app.option_precio_categoria.configure(values=["-- Sin datos --"])
        app.option_precio_categoria.set("-- Sin datos --")


def _on_extraer_menu(app):
    user = app.entry_precios_user.get().strip()
    pwd = app.entry_precios_pass.get().strip()
    if not user or not pwd:
        _log_precios(app, "❌ Ingresa usuario y contraseña.")
        return

    headless = not bool(app.check_precios_visible.get())
    
    _log_precios(app, "🔄 Iniciando extracción de menú dinámico...")
    app.btn_iniciar_precios.configure(state="disabled")

    import workers
    threading.Thread(
        target=workers.execute_extraer_menu_precios,
        args=(app, user, pwd, headless, _log_precios),
        daemon=True
    ).start()

def _on_test_precios(app):
    user = app.entry_precios_user.get().strip()
    pwd = app.entry_precios_pass.get().strip()
    if not user or not pwd:
        _log_precios(app, "❌ Ingresa usuario y contraseña.")
        return
    if not app._precios_json_data:
        _log_precios(app, "❌ Carga primero el archivo JSON de precios.")
        return

    headless = not bool(app.check_precios_visible.get())
    acuerdo_str = app.option_precio_acuerdo.get()
    catalogo_str = app.option_precio_catalogo.get()
    categoria_str = app.option_precio_categoria.get()

    # Extraer solo el value (antes del primer ' - ')
    acuerdo_val = acuerdo_str.split(" - ")[0].strip()
    catalogo_val = catalogo_str.split(" - ")[0].strip()
    categoria_val = categoria_str.split(" - ")[0].strip()

    _log_precios(app, "🧪 Iniciando TEST (1 producto)...")
    _log_precios(app, f"   Acuerdo: {acuerdo_str}")
    _log_precios(app, f"   Catálogo: {catalogo_str}")
    _log_precios(app, f"   Categoría: {categoria_str}")

    app.btn_test_precios.configure(state="disabled")
    app.btn_iniciar_precios.configure(state="disabled")

    import workers
    threading.Thread(
        target=workers.execute_test_precios,
        args=(app, user, pwd, headless, _log_precios,
              app._precios_json_data, acuerdo_val, catalogo_val, categoria_val),
        daemon=True
    ).start()

def _on_iniciar_precios(app):
    user = app.entry_precios_user.get().strip()
    pwd = app.entry_precios_pass.get().strip()
    if not user or not pwd:
        _log_precios(app, "❌ Ingresa usuario y contraseña.")
        return
    if not app._precios_json_data:
        _log_precios(app, "❌ Carga primero el archivo JSON de precios.")
        return

    headless = not bool(app.check_precios_visible.get())
    acuerdo_str = app.option_precio_acuerdo.get()
    catalogo_str = app.option_precio_catalogo.get()
    categoria_str = app.option_precio_categoria.get()

    acuerdo_val = acuerdo_str.split(" - ")[0].strip()
    catalogo_val = catalogo_str.split(" - ")[0].strip()
    categoria_val = categoria_str.split(" - ")[0].strip()

    _log_precios(app, "🚀 Iniciando subida de precios real...")
    _log_precios(app, f"   Acuerdo: {acuerdo_str}")
    _log_precios(app, f"   Catálogo: {catalogo_str}")
    _log_precios(app, f"   Categoría: {categoria_str}")

    app.btn_test_precios.configure(state="disabled")
    app.btn_iniciar_precios.configure(state="disabled")

    import workers
    threading.Thread(
        target=workers.execute_iniciar_precios,
        args=(app, user, pwd, headless, _log_precios,
              app._precios_json_data, acuerdo_val, catalogo_val, categoria_val),
        daemon=True
    ).start()


import customtkinter as ctk
import threading
from tkinter import filedialog
import os
import json

def build_precios_json_tab(app, parent):
    """
    Construye la UI para la nueva pestaña de Subir Precios JSON.
    """
    app._precios_json_path = ""
    app._precios_json_data = []

    # LEFT COLUMN
    left = ctk.CTkScrollableFrame(parent, fg_color="transparent")
    left.grid(row=0, column=0, padx=(0, 6), sticky="nsew")
    left.grid_columnconfigure(0, weight=1)

    # Título
    ctk.CTkLabel(
        left, text="💰 Subir Precios JSON",
        font=ctk.CTkFont(size=18, weight="bold"),
    ).grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")
    ctk.CTkLabel(
        left, text="Automatiza la subida de precios desde un archivo JSON",
        font=ctk.CTkFont(size=11), text_color="gray60",
    ).grid(row=1, column=0, padx=12, pady=(0, 8), sticky="w")

    # 1. Credenciales
    frame_creds = ctk.CTkFrame(left, fg_color="gray10")
    frame_creds.grid(row=2, column=0, padx=12, pady=(4, 12), sticky="ew")
    frame_creds.grid_columnconfigure(1, weight=1)

    ctk.CTkLabel(
        frame_creds, text="Credenciales", font=ctk.CTkFont(size=14, weight="bold")
    ).grid(row=0, column=0, columnspan=2, padx=10, pady=(8, 4), sticky="w")

    ctk.CTkLabel(frame_creds, text="Usuario:").grid(row=1, column=0, padx=10, pady=4, sticky="w")
    app.entry_precios_user = ctk.CTkEntry(frame_creds, width=200)
    app.entry_precios_user.grid(row=1, column=1, padx=10, pady=4, sticky="ew")

    ctk.CTkLabel(frame_creds, text="Contraseña:").grid(row=2, column=0, padx=10, pady=4, sticky="w")
    app.entry_precios_pass = ctk.CTkEntry(frame_creds, width=200, show="*")
    app.entry_precios_pass.grid(row=2, column=1, padx=10, pady=4, sticky="ew")

    # 2. Selección de JSON
    frame_json = ctk.CTkFrame(left, fg_color="gray10")
    frame_json.grid(row=3, column=0, padx=12, pady=(0, 10), sticky="ew")
    frame_json.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(
        frame_json, text="Archivo JSON de Precios",
        font=ctk.CTkFont(size=14, weight="bold"), anchor="w",
    ).grid(row=0, column=0, padx=10, pady=(8, 4), sticky="w")

    btn_file = ctk.CTkButton(
        frame_json, text="Seleccionar archivo .json",
        height=32, font=ctk.CTkFont(size=12),
        command=lambda: _pick_json(app, lbl_file),
    )
    btn_file.grid(row=1, column=0, padx=10, pady=4, sticky="w")
    
    lbl_file = ctk.CTkLabel(frame_json, text="Sin archivo", text_color="gray60", font=ctk.CTkFont(size=11))
    lbl_file.grid(row=2, column=0, padx=10, pady=(0, 8), sticky="w")

    # 3. Menú Dinámico
    frame_menu = ctk.CTkFrame(left, fg_color="gray10")
    frame_menu.grid(row=4, column=0, padx=12, pady=(0, 10), sticky="ew")
    frame_menu.grid_columnconfigure(1, weight=1)

    ctk.CTkLabel(
        frame_menu, text="Filtros Dinámicos (t_ProductoOfertadoAmp)",
        font=ctk.CTkFont(size=14, weight="bold"), anchor="w",
    ).grid(row=0, column=0, columnspan=2, padx=10, pady=(8, 4), sticky="w")

    # Botón para extraer el menú
    btn_extraer = ctk.CTkButton(
        frame_menu, text="🔄 Extraer Menú Dinámico",
        height=32, font=ctk.CTkFont(size=12),
        fg_color="#8e44ad", hover_color="#732d91",
        command=lambda: _on_extraer_menu(app)
    )
    btn_extraer.grid(row=1, column=0, columnspan=2, padx=10, pady=(4, 12), sticky="ew")

    # Dropdowns
    app.option_precio_acuerdo = ctk.CTkOptionMenu(frame_menu, values=["-- Extraer menú primero --"], width=300, command=lambda v: _on_precio_acuerdo_changed(app, v))
    app.option_precio_catalogo = ctk.CTkOptionMenu(frame_menu, values=["-- Extraer menú primero --"], width=300, command=lambda v: _on_precio_catalogo_changed(app, v))
    app.option_precio_categoria = ctk.CTkOptionMenu(frame_menu, values=["-- Extraer menú primero --"], width=300)

    ctk.CTkLabel(frame_menu, text="Acuerdo:").grid(row=2, column=0, padx=10, pady=4, sticky="w")
    app.option_precio_acuerdo.grid(row=2, column=1, padx=10, pady=4, sticky="ew")

    ctk.CTkLabel(frame_menu, text="Catálogo:").grid(row=3, column=0, padx=10, pady=4, sticky="w")
    app.option_precio_catalogo.grid(row=3, column=1, padx=10, pady=4, sticky="ew")

    ctk.CTkLabel(frame_menu, text="Categoría:").grid(row=4, column=0, padx=10, pady=4, sticky="w")
    app.option_precio_categoria.grid(row=4, column=1, padx=10, pady=4, sticky="ew")

    app.check_precios_visible = ctk.CTkCheckBox(frame_menu, text="👁 Ver navegador (mostrar ventana)")
    app.check_precios_visible.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 10), sticky="w")


    # RIGHT COLUMN (Ejecución y Logs)
    right = ctk.CTkFrame(parent)
    right.grid(row=0, column=1, padx=(6, 0), sticky="nsew")
    right.grid_columnconfigure(0, weight=1)
    right.grid_rowconfigure(2, weight=1)

    ctk.CTkLabel(
        right, text="Estado de Ejecución",
        font=ctk.CTkFont(size=14, weight="bold"), anchor="w",
    ).grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")

    status_row = ctk.CTkFrame(right, fg_color="transparent")
    status_row.grid(row=1, column=0, padx=12, pady=4, sticky="ew")
    app.lbl_precios_status = ctk.CTkLabel(status_row, text="Listo para extraer o iniciar", font=ctk.CTkFont(size=13, weight="bold"))
    app.lbl_precios_status.pack(side="left")

    app.log_box_precios = ctk.CTkTextbox(right, wrap="word", font=ctk.CTkFont(family="Courier New", size=11))
    app.log_box_precios.grid(row=2, column=0, padx=12, pady=(4, 12), sticky="nsew")
    app.log_box_precios.configure(state="disabled")

    # Botón Iniciar Proceso (en la parte inferior)
    app.btn_iniciar_precios = ctk.CTkButton(
        right, text="▶ Iniciar Subida de Precios", height=40,
        font=ctk.CTkFont(size=14, weight="bold"),
        fg_color="#27ae60", hover_color="#219150",
        command=lambda: _on_iniciar_precios(app)
    )
    app.btn_iniciar_precios.grid(row=4, column=0, padx=12, pady=(0, 12), sticky="ew")

    # Botón TEST (1 producto)
    app.btn_test_precios = ctk.CTkButton(
        right, text="🧪 TEST (1 producto)", height=36,
        font=ctk.CTkFont(size=13, weight="bold"),
        fg_color="#2c3e50", hover_color="#34495e",
        command=lambda: _on_test_precios(app)
    )
    app.btn_test_precios.grid(row=3, column=0, padx=12, pady=(4, 4), sticky="ew")

    # Intentar cargar el menú extraído previamente
    import utils_mod.config_helper as ch
    json_path = ch.get_writable_path("dropdowns_precios.json", os.path.dirname(__file__))
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                combinaciones = json.load(f)
            app._precios_combinaciones = combinaciones
            acuerdos_str = [f"{c['acuerdo']['value']} - {c['acuerdo']['text']}" for c in combinaciones]
            acuerdos_str = list(dict.fromkeys(acuerdos_str))
            if acuerdos_str:
                app.option_precio_acuerdo.configure(values=acuerdos_str)
                app.option_precio_acuerdo.set(acuerdos_str[0])
                try:
                    _on_precio_acuerdo_changed(app, acuerdos_str[0])
                except Exception:
                    pass
                app.btn_iniciar_precios.configure(state="normal")
        except Exception:
            pass


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


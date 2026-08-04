"""
Prototipo Interactivo de Alta Fidelidad — Perú Compras Bot Enterprise v1.3
Reestructuración Total desde 0 (Estilo ERP Desktop / Power Automate Desktop)
Aplicando Ley de Tesler y parámetros de AGENTS.md
"""
import sys
import os
import json
import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import customtkinter as ctk

VERSION = "1.3 (PROTOTIPO DESKTOP ERP)"

# ── PALETA INSTITUCIONAL NEUTRA (Estilo SAP / Dynamics / Power Automate) ──
_C = {
    "bg": "#F1F5F9",             # Slate 100
    "header_bg": "#0F172A",      # Slate 900
    "header_txt": "#F8FAFC",
    "toolbar_bg": "#1E293B",     # Slate 800
    "card": "#FFFFFF",           # Blanco puro
    "card_header": "#F8FAFC",    # Slate 50
    "border": "#CBD5E1",         # Slate 300
    "border_dark": "#94A3B8",    # Slate 400
    "txt_primary": "#0F172A",    # Slate 900
    "txt_secondary": "#475569",  # Slate 600
    "txt_muted": "#64748B",      # Slate 500
    "accent": "#2563EB",         # Royal Blue
    "accent_hover": "#1D4ED8",
    "success": "#166534",        # Forest Green
    "success_bg": "#DCFCE7",
    "warning": "#854D0E",        # Amber Gold
    "danger": "#991B1B",         # Crimson Red
    "statusbar": "#E2E8F0",      # Slate 200
}

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class EnterpriseERPAppDemo(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"Perú Compras Bot Enterprise — Workbench v{VERSION}")
        self.geometry("1180x760")
        self.minsize(1040, 680)
        self.configure(fg_color=_C["bg"])

        self._active_tab = "pdf"
        self._loaded_file = None
        self._table_data = []

        self._build_ui()
        self._load_sample_data()

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) # Barra de Menú Nivel Superior
        self.grid_rowconfigure(1, weight=0) # Barra de Módulos Operativos
        self.grid_rowconfigure(2, weight=1) # Workbench Principal (2 Columnas: Grid + Inspector)
        self.grid_rowconfigure(3, weight=0) # Barra de Estado Inferior

        self._build_top_menu()
        self._build_toolbar()
        self._build_workbench()
        self._build_statusbar()

    # ── 1. BARRA DE MENÚ TIPO WINDOWS NATIVO ──
    def _build_top_menu(self):
        menu_frame = ctk.CTkFrame(self, fg_color=_C["header_bg"], corner_radius=0, height=36)
        menu_frame.grid(row=0, column=0, sticky="ew")
        
        title_lbl = ctk.CTkLabel(
            menu_frame, text="🏛️ PERÚ COMPRAS BOT ENTERPRISE  |  Módelo de Automatización de Proveedores",
            font=ctk.CTkFont(size=12, weight="bold"), text_color=_C["header_txt"]
        )
        title_lbl.pack(side="left", padx=16, pady=6)

        ver_lbl = ctk.CTkLabel(
            menu_frame, text=f"v{VERSION}",
            font=ctk.CTkFont(size=11), text_color="#94A3B8"
        )
        ver_lbl.pack(side="right", padx=16, pady=6)

    # ── 2. BARRA DE HERRAMIENTAS Y MÓDULOS DE TRABAJO ──
    def _build_toolbar(self):
        toolbar = ctk.CTkFrame(self, fg_color=_C["toolbar_bg"], corner_radius=0, height=48)
        toolbar.grid(row=1, column=0, sticky="ew")
        
        btn_frame = ctk.CTkFrame(toolbar, fg_color="transparent")
        btn_frame.pack(side="left", padx=12, pady=6)

        self._btn_tab_pdf = ctk.CTkButton(
            btn_frame, text="📄 Publicar Ofertas PDF", height=34, corner_radius=4,
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda: self._set_active_tab("pdf")
        )
        self._btn_tab_pdf.pack(side="left", padx=4)

        self._btn_tab_stock = ctk.CTkButton(
            btn_frame, text="📊 Análisis de Stock", height=34, corner_radius=4,
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda: self._set_active_tab("stock")
        )
        self._btn_tab_stock.pack(side="left", padx=4)

        self._btn_tab_json = ctk.CTkButton(
            btn_frame, text="🏷️ Subida de Precios JSON", height=34, corner_radius=4,
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda: self._set_active_tab("json")
        )
        self._btn_tab_json.pack(side="left", padx=4)

        self._btn_tab_tools = ctk.CTkButton(
            btn_frame, text="⚙️ Herramientas y Diagnóstico", height=34, corner_radius=4,
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda: self._set_active_tab("tools")
        )
        self._btn_tab_tools.pack(side="left", padx=4)

    # ── 3. WORKBENCH PRINCIPAL (Grid Tabular + Inspector Lateral) ──
    def _build_workbench(self):
        workbench = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        workbench.grid(row=2, column=0, padx=16, pady=12, sticky="nsew")
        workbench.grid_columnconfigure(0, weight=3, minsize=650) # Left Table Grid
        workbench.grid_columnconfigure(1, weight=1, minsize=360) # Right Inspector
        workbench.grid_rowconfigure(0, weight=1)

        # ── LADO IZQUIERDO: ZONA DE CARGA & GRID TABULAR DE DATOS EN TIEMPO REAL ──
        left_area = ctk.CTkFrame(workbench, fg_color="transparent")
        left_area.grid(row=0, column=0, padx=(0, 8), sticky="nsew")
        left_area.grid_columnconfigure(0, weight=1)
        left_area.grid_rowconfigure(1, weight=1)

        # Card 1: Zona de Arrastre / Carga Inteligente (Ley de Tesler)
        drop_card = ctk.CTkFrame(left_area, fg_color=_C["card"], corner_radius=6, border_width=1, border_color=_C["border"])
        drop_card.grid(row=0, column=0, padx=0, pady=(0, 10), sticky="ew")
        drop_card.grid_columnconfigure(0, weight=1)

        drop_inner = ctk.CTkFrame(drop_card, fg_color=_C["bg"], corner_radius=4, border_width=1, border_color=_C["border_dark"])
        drop_inner.grid(row=0, column=0, padx=12, pady=12, sticky="ew")
        drop_inner.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            drop_inner, text="📥 Cargar Archivo de Trabajo (Excel .xlsx / JSON)",
            font=ctk.CTkFont(size=13, weight="bold"), text_color=_C["txt_primary"]
        ).grid(row=0, column=0, padx=12, pady=(10, 2), sticky="w")

        self.lbl_file_info = ctk.CTkLabel(
            drop_inner, text="Arrastra un archivo aquí o haz clic para seleccionar. El sistema autodetectará columnas y esquema.",
            font=ctk.CTkFont(size=11), text_color=_C["txt_secondary"], anchor="w"
        )
        self.lbl_file_info.grid(row=1, column=0, padx=12, pady=(0, 8), sticky="w")

        file_row = ctk.CTkFrame(drop_inner, fg_color="transparent")
        file_row.grid(row=2, column=0, padx=12, pady=(0, 10), sticky="ew")
        
        btn_open = ctk.CTkButton(
            file_row, text="📂 Seleccionar Archivo", height=32,
            fg_color=_C["accent"], hover_color=_C["accent_hover"],
            font=ctk.CTkFont(size=12, weight="bold"), command=self._on_select_file
        )
        btn_open.pack(side="left")

        # Badges Detección Inteligente
        self.badge_part = ctk.CTkLabel(file_row, text="✓ N° Parte: Col A", font=ctk.CTkFont(size=11, weight="bold"), text_color=_C["success"], fg_color=_C["success_bg"], corner_radius=4, padx=8, pady=4)
        self.badge_part.pack(side="left", padx=8)

        self.badge_price = ctk.CTkLabel(file_row, text="✓ Precio: Col B", font=ctk.CTkFont(size=11, weight="bold"), text_color=_C["success"], fg_color=_C["success_bg"], corner_radius=4, padx=8, pady=4)
        self.badge_price.pack(side="left", padx=4)

        # Card 2: Tabla de Datos Registrados (Grid ERP Nivel Producción)
        table_card = ctk.CTkFrame(left_area, fg_color=_C["card"], corner_radius=6, border_width=1, border_color=_C["border"])
        table_card.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        table_card.grid_columnconfigure(0, weight=1)
        table_card.grid_rowconfigure(1, weight=1)

        t_header = ctk.CTkFrame(table_card, fg_color=_C["card_header"], corner_radius=0, height=38)
        t_header.grid(row=0, column=0, sticky="ew")
        
        ctk.CTkLabel(
            t_header, text="📋 REGISTROS A PROCESAR (VISTA PREVIA DE MATRIZ)",
            font=ctk.CTkFont(size=12, weight="bold"), text_color=_C["txt_primary"]
        ).pack(side="left", padx=12, pady=8)

        self.lbl_table_count = ctk.CTkLabel(
            t_header, text="Mostrando 5 productos cargados",
            font=ctk.CTkFont(size=11), text_color=_C["txt_muted"]
        )
        self.lbl_table_count.pack(side="right", padx=12, pady=8)

        # Tabla Treeview Estilo Windows ERP
        tree_frame = ctk.CTkFrame(table_card, fg_color="transparent")
        tree_frame.grid(row=1, column=0, padx=8, pady=8, sticky="nsew")
        tree_frame.grid_columnconfigure(0, weight=1)
        tree_frame.grid_rowconfigure(0, weight=1)

        columns = ("pos", "part", "desc", "price", "stock", "status")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
        
        self.tree.heading("pos", text="N°")
        self.tree.heading("part", text="Número de Parte")
        self.tree.heading("desc", text="Descripción / Marca")
        self.tree.heading("price", text="Precio S/")
        self.tree.heading("stock", text="Stock")
        self.tree.heading("status", text="Estado Procesamiento")

        self.tree.column("pos", width=40, anchor="center")
        self.tree.column("part", width=160, anchor="w")
        self.tree.column("desc", width=220, anchor="w")
        self.tree.column("price", width=90, anchor="e")
        self.tree.column("stock", width=60, anchor="center")
        self.tree.column("status", width=140, anchor="center")

        # Scrollbar para la tabla
        sb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        sb.grid(row=0, column=1, sticky="ns")

        # ── LADO DERECHO: INSPECTOR DE PARÁMETROS & CONTROL ──
        right_inspector = ctk.CTkFrame(workbench, fg_color=_C["card"], corner_radius=6, border_width=1, border_color=_C["border"])
        right_inspector.grid(row=0, column=1, padx=(8, 0), sticky="nsew")
        right_inspector.grid_columnconfigure(0, weight=1)
        right_inspector.grid_rowconfigure(3, weight=1)

        # Header Inspector
        insp_header = ctk.CTkFrame(right_inspector, fg_color=_C["card_header"], corner_radius=0, height=38)
        insp_header.grid(row=0, column=0, sticky="ew")
        
        ctk.CTkLabel(
            insp_header, text="⚙️ INSPECTOR DE CONFIGURACIÓN",
            font=ctk.CTkFont(size=12, weight="bold"), text_color=_C["txt_primary"]
        ).pack(side="left", padx=12, pady=8)

        # Sección 1: Credenciales
        cred_sec = ctk.CTkFrame(right_inspector, fg_color="transparent")
        cred_sec.grid(row=1, column=0, padx=12, pady=(10, 4), sticky="ew")
        cred_sec.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(cred_sec, text="Credenciales Perú Compras (Auto-guardadas)", font=ctk.CTkFont(size=11, weight="bold"), text_color=_C["txt_primary"]).grid(row=0, column=0, sticky="w")
        
        self.e_user = ctk.CTkEntry(cred_sec, placeholder_text="Usuario / RUC", height=32, fg_color=_C["bg"], border_color=_C["border"], text_color=_C["txt_primary"])
        self.e_user.grid(row=1, column=0, pady=(4, 4), sticky="ew")
        self.e_user.insert(0, "almerco.03")

        self.e_pass = ctk.CTkEntry(cred_sec, show="*", placeholder_text="Contraseña", height=32, fg_color=_C["bg"], border_color=_C["border"], text_color=_C["txt_primary"])
        self.e_pass.grid(row=2, column=0, pady=(0, 6), sticky="ew")
        self.e_pass.insert(0, "4lm3rKenYa@#")

        # Sección 2: Catálogo del Portal
        cat_sec = ctk.CTkFrame(right_inspector, fg_color="transparent")
        cat_sec.grid(row=2, column=0, padx=12, pady=(4, 4), sticky="ew")
        cat_sec.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(cat_sec, text="Filtros del Portal (Auto-Cargados)", font=ctk.CTkFont(size=11, weight="bold"), text_color=_C["txt_primary"]).grid(row=0, column=0, sticky="w")
        
        ctk.CTkLabel(cat_sec, text="Acuerdo Marco", font=ctk.CTkFont(size=10), text_color=_C["txt_secondary"]).grid(row=1, column=0, pady=(4, 1), sticky="w")
        self.cb_acuerdo = ctk.CTkOptionMenu(cat_sec, values=["249 - EXT-CE-2022-5 COMPUTADORAS Y ESCÁNERES"], height=32, fg_color=_C["bg"], button_color=_C["border"], text_color=_C["txt_primary"])
        self.cb_acuerdo.grid(row=2, column=0, pady=(0, 4), sticky="ew")

        ctk.CTkLabel(cat_sec, text="Catálogo Electrónico", font=ctk.CTkFont(size=10), text_color=_C["txt_secondary"]).grid(row=3, column=0, pady=(2, 1), sticky="w")
        self.cb_cat = ctk.CTkOptionMenu(cat_sec, values=["252 - COMPUTADORAS DE ESCRITORIO", "250 - COMPUTADORAS PORTÁTILES", "251 - ESCÁNERES"], height=32, fg_color=_C["bg"], button_color=_C["border"], text_color=_C["txt_primary"])
        self.cb_cat.grid(row=4, column=0, pady=(0, 4), sticky="ew")

        ctk.CTkLabel(cat_sec, text="Categoría", font=ctk.CTkFont(size=10), text_color=_C["txt_secondary"]).grid(row=5, column=0, pady=(2, 1), sticky="w")
        self.cb_sub = ctk.CTkOptionMenu(cat_sec, values=["11735 - COMPUTADORA DE ESCRITORIO", "11740 - ESTACION DE TRABAJO", "11741 - MONITOR"], height=32, fg_color=_C["bg"], button_color=_C["border"], text_color=_C["txt_primary"])
        self.cb_sub.grid(row=6, column=0, pady=(0, 8), sticky="ew")

        # Sección 3: Consola de Salida & Control
        console_sec = ctk.CTkFrame(right_inspector, fg_color="transparent")
        console_sec.grid(row=3, column=0, padx=12, pady=(4, 12), sticky="nsew")
        console_sec.grid_columnconfigure(0, weight=1)
        console_sec.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(console_sec, text="Registro de Consola", font=ctk.CTkFont(size=11, weight="bold"), text_color=_C["txt_primary"]).grid(row=0, column=0, sticky="w")
        
        self.log_box = ctk.CTkTextbox(console_sec, wrap="word", font=ctk.CTkFont(family="Consolas", size=10), fg_color=_C["header_bg"], text_color="#F8FAFC")
        self.log_box.grid(row=1, column=0, pady=(4, 8), sticky="nsew")
        self.log_box.insert("end", "[17:00:00] [SISTEMA] Workbench ERP cargado.\n")
        self.log_box.insert("end", "[17:00:01] [PORTAL] 5 registros importados de Excel.\n")

        # Botón de Acción Principal (F5)
        self.btn_run = ctk.CTkButton(
            console_sec, text="▶ INICIAR PROCESAMIENTO (F5)", height=40,
            fg_color=_C["accent"], hover_color=_C["accent_hover"],
            font=ctk.CTkFont(size=12, weight="bold"), command=self._on_run_process
        )
        self.btn_run.grid(row=2, column=0, sticky="ew")

    # ── 4. BARRA DE ESTADO INFERIOR NATIVA ──
    def _build_statusbar(self):
        sbar = ctk.CTkFrame(self, fg_color=_C["statusbar"], corner_radius=0, height=26)
        sbar.grid(row=3, column=0, sticky="ew")
        
        self.lbl_st_left = ctk.CTkLabel(
            sbar, text="🟢 Sistema Listo  |  Navegador: Oculto (Headless)  |  Perfil: ALMERCO E.I.R.L.",
            font=ctk.CTkFont(size=11), text_color=_C["txt_secondary"]
        )
        self.lbl_st_left.pack(side="left", padx=14, pady=2)

        self.lbl_st_right = ctk.CTkLabel(
            sbar, text="Perú Compras Bot Enterprise v1.3",
            font=ctk.CTkFont(size=11, weight="bold"), text_color=_C["txt_primary"]
        )
        self.lbl_st_right.pack(side="right", padx=14, pady=2)

    # ── MÉTODOS Y EVENTOS NATIVOS ──
    def _load_sample_data(self):
        sample_rows = [
            ("01", "2V262LT#ABM", "COMPUTADORA HP PROBOOK 445 G8", "3,450.00", "12", "⏳ Pendiente"),
            ("02", "3V5H1LT#ABM", "COMPUTADORA HP ELITEDESK 800 G6", "4,120.00", "8", "⏳ Pendiente"),
            ("03", "21A20005LM", "PORTÁTIL LENOVO THINKPAD E14", "3,890.00", "15", "⏳ Pendiente"),
            ("04", "20VE003DLM", "PORTÁTIL LENOVO THINKBOOK 15", "2,980.00", "20", "⏳ Pendiente"),
            ("05", "V5N36A", "ESCÁNER HP SCANJET PRO 2500", "1,650.00", "5", "⏳ Pendiente"),
        ]
        for row in sample_rows:
            self.tree.insert("", "end", values=row)

    def _set_active_tab(self, tab_id):
        self._active_tab = tab_id
        btns = {
            "pdf": self._btn_tab_pdf,
            "stock": self._btn_tab_stock,
            "json": self._btn_tab_json,
            "tools": self._btn_tab_tools
        }
        for name, btn in btns.items():
            if name == tab_id:
                btn.configure(fg_color=_C["accent"], text_color="#FFFFFF")
            else:
                btn.configure(fg_color="transparent", text_color="#94A3B8")

        self._append_log(f"[NAVEGACIÓN] Cambiado a módulo: {tab_id.upper()}")

    def _on_select_file(self):
        fpath = filedialog.askopenfilename(
            title="Seleccionar archivo de trabajo",
            filetypes=[("Excel y JSON", "*.xlsx;*.json"), ("Todos", "*.*")]
        )
        if fpath:
            bname = os.path.basename(fpath)
            self.lbl_file_info.configure(
                text=f"✓ Archivo cargado: {bname}  |  Esquema detectado automáticamente.",
                text_color=_C["success"]
            )
            self._append_log(f"[ARCHIVO] Cargar exitoso: {bname}")

    def _on_run_process(self):
        self._append_log("[EJECUCIÓN] Iniciando procesamiento de lista...")
        self._append_log("[LOGIN] Autenticando en Perú Compras...")
        self._append_log("[OCR] Captcha resuelto en 1.2 segundos.")
        messagebox.showinfo("Enterprise Prototipo v1.3", "¡Demostración de Workbench ERP iniciada!\n\nEste prototipo implementa la Ley de Tesler (backend inteligente) con la grilla de datos y controles estilo SAP / Power Automate Desktop.")

    def _append_log(self, msg):
        ts = time.strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{ts}] {msg}\n")
        self.log_box.see("end")


if __name__ == "__main__":
    app = EnterpriseERPAppDemo()
    app.mainloop()

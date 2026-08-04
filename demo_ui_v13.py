"""
Demo de Prototipo Interactivo UX/UI — Perú Compras Bot v1.3
Aplicando Ley de Tesler y parámetros Anti-IA de AGENTS.md
"""
import sys
import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk

VERSION = "1.3 (DEMO PROTOTIPO)"

# ── SISTEMA DE DISEÑO (Paleta Sobria Neutra - Estilo ERP Desktop) ──
_C = {
    "bg": "#F8FAFC",             # Slate 50
    "topbar": "#0F172A",         # Slate 900
    "topbar_txt": "#F8FAFC",
    "topbar_active": "#1E293B",  # Slate 800
    "card": "#FFFFFF",           # Blanco puro
    "card_bg": "#F1F5F9",        # Slate 100
    "border": "#CBD5E1",         # Slate 300
    "border_focus": "#94A3B8",   # Slate 400
    "txt_primary": "#0F172A",    # Slate 900
    "txt_secondary": "#475569",  # Slate 600
    "txt_muted": "#64748B",      # Slate 500
    "accent": "#1D4ED8",         # Royal Blue
    "accent_hover": "#1E40AF",
    "success": "#15803D",        # Forest Green
    "danger": "#B91C1C",         # Crimson Red
    "statusbar": "#E2E8F0",      # Slate 200
}

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class DemoAppV13(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"Perú Compras Bot — Prototipo v{VERSION}")
        self.geometry("1100x740")
        self.minsize(980, 640)
        self.configure(fg_color=_C["bg"])

        self._active_module = "pdf"
        self._build_ui()

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) # Header / Top Navbar
        self.grid_rowconfigure(1, weight=1) # Dynamic Content Area
        self.grid_rowconfigure(2, weight=0) # Bottom Status Bar

        self._build_top_navbar()
        self._build_content_area()
        self._build_status_bar()

    # ── BARRA SUPERIOR DE MÓDULOS (Navegación Desktop Novedosa) ──
    def _build_top_navbar(self):
        navbar = ctk.CTkFrame(self, fg_color=_C["topbar"], corner_radius=0, height=54)
        navbar.grid(row=0, column=0, sticky="ew")
        navbar.grid_columnconfigure(1, weight=1)

        # Brand / Title
        brand_frame = ctk.CTkFrame(navbar, fg_color="transparent")
        brand_frame.pack(side="left", padx=16, pady=10)

        ctk.CTkLabel(
            brand_frame, text="PERÚ COMPRAS BOT",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=_C["topbar_txt"]
        ).pack(side="left")

        ctk.CTkLabel(
            brand_frame, text=f"v{VERSION}",
            font=ctk.CTkFont(size=11),
            text_color="#94A3B8"
        ).pack(side="left", padx=(8, 0))

        # Modulos / Selector Tabs
        modules_frame = ctk.CTkFrame(navbar, fg_color="transparent")
        modules_frame.pack(side="right", padx=16)

        self._nav_btn_pdf = ctk.CTkButton(
            modules_frame, text="📄 Carga de Ofertas PDF",
            height=34, corner_radius=4,
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda: self._switch_module("pdf")
        )
        self._nav_btn_pdf.pack(side="left", padx=4)

        self._nav_btn_stock = ctk.CTkButton(
            modules_frame, text="📊 Análisis de Stock",
            height=34, corner_radius=4,
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda: self._switch_module("stock")
        )
        self._nav_btn_stock.pack(side="left", padx=4)

        self._nav_btn_json = ctk.CTkButton(
            modules_frame, text="🏷️ Precios JSON",
            height=34, corner_radius=4,
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda: self._switch_module("json")
        )
        self._nav_btn_json.pack(side="left", padx=4)

        self._nav_btn_guide = ctk.CTkButton(
            modules_frame, text="📖 Instrucciones",
            height=34, corner_radius=4,
            font=ctk.CTkFont(size=12, weight="bold"),
            command=lambda: self._switch_module("guide")
        )
        self._nav_btn_guide.pack(side="left", padx=4)

    # ── ÁREA DE CONTENIDO PRINCIPAL (Ley de Tesler: 2 Columnas Limpias) ──
    def _build_content_area(self):
        self.main_container = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.main_container.grid(row=1, column=0, padx=16, pady=12, sticky="nsew")
        self.main_container.grid_columnconfigure(0, weight=1, minsize=420)
        self.main_container.grid_columnconfigure(1, weight=1, minsize=460)
        self.main_container.grid_rowconfigure(0, weight=1)

        # Columna Izquierda: Formulario Simple (Paso 1, 2, 3)
        self.left_col = ctk.CTkScrollableFrame(
            self.main_container, fg_color="transparent",
            scrollbar_button_color=_C["border"]
        )
        self.left_col.grid(row=0, column=0, padx=(0, 8), sticky="nsew")
        self.left_col.grid_columnconfigure(0, weight=1)

        # Columna Derecha: Consola Ejecutiva y Monitor
        self.right_col = ctk.CTkFrame(
            self.main_container, fg_color=_C["card"], corner_radius=6,
            border_width=1, border_color=_C["border"]
        )
        self.right_col.grid(row=0, column=1, padx=(8, 0), sticky="nsew")
        self.right_col.grid_columnconfigure(0, weight=1)
        self.right_col.grid_rowconfigure(1, weight=1)

        self._build_left_form()
        self._build_right_console()
        self._switch_module("pdf")

    def _build_left_form(self):
        # Card 1: Credenciales (Recordadas automáticamente)
        card1 = self._create_card(self.left_col, "1. Credenciales Perú Compras")
        
        ctk.CTkLabel(
            card1, text="Usuario / RUC", font=ctk.CTkFont(size=11),
            text_color=_C["txt_secondary"], anchor="w"
        ).grid(row=0, column=0, padx=14, pady=(10, 2), sticky="w")
        
        e_user = ctk.CTkEntry(
            card1, placeholder_text="Usuario o RUC", height=34,
            fg_color=_C["card_bg"], border_color=_C["border"], text_color=_C["txt_primary"]
        )
        e_user.grid(row=1, column=0, padx=14, pady=(0, 8), sticky="ew")
        e_user.insert(0, "almerco.03")

        ctk.CTkLabel(
            card1, text="Contraseña", font=ctk.CTkFont(size=11),
            text_color=_C["txt_secondary"], anchor="w"
        ).grid(row=2, column=0, padx=14, pady=(0, 2), sticky="w")
        
        e_pass = ctk.CTkEntry(
            card1, show="*", height=34,
            fg_color=_C["card_bg"], border_color=_C["border"], text_color=_C["txt_primary"]
        )
        e_pass.grid(row=3, column=0, padx=14, pady=(0, 10), sticky="ew")
        e_pass.insert(0, "4lm3rKenYa@#")

        # Card 2: Archivo de Entrada (Auto-Detección de Esquema)
        card2 = self._create_card(self.left_col, "2. Archivo de Trabajo (Excel / JSON)")
        
        btn_file = ctk.CTkButton(
            card2, text="📂 Seleccionar Archivo .xlsx / .json", height=34,
            fg_color=_C["accent"], hover_color=_C["accent_hover"],
            font=ctk.CTkFont(size=12, weight="bold"),
            command=self._on_select_file
        )
        btn_file.grid(row=0, column=0, padx=14, pady=(12, 4), sticky="w")

        self.lbl_file_status = ctk.CTkLabel(
            card2, text="Ningún archivo cargado aún.",
            font=ctk.CTkFont(size=11), text_color=_C["txt_muted"], anchor="w"
        )
        self.lbl_file_status.grid(row=1, column=0, padx=14, pady=(0, 10), sticky="w")

        # Card 3: Parámetros del Portal (Cargados dinámicamente)
        card3 = self._create_card(self.left_col, "3. Configuración del Catálogo (Autocompletado)")
        
        ctk.CTkLabel(card3, text="Acuerdo Marco", font=ctk.CTkFont(size=11), text_color=_C["txt_secondary"]).grid(row=0, column=0, padx=14, pady=(8, 2), sticky="w")
        cb_acuerdo = ctk.CTkOptionMenu(
            card3, values=["EXT-CE-2022-5 COMPUTADORAS DE ESCRITORIO Y PORTÁTILES"],
            height=34, fg_color=_C["card_bg"], button_color=_C["border"], text_color=_C["txt_primary"],
            dropdown_fg_color=_C["card"], dropdown_text_color=_C["txt_primary"]
        )
        cb_acuerdo.grid(row=1, column=0, padx=14, pady=(0, 8), sticky="ew")

        ctk.CTkLabel(card3, text="Catálogo Electrónico", font=ctk.CTkFont(size=11), text_color=_C["txt_secondary"]).grid(row=2, column=0, padx=14, pady=(0, 2), sticky="w")
        cb_cat = ctk.CTkOptionMenu(
            card3, values=["COMPUTADORAS DE ESCRITORIO", "COMPUTADORAS PORTÁTILES", "ESCÁNERES"],
            height=34, fg_color=_C["card_bg"], button_color=_C["border"], text_color=_C["txt_primary"],
            dropdown_fg_color=_C["card"], dropdown_text_color=_C["txt_primary"]
        )
        cb_cat.grid(row=3, column=0, padx=14, pady=(0, 8), sticky="ew")

        ctk.CTkLabel(card3, text="Categoría", font=ctk.CTkFont(size=11), text_color=_C["txt_secondary"]).grid(row=4, column=0, padx=14, pady=(0, 2), sticky="w")
        cb_sub = ctk.CTkOptionMenu(
            card3, values=["COMPUTADORA DE ESCRITORIO", "ESTACION DE TRABAJO", "MONITOR"],
            height=34, fg_color=_C["card_bg"], button_color=_C["border"], text_color=_C["txt_primary"],
            dropdown_fg_color=_C["card"], dropdown_text_color=_C["txt_primary"]
        )
        cb_sub.grid(row=5, column=0, padx=14, pady=(0, 12), sticky="ew")

    def _build_right_console(self):
        header = ctk.CTkFrame(self.right_col, fg_color=_C["card_bg"], corner_radius=0, height=42)
        header.grid(row=0, column=0, sticky="ew")
        
        ctk.CTkLabel(
            header, text="MONITOR DE EJECUCIÓN Y REGISTROS",
            font=ctk.CTkFont(size=12, weight="bold"), text_color=_C["txt_primary"]
        ).pack(side="left", padx=14, pady=10)

        # Consola de Texto
        self.log_box = ctk.CTkTextbox(
            self.right_col, wrap="word", font=ctk.CTkFont(family="Consolas", size=11),
            fg_color="#0F172A", text_color="#F8FAFC", border_width=0
        )
        self.log_box.grid(row=1, column=0, padx=12, pady=12, sticky="nsew")
        self.log_box.insert("end", "[16:53:00] [SISTEMA] Demo v1.3 cargada correctamente.\n")
        self.log_box.insert("end", "[16:53:01] [PORTAL] Catálogos sincronizados desde cache local (3 acuerdos disp).\n")
        self.log_box.see("end")

        # Botón de Acción Principal (Ley de Tesler: 1 solo clic)
        actions_frame = ctk.CTkFrame(self.right_col, fg_color="transparent")
        actions_frame.grid(row=2, column=0, padx=12, pady=(0, 12), sticky="ew")
        actions_frame.grid_columnconfigure(0, weight=1)

        self.btn_run = ctk.CTkButton(
            actions_frame, text="▶ INICIAR AUTOMATIZACIÓN", height=42,
            fg_color=_C["accent"], hover_color=_C["accent_hover"],
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._on_run_demo
        )
        self.btn_run.grid(row=0, column=0, sticky="ew")

    def _build_status_bar(self):
        sbar = ctk.CTkFrame(self, fg_color=_C["statusbar"], corner_radius=0, height=28)
        sbar.grid(row=2, column=0, sticky="ew")
        
        lbl_st = ctk.CTkLabel(
            sbar, text="Estado: Listo  |  Navegador: Oculto (Headless)  |  Conexión SSL: Verificada",
            font=ctk.CTkFont(size=11), text_color=_C["txt_secondary"]
        )
        lbl_st.pack(side="left", padx=14, pady=4)

        lbl_ver = ctk.CTkLabel(
            sbar, text="Perú Compras Bot Enterprise v1.3",
            font=ctk.CTkFont(size=11, weight="bold"), text_color=_C["txt_primary"]
        )
        lbl_ver.pack(side="right", padx=14, pady=4)

    def _create_card(self, parent, title):
        lbl = ctk.CTkLabel(
            parent, text=title, font=ctk.CTkFont(size=12, weight="bold"),
            text_color=_C["txt_primary"], anchor="w"
        )
        lbl.pack(anchor="w", padx=2, pady=(10, 4))

        card = ctk.CTkFrame(
            parent, fg_color=_C["card"], corner_radius=6,
            border_width=1, border_color=_C["border"]
        )
        card.pack(fill="x", padx=0, pady=(0, 6))
        card.grid_columnconfigure(0, weight=1)
        return card

    def _switch_module(self, mod_id):
        self._active_module = mod_id
        btns = {
            "pdf": self._nav_btn_pdf,
            "stock": self._nav_btn_stock,
            "json": self._nav_btn_json,
            "guide": self._nav_btn_guide
        }
        for name, btn in btns.items():
            if name == mod_id:
                btn.configure(fg_color=_C["topbar_active"], text_color="#FFFFFF")
            else:
                btn.configure(fg_color="transparent", text_color="#94A3B8")

        self.log_box.insert("end", f"[{self._time_now()}] [NAVEGACIÓN] Módulo activo: {mod_id.upper()}\n")
        self.log_box.see("end")

    def _on_select_file(self):
        fpath = filedialog.askopenfilename(
            title="Seleccionar archivo de trabajo",
            filetypes=[("Excel y JSON", "*.xlsx;*.json"), ("Todos", "*.*")]
        )
        if fpath:
            bname = os.path.basename(fpath)
            self.lbl_file_status.configure(
                text=f"✓ Archivo cargado: {bname} (Esquema detectado automáticamente)",
                text_color=_C["success"]
            )
            self.log_box.insert("end", f"[{self._time_now()}] [ARCHIVOS] Cargado: {bname} -> Columnas autodetectadas: PartNumber, Precio, Stock\n")
            self.log_box.see("end")

    def _on_run_demo(self):
        self.log_box.insert("end", f"[{self._time_now()}] [EJECUCIÓN] Iniciando flujo automatizado...\n")
        self.log_box.insert("end", f"[{self._time_now()}] [LOGIN] Iniciando sesión en Perú Compras...\n")
        self.log_box.insert("end", f"[{self._time_now()}] [CAPTCHA] OCR resolución rápida exitosa (código 6 chars).\n")
        self.log_box.insert("end", f"[{self._time_now()}] [PROCESO] Aplicando filtros y ofertas en catálogo...\n")
        self.log_box.see("end")
        messagebox.showinfo("Prototipo v1.3", "¡Demostración de flujo iniciada correctamente!\n\nEste prototipo implementa la Ley de Tesler (complejidad en el backend) y el diseño sobrio de escritorio.")

    def _time_now(self):
        import time
        return time.strftime("%H:%M:%S")


if __name__ == "__main__":
    app = DemoAppV13()
    app.mainloop()

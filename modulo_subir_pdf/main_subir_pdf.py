import sys, os, queue, threading, time, json, re
from io import BytesIO
from pathlib import Path
from tkinter import filedialog

VERSION = "1.0"

# ── Paths ─────────────────────────────────────────────────────────
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

from automation.browser import init_browser, close_browser
from automation.login import do_login
from utils.logger import LogWriter

# Imports locales del módulo (renombrados para evitar conflicto con el proyecto raíz)
from utils_mod.excel_parser_mod import get_sheets, detect_columns, parse_excel
from utils_mod.logger_mod import LogWriter as LocalLogWriter

try:
    import customtkinter as ctk
    from PIL import Image
except ImportError:
    print("Error: instala customtkinter y Pillow: pip install customtkinter pillow")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════════════
#  Helpers
# ═══════════════════════════════════════════════════════════════════
def _make_stock_log(append_fn):
    # ponytail: puente ligero LogWriter → callback UI (pestaña 2)
    class _StockLog:
        def info(self, msg): append_fn(str(msg))
        def warning(self, msg): append_fn(f"⚠ {msg}")
        def error(self, msg): append_fn(f"❌ {msg}")
        def success(self, msg): append_fn(f"✅ {msg}")
        def ok(self, msg): append_fn(f"✅ {msg}")
    return _StockLog()


# ═══════════════════════════════════════════════════════════════════
#  BRIDGE — Comunicación UI ↔ Thread (CAPTCHA manual)
# ═══════════════════════════════════════════════════════════════════

class CaptchaBridge:
    def __init__(self):
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.image_bytes = None
        self.user_code = ""
        self.stop_event = None

    def request(self, img):
        with self.lock:
            self.image_bytes = img
            self.user_code = ""
            self.event.clear()
        while True:
            if self.stop_event and self.stop_event.is_set():
                self.event.set()
                return ""
            if self.event.wait(timeout=0.5):
                break
        with self.lock:
            return self.user_code

    def respond(self, code):
        with self.lock:
            self.user_code = code
            self.image_bytes = None
        self.event.set()


# ═══════════════════════════════════════════════════════════════════
#  APP
# ═══════════════════════════════════════════════════════════════════

class SubirPdfApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"Peru Compras — Subir PDF v{VERSION}")
        self.geometry("960x780")
        self.minsize(820, 640)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.log_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.captcha_bridge = CaptchaBridge()
        self._running = False
        self._log_lines = []
        self._ok = 0
        self._errors = 0
        self._total = 0

        self._excel_path = ""
        self._excel_rows = []
        self._excel_columns = []

        self._catalog_data = {}
        self._catalog_combos = []
        self._load_dropdown_json()

        self._build_ui()
        self.poll_queue()

    def _load_dropdown_json(self):
        # ponytail: usar resource_path para que funcione empaquetado con PyInstaller
        try:
            try:
                from resource_helper import resource_path
            except Exception:
                _root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                if _root not in sys.path:
                    sys.path.insert(0, _root)
                from resource_helper import resource_path
            candidates = [
                resource_path("modulo_subir_pdf/combinaciones_computadoras.json"),
                resource_path("modulo_subir_pdf/dropdown_options_modificar.json"),
            ]
            json_path = ""
            for cand in candidates:
                if os.path.isfile(cand):
                    json_path = cand
                    break
            if not json_path:
                return
            with open(json_path, "r", encoding="utf-8") as f:
                self._catalog_data = json.load(f)
        except Exception:
            pass

    # ── Build UI (Sidebar Layout & Enterprise Architecture) ────────

    def _build_ui(self):
        self.configure(fg_color="#111827")
        self.grid_columnconfigure(0, weight=0, minsize=220) # Sidebar
        self.grid_columnconfigure(1, weight=1)              # Main Content
        self.grid_rowconfigure(0, weight=1)                 # Workspace
        self.grid_rowconfigure(1, weight=0)                 # Footer

        # ═══════════════════════════════════════════════════════════
        # 1. SIDEBAR IZQUIERDO (#1f2937)
        # ═══════════════════════════════════════════════════════════
        sidebar = ctk.CTkFrame(self, fg_color="#1f2937", corner_radius=0, border_width=1, border_color="#374151")
        sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        sidebar.grid_rowconfigure(6, weight=1)

        # Header Badge Sidebar
        badge_box = ctk.CTkFrame(sidebar, fg_color="#111827", corner_radius=8, border_width=1, border_color="#374151")
        badge_box.grid(row=0, column=0, padx=14, pady=16, sticky="ew")
        
        ctk.CTkLabel(
            badge_box, text="PERÚ COMPRAS", font=ctk.CTkFont(size=14, weight="bold"), text_color="#38bdf8"
        ).pack(anchor="w", padx=10, pady=(8, 0))
        ctk.CTkLabel(
            badge_box, text=f"Automation Suite v{VERSION}", font=ctk.CTkFont(size=10), text_color="#9ca3af"
        ).pack(anchor="w", padx=10, pady=(0, 8))

        # Botones de Navegación Lateral
        self._nav_buttons = {}
        nav_items = [
            ("pdf", "Carga de PDFs"),
            ("stock", "Análisis de Stock"),
            ("json", "Precios JSON"),
            ("guide", "Guía e Instrucciones"),
            ("tools", "Herramientas Avanzadas"),
        ]

        for idx, (view_id, label) in enumerate(nav_items, start=1):
            btn = ctk.CTkButton(
                sidebar,
                text=label,
                height=38,
                corner_radius=6,
                anchor="w",
                font=ctk.CTkFont(size=12, weight="bold"),
                fg_color="transparent",
                text_color="#9ca3af",
                hover_color="#374151",
                command=lambda v=view_id: self._switch_view(v),
            )
            btn.grid(row=idx, column=0, padx=12, pady=3, sticky="ew")
            self._nav_buttons[view_id] = btn

        # Footer Sidebar (Estado del Sistema)
        sys_status_box = ctk.CTkFrame(sidebar, fg_color="#111827", corner_radius=6)
        sys_status_box.grid(row=7, column=0, padx=12, pady=14, sticky="ew")
        ctk.CTkLabel(
            sys_status_box, text="Estado: Operativo", font=ctk.CTkFont(size=10, weight="bold"), text_color="#10b981"
        ).pack(padx=8, pady=6)

        # ═══════════════════════════════════════════════════════════
        # 2. MAIN CONTENT AREA (#111827)
        # ═══════════════════════════════════════════════════════════
        self.main_container = ctk.CTkFrame(self, fg_color="#111827", corner_radius=0)
        self.main_container.grid(row=0, column=1, padx=16, pady=(16, 8), sticky="nsew")
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)

        self._views = {}

        # ── Vista 1: Carga de PDFs ──
        view_pdf = ctk.CTkFrame(self.main_container, fg_color="transparent")
        view_pdf.grid_columnconfigure(0, weight=1, minsize=360)
        view_pdf.grid_columnconfigure(1, weight=1, minsize=360)
        view_pdf.grid_rowconfigure(0, weight=1)

        left_col = ctk.CTkScrollableFrame(view_pdf, fg_color="transparent")
        left_col.grid(row=0, column=0, padx=(0, 8), sticky="nsew")
        left_col.grid_columnconfigure(0, weight=1)

        self._build_credentials_section(left_col)
        self._build_excel_section(left_col)
        self._build_catalog_section(left_col)
        self._build_opciones_section(left_col)

        right_col = ctk.CTkFrame(view_pdf, fg_color="#1f2937", corner_radius=8, border_width=1, border_color="#374151")
        right_col.grid(row=0, column=1, padx=(8, 0), sticky="nsew")
        right_col.grid_columnconfigure(0, weight=1)
        right_col.grid_rowconfigure(0, weight=1)
        self._build_execution_section(right_col)

        self._views["pdf"] = view_pdf

        # ── Vista 2: Análisis de Stock ──
        view_stock = ctk.CTkFrame(self.main_container, fg_color="transparent")
        view_stock.grid_columnconfigure(0, weight=1, minsize=360)
        view_stock.grid_columnconfigure(1, weight=1, minsize=360)
        view_stock.grid_rowconfigure(0, weight=1)
        self._build_stock_tab(left_col=None, right_col=None, parent=view_stock)
        self._views["stock"] = view_stock

        # ── Vista 3: Precios JSON ──
        view_json = ctk.CTkFrame(self.main_container, fg_color="transparent")
        view_json.grid_columnconfigure(0, weight=1)
        view_json.grid_rowconfigure(0, weight=1)
        import tab_precios_json
        tab_precios_json.build_precios_json_tab(self, parent=view_json)
        self._views["json"] = view_json

        # ── Vista 4: Guía e Instrucciones ──
        view_guide = ctk.CTkFrame(self.main_container, fg_color="transparent")
        import gui_instructions_tab
        gui_instructions_tab.build_instructions_tab(view_guide)
        self._views["guide"] = view_guide

        # ── Vista 5: Herramientas Avanzadas ──
        view_tools = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self._build_advanced_tools_tab(view_tools)
        self._views["tools"] = view_tools

        # ═══════════════════════════════════════════════════════════
        # 3. FOOTER CORPORATIVO (#1f2937)
        # ═══════════════════════════════════════════════════════════
        footer = ctk.CTkFrame(self, fg_color="#1f2937", corner_radius=8, border_width=1, border_color="#374151")
        footer.grid(row=1, column=1, padx=16, pady=(0, 14), sticky="ew")

        f_layout = ctk.CTkFrame(footer, fg_color="transparent")
        f_layout.pack(fill="x", padx=14, pady=8)

        self.lbl_footer_status = ctk.CTkLabel(
            f_layout, text="Listo para iniciar procesamiento.", font=ctk.CTkFont(size=12), text_color="#9ca3af"
        )
        self.lbl_footer_status.pack(side="left", padx=4)

        self.btn_stop = ctk.CTkButton(
            f_layout,
            text="Detener",
            width=110,
            height=38,
            fg_color="#dc2626",
            hover_color="#b91c1c",
            state="disabled",
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._on_stop,
        )
        self.btn_stop.pack(side="right", padx=(8, 0))

        self.btn_launch = ctk.CTkButton(
            f_layout,
            text="Iniciar Procesamiento",
            width=220,
            height=38,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._on_launch,
        )
        self.btn_launch.pack(side="right", padx=4)

        # Mostrar Vista Inicial ("pdf")
        self._switch_view("pdf")

    def _switch_view(self, view_id):
        """Cambia de vista activa en el main_container y actualiza botones laterales."""
        for v_name, frame in self._views.items():
            if v_name == view_id:
                frame.grid(row=0, column=0, sticky="nsew")
            else:
                frame.grid_forget()

        for v_name, btn in self._nav_buttons.items():
            if v_name == view_id:
                btn.configure(fg_color="#2563eb", text_color="#f9fafb")
            else:
                btn.configure(fg_color="transparent", text_color="#9ca3af")

    def _build_advanced_tools_tab(self, parent):
        """Construye la vista de Herramientas Avanzadas para desarrollo/pruebas."""
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)

        box = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        box.grid(row=0, column=0, padx=16, pady=16, sticky="nsew")
        box.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            box, text="Herramientas Avanzadas de Diagnóstico", font=ctk.CTkFont(size=16, weight="bold"), text_color="#f9fafb"
        ).pack(anchor="w", pady=(0, 6))

        ctk.CTkLabel(
            box, text="Pruebas aisladas, scrapers y descubrimiento de endpoints del portal.", font=ctk.CTkFont(size=11), text_color="#9ca3af"
        ).pack(anchor="w", pady=(0, 16))

        # Grupo 1: Pruebas Cortas
        g1 = ctk.CTkFrame(box, fg_color="#1f2937", corner_radius=8, border_width=1, border_color="#374151")
        g1.pack(fill="x", pady=6, ipadx=14, ipady=12)
        ctk.CTkLabel(g1, text="Pruebas Directas", font=ctk.CTkFont(size=13, weight="bold"), text_color="#2563eb").pack(anchor="w", padx=12, pady=4)

        b_row1 = ctk.CTkFrame(g1, fg_color="transparent")
        b_row1.pack(fill="x", padx=12, pady=4)

        self.btn_test = ctk.CTkButton(b_row1, text="Test (1 Ficha)", width=150, height=34, fg_color="#374151", hover_color="#4b5563", command=self._on_test)
        self.btn_test.pack(side="left", padx=(0, 8))

        self.btn_nro = ctk.CTkButton(b_row1, text="Solo N° de Parte", width=150, height=34, fg_color="#374151", hover_color="#4b5563", command=self._on_nro_parte)
        self.btn_nro.pack(side="left", padx=8)

        self.btn_certs = ctk.CTkButton(b_row1, text="Solo Certificaciones", width=160, height=34, fg_color="#374151", hover_color="#4b5563", command=self._on_certs_only)
        self.btn_certs.pack(side="left", padx=8)

        # Grupo 2: Extracción y Discovery
        g2 = ctk.CTkFrame(box, fg_color="#252538", corner_radius=8)
        g2.pack(fill="x", pady=6, ipadx=12, ipady=10)
        ctk.CTkLabel(g2, text="Extracción y Scrapers", font=ctk.CTkFont(size=13, weight="bold"), text_color="#2563eb").pack(anchor="w", padx=12, pady=4)

        b_row2 = ctk.CTkFrame(g2, fg_color="transparent")
        b_row2.pack(fill="x", padx=12, pady=4)

        self.btn_extract = ctk.CTkButton(
            b_row2, text="Extraer Reportes", width=160, height=34,
            fg_color="#334155", hover_color="#475569",
            command=self._on_extract,
        )
        self.btn_extract.pack(side="left", padx=(0, 8))

        self.btn_compare = ctk.CTkButton(
            b_row2, text="Comparar Fichas", width=150, height=34,
            fg_color="#334155", hover_color="#475569",
            command=self._on_compare,
        )
        self.btn_compare.pack(side="left", padx=8)

        self.btn_discovery = ctk.CTkButton(
            b_row2, text="Discovery v1", width=130, height=34,
            fg_color="#334155", hover_color="#475569",
            command=self._on_discovery,
        )
        self.btn_discovery.pack(side="left", padx=8)

        self.btn_discovery2 = ctk.CTkButton(
            b_row2, text="Discovery v2", width=130, height=34,
            fg_color="#334155", hover_color="#475569",
            command=self._on_discovery2,
        )
        self.btn_discovery2.pack(side="left", padx=8)


    # ── Credentials Section ───────────────────────────────────────

    # ── Pestaña 2: Stock/Cobertura/Plazo ─────────────────────────

    def _build_stock_tab(self, left_col=None, right_col=None, parent=None):
        """Construye la UI para el modo stock/cobertura/plazo (réplica del otro bot)."""
        if parent is None:
            parent = right_col

        # Estado
        self._stock_excel_path = ""
        self._stock_excel_df = []
        self._stock_running = False
        self._stock_stop_event = threading.Event()
        self._stock_log_queue = queue.Queue()
        self._stock_log_lines = []
        self._stock_total = 0
        self._stock_ok = 0
        self._stock_errors = 0
        self._stock_report_path = ""

        # LEFT COLUMN
        left = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        left.grid(row=0, column=0, padx=(0, 6), sticky="nsew")
        left.grid_columnconfigure(0, weight=1)

        # Título
        ctk.CTkLabel(
            left, text="📊 Modo Stock/Cobertura/Plazo",
            font=ctk.CTkFont(size=18, weight="bold"),
        ).grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")
        ctk.CTkLabel(
            left, text="Réplica del flujo del otro bot PeruCompras en Playwright",
            font=ctk.CTkFont(size=11), text_color="gray60",
        ).grid(row=1, column=0, padx=12, pady=(0, 8), sticky="w")

        # ── Sección 0: Credenciales propias de este flujo ──
        ctk.CTkLabel(left, text="Credenciales (flujo independiente)",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color="#5dade2").grid(row=2, column=0, padx=12, pady=(8, 4), sticky="w")
        frame_creds = ctk.CTkFrame(left, fg_color="gray10")
        frame_creds.grid(row=3, column=0, padx=12, pady=(0, 8), sticky="ew")
        frame_creds.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(frame_creds, text="Usuario:", anchor="w"
                     ).grid(row=0, column=0, padx=10, pady=4, sticky="w")
        self.entry_stock_user = ctk.CTkEntry(frame_creds)
        self.entry_stock_user.insert(0, "fernando.trinidad")
        self.entry_stock_user.grid(row=0, column=1, padx=10, pady=4, sticky="ew")

        ctk.CTkLabel(frame_creds, text="Contraseña:", anchor="w"
                     ).grid(row=1, column=0, padx=10, pady=(0, 8), sticky="w")
        self.entry_stock_pass = ctk.CTkEntry(frame_creds, show="*")
        self.entry_stock_pass.insert(0, "po!tLKB#8^r4e")
        self.entry_stock_pass.grid(row=1, column=1, padx=10, pady=(0, 8), sticky="ew")

        # ── Sección 1: Excel de productos ──
        ctk.CTkLabel(left, text="Excel de productos (Parte + Stock)",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color="#5dade2").grid(row=4, column=0, padx=12, pady=(12, 4), sticky="w")
        frame_excel = ctk.CTkFrame(left, fg_color="gray10")
        frame_excel.grid(row=5, column=0, padx=12, pady=(0, 8), sticky="ew")
        frame_excel.grid_columnconfigure(0, weight=1)

        self.lbl_stock_excel = ctk.CTkLabel(
            frame_excel, text="(sin archivo)", text_color="gray60", anchor="w"
        )
        self.lbl_stock_excel.grid(row=0, column=0, padx=10, pady=8, sticky="ew")

        btn_row = ctk.CTkFrame(frame_excel, fg_color="transparent")
        btn_row.grid(row=1, column=0, padx=10, pady=(0, 8), sticky="ew")
        ctk.CTkButton(
            btn_row, text="📂 Cargar Excel", width=120,
            command=self._on_load_stock_excel,
        ).pack(side="left", padx=(0, 6))
        ctk.CTkButton(
            btn_row, text="📋 Descargar Plantilla", width=160,
            command=self._on_download_stock_template,
            fg_color="#2c3e50", hover_color="#34495e",
        ).pack(side="left")
        self.lbl_stock_summary = ctk.CTkLabel(
            frame_excel, text="", text_color="gray60", anchor="w"
        )
        self.lbl_stock_summary.grid(row=2, column=0, padx=10, pady=(0, 8), sticky="ew")

        # ── Sección 2: Filtros del portal ──
        ctk.CTkLabel(left, text="Filtros del portal (Acuerdo > Catálogo > Categoría)",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color="#5dade2").grid(row=6, column=0, padx=12, pady=(12, 4), sticky="w")
        frame_filtros = ctk.CTkFrame(left, fg_color="gray10")
        frame_filtros.grid(row=7, column=0, padx=12, pady=(0, 8), sticky="ew")
        frame_filtros.grid_columnconfigure(1, weight=1)

        # Cargar JSON de combos extraídos
        self._stock_combos_data = self._load_stock_combos_json()
        acuerdos_list = self._stock_combos_data.get("acuerdos", [])
        acuerdo_values = [a["text"] for a in acuerdos_list] if acuerdos_list else ["-- Sin datos --"]

        # Acuerdo
        ctk.CTkLabel(frame_filtros, text="Acuerdo:", anchor="w"
                     ).grid(row=0, column=0, padx=10, pady=4, sticky="w")
        self.option_stock_acuerdo = ctk.CTkOptionMenu(
            frame_filtros, values=acuerdo_values, width=300,
            command=self._on_stock_acuerdo_changed,
        )
        self.option_stock_acuerdo.grid(row=0, column=1, padx=10, pady=4, sticky="ew")
        if acuerdo_values and acuerdo_values[0] != "-- Sin datos --":
            self.option_stock_acuerdo.set(acuerdo_values[0])

        # Catálogo
        ctk.CTkLabel(frame_filtros, text="Catálogo:", anchor="w"
                     ).grid(row=1, column=0, padx=10, pady=4, sticky="w")
        self.option_stock_catalogo = ctk.CTkOptionMenu(
            frame_filtros, values=["-- Seleccione acuerdo primero --"], width=300,
            command=self._on_stock_catalogo_changed,
        )
        self.option_stock_catalogo.grid(row=1, column=1, padx=10, pady=4, sticky="ew")

        # Categoría
        ctk.CTkLabel(frame_filtros, text="Categoría:", anchor="w"
                     ).grid(row=2, column=0, padx=10, pady=4, sticky="w")
        self.option_stock_categoria = ctk.CTkOptionMenu(
            frame_filtros, values=["-- Seleccione catálogo primero --"], width=300,
        )
        self.option_stock_categoria.grid(row=2, column=1, padx=10, pady=4, sticky="ew")

        # Pausa entre productos
        ctk.CTkLabel(frame_filtros, text="Pausa (seg):", anchor="w"
                     ).grid(row=3, column=0, padx=10, pady=4, sticky="w")
        self.entry_stock_pausa = ctk.CTkEntry(frame_filtros, width=80)
        self.entry_stock_pausa.insert(0, "2")
        self.entry_stock_pausa.grid(row=3, column=1, padx=10, pady=4, sticky="w")

        # Ver navegador (mostrar ventana del browser)
        self.check_stock_visible = ctk.CTkCheckBox(
            frame_filtros, text="👁 Ver navegador (mostrar ventana)",
        )
        self.check_stock_visible.grid(row=4, column=0, columnspan=2, padx=10, pady=(6, 4), sticky="w")

        # Cargar catálogos del primer acuerdo por defecto
        if acuerdos_list:
            self._on_stock_acuerdo_changed(acuerdo_values[0])

        # ── Botones de acción ──
        ctk.CTkLabel(left, text="Acciones",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color="#5dade2").grid(row=8, column=0, padx=12, pady=(12, 4), sticky="w")
        frame_btns = ctk.CTkFrame(left, fg_color="transparent")
        frame_btns.grid(row=9, column=0, padx=12, pady=(0, 8), sticky="ew")

        self.btn_stock_start = ctk.CTkButton(
            frame_btns, text="▶ Iniciar Stock", width=180, height=42,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._on_stock_start,
        )
        self.btn_stock_start.pack(side="left", padx=(0, 8))

        self.btn_stock_stop = ctk.CTkButton(
            frame_btns, text="■ Detener", width=120, height=42,
            fg_color="#c0392b", hover_color="#96281b", state="disabled",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._on_stock_stop,
        )
        self.btn_stock_stop.pack(side="left", padx=(0, 8))

        # Estado
        self.lbl_stock_status = ctk.CTkLabel(
            frame_btns, text="Listo", text_color="#5dade2",
            font=ctk.CTkFont(size=12, weight="bold"),
        )
        self.lbl_stock_status.pack(side="left", padx=12)

        # RIGHT COLUMN: log + stats
        right = ctk.CTkFrame(parent)
        right.grid(row=0, column=1, padx=(6, 0), sticky="nsew")
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(1, weight=1)

        # Stats
        stats = ctk.CTkFrame(right, fg_color="gray15")
        stats.grid(row=0, column=0, padx=8, pady=(8, 4), sticky="ew")
        stats.grid_columnconfigure((0, 1, 2, 3), weight=1)

        ctk.CTkLabel(stats, text="Total", font=ctk.CTkFont(size=11), text_color="gray60"
                     ).grid(row=0, column=0, padx=8, pady=(4, 0))
        self.lbl_stock_stat_total = ctk.CTkLabel(stats, text="0", font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_stock_stat_total.grid(row=1, column=0, padx=8, pady=(0, 4))

        ctk.CTkLabel(stats, text="OK", font=ctk.CTkFont(size=11), text_color="#5dade2"
                     ).grid(row=0, column=1, padx=8, pady=(4, 0))
        self.lbl_stock_stat_ok = ctk.CTkLabel(stats, text="0", font=ctk.CTkFont(size=20, weight="bold"),
                                              text_color="#5dade2")
        self.lbl_stock_stat_ok.grid(row=1, column=1, padx=8, pady=(0, 4))

        ctk.CTkLabel(stats, text="Fallos", font=ctk.CTkFont(size=11), text_color="#e74c3c"
                     ).grid(row=0, column=2, padx=8, pady=(4, 0))
        self.lbl_stock_stat_fail = ctk.CTkLabel(stats, text="0", font=ctk.CTkFont(size=20, weight="bold"),
                                                text_color="#e74c3c")
        self.lbl_stock_stat_fail.grid(row=1, column=2, padx=8, pady=(0, 4))

        ctk.CTkLabel(stats, text="Reporte", font=ctk.CTkFont(size=11), text_color="gray60"
                     ).grid(row=0, column=3, padx=8, pady=(4, 0))
        self.lbl_stock_report = ctk.CTkLabel(stats, text="(ninguno)", font=ctk.CTkFont(size=10),
                                            text_color="gray60", wraplength=200)
        self.lbl_stock_report.grid(row=1, column=3, padx=8, pady=(0, 4))

        # Progreso
        self.progress_stock = ctk.CTkProgressBar(right)
        self.progress_stock.grid(row=2, column=0, padx=8, pady=4, sticky="ew")
        self.progress_stock.set(0)

        # Log
        self.log_stock = ctk.CTkTextbox(right, font=ctk.CTkFont(family="Consolas", size=11))
        self.log_stock.grid(row=1, column=0, padx=8, pady=(4, 8), sticky="nsew")
        self.log_stock.configure(state="disabled")

    def _on_load_stock_excel(self):
        from tkinter import filedialog
        path = filedialog.askopenfilename(
            title="Seleccionar Excel de stock",
            filetypes=[("Excel", "*.xlsx *.xls")],
        )
        if not path:
            return
        self._stock_excel_path = path
        self.lbl_stock_excel.configure(text=os.path.basename(path), text_color="white")
        # Validar
        try:
            from automation_otro_bot.stock import analizar_excel_stock
            res = analizar_excel_stock(path)
            if res["valido"]:
                self._stock_excel_df = res["df"]
                self.lbl_stock_summary.configure(
                    text=f"✅ {len(res['df'])} productos válidos" +
                         (f" | ⚠ {len(res['errores'])} errores" if res["errores"] else ""),
                    text_color="#5dade2",
                )
            else:
                self.lbl_stock_summary.configure(
                    text=f"❌ Errores: {'; '.join(res['errores'][:3])}",
                    text_color="#e74c3c",
                )
                self._stock_excel_df = []
        except Exception as e:
            self.lbl_stock_summary.configure(text=f"❌ Error: {e}", text_color="#e74c3c")

    def _on_download_stock_template(self):
        from tkinter import filedialog
        try:
            from openpyxl import Workbook
            wb = Workbook()
            ws = wb.active
            ws.title = "Stock"
            ws.append(["Parte", "Stock", "Ficha"])
            for ejemplo in [("EMU5R6000", 1000, 2267958),
                            ("EMU5R6001", 500, 2267950),
                            ("EMU5R6002", 2000, 2271431)]:
                ws.append(ejemplo)
            path = filedialog.asksaveasfilename(
                title="Guardar plantilla",
                defaultextension=".xlsx",
                filetypes=[("Excel", "*.xlsx")],
                initialfile="plantilla_stock.xlsx",
            )
            if path:
                wb.save(path)
                self._append_stock_log(f"📋 Plantilla guardada: {path}")
        except Exception as e:
            self._append_stock_log(f"❌ Error creando plantilla: {e}")

    def _load_stock_combos_json(self) -> dict:
        # ponytail: usar resource_path para que funcione empaquetado con PyInstaller
        try:
            try:
                from resource_helper import resource_path
            except Exception:
                import sys
                _root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                if _root not in sys.path:
                    sys.path.insert(0, _root)
                from resource_helper import resource_path
            json_path = resource_path("modulo_subir_pdf/dropdowns_mejora_basica.json")
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            self._append_stock_log(f"⚠ No se pudo cargar dropdowns_mejora_basica.json: {e}")
            return {"acuerdos": [], "combinaciones": []}

    def _on_stock_acuerdo_changed(self, acuerdo_text: str):
        # Filtrar combinaciones cuyo acuerdo (por coincidencia de texto) coincida
        acuerdos_data = self._stock_combos_data.get("acuerdos", [])
        acuerdo_value = None
        for a in acuerdos_data:
            if a.get("text") == acuerdo_text:
                acuerdo_value = a.get("value")
                break

        catalogos_set = set()
        for combo in self._stock_combos_data.get("combinaciones", []):
            if acuerdo_value and combo.get("acuerdo", {}).get("value") == acuerdo_value:
                cat = combo.get("catalogo", {})
                if cat.get("text"):
                    catalogos_set.add(cat["text"])

        catalogos = sorted(catalogos_set) if catalogos_set else ["-- Sin catálogos para este acuerdo --"]
        self.option_stock_catalogo.configure(values=catalogos)
        self.option_stock_catalogo.set(catalogos[0])
        # Disparar cascada de categoría
        self._on_stock_catalogo_changed(catalogos[0])

    def _on_stock_catalogo_changed(self, catalogo_text: str):
        acuerdos_data = self._stock_combos_data.get("acuerdos", [])
        acuerdo_sel = self.option_stock_acuerdo.get().strip()
        acuerdo_value = None
        for a in acuerdos_data:
            if a.get("text") == acuerdo_sel:
                acuerdo_value = a.get("value")
                break

        categorias_set = set()
        for combo in self._stock_combos_data.get("combinaciones", []):
            if combo.get("acuerdo", {}).get("value") != acuerdo_value:
                continue
            if combo.get("catalogo", {}).get("text") != catalogo_text:
                continue
            cat = combo.get("categoria", {})
            if cat.get("text"):
                categorias_set.add(cat["text"])

        categorias = sorted(categorias_set) if categorias_set else ["-- Sin categorías para este catálogo --"]
        self.option_stock_categoria.configure(values=categorias)
        self.option_stock_categoria.set(categorias[0])

    def _on_stock_start(self):
        if self._stock_running:
            return
        if not self._stock_excel_df:
            self._append_stock_log("❌ Carga un Excel con productos primero")
            return
        try:
            pausa = float(self.entry_stock_pausa.get() or "2")
        except ValueError:
            pausa = 2.0
        acuerdo = self.option_stock_acuerdo.get().strip()
        catalogo = self.option_stock_catalogo.get().strip()
        categoria = self.option_stock_categoria.get().strip()
        # Credenciales propias de la pestaña 2 (flujo independiente)
        usuario = self.entry_stock_user.get().strip()
        password = self.entry_stock_pass.get().strip()
        if not usuario or not password:
            self._append_stock_log("❌ Credenciales vacías (rellena Usuario y Contraseña)")
            return
        if "Seleccione" in acuerdo or "Sin datos" in acuerdo:
            self._append_stock_log("❌ Selecciona un Acuerdo válido")
            return
        if "Seleccione" in catalogo or "Sin datos" in catalogo:
            self._append_stock_log("❌ Selecciona un Catálogo válido")
            return
        if "Seleccione" in categoria or "Sin datos" in categoria:
            self._append_stock_log("❌ Selecciona una Categoría válida")
            return

        self._stock_running = True
        self._stock_stop_event.clear()
        self.btn_stock_start.configure(state="disabled")
        self.btn_stock_stop.configure(state="normal")
        self.lbl_stock_status.configure(text="En ejecución...", text_color="#f39c12")
        self.lbl_stock_report.configure(text="(en proceso...)", text_color="gray60")

        threading.Thread(
            target=self._execute_stock,
            args=(usuario, password, acuerdo, catalogo, categoria, pausa),
            daemon=True,
        ).start()

    def _on_stock_stop(self):
        if not self._stock_running:
            return
        self._stock_stop_event.set()
        self.lbl_stock_status.configure(text="Deteniendo...", text_color="#e74c3c")
        # ponytail: cerrar el navegador forzosamente para interrumpir operaciones
        # bloqueantes de Playwright (page.wait_for_*, page.click, etc.)
        try:
            if getattr(self, "_stock_browser", None):
                self._stock_browser.close()
        except Exception:
            pass
        self._append_stock_log("⏹ Detención solicitada")

    def _append_stock_log(self, msg):
        ts = time.strftime("%H:%M:%S")
        line = f"[{ts}] {msg}\n"
        try:
            self.log_stock.configure(state="normal")
            self.log_stock.insert("end", line)
            self.log_stock.see("end")
            self.log_stock.configure(state="disabled")
        except Exception:
            pass

    def _execute_stock(self, usuario, password, acuerdo, catalogo, categoria, pausa):
        import workers
        workers.execute_stock(self, usuario, password, acuerdo, catalogo, categoria, pausa)
    def _build_credentials_section(self, parent):
        self._section_label(parent, "Credenciales de Peru Compras", 0)

        frame = ctk.CTkFrame(parent, fg_color="gray10")
        frame.grid(row=1, column=0, padx=12, pady=(0, 10), sticky="ew")
        frame.grid_columnconfigure(0, weight=1)

        # Usuario
        ctk.CTkLabel(
            frame, text="Usuario", font=ctk.CTkFont(size=11),
            text_color="gray60", anchor="w",
        ).grid(row=0, column=0, padx=12, pady=(10, 1), sticky="w")
        self.entry_user = ctk.CTkEntry(frame, placeholder_text="Usuario o RUC", height=34)
        self.entry_user.grid(row=1, column=0, padx=12, pady=(0, 8), sticky="ew")
        self.entry_user.insert(0, "almerco.03")

        # Password
        pass_frame = ctk.CTkFrame(frame, fg_color="transparent")
        pass_frame.grid(row=2, column=0, padx=12, pady=(0, 2), sticky="ew")
        pass_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            pass_frame, text="Contraseña", font=ctk.CTkFont(size=11),
            text_color="gray60", anchor="w",
        ).grid(row=0, column=0, columnspan=2, padx=0, pady=(0, 1), sticky="w")

        self._pw_visible = False
        self.entry_pass = ctk.CTkEntry(
            pass_frame, placeholder_text="Contraseña", show="*", height=34
        )
        self.entry_pass.grid(row=1, column=0, pady=(0, 8), sticky="ew")
        self.entry_pass.insert(0, "4lm3rKenYa@#")
        self.btn_eye = ctk.CTkButton(
            pass_frame, text="▸", width=34, height=34,
            font=ctk.CTkFont(size=14), command=self._toggle_password,
        )
        self.btn_eye.grid(row=1, column=1, padx=(6, 0), pady=(0, 8))

        # Mostrar navegador
        self.check_visible = ctk.CTkCheckBox(
            frame, text="Mostrar navegador en pantalla",
            font=ctk.CTkFont(size=12),
        )
        self.check_visible.grid(row=3, column=0, padx=12, pady=(2, 10), sticky="w")

    def _toggle_password(self):
        self._pw_visible = not self._pw_visible
        self.entry_pass.configure(show="" if self._pw_visible else "*")
        self.btn_eye.configure(text="◂" if self._pw_visible else "▸")

    # ── Excel Section ─────────────────────────────────────────────

    def _build_excel_section(self, parent):
        self._section_label(parent, "Archivo Excel", 2)

        frame = ctk.CTkFrame(parent, fg_color="gray10")
        frame.grid(row=3, column=0, padx=12, pady=(0, 10), sticky="ew")
        frame.grid_columnconfigure(0, weight=1)

        # File picker
        file_row = ctk.CTkFrame(frame, fg_color="transparent")
        file_row.grid(row=0, column=0, padx=12, pady=(10, 4), sticky="ew")
        file_row.grid_columnconfigure(0, weight=1)
        self.btn_file = ctk.CTkButton(
            file_row, text="Seleccionar archivo .xlsx",
            height=32, font=ctk.CTkFont(size=12),
            command=self._pick_excel,
        )
        self.btn_file.pack(side="left")
        self.lbl_file = ctk.CTkLabel(
            file_row, text="Sin archivo", text_color="gray60",
            font=ctk.CTkFont(size=11),
        )
        self.lbl_file.pack(side="left", padx=10)

        # Sheet selector
        ctk.CTkLabel(
            frame, text="Pestaña del Excel", font=ctk.CTkFont(size=11),
            text_color="gray60", anchor="w",
        ).grid(row=1, column=0, padx=12, pady=(4, 1), sticky="w")
        self.combo_sheet = ctk.CTkComboBox(
            frame, values=["Primero cargá un Excel"],
            state="disabled", height=32,
            command=self._on_sheet_changed,
        )
        self.combo_sheet.grid(row=2, column=0, padx=12, pady=(0, 6), sticky="ew")

        # Column mapping — solo N° de Parte
        map_frame = ctk.CTkFrame(frame, fg_color="transparent")
        map_frame.grid(row=3, column=0, padx=12, pady=(4, 4), sticky="ew")
        map_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            map_frame, text="Columna N° de Parte", font=ctk.CTkFont(size=11),
            text_color="gray60", anchor="w",
        ).grid(row=0, column=0, padx=(0, 4), pady=(0, 1), sticky="w")

        self.combo_parte = ctk.CTkComboBox(
            map_frame, values=["--"], state="disabled", height=32,
        )
        self.combo_parte.grid(row=1, column=0, padx=(0, 4), sticky="ew")

        # Info
        self.lbl_excel_info = ctk.CTkLabel(
            frame, text="", font=ctk.CTkFont(size=11),
            text_color="gray60", anchor="w",
        )
        self.lbl_excel_info.grid(row=4, column=0, padx=12, pady=(2, 10), sticky="w")

    def _pick_excel(self):
        path = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Excel", "*.xlsx"), ("Todos", "*.*")],
        )
        if not path:
            return
        try:
            sheets = get_sheets(path)
            if not sheets:
                self.lbl_file.configure(text="Sin pestañas en el Excel", text_color="#e74c3c")
                return

            self._excel_path = path
            name = os.path.basename(path)
            self.lbl_file.configure(text=name, text_color="#5dade2")
            self.combo_sheet.configure(values=sheets, state="readonly")
            self.combo_sheet.set(sheets[0])
            self._on_sheet_changed(sheets[0])
        except Exception as e:
            self.lbl_file.configure(text=f"Error: {e}", text_color="#e74c3c")

    def _on_sheet_changed(self, choice):
        if not self._excel_path or not choice:
            return
        try:
            import openpyxl
            wb = openpyxl.load_workbook(self._excel_path, read_only=True, data_only=True)
            ws = wb[choice]

            # Leer todos los headers de la fila 1 (primeros 20 para cubrir)
            all_headers = []
            # Leer fila 1 como header principal
            row1 = [cell for cell in ws.iter_rows(min_row=1, max_row=1, values_only=True)]
            if row1 and row1[0]:
                for v in row1[0]:
                    if v is not None and str(v).strip():
                        h = str(v).strip()
                        if h not in all_headers and h.lower() not in ("none", ""):
                            all_headers.append(h)
            # Si fila 1 no tiene nada, buscar en filas 2-10
            if not all_headers:
                for row in ws.iter_rows(min_row=2, max_row=10, values_only=True):
                    for v in (row or []):
                        if v is not None and str(v).strip():
                            h = str(v).strip()
                            if h not in all_headers and not h.replace(".","").replace(",","").isdigit():
                                all_headers.append(h)
                    if all_headers:
                        break

            # Si no hay headers, usar columna por defecto
            if not all_headers:
                all_headers = ["Columna A"]

            row_count = ws.max_row or 0
            wb.close()

            # Detectar columna de parte usando el parser (ya corregido)
            cols_detected = detect_columns(self._excel_path, choice)
            parte_col_detect = cols_detected.get("parte_col") or all_headers[0]

            # Parse simple
            rows_data = parse_excel(
                self._excel_path, choice,
                parte_col=parte_col_detect,
            )
            self._excel_rows = rows_data

            opts = ["-- Seleccionar --"] + all_headers
            self.combo_parte.configure(values=opts, state="readonly")
            self.combo_parte.set(parte_col_detect if parte_col_detect in all_headers else opts[0])

            self.lbl_excel_info.configure(
                text=f"{len(rows_data)} filas · {len(all_headers)} cols · Pestaña: {choice}",
                text_color="gray60",
            )
        except Exception as e:
            self.lbl_excel_info.configure(text=f"Error: {e}", text_color="#e74c3c")

    # ── Catalog Section (Cascada Catálogo → Categoría → Estado) ─────

    def _build_catalog_section(self, parent):
        row_offset = 4
        self._section_label(parent, "Configuración del Catálogo (EXT-CE-2022-5)", row_offset)

        frame = ctk.CTkFrame(parent, fg_color="gray10")
        frame.grid(row=row_offset+1, column=0, padx=12, pady=(0, 10), sticky="ew")
        frame.grid_columnconfigure(0, weight=1)

        comb_data = self._catalog_data.get("combinaciones", [])
        if not comb_data:
            ctk.CTkLabel(
                frame,
                text="combinaciones_computadoras.json no encontrado.\nEjecutá extract_combinaciones.py primero",
                text_color="#f39c12", font=ctk.CTkFont(size=11), wraplength=280,
                justify="left",
            ).grid(row=0, column=0, padx=12, pady=10)
            return

        # Catálogo
        ctk.CTkLabel(frame, text="Catálogo Electrónico", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(
            row=0, column=0, padx=12, pady=(8, 1), sticky="w")
        self.combo_catalogo = ctk.CTkComboBox(
            frame, values=self._opts_texts(comb_data), state="readonly", height=32,
            command=self._on_catalogo_changed,
        )
        self.combo_catalogo.grid(row=1, column=0, padx=12, pady=(0, 6), sticky="ew")
        if comb_data:
            self.combo_catalogo.set(self._opts_texts(comb_data)[0])

        # Categoría
        ctk.CTkLabel(frame, text="Categoría", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(
            row=2, column=0, padx=12, pady=(4, 1), sticky="w")
        self.combo_categoria = ctk.CTkComboBox(
            frame, values=["Seleccioná un Catálogo"], state="readonly", height=32,
            command=self._on_categoria_changed,
        )
        self.combo_categoria.grid(row=3, column=0, padx=12, pady=(0, 6), sticky="ew")

        # Estado
        ctk.CTkLabel(frame, text="Estado", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(
            row=4, column=0, padx=12, pady=(4, 1), sticky="w")
        self.combo_estado = ctk.CTkComboBox(
            frame, values=["Seleccioná una Categoría"], state="readonly", height=32,
        )
        self.combo_estado.grid(row=5, column=0, padx=12, pady=(0, 8), sticky="ew")

        # Trigger inicial
        self._on_catalogo_changed(self._opts_texts(comb_data)[0])

    def _opts_texts(self, data):
        return [f"{o['value']} - {o['text'][:60]}" for o in data] if data else []

    def _find_children(self, combo_text):
        val = combo_text.split(" - ")[0].strip() if " - " in combo_text else ""
        comb_data = self._catalog_data.get("combinaciones", [])
        for node in comb_data:
            if node["value"] == val:
                return node.get("children", [])
        return []

    def _on_catalogo_changed(self, choice):
        children = self._find_children(choice)
        texts = self._opts_texts(children)
        if texts:
            self.combo_categoria.configure(values=texts)
            self.combo_categoria.set(texts[0])
            self._on_categoria_changed(texts[0])
        else:
            self.combo_categoria.configure(values=["Sin categorías"])
            self.combo_estado.configure(values=["Sin estados"])

    def _on_categoria_changed(self, choice):
        # Buscar en el nodo actual de catalogo
        cat_val = self.combo_catalogo.get().split(" - ")[0].strip() if " - " in self.combo_catalogo.get() else ""
        comb_data = self._catalog_data.get("combinaciones", [])
        for node in comb_data:
            if node["value"] == cat_val:
                for child in node.get("children", []):
                    val = choice.split(" - ")[0].strip() if " - " in choice else ""
                    if child["value"] == val:
                        estados = child.get("children", [])
                        texts = self._opts_texts(estados)
                        if texts:
                            self.combo_estado.configure(values=texts)
                            self.combo_estado.set(texts[0])
                        else:
                            self.combo_estado.configure(values=["Sin estados"])
                        return
        self.combo_estado.configure(values=["Sin estados"])

    # ── Opciones Section ──────────────────────────────────────────

    def _build_opciones_section(self, parent):
        row_offset = 6
        self._section_label(parent, "Opciones de Procesamiento", row_offset)

        frame = ctk.CTkFrame(parent, fg_color="gray10")
        frame.grid(row=row_offset+1, column=0, padx=12, pady=(0, 10), sticky="ew")
        frame.grid_columnconfigure(0, weight=1)

        # Pausa entre productos
        ctk.CTkLabel(
            frame, text="Pausa entre productos (segundos)",
            font=ctk.CTkFont(size=11), text_color="gray60", anchor="w",
        ).grid(row=0, column=0, padx=12, pady=(10, 1), sticky="w")
        self.slider_pausa = ctk.CTkSlider(frame, from_=0.5, to=5.0, number_of_steps=9)
        self.slider_pausa.grid(row=1, column=0, padx=12, pady=(0, 2), sticky="ew")
        self.slider_pausa.set(1.5)
        self.lbl_pausa = ctk.CTkLabel(
            frame, text="1.5 s", font=ctk.CTkFont(size=11), text_color="gray60",
        )
        self.lbl_pausa.grid(row=2, column=0, padx=12, pady=(0, 6), sticky="w")
        self.slider_pausa.configure(command=lambda v: self.lbl_pausa.configure(text=f"{v:.1f} s"))

        # Separador
        ctk.CTkFrame(frame, height=1, fg_color="gray25").grid(
            row=3, column=0, padx=12, pady=4, sticky="ew"
        )

        # Info de modo
        ctk.CTkLabel(
            frame,
            text="ℹ  Este módulo usa Playwright para subir archivos.\n"
                 "   Los endpoints se ajustan según la sección del portal.",
            font=ctk.CTkFont(size=11),
            text_color="gray50",
            anchor="w",
            justify="left",
        ).grid(row=4, column=0, padx=12, pady=(4, 10), sticky="w")

    # ── Execution Section ─────────────────────────────────────────

    def _build_execution_section(self, parent):
        self._section_label(parent, "Ejecución", 0)

        frame = ctk.CTkFrame(parent, fg_color="gray10")
        frame.grid(row=1, column=0, padx=12, pady=(0, 4), sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(5, weight=1)

        # Status bar
        status_row = ctk.CTkFrame(frame, fg_color="transparent")
        status_row.grid(row=0, column=0, padx=12, pady=(8, 4), sticky="ew")
        self.lbl_status = ctk.CTkLabel(
            status_row, text="Listo para iniciar",
            font=ctk.CTkFont(size=13, weight="bold"),
        )
        self.lbl_status.pack(side="left")
        self.lbl_counter = ctk.CTkLabel(
            status_row, text="", font=ctk.CTkFont(size=12), text_color="gray60",
        )
        self.lbl_counter.pack(side="right")

        # Progress bar
        self.progress = ctk.CTkProgressBar(frame, height=8)
        self.progress.grid(row=2, column=0, padx=12, pady=(0, 4), sticky="ew")
        self.progress.set(0)

        # Resumen de resultados (mini-stats)
        stats_row = ctk.CTkFrame(frame, fg_color="transparent")
        stats_row.grid(row=3, column=0, padx=12, pady=(0, 4), sticky="ew")
        stats_row.grid_columnconfigure((0, 1, 2), weight=1)

        self._stat_ok = self._make_stat(stats_row, "✓  OK", "#2ecc71", 0)
        self._stat_warn = self._make_stat(stats_row, "⚠  No encontrado", "#f39c12", 1)
        self._stat_err = self._make_stat(stats_row, "✗  Error", "#e74c3c", 2)

        # Captcha panel (oculto por defecto)
        self._build_captcha_panel(frame)

        # Log
        self.log_box = ctk.CTkTextbox(frame, wrap="word", font=ctk.CTkFont(family="Courier New", size=11))
        self.log_box.grid(row=5, column=0, padx=12, pady=(2, 8), sticky="nsew")
        self.log_box.configure(state="disabled")
        self.log_box.tag_config("ok",       foreground="#f1c40f")
        self.log_box.tag_config("error",    foreground="#e74c3c")
        self.log_box.tag_config("info",     foreground="#95a5a6")
        self.log_box.tag_config("warn",     foreground="#f39c12")
        self.log_box.tag_config("done",     foreground="#5dade2")
        self.log_box.tag_config("complete", foreground="#2ecc71")
        self.log_box.tag_config("existing", foreground="#3498db")
        self.log_box.tag_config("notfound", foreground="#c0392b")

    def _make_stat(self, parent, label, color, col):
        f = ctk.CTkFrame(parent, fg_color="gray14", corner_radius=6)
        f.grid(row=0, column=col, padx=3, pady=2, sticky="ew")
        lbl_n = ctk.CTkLabel(f, text="0", font=ctk.CTkFont(size=20, weight="bold"), text_color=color)
        lbl_n.pack(pady=(6, 0))
        ctk.CTkLabel(f, text=label, font=ctk.CTkFont(size=10), text_color="gray60").pack(pady=(0, 6))
        return lbl_n

    # ── Captcha Panel ─────────────────────────────────────────────

    def _build_captcha_panel(self, parent):
        self.captcha_panel = ctk.CTkFrame(parent, fg_color="gray14")
        self.captcha_panel.grid(row=4, column=0, padx=12, pady=(0, 4), sticky="ew")
        self.captcha_panel.grid_remove()
        self.captcha_panel.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.captcha_panel,
            text="CAPTCHA — Ingresá el código",
            font=ctk.CTkFont(size=12, weight="bold"), anchor="w",
        ).grid(row=0, column=0, padx=8, pady=(6, 4), sticky="w")

        self.captcha_img_lbl = ctk.CTkLabel(self.captcha_panel, text="")
        self.captcha_img_lbl.grid(row=1, column=0, padx=8, pady=(0, 4))

        cap_row = ctk.CTkFrame(self.captcha_panel, fg_color="transparent")
        cap_row.grid(row=2, column=0, padx=8, pady=(0, 8), sticky="ew")
        cap_row.grid_columnconfigure(0, weight=1)

        self.captcha_entry = ctk.CTkEntry(cap_row, placeholder_text="Código", height=30)
        self.captcha_entry.grid(row=0, column=0, padx=(0, 6), sticky="ew")
        self.captcha_entry.bind("<Return>", lambda e: self._on_captcha_submit())

        ctk.CTkButton(
            cap_row, text="Enviar", width=60, height=30,
            command=self._on_captcha_submit,
        ).grid(row=0, column=1)

        self._captcha_img = None

    def _show_captcha(self, image_bytes):
        img = Image.open(BytesIO(image_bytes))
        img = img.resize((250, 66), Image.LANCZOS)
        self._captcha_img = ctk.CTkImage(light_image=img, dark_image=img, size=(250, 66))
        self.captcha_img_lbl.configure(image=self._captcha_img)
        self.captcha_entry.delete(0, "end")
        self.captcha_entry.focus_set()
        self.captcha_panel.grid()

    def _hide_captcha_panel(self):
        self.captcha_panel.grid_remove()

    def _on_captcha_submit(self):
        code = self.captcha_entry.get().strip()
        if code:
            self.captcha_bridge.respond(code)
            self._hide_captcha_panel()
            self._log("CAPTCHA manual: " + code, "info")

    # ── Helpers ───────────────────────────────────────────────────

    def _section_label(self, parent, text, row):
        ctk.CTkLabel(
            parent, text=text,
            font=ctk.CTkFont(size=14, weight="bold"), anchor="w",
        ).grid(row=row, column=0, padx=12, pady=(8, 4), sticky="w")

    def _log(self, msg, level="info"):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", msg + "\n", level)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")
        self._log_lines.append({"level": level, "msg": msg})

    # ── Test Flow ──────────────────────────────────────────────

    def _on_test(self):
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return

        if not hasattr(self, 'combo_catalogo') or not self._catalog_data:
            self.lbl_status.configure(text="No hay datos de catálogo cargados", text_color="#e74c3c")
            return

        headless = not bool(self.check_visible.get())

        def _val(combo):
            t = combo.get()
            return t.split(" - ")[0].strip() if " - " in t else ""

        pre_selected = {
            "acuerdo": "249",
            "catalogo": _val(self.combo_catalogo),
            "categoria": _val(self.combo_categoria),
            "estado": _val(self.combo_estado),
        }

        self._running = True
        self._log_lines.clear()
        self.stop_event.clear()
        self.captcha_bridge.stop_event = self.stop_event
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self.progress.set(0)
        self.lbl_status.configure(text="🧪 Test Flow en marcha...", text_color="#f39c12")
        self.btn_launch.configure(state="disabled")
        self.btn_test.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        self._hide_captcha_panel()

        threading.Thread(
            target=self._execute_test,
            args=(user, pwd, headless, pre_selected),
            daemon=True,
        ).start()

    def _on_certs_only(self):
        """Handler del botón 'Solo Certificaciones': entra a cada ficha y agrega ISO 9001/14001."""
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return
        if not self._excel_rows or not self._excel_path:
            self.lbl_status.configure(text="Cargá un Excel antes de iniciar", text_color="#e74c3c")
            return
        if not hasattr(self, 'combo_catalogo') or not self._catalog_data:
            self.lbl_status.configure(text="No hay datos de catálogo cargados", text_color="#e74c3c")
            return

        headless = not bool(self.check_visible.get())

        def _val(combo):
            t = combo.get()
            return t.split(" - ")[0].strip() if " - " in t else ""

        pre_selected = {
            "acuerdo": "249",
            "catalogo": _val(self.combo_catalogo),
            "categoria": _val(self.combo_categoria),
            "estado": _val(self.combo_estado),
        }

        self._running = True
        self._log_lines.clear()
        self.stop_event.clear()
        self.captcha_bridge.stop_event = self.stop_event
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self.progress.set(0)
        self.lbl_status.configure(text="🏅 Solo Certificaciones en marcha...", text_color="#8e44ad")
        self.btn_launch.configure(state="disabled")
        self.btn_test.configure(state="disabled")
        self.btn_certs.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        self._hide_captcha_panel()

        threading.Thread(
            target=self._execute_certs_only,
            args=(user, pwd, headless, pre_selected),
            daemon=True,
        ).start()

    def _on_extract(self):
        """Handler del botón 'Extraer Reportes': descarga reportes de Producto Ofertado."""
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return

        headless = not bool(self.check_visible.get())

        self._running = True
        self._log_lines.clear()
        self.stop_event.clear()
        self.captcha_bridge.stop_event = self.stop_event
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self.progress.set(0)
        self.lbl_status.configure(text="📊 Extrayendo reportes...", text_color="#3498db")
        self.btn_launch.configure(state="disabled")
        self.btn_test.configure(state="disabled")
        self.btn_certs.configure(state="disabled")
        self.btn_nro.configure(state="disabled")
        self.btn_extract.configure(state="disabled")
        self.btn_compare.configure(state="disabled")
        self.btn_discovery.configure(state="disabled")
        self.btn_discovery2.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        self._hide_captcha_panel()

        threading.Thread(
            target=self._execute_extract,
            args=(user, pwd, headless),
            daemon=True,
        ).start()
    def _execute_extract(self, usuario, password, headless):
        import workers
        workers.execute_extract(self, usuario, password, headless)
    def _execute_certs_only(self, usuario, password, headless, pre_selected):
        import workers
        workers.execute_certs_only(self, usuario, password, headless, pre_selected)
    def _on_nro_parte(self):
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return
        if not self._excel_rows or not self._excel_path:
            self.lbl_status.configure(text="Cargá un Excel antes de iniciar", text_color="#e74c3c")
            return

        headless = not bool(self.check_visible.get())

        def _val(combo):
            t = combo.get()
            return t.split(" - ")[0].strip() if " - " in t else ""

        pre_selected = {
            "acuerdo": "249",
            "catalogo": _val(self.combo_catalogo),
            "categoria": _val(self.combo_categoria),
            "estado": _val(self.combo_estado),
        }

        self._running = True
        self._log_lines.clear()
        self.stop_event.clear()
        self.captcha_bridge.stop_event = self.stop_event
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self.progress.set(0)
        self.lbl_status.configure(text="🏷️ Solo N° de Parte en marcha...", text_color="#d35400")
        self.btn_launch.configure(state="disabled")
        self.btn_test.configure(state="disabled")
        self.btn_certs.configure(state="disabled")
        self.btn_nro.configure(state="disabled")
        self.btn_extract.configure(state="disabled")
        self.btn_compare.configure(state="disabled")
        self.btn_discovery.configure(state="disabled")
        self.btn_discovery2.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        self._hide_captcha_panel()

        threading.Thread(
            target=self._execute_nro_parte,
            args=(user, pwd, headless, pre_selected),
            daemon=True,
        ).start()

    def _execute_nro_parte(self, usuario, password, headless, pre_selected):
        import workers
        workers.execute_nro_parte(self, usuario, password, headless, pre_selected)
    def _on_compare(self):
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return
        if not self._excel_rows or not self._excel_path:
            self.lbl_status.configure(text="Cargá un Excel antes de iniciar", text_color="#e74c3c")
            return

        headless = not bool(self.check_visible.get())
        def _val(combo):
            t = combo.get()
            return t.split(" - ")[0].strip() if " - " in t else ""
        pre_selected = {
            "acuerdo": _val(self.combo_acuerdo) if hasattr(self, "combo_acuerdo") else "249",
            "catalogo": _val(self.combo_catalogo),
            "categoria": _val(self.combo_categoria),
            "estado": _val(self.combo_estado),
        }

        self._running = True
        self._log_lines.clear()
        self.stop_event.clear()
        self.captcha_bridge.stop_event = self.stop_event
        self.log_box.configure(state="normal"); self.log_box.delete("1.0", "end"); self.log_box.configure(state="disabled")
        self.progress.set(0)
        self.lbl_status.configure(text="🔍 Comparando fichas...", text_color="#16a085")
        for b in ("launch", "test", "certs", "nro", "extract", "compare"):
            getattr(self, f"btn_{b}").configure(state="disabled")
        self.btn_stop.configure(state="normal")
        self._hide_captcha_panel()

        threading.Thread(
            target=self._execute_compare,
            args=(user, pwd, headless, pre_selected),
            daemon=True,
        ).start()

    def _execute_compare(self, usuario, password, headless, pre_selected):
        import workers
        workers.execute_compare(self, usuario, password, headless, pre_selected)
    def _on_discovery(self):
        """Handler del botón 'Discovery': ejecuta el script discovery_perucompras.py."""
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return
        headless = not bool(self.check_visible.get())
        self._running = True
        self._log_lines.clear()
        self.stop_event.clear()
        self.captcha_bridge.stop_event = self.stop_event
        self.log_box.configure(state="normal"); self.log_box.delete("1.0", "end"); self.log_box.configure(state="disabled")
        self.progress.set(0)
        self.lbl_status.configure(text="🕵️ Discovery en marcha...", text_color="#2c3e50")
        for b in ("launch", "test", "certs", "nro", "extract", "compare", "discovery"):
            try: getattr(self, f"btn_{b}").configure(state="disabled")
            except AttributeError: pass
        self.btn_stop.configure(state="normal")
        self._hide_captcha_panel()
        threading.Thread(
            target=self._execute_discovery, args=(user, pwd, headless),
            daemon=True,
        ).start()

    def _execute_discovery(self, usuario, password, headless):
        import workers
        workers.execute_discovery(self, usuario, password, headless)
    def _on_discovery2(self):
        """Handler del botón 'Discovery v2': scraping profundo multi-técnica."""
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return
        headless = not bool(self.check_visible.get())
        self._running = True
        self._log_lines.clear()
        self.stop_event.clear()
        self.captcha_bridge.stop_event = self.stop_event
        self.log_box.configure(state="normal"); self.log_box.delete("1.0", "end"); self.log_box.configure(state="disabled")
        self.progress.set(0)
        self.lbl_status.configure(text="🕵️ v2 en marcha...", text_color="#566573")
        for b in ("launch", "test", "certs", "nro", "extract", "compare", "discovery", "discovery2"):
            try: getattr(self, f"btn_{b}").configure(state="disabled")
            except AttributeError: pass
        self.btn_stop.configure(state="normal")
        self._hide_captcha_panel()
        threading.Thread(
            target=self._execute_discovery2, args=(user, pwd, headless),
            daemon=True,
        ).start()

    def _execute_discovery2(self, usuario, password, headless):
        import workers
        workers.execute_discovery2(self, usuario, password, headless)
    def _execute_test(self, usuario, password, headless, pre_selected):
        import workers
        workers.execute_test(self, usuario, password, headless, pre_selected)
    def _on_launch(self):
        user = self.entry_user.get().strip()
        pwd  = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return

        if not self._excel_rows or not self._excel_path:
            self.lbl_status.configure(
                text="Cargá un Excel antes de iniciar el procesamiento",
                text_color="#e74c3c",
            )
            return

        # Usar las mismas filas que el Test Flow (ya parseadas con la columna auto-detectada)
        rows = self._excel_rows

        if not rows:
            self.lbl_status.configure(text="El Excel no tiene filas de datos", text_color="#e74c3c")
            return

        self._running = True
        self._ok = 0
        self._errors = 0
        self._total = len(rows)
        self._log_lines.clear()
        self.stop_event.clear()
        self.captcha_bridge.stop_event = self.stop_event

        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")

        self.progress.set(0)
        self._stat_ok.configure(text="0")
        self._stat_warn.configure(text="0")
        self._stat_err.configure(text="0")
        self.lbl_status.configure(text="Iniciando...", text_color="white")
        self.btn_launch.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        self.btn_certs.configure(state="disabled")
        self._hide_captcha_panel()

        headless = not bool(self.check_visible.get())
        pausa    = self.slider_pausa.get()

        # Valores de los dropdowns en cascada
        def _val(combo):
            t = combo.get()
            return t.split(" - ")[0].strip() if " - " in t else ""

        acuerdo_data = self._catalog_data.get("acuerdo", {})
        pre_selected = {
            "acuerdo": acuerdo_data.get("value", "249"),
            "catalogo": _val(self.combo_catalogo),
            "categoria": _val(self.combo_categoria),
            "estado": _val(self.combo_estado),
        }

        threading.Thread(
            target=self._execute,
            args=(user, pwd, headless, rows, pausa, pre_selected),
            daemon=True,
        ).start()

    def _execute(self, usuario, password, headless, rows, pausa, pre_selected=None):
        import workers
        workers.execute(self, usuario, password, headless, rows, pausa, pre_selected)
    def _on_stop(self):
        self.stop_event.set()
        self._running = False
        self.btn_stop.configure(state="disabled", text="Deteniendo...")
        self._log("Detención solicitada", "warn")
        self.after(3000, self._reset_after_stop)

    def _reset_after_stop(self):
        self.btn_launch.configure(state="normal")
        self.btn_stop.configure(state="disabled", text="■  Detener")
        self.btn_test.configure(state="normal")
        self.btn_certs.configure(state="normal")
        self.btn_nro.configure(state="normal")
        self.btn_extract.configure(state="normal")
        self.btn_compare.configure(state="normal")
        self.btn_discovery.configure(state="normal")
        self.btn_discovery2.configure(state="normal")
        self.lbl_status.configure(text="Detenido — listo para iniciar", text_color="#f39c12")

    # ── Queue Polling ─────────────────────────────────────────────

    def poll_queue(self):
        try:
            while True:
                item = self.log_queue.get_nowait()
                t = item.get("type") if isinstance(item, dict) else None

                if t == "log":
                    self._log(item.get("msg", ""), item.get("level", "info"))
                elif t == "progress":
                    cur = item.get("current", 0)
                    tot = item.get("total", 1)
                    self.lbl_status.configure(text=f"Procesando producto {cur} de {tot}")
                    self.lbl_counter.configure(text=f"{cur}/{tot}")
                    self.progress.set(cur / tot if tot > 0 else 0)
                elif t == "stat_ok":
                    self._stat_ok.configure(text=str(item.get("value", 0)))
                elif t == "stat_warn":
                    self._stat_warn.configure(text=str(item.get("value", 0)))
                elif t == "stat_err":
                    self._stat_err.configure(text=str(item.get("value", 0)))
                elif t == "done":
                    ok  = item.get("ok", 0)
                    err = item.get("errors", 0)
                    self._running = False
                    self.lbl_status.configure(
                        text=f"Finalizado  ·  {ok} OK  ·  {err} errores"
                    )
                    self.progress.set(1)
                    self.btn_launch.configure(state="normal")
                    self.btn_stop.configure(state="disabled", text="■  Detener")

                # Compatibilidad con LogWriter que usa tuplas (level, msg)
                elif isinstance(item, tuple) and len(item) == 2:
                    level, msg = item
                    level_map = {
                        "OK": "ok", "ERROR": "error",
                        "WARN": "warn", "DONE": "done", "INFO": "info",
                    }
                    tag = level_map.get(level, "info")

                    if level == "DONE":
                        self._running = False
                        self.lbl_status.configure(text=msg)
                        self.progress.set(1)
                        self.btn_launch.configure(state="normal")
                        self.btn_stop.configure(state="disabled", text="■  Detener")
                    else:
                        self._log(msg, tag)

        except queue.Empty:
            pass

        # Verificar bridge de captcha
        with self.captcha_bridge.lock:
            if (
                self.captcha_bridge.image_bytes is not None
                and not self.captcha_bridge.event.is_set()
            ):
                self._show_captcha(self.captcha_bridge.image_bytes)

        self.after(200, self.poll_queue)


# ═══════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app = SubirPdfApp()
    app.mainloop()

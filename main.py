import sys, os, queue, threading, csv, time, json
from io import BytesIO
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

# ── Paths ────────────────────────────────────────────────────────
if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from automation.browser import init_browser, close_browser
from automation.login import do_login
from automation.navigation import setup_catalog_search
from automation.offer_loop import run_offer_loop
from utils.excel_parser import get_sheets, get_columns, parse_excel
from utils.excel_writer import write_results
from utils.logger import LogWriter

# ═══════════════════════════════════════════════════════════════════
#  BRIDGES (Comunicación UI ↔ Automation Thread)
# ═══════════════════════════════════════════════════════════════════

class CaptchaBridge:
    def __init__(self):
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.image_bytes = None
        self.user_code = ""
    def request(self, img):
        with self.lock: self.image_bytes = img; self.user_code = ""; self.event.clear()
        self.event.wait()
        with self.lock: return self.user_code
    def respond(self, code):
        with self.lock: self.user_code = code; self.image_bytes = None
        self.event.set()

class CatalogBridge:
    def __init__(self):
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.step = ""; self.options = []; self.selection = ""
    def request_step(self, step, opts):
        with self.lock: self.step = step; self.options = opts; self.selection = ""; self.event.clear()
        self.event.wait()
        with self.lock: return self.selection
    def respond_step(self, val):
        with self.lock: self.selection = val; self.options = []
        self.event.set()


# ═══════════════════════════════════════════════════════════════════
#  APP PRINCIPAL — Single Screen
# ═══════════════════════════════════════════════════════════════════

class PeruComprasApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Peru Compras Bot")
        self.geometry("960x760")
        self.minsize(820, 640)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.log_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.captcha_bridge = CaptchaBridge()
        self.catalog_bridge = CatalogBridge()
        self._running = False
        self._log_lines = []
        self._ok = 0; self._errors = 0; self._total = 0

        self._build_ui()
        self.poll_queue()

    # ── Build UI ──────────────────────────────────────────────────

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        # ── HEADER ──
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, padx=20, pady=(16, 4), sticky="ew")
        ctk.CTkLabel(header, text="Peru Compras Bot",
                     font=ctk.CTkFont(size=22, weight="bold")).pack(side="left")
        ctk.CTkLabel(header, text="Automatización de ofertas",
                     font=ctk.CTkFont(size=12), text_color="gray60").pack(side="left", padx=12)

        # ── MAIN CONTENT ──
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, padx=20, pady=(0, 8), sticky="nsew")
        content.grid_columnconfigure(0, weight=1, minsize=340)
        content.grid_columnconfigure(1, weight=1, minsize=340)
        content.grid_rowconfigure(0, weight=1)

        # LEFT COLUMN
        left = ctk.CTkScrollableFrame(content, fg_color="transparent")
        left.grid(row=0, column=0, padx=(0, 6), sticky="nsew")
        left.grid_columnconfigure(0, weight=1)

        self._build_credentials_section(left)
        self._build_excel_section(left)
        self._build_catalog_section(left)

        # Cargar opciones de catalogo desde JSON (si existe)
        self._catalog_data = None
        self._load_catalog_json()

        # RIGHT COLUMN
        right = ctk.CTkFrame(content)
        right.grid(row=0, column=1, padx=(6, 0), sticky="nsew")
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(0, weight=1)

        self._build_execution_section(right)

        # ── FOOTER ──
        footer = ctk.CTkFrame(self, fg_color="transparent")
        footer.grid(row=2, column=0, padx=20, pady=(4, 12), sticky="ew")
        footer.grid_columnconfigure(0, weight=1)

        self.btn_launch = ctk.CTkButton(
            footer, text="▶ Iniciar Procesamiento", height=42,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self._on_launch
        )
        self.btn_launch.pack(side="right", padx=(8, 0))

        self.btn_stop = ctk.CTkButton(
            footer, text="■ Detener", height=42, fg_color="#c0392b",
            hover_color="#96281b", state="disabled",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._on_stop
        )
        self.btn_stop.pack(side="right", padx=8)

    # ── Credentials Section ───────────────────────────────────────

    def _build_credentials_section(self, parent):
        self._section_label(parent, "Credenciales de Peru Compras", 0)

        frame = ctk.CTkFrame(parent, fg_color="gray10")
        frame.grid(row=1, column=0, padx=12, pady=(0, 10), sticky="ew")
        frame.grid_columnconfigure(0, weight=1)

        # Usuario
        ctk.CTkLabel(frame, text="Usuario", font=ctk.CTkFont(size=11), text_color="gray60",
                     anchor="w").grid(row=0, column=0, padx=12, pady=(10, 1), sticky="w")
        self.entry_user = ctk.CTkEntry(frame, placeholder_text="Usuario o RUC", height=34)
        self.entry_user.grid(row=1, column=0, padx=12, pady=(0, 8), sticky="ew")
        self.entry_user.insert(0, "estalin.huamali01")

        # Password row
        pass_frame = ctk.CTkFrame(frame, fg_color="transparent")
        pass_frame.grid(row=2, column=0, padx=12, pady=(0, 2), sticky="ew")
        pass_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(pass_frame, text="Contraseña", font=ctk.CTkFont(size=11), text_color="gray60",
                     anchor="w").grid(row=0, column=0, columnspan=2, padx=0, pady=(0, 1), sticky="w")
        self._pw_visible = False
        self.entry_pass = ctk.CTkEntry(pass_frame, placeholder_text="Contraseña", show="*", height=34)
        self.entry_pass.grid(row=1, column=0, pady=(0, 8), sticky="ew")
        self.entry_pass.insert(0, "PE/CyG6c&1R4T=")
        self.btn_eye = ctk.CTkButton(pass_frame, text="▸", width=34, height=34,
                                     font=ctk.CTkFont(size=14), command=self._toggle_password)
        self.btn_eye.grid(row=1, column=1, padx=(6, 0), pady=(0, 8))

        # Checkbox
        self.check_visible = ctk.CTkCheckBox(frame, text="Mostrar navegador en pantalla",
                                             font=ctk.CTkFont(size=12))
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
        self.btn_file = ctk.CTkButton(file_row, text="Seleccionar archivo .xlsx",
                                      height=32, font=ctk.CTkFont(size=12),
                                      command=self._pick_excel)
        self.btn_file.pack(side="left")
        self.lbl_file = ctk.CTkLabel(file_row, text="Sin archivo", text_color="gray60",
                                     font=ctk.CTkFont(size=11))
        self.lbl_file.pack(side="left", padx=10)

        # Sheet selector
        ctk.CTkLabel(frame, text="Pestaña del Excel", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(row=1, column=0, padx=12,
                     pady=(4, 1), sticky="w")
        self.combo_sheet = ctk.CTkComboBox(frame, values=["Primero cargá un Excel"],
                                           state="disabled", height=32,
                                           command=self._on_sheet_changed)
        self.combo_sheet.grid(row=2, column=0, padx=12, pady=(0, 6), sticky="ew")

        # Column mapping
        map_frame = ctk.CTkFrame(frame, fg_color="transparent")
        map_frame.grid(row=3, column=0, padx=12, pady=(4, 4), sticky="ew")
        map_frame.grid_columnconfigure(0, weight=1)
        map_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(map_frame, text="Columna N° de Parte", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(row=0, column=0, padx=(0, 6), pady=(0, 1), sticky="w")
        ctk.CTkLabel(map_frame, text="Columna de Precio", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(row=0, column=1, padx=(6, 0), pady=(0, 1), sticky="w")
        self.combo_parte = ctk.CTkComboBox(map_frame, values=["--"], state="disabled", height=32)
        self.combo_parte.grid(row=1, column=0, padx=(0, 6), sticky="ew")
        self.combo_precio = ctk.CTkComboBox(map_frame, values=["--"], state="disabled", height=32)
        self.combo_precio.grid(row=1, column=1, padx=(6, 0), sticky="ew")

        # Info
        self.lbl_excel_info = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=11),
                                           text_color="gray60", anchor="w")
        self.lbl_excel_info.grid(row=4, column=0, padx=12, pady=(2, 10), sticky="w")

    def _pick_excel(self):
        path = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Excel", "*.xlsx"), ("Todos", "*.*")]
        )
        if not path:
            return
        try:
            sheets = get_sheets(path)
            if not sheets:
                self.lbl_file.configure(text="Sin pestañas en el Excel", text_color="#e74c3c")
                return

            self._excel_path = path
            self._excel_sheets = sheets

            name = os.path.basename(path)
            self.lbl_file.configure(text=name, text_color="#5dade2")
            self.combo_sheet.configure(values=sheets, state="readonly")
            self.combo_sheet.set(sheets[0])
            self._on_sheet_changed(sheets[0])
        except Exception as e:
            self.lbl_file.configure(text="Error: %s" % e, text_color="#e74c3c")

    def _on_sheet_changed(self, choice):
        path = getattr(self, '_excel_path', None)
        if not path or not choice:
            return
        try:
            cols = get_columns(path, choice)
            rows = parse_excel(path, choice)
            self._excel_rows = rows
            self._excel_columns = cols

            opts = ["-- Seleccionar --"] + cols
            self.combo_parte.configure(values=opts, state="readonly")
            parte_found = False
            for col in cols:
                cl = col.lower()
                for g in ["part number", "n° de parte", "nro.parte", "nro. parte",
                          "código único", "codigo unico"]:
                    if g in cl:
                        self.combo_parte.set(col)
                        parte_found = True
                        break
                if parte_found:
                    break
            if not parte_found:
                self.combo_parte.set(opts[0])

            self.combo_precio.configure(values=opts, state="readonly")
            precio_found = False
            for col in cols:
                cl = col.lower()
                for g in ["precio de lista", "precios de lista",
                          "precio referencial", "precio unitario",
                          "precio"]:
                    if g in cl:
                        self.combo_precio.set(col)
                        precio_found = True
                        break
                if precio_found:
                    break
            if not precio_found:
                self.combo_precio.set(opts[0])

            self.lbl_excel_info.configure(
                text="%s filas · %s · Pestaña: %s" % (len(rows), "%d cols" % len(cols), choice))
        except Exception as e:
            self.lbl_excel_info.configure(text="Error: %s" % e, text_color="#e74c3c")

    # ── Catalog Section (Dropdowns en cascada) ─────────────────────

    def _build_catalog_section(self, parent):
        self._section_label(parent, "Configuracion del Catalogo", 4)

        frame = ctk.CTkFrame(parent, fg_color="gray10")
        frame.grid(row=5, column=0, padx=12, pady=(0, 10), sticky="ew")
        frame.grid_columnconfigure(0, weight=1)

        # Acuerdo Marco
        ctk.CTkLabel(frame, text="Acuerdo Marco", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(row=0, column=0, padx=12, pady=(10, 1), sticky="w")
        self.combo_acuerdo = ctk.CTkComboBox(frame, values=["Ejecuta extract_catalog.py primero"],
                                             state="readonly", height=32,
                                             command=self._on_acuerdo_changed)
        self.combo_acuerdo.grid(row=1, column=0, padx=12, pady=(0, 6), sticky="ew")

        # Catalogo Electronico
        ctk.CTkLabel(frame, text="Catalogo Electronico", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(row=2, column=0, padx=12, pady=(4, 1), sticky="w")
        self.combo_catalogo = ctk.CTkComboBox(frame, values=["Selecciona un Acuerdo Marco"],
                                              state="readonly", height=32,
                                              command=self._on_catalogo_changed)
        self.combo_catalogo.grid(row=3, column=0, padx=12, pady=(0, 6), sticky="ew")

        # Categoria
        ctk.CTkLabel(frame, text="Categoria", font=ctk.CTkFont(size=11),
                     text_color="gray60", anchor="w").grid(row=4, column=0, padx=12, pady=(4, 1), sticky="w")
        self.combo_categoria = ctk.CTkComboBox(frame, values=["Selecciona un Catalogo"],
                                               state="readonly", height=32)
        self.combo_categoria.grid(row=5, column=0, padx=12, pady=(0, 10), sticky="ew")

    # ── Carga de catalog_options.json ──────────────────────────

    def _load_catalog_json(self):
        json_path = os.path.join(BASE_DIR, "catalog_options.json")
        if not os.path.isfile(json_path):
            return
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                self._catalog_data = json.load(f)
            # Poblar Acuerdo Marco
            acuerdos = self._catalog_data.get("acuerdos", [])
            if acuerdos:
                texts = ["%s - %s" % (a["value"], a["text"][:65]) for a in acuerdos]
                self.combo_acuerdo.configure(values=texts)
                self.combo_acuerdo.set(texts[0])
                self.combo_catalogo.configure(state="readonly")
                self.combo_categoria.configure(state="readonly")
        except Exception as e:
            print("Error cargando catalog_options.json:", e)

    def _on_acuerdo_changed(self, choice):
        if not self._catalog_data:
            return
        val = choice.split(" - ")[0].strip()
        catalogos = self._catalog_data.get("catalogos", {}).get(val, [])
        if catalogos:
            texts = ["%s - %s" % (c["value"], c["text"][:65]) for c in catalogos]
            self.combo_catalogo.configure(values=texts)
            self.combo_catalogo.set(texts[0])
            # Trigger cascada a categorias
            self._on_catalogo_changed(texts[0])
        else:
            self.combo_catalogo.configure(values=["Sin catalogos"])
            self.combo_categoria.configure(values=["Sin categorias"])

    def _on_catalogo_changed(self, choice):
        if not self._catalog_data:
            return
        val = choice.split(" - ")[0].strip() if " - " in choice else ""
        categorias = self._catalog_data.get("categorias", {}).get(val, [])
        if categorias:
            texts = ["%s - %s" % (c["value"], c["text"][:65]) for c in categorias]
            self.combo_categoria.configure(values=texts)
            self.combo_categoria.set(texts[0])
        else:
            self.combo_categoria.configure(values=["Sin categorias"])

    # ── Execution Section ─────────────────────────────────────────

    def _build_execution_section(self, parent):
        self._section_label(parent, "Ejecución", 0)

        frame = ctk.CTkFrame(parent, fg_color="gray10")
        frame.grid(row=1, column=0, padx=12, pady=(0, 4), sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        # Status bar
        status_row = ctk.CTkFrame(frame, fg_color="transparent")
        status_row.grid(row=0, column=0, padx=12, pady=(8, 4), sticky="ew")
        self.lbl_status = ctk.CTkLabel(status_row, text="Listo para iniciar",
                                       font=ctk.CTkFont(size=13, weight="bold"))
        self.lbl_status.pack(side="left")
        self.lbl_counter = ctk.CTkLabel(status_row, text="", font=ctk.CTkFont(size=12),
                                        text_color="gray60")
        self.lbl_counter.pack(side="right")

        # Progress
        self.progress = ctk.CTkProgressBar(frame, height=8)
        self.progress.grid(row=2, column=0, padx=12, pady=(0, 4), sticky="ew")
        self.progress.set(0)

        # Log (creado primero para que exista antes que los paneles)
        self.log_box = ctk.CTkTextbox(frame, wrap="word", font=ctk.CTkFont(size=11))
        self.log_box.grid(row=5, column=0, padx=12, pady=(2, 8), sticky="nsew")
        self.log_box.configure(state="disabled")
        self.log_box.tag_config("ok", foreground="#2ecc71")
        self.log_box.tag_config("error", foreground="#e74c3c")
        self.log_box.tag_config("info", foreground="#95a5a6")
        self.log_box.tag_config("warn", foreground="#f39c12")
        frame.grid_rowconfigure(5, weight=1)

        # Catalog panel (oculto) - only captcha stays in execution
        self._build_captcha_panel(frame)

    # ── Captcha Panel ─────────────────────────────────────────────

    def _build_captcha_panel(self, parent):
        self.captcha_panel = ctk.CTkFrame(parent, fg_color="gray14")
        self.captcha_panel.grid(row=4, column=0, padx=12, pady=(0, 4), sticky="ew")
        self.captcha_panel.grid_remove()
        self.captcha_panel.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.captcha_panel, text="CAPTCHA — Ingresá el código",
                     font=ctk.CTkFont(size=12, weight="bold"), anchor="w").grid(
            row=0, column=0, padx=8, pady=(6, 4), sticky="w")
        self.captcha_img_lbl = ctk.CTkLabel(self.captcha_panel, text="")
        self.captcha_img_lbl.grid(row=1, column=0, padx=8, pady=(0, 4))
        cap_row = ctk.CTkFrame(self.captcha_panel, fg_color="transparent")
        cap_row.grid(row=2, column=0, padx=8, pady=(0, 8), sticky="ew")
        cap_row.grid_columnconfigure(0, weight=1)
        self.captcha_entry = ctk.CTkEntry(cap_row, placeholder_text="Código", height=30)
        self.captcha_entry.grid(row=0, column=0, padx=(0, 6), sticky="ew")
        self.captcha_entry.bind("<Return>", lambda e: self._on_captcha_submit())
        ctk.CTkButton(cap_row, text="Enviar", width=60, height=30,
                      command=self._on_captcha_submit).grid(row=0, column=1)
        self._captcha_img = None

    def _show_captcha(self, image_bytes):
        img = Image.open(BytesIO(image_bytes))
        img = img.resize((250, 66), Image.LANCZOS)
        self._captcha_img = ctk.CTkImage(light_image=img, dark_image=img, size=(250, 66))
        self.captcha_img_lbl.configure(image=self._captcha_img)
        self.captcha_entry.delete(0, "end")
        self.captcha_entry.focus_set()
        self.captcha_panel.grid()
        self.log_box.configure(height=100)

    def _hide_captcha_panel(self):
        self.captcha_panel.grid_remove()
        self.log_box.configure(height=180)

    def _on_captcha_submit(self):
        code = self.captcha_entry.get().strip()
        if code:
            self.captcha_bridge.respond(code)
            self._hide_captcha_panel()
            self._log("CAPTCHA manual: " + code, "info")

    def _populate_catalog_step(self, step, options):
        pass

    # ── Helpers ───────────────────────────────────────────────────

    def _section_label(self, parent, text, row):
        ctk.CTkLabel(parent, text=text, font=ctk.CTkFont(size=14, weight="bold"),
                     anchor="w").grid(row=row, column=0, padx=12, pady=(8, 4), sticky="w")

    def _log(self, msg, level="info"):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", msg + "\n", level)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")
        self._log_lines.append({"level": level, "msg": msg})

    # ── Launch / Stop ─────────────────────────────────────────────

    def _on_launch(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pass.get().strip()
        if not user or not pwd:
            self.lbl_status.configure(text="Ingresá usuario y contraseña", text_color="#e74c3c")
            return
        parte = self.combo_parte.get()
        precio = self.combo_precio.get()
        sheet = self.combo_sheet.get()
        if (parte == "-- Seleccionar --" or precio == "-- Seleccionar --"
                or sheet == "Primero cargá un Excel"
                or not hasattr(self, '_excel_rows')
                or not self._excel_rows):
            self.lbl_status.configure(text="Cargá un Excel, elegí pestaña y columnas", text_color="#e74c3c")
            return

        self._running = True
        self._ok = 0; self._errors = 0; self._total = 0
        self._log_lines.clear()
        self.stop_event.clear()

        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")

        self.progress.set(0)
        self.lbl_status.configure(text="Iniciando...", text_color="white")
        self.btn_launch.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        self._hide_captcha_panel()

        # Leer seleccion pre-elegida del catalogo
        def _sel(combo):
            t = combo.get()
            return t.split(" - ")[0].strip() if " - " in t else ""

        pre_selected = {
            "acuerdo": _sel(self.combo_acuerdo),
            "catalogo": _sel(self.combo_catalogo),
            "categoria": _sel(self.combo_categoria),
        }

        creds = {
            "usuario": user, "password": pwd,
            "captcha_key": "", "headless": not self.check_visible.get(),
        }
        excel_data = {
            "rows": self._excel_rows,
            "parte_col": parte,
            "precio_col": precio,
            "path": self._excel_path,
            "sheet": sheet,
        }

        threading.Thread(target=self._execute, args=(creds, excel_data, pre_selected), daemon=True).start()

    def _execute(self, creds, data, pre_selected):
        log = LogWriter(self.log_queue)
        stop = self.stop_event
        pw = browser = None
        try:
            log.info("Iniciando navegador...")
            pw, browser, page = init_browser(headless=creds["headless"])
            log.info("Navegador listo")

            ok = do_login(page, creds["usuario"], creds["password"],
                          creds["captcha_key"], log, stop, self.captcha_bridge)
            if not ok or stop.is_set():
                if not ok: log.error("Login fallido.")
                return

            # Configurar catalogo con valores pre-seleccionados (sin bridge)
            result = setup_catalog_search(page, log, self.catalog_bridge,
                                          pre_selected=pre_selected)
            if not result or stop.is_set():
                if not result: log.error("Configuracion del catalogo fallida.")
                return

            self._total = len(data["rows"])
            log.info("Procesando %d filas..." % self._total)
            results = run_offer_loop(page, data["rows"], data["parte_col"], data["precio_col"],
                           log, stop, creds, creds["captcha_key"],
                           creds["usuario"], creds["password"],
                           self.captcha_bridge, self.catalog_bridge,
                           pre_selected=pre_selected)

            # Escribir Excel coloreado
            if results and data.get("path") and data.get("sheet"):
                try:
                    out = write_results(data["path"], data["sheet"], results)
                    log.ok("Excel coloreado guardado: %s" % os.path.basename(out))
                except Exception as e:
                    log.warn("No se pudo escribir el Excel: %s" % e)

        except Exception as e:
            log.error(f"Error fatal: {e}")
        finally:
            if browser and pw:
                try: close_browser(pw, browser); log.info("Navegador cerrado")
                except: pass

    def _on_stop(self):
        self.stop_event.set()
        self.btn_stop.configure(state="disabled", text="Deteniendo...")
        self._log("Detención solicitada", "warn")

    # ── Queue Polling ─────────────────────────────────────────────

    def poll_queue(self):
        try:
            while True:
                item = self.log_queue.get_nowait()
                t = item.get("type")
                if t == "log":
                    self._log(item.get("msg", ""), item.get("level", "info"))
                elif t == "progress":
                    cur = item.get("current", 0); tot = item.get("total", 1)
                    self.lbl_status.configure(text=f"Procesando fila {cur} de {tot}")
                    self.lbl_counter.configure(text=f"{cur}/{tot}")
                    self.progress.set(cur / tot if tot > 0 else 0)
                elif t == "done":
                    self._ok = item.get("ok", 0); self._errors = item.get("errors", 0)
                    self._running = False
                    self.lbl_status.configure(
                        text=f"Finalizado  ·  {self._ok} OK  ·  {self._errors} errores")
                    self.progress.set(1)
                    self.btn_launch.configure(state="normal")
                    self.btn_stop.configure(state="disabled", text="■ Detener")
        except queue.Empty:
            pass

        # Verificar bridges
        with self.captcha_bridge.lock:
            if self.captcha_bridge.image_bytes is not None and not self.captcha_bridge.event.is_set():
                self._show_captcha(self.captcha_bridge.image_bytes)
        with self.catalog_bridge.lock:
            if self.catalog_bridge.options and not self.catalog_bridge.event.is_set():
                self._populate_catalog_step(self.catalog_bridge.step, self.catalog_bridge.options)

        self.after(200, self.poll_queue)


# ═══════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app = PeruComprasApp()
    app.mainloop()

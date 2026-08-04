"""
Peru Compras Bot — Prototipo de Escritorio v1.4
Diseño desde 0: patrones nativos Windows Forms / SIAF
Sin emojis, sin paleta AI, sin glassmorphism.
Referencia: Portal Catalogos Peru Compras (azul institucional #006CA8)
"""
import sys
import os
import time
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

VERSION = "1.4 (DEMO)"

# ── PALETA INSTITUCIONAL (Peru Compras real) ──────────────────────
_AZUL       = "#006CA8"
_AZUL_DARK  = "#00507E"
_GRIS_BG    = "#F0F0F0"
_GRIS_PANEL = "#E8E8E8"
_GRIS_LINEA = "#C8C8C8"
_GRIS_TH    = "#D4D4D4"
_BLANCO     = "#FFFFFF"
_NEGRO      = "#1A1A1A"
_TEXTO      = "#2B2B2B"
_TEXTO_SEC  = "#555555"
_VERDE      = "#1B6B1B"
_VERDE_BG   = "#DFF0D8"
_ROJO       = "#8B1A1A"
_AMARILLO_BG= "#FCF8E3"


class PeruComprasDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"Peru Compras Bot — Sistema de Automatizacion de Ofertas  v{VERSION}")
        self.geometry("1180x720")
        self.minsize(960, 580)
        self.configure(bg=_GRIS_BG)

        self._modulo_activo = "pdf"
        self._archivo = tk.StringVar()
        # statusbar labels — inicializados en _build_ui
        self._st_estado = None
        self._st_navegador = None
        self._st_registros = None
        self._st_modulo = None

        self._setup_styles()
        self._build_ui()
        self._log("Sistema cargado. Peru Compras Bot v" + VERSION, "info")
        self._log("Catalogo local verificado: 249 acuerdos disponibles.", "ok")

    def _setup_styles(self):
        s = ttk.Style(self)
        s.theme_use("clam")

        # Tabla (Treeview) — estilo nativo Windows sin iconos raros
        s.configure("Hoja.Treeview",
            font=("Segoe UI", 10),
            rowheight=22,
            background=_BLANCO,
            foreground=_TEXTO,
            fieldbackground=_BLANCO,
            borderwidth=0,
        )
        s.configure("Hoja.Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background=_GRIS_TH,
            foreground=_NEGRO,
            relief="flat",
            padding=(6, 4),
        )
        s.map("Hoja.Treeview",
            background=[("selected", _AZUL)],
            foreground=[("selected", _BLANCO)],
        )
        s.configure("Hoja.Treeview.Heading",
            borderwidth=1,
        )

        # Scrollbar fina
        s.configure("TScrollbar", troughcolor=_GRIS_BG, background=_GRIS_PANEL, relief="flat")

    def _build_ui(self):
        # ── Barra de título institucional ──
        titulo = tk.Frame(self, bg=_AZUL, height=32)
        titulo.pack(fill="x", side="top")
        titulo.pack_propagate(False)
        tk.Label(titulo, text="PERU COMPRAS BOT — Sistema de Automatizacion de Ofertas y Catalogos",
                 bg=_AZUL, fg=_BLANCO, font=("Segoe UI", 11, "bold"),
                 anchor="w").pack(side="left", padx=14, fill="y")
        tk.Label(titulo, text=f"THE KING COMPUTER E.I.R.L.  |  v{VERSION}",
                 bg=_AZUL, fg="#AACCDD", font=("Segoe UI", 10)).pack(side="right", padx=14, fill="y")
        tk.Frame(titulo, bg=_AZUL_DARK, height=2).place(relx=0, rely=1, relwidth=1, anchor="sw")

        # ── Barra de menú clásica ──
        menubar = tk.Menu(self, font=("Segoe UI", 10), bg=_GRIS_PANEL, fg=_NEGRO,
                          relief="flat", bd=0)
        m_arch = tk.Menu(menubar, tearoff=0, font=("Segoe UI", 10))
        m_arch.add_command(label="Abrir archivo...", command=self._abrir_archivo)
        m_arch.add_command(label="Limpiar tabla")
        m_arch.add_separator()
        m_arch.add_command(label="Salir", command=self.destroy)
        menubar.add_cascade(label="Archivo", menu=m_arch)
        m_acc = tk.Menu(menubar, tearoff=0, font=("Segoe UI", 10))
        m_acc.add_command(label="Iniciar procesamiento (F5)", command=self._ejecutar)
        m_acc.add_command(label="Detener ejecucion")
        menubar.add_cascade(label="Acciones", menu=m_acc)
        m_cfg = tk.Menu(menubar, tearoff=0, font=("Segoe UI", 10))
        m_cfg.add_command(label="Guardado automatico de credenciales")
        m_cfg.add_command(label="Preferencias del sistema")
        menubar.add_cascade(label="Configuracion", menu=m_cfg)
        m_hlp = tk.Menu(menubar, tearoff=0, font=("Segoe UI", 10))
        m_hlp.add_command(label="Manual de usuario")
        m_hlp.add_command(label="Acerca del sistema...")
        menubar.add_cascade(label="Ayuda", menu=m_hlp)
        self.config(menu=menubar)

        # ── Barra de módulos (tabs de trabajo) ──
        tabs_frame = tk.Frame(self, bg=_GRIS_PANEL, bd=0)
        tabs_frame.pack(fill="x")
        tk.Frame(tabs_frame, bg=_GRIS_LINEA, height=1).pack(fill="x", side="bottom")

        self._tab_btns = {}
        MODULOS = [
            ("pdf",   "Publicacion de Ofertas PDF"),
            ("stock", "Actualizacion de Stock"),
            ("json",  "Subida de Precios JSON"),
            ("guide", "Instrucciones de Uso"),
        ]
        tab_inner = tk.Frame(tabs_frame, bg=_GRIS_PANEL)
        tab_inner.pack(side="left", padx=0)
        for mid, mlabel in MODULOS:
            btn = tk.Label(tab_inner, text=mlabel, font=("Segoe UI", 10),
                           padx=16, pady=6, cursor="hand2", bg=_GRIS_BG, fg=_TEXTO_SEC)
            btn.pack(side="left")
            tk.Frame(tab_inner, bg=_GRIS_LINEA, width=1).pack(side="left", fill="y")
            btn.bind("<Button-1>", lambda e, m=mid, b=btn: self._cambiar_modulo(m, b))
            self._tab_btns[mid] = btn
        # Se llamará al final de _build_ui cuando los labels ya existan

        # ── Cuerpo principal (2 columnas) ──
        cuerpo = tk.Frame(self, bg=_GRIS_BG)
        cuerpo.pack(fill="both", expand=True)
        cuerpo.columnconfigure(0, weight=1)
        cuerpo.columnconfigure(1, weight=0, minsize=310)
        cuerpo.rowconfigure(0, weight=1)

        # Columna izquierda: zona de trabajo
        zona = tk.Frame(cuerpo, bg=_BLANCO, bd=0)
        zona.grid(row=0, column=0, sticky="nsew")
        tk.Frame(cuerpo, bg=_GRIS_LINEA, width=1).grid(row=0, column=0, sticky="nse")
        zona.columnconfigure(0, weight=1)
        zona.rowconfigure(1, weight=1)

        # Sección de carga de archivo
        sec_carga = tk.Frame(zona, bg=_BLANCO, bd=0)
        sec_carga.grid(row=0, column=0, sticky="ew", padx=0)
        tk.Frame(sec_carga, bg=_GRIS_LINEA, height=1).pack(fill="x", side="bottom")

        cabecera = tk.Frame(sec_carga, bg=_GRIS_PANEL, pady=3)
        cabecera.pack(fill="x")
        tk.Label(cabecera, text="CARGA DE ARCHIVO DE TRABAJO",
                 font=("Segoe UI", 9, "bold"), bg=_GRIS_PANEL, fg=_TEXTO_SEC,
                 anchor="w").pack(side="left", padx=10)

        fila_arch = tk.Frame(sec_carga, bg=_BLANCO, pady=7)
        fila_arch.pack(fill="x", padx=10)

        tk.Label(fila_arch, text="Archivo:", font=("Segoe UI", 10),
                 bg=_BLANCO, fg=_TEXTO_SEC).pack(side="left")
        e_arch = tk.Entry(fila_arch, textvariable=self._archivo,
                          font=("Segoe UI", 10), bd=1, relief="sunken",
                          state="readonly", readonlybackground=_GRIS_BG, width=55)
        e_arch.pack(side="left", padx=(6, 4))
        tk.Button(fila_arch, text="Examinar...", font=("Segoe UI", 10),
                  bg=_GRIS_PANEL, fg=_NEGRO, bd=1, relief="raised",
                  command=self._abrir_archivo).pack(side="left", padx=2)
        tk.Button(fila_arch, text="Limpiar", font=("Segoe UI", 10),
                  bg=_GRIS_PANEL, fg=_NEGRO, bd=1, relief="raised",
                  command=lambda: self._archivo.set("")).pack(side="left", padx=2)

        self._lbl_deteccion = tk.Label(sec_carga, text="",
                  font=("Segoe UI", 10), bg=_VERDE_BG, fg=_VERDE,
                  anchor="w", padx=8, pady=3)

        # Tabla de productos
        tabla_frame = tk.Frame(zona, bg=_BLANCO)
        tabla_frame.grid(row=1, column=0, sticky="nsew")
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)

        COLS = ("#", "Numero de Parte", "Descripcion / Marca", "Precio Lista S/", "Stock Disp.", "Estado en Portal")
        self._tree = ttk.Treeview(tabla_frame, columns=COLS, show="headings",
                                   style="Hoja.Treeview", selectmode="extended")
        col_widths = [35, 140, 260, 100, 75, 130]
        col_anchors = ["center", "w", "w", "e", "center", "center"]
        for col, w, a in zip(COLS, col_widths, col_anchors):
            self._tree.heading(col, text=col)
            self._tree.column(col, width=w, anchor=a, stretch=(col == "Descripcion / Marca"))

        sb_v = ttk.Scrollbar(tabla_frame, orient="vertical", command=self._tree.yview)
        self._tree.configure(yscrollcommand=sb_v.set)
        self._tree.grid(row=0, column=0, sticky="nsew")
        sb_v.grid(row=0, column=1, sticky="ns")

        # Datos de muestra
        datos = [
            ("1", "2V262LT#ABM",  "HP PROBOOK 445 G8 / HP",         "3,450.00", "12", "Pendiente"),
            ("2", "3V5H1LT#ABM",  "HP ELITEDESK 800 G6 / HP",       "4,120.00", "8",  "Pendiente"),
            ("3", "21A20005LM",   "THINKPAD E14 GEN 2 / LENOVO",    "3,890.00", "15", "Pendiente"),
            ("4", "20VE003DLM",   "THINKBOOK 15 GEN 2 / LENOVO",    "2,980.00", "20", "Pendiente"),
            ("5", "V5N36A",       "SCANJET PRO 2500 F1 / HP",        "1,650.00", "5",  "Pendiente"),
        ]
        for i, d in enumerate(datos):
            tag = "par" if i % 2 == 0 else "impar"
            self._tree.insert("", "end", values=d, tags=(tag,))
        self._tree.tag_configure("par",   background=_BLANCO)
        self._tree.tag_configure("impar", background="#F7F7F7")

        # Columna derecha: inspector
        inspector = tk.Frame(cuerpo, bg=_BLANCO, bd=0)
        inspector.grid(row=0, column=1, sticky="nsew")
        inspector.columnconfigure(0, weight=1)
        inspector.rowconfigure(1, weight=1)

        tk.Label(inspector, text="CONFIGURACION DE EJECUCION",
                 font=("Segoe UI", 9, "bold"), bg=_AZUL, fg=_BLANCO,
                 anchor="w", padx=10, pady=6).grid(row=0, column=0, sticky="ew")

        cuerpo_insp = tk.Frame(inspector, bg=_BLANCO, padx=12, pady=8)
        cuerpo_insp.grid(row=1, column=0, sticky="nsew")
        cuerpo_insp.columnconfigure(1, weight=1)
        fila = [0]

        def agregar_separador(titulo):
            sep_f = tk.Frame(cuerpo_insp, bg=_BLANCO)
            sep_f.grid(row=fila[0], column=0, columnspan=2, sticky="ew", pady=(10, 4))
            tk.Label(sep_f, text=titulo, font=("Segoe UI", 9, "bold"),
                     bg=_BLANCO, fg=_AZUL).pack(side="left")
            tk.Frame(sep_f, bg=_GRIS_LINEA, height=1).pack(side="bottom", fill="x")
            fila[0] += 1

        def agregar_campo(label, widget_type="entry", valores=None, es_password=False):
            tk.Label(cuerpo_insp, text=label + ":", font=("Segoe UI", 10),
                     bg=_BLANCO, fg=_TEXTO_SEC, anchor="e").grid(
                         row=fila[0], column=0, sticky="e", padx=(0, 6), pady=2)
            if widget_type == "entry":
                show = "*" if es_password else ""
                w = tk.Entry(cuerpo_insp, font=("Segoe UI", 10), bd=1, relief="sunken",
                             bg=_GRIS_BG, show=show)
            else:
                w = ttk.Combobox(cuerpo_insp, values=valores or [], font=("Segoe UI", 10),
                                 state="readonly")
                if valores:
                    w.set(valores[0])
            w.grid(row=fila[0], column=1, sticky="ew", pady=2)
            fila[0] += 1
            return w

        agregar_separador("Acceso al Portal Peru Compras")
        w_user = agregar_campo("RUC / Usuario")
        w_user.insert(0, "almerco.03")
        agregar_campo("Contrasena", es_password=True)

        agregar_separador("Parametros de Catalogo")
        agregar_campo("Acuerdo", "combo", ["249 - EXT-CE-2022-5"])
        agregar_campo("Catalogo", "combo", [
            "252 - COMPUTADORAS ESCRITORIO",
            "250 - COMPUTADORAS PORTATILES",
            "251 - ESCANERES",
        ])
        agregar_campo("Categoria", "combo", [
            "11735 - COMP. ESCRITORIO",
            "11740 - ESTACION TRABAJO",
            "11741 - MONITOR",
        ])
        self._pausa_var = tk.StringVar(value="2")
        tk.Label(cuerpo_insp, text="Pausa (seg):", font=("Segoe UI", 10),
                 bg=_BLANCO, fg=_TEXTO_SEC, anchor="e").grid(
                     row=fila[0], column=0, sticky="e", padx=(0, 6), pady=2)
        tk.Entry(cuerpo_insp, textvariable=self._pausa_var,
                 font=("Segoe UI", 10), bd=1, relief="sunken",
                 bg=_GRIS_BG).grid(row=fila[0], column=1, sticky="ew", pady=2)
        fila[0] += 1

        agregar_separador("Opciones")
        for opc in ["Navegador oculto (headless)", "Guardar credenciales", "Exportar log al finalizar"]:
            v = tk.BooleanVar(value=(opc != "Exportar log al finalizar"))
            tk.Checkbutton(cuerpo_insp, text=opc, variable=v,
                           font=("Segoe UI", 10), bg=_BLANCO, fg=_TEXTO,
                           activebackground=_BLANCO).grid(
                               row=fila[0], column=0, columnspan=2, sticky="w", pady=1)
            fila[0] += 1

        # Consola de eventos
        consola_frame = tk.Frame(inspector, bg=_NEGRO)
        consola_frame.grid(row=2, column=0, sticky="ew")
        tk.Frame(inspector, bg=_AZUL, height=2).grid(row=2, column=0, sticky="new")

        self._consola = tk.Text(inspector, height=7, font=("Consolas", 9),
                                bg="#1A1A2E", fg="#E0E0E0", bd=0, relief="flat",
                                state="disabled", wrap="word")
        self._consola.grid(row=3, column=0, sticky="ew")
        self._consola.tag_configure("ok",   foreground="#90EE90")
        self._consola.tag_configure("warn", foreground="#FFD700")
        self._consola.tag_configure("err",  foreground="#FF6B6B")
        self._consola.tag_configure("info", foreground="#87CEEB")

        # Botón ejecutar
        tk.Button(inspector, text="INICIAR PROCESAMIENTO  (F5)",
                  font=("Segoe UI", 11, "bold"), bg=_AZUL, fg=_BLANCO,
                  activebackground=_AZUL_DARK, bd=0, pady=10,
                  command=self._ejecutar).grid(row=4, column=0, sticky="ew")

        # ── Barra de estado inferior ──
        statusbar = tk.Frame(self, bg=_GRIS_PANEL, bd=0)
        statusbar.pack(fill="x", side="bottom")
        tk.Frame(statusbar, bg=_GRIS_LINEA, height=1).pack(fill="x", side="top")

        def st_seg(texto, color=_TEXTO_SEC, bold=False):
            lbl = tk.Label(statusbar, text=texto,
                           font=("Segoe UI", 10, "bold" if bold else "normal"),
                           bg=_GRIS_PANEL, fg=color, pady=3, padx=10)
            lbl.pack(side="left")
            tk.Frame(statusbar, bg=_GRIS_LINEA, width=1).pack(side="left", fill="y", pady=2)
            return lbl

        self._st_estado    = st_seg("Listo", _VERDE, bold=True)
        self._st_navegador = st_seg("Navegador: No iniciado")
        self._st_registros = st_seg("Registros: 5 cargados")
        self._st_modulo    = st_seg("Modulo: Publicacion de Ofertas PDF")
        tk.Label(statusbar, text=f"Peru Compras Bot v{VERSION}",
                 font=("Segoe UI", 10), bg=_GRIS_PANEL, fg=_TEXTO_SEC,
                 padx=10).pack(side="right")

        self.bind("<F5>", lambda e: self._ejecutar())

        # Activar tab inicial ahora que todos los labels existen
        self._cambiar_modulo("pdf", self._tab_btns["pdf"], silent=True)

    def _cambiar_modulo(self, mid, btn, silent=False):
        for k, b in self._tab_btns.items():
            if k == mid:
                b.config(bg=_BLANCO, fg=_AZUL, font=("Segoe UI", 10, "bold"),
                         relief="solid", bd=0)
                tk.Frame(b, bg=_AZUL, height=2).place(relx=0, rely=1, relwidth=1, anchor="sw")
            else:
                b.config(bg=_GRIS_BG, fg=_TEXTO_SEC, font=("Segoe UI", 10),
                         relief="flat", bd=0)
        self._modulo_activo = mid
        nombres = {"pdf": "Publicacion de Ofertas PDF", "stock": "Actualizacion de Stock",
                   "json": "Subida de Precios JSON", "guide": "Instrucciones de Uso"}
        self._st_modulo.config(text="Modulo: " + nombres.get(mid, mid))
        if not silent:
            self._log("Cambiado a modulo: " + nombres.get(mid, mid), "info")

    def _abrir_archivo(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de trabajo",
            filetypes=[("Archivos validos", "*.xlsx *.json"), ("Todos", "*.*")]
        )
        if ruta:
            self._archivo.set(os.path.basename(ruta))
            self._lbl_deteccion.config(
                text="Deteccion automatica: PartNumber=ColA  |  PrecioLista=ColB  |  Stock=ColC")
            self._lbl_deteccion.pack(fill="x", padx=10, pady=(0, 6))
            self._log("Archivo cargado: " + os.path.basename(ruta), "ok")

    def _ejecutar(self):
        self._st_estado.config(text="Procesando...", fg=_TEXTO_SEC)
        self._st_navegador.config(text="Navegador: Iniciando")
        self._log("Conectando con catalogos.perucompras.gob.pe...", "info")
        self.after(800, lambda: self._log("Login exitoso. CAPTCHA resuelto.", "ok"))
        self.after(1500, lambda: self._log("Oferta actualizada: 2V262LT#ABM -> S/ 3,450.00", "ok"))
        self.after(1500, lambda: self._st_estado.config(text="Listo", fg=_VERDE))
        self.after(1500, lambda: self._st_navegador.config(text="Navegador: Oculto (activo)"))

    def _log(self, msg, tipo="info"):
        ts = time.strftime("%H:%M:%S")
        self._consola.config(state="normal")
        self._consola.insert("end", f"[{ts}] {msg}\n", tipo)
        self._consola.see("end")
        self._consola.config(state="disabled")


if __name__ == "__main__":
    app = PeruComprasDemo()
    app.mainloop()

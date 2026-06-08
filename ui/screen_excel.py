from tkinter import filedialog
import customtkinter as ctk

from utils.excel_parser import get_columns, parse_excel


class ScreenExcel(ctk.CTkFrame):
    def __init__(self, app, container):
        super().__init__(container)
        self.app = app

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self, text="Cargar Archivo Excel",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).grid(row=0, column=0, pady=(30, 15))

        self.btn_file = ctk.CTkButton(
            self, text="Seleccionar archivo .xlsx", command=self._pick_file
        )
        self.btn_file.grid(row=1, column=0, padx=60, pady=(0, 8))

        self.lbl_file = ctk.CTkLabel(self, text="Ningún archivo seleccionado", text_color="gray")
        self.lbl_file.grid(row=2, column=0, pady=(0, 20))

        self.mapping_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.mapping_frame.grid(row=3, column=0, padx=60, sticky="ew")
        self.mapping_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.mapping_frame, text="Columna de Número de Parte", anchor="w").grid(
            row=0, column=0, sticky="w", pady=(0, 2)
        )
        self.combo_parte = ctk.CTkComboBox(
            self.mapping_frame, values=["-- Seleccionar --"], state="disabled"
        )
        self.combo_parte.grid(row=1, column=0, sticky="ew", pady=(0, 12))

        ctk.CTkLabel(self.mapping_frame, text="Columna de Precio", anchor="w").grid(
            row=2, column=0, sticky="w", pady=(0, 2)
        )
        self.combo_precio = ctk.CTkComboBox(
            self.mapping_frame, values=["-- Seleccionar --"], state="disabled"
        )
        self.combo_precio.grid(row=3, column=0, sticky="ew", pady=(0, 12))

        self.lbl_total = ctk.CTkLabel(
            self.mapping_frame, text="Total de filas a procesar: 0", anchor="w"
        )
        self.lbl_total.grid(row=4, column=0, sticky="w", pady=(10, 5))

        ctk.CTkLabel(self.mapping_frame, text="Previsualización (primeras 5 filas):", anchor="w").grid(
            row=5, column=0, sticky="w", pady=(15, 5)
        )

        self.preview_frame = ctk.CTkScrollableFrame(self.mapping_frame, height=120)
        self.preview_frame.grid(row=6, column=0, sticky="ew", pady=(0, 10))
        self.preview_frame.grid_columnconfigure(0, weight=1)

        self.preview_labels: list[ctk.CTkLabel] = []

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.grid(row=4, column=0, padx=60, pady=(10, 30), sticky="ew")
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)

        self.btn_back = ctk.CTkButton(
            btn_frame, text="← Volver", fg_color="gray", command=self._on_back
        )
        self.btn_back.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        self.btn_start = ctk.CTkButton(
            btn_frame, text="Iniciar →", state="disabled", command=self._on_start
        )
        self.btn_start.grid(row=0, column=1, padx=(5, 0), sticky="ew")

        self._columns: list[str] = []
        self._rows: list[dict] = []

    def on_enter(self):
        pass

    def _pick_file(self):
        path = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
        )
        if not path:
            return

        try:
            self._columns = get_columns(path)
            cols = ["-- Seleccionar --"] + self._columns
            self.combo_parte.configure(values=cols, state="readonly")
            self.combo_parte.set("-- Seleccionar --")
            self.combo_precio.configure(values=cols, state="readonly")
            self.combo_precio.set("-- Seleccionar --")

            self._rows = parse_excel(path)
            self.lbl_file.configure(text=f"Archivo: {path.split('/')[-1].split(chr(92))[-1]}")
            self.lbl_total.configure(text=f"Total de filas a procesar: {len(self._rows)}")

            self._refresh_preview()
        except Exception as e:
            self.lbl_file.configure(text=f"Error al leer archivo: {e}", text_color="red")

    def _refresh_preview(self):
        for lbl in self.preview_labels:
            lbl.destroy()
        self.preview_labels.clear()

        preview = self._rows[:5]
        if not preview:
            ctk.CTkLabel(self.preview_frame, text="Sin datos").pack(anchor="w")
            return

        for i, row in enumerate(preview):
            text = ", ".join(f"{k}={v}" for k, v in list(row.items()))
            lbl = ctk.CTkLabel(self.preview_frame, text=f"[{i+1}] {text[:100]}", anchor="w")
            lbl.pack(anchor="w", pady=1)
            self.preview_labels.append(lbl)

    def _on_back(self):
        self.app.show_screen("login")

    def _on_start(self):
        parte = self.combo_parte.get()
        precio = self.combo_precio.get()
        if parte == "-- Seleccionar --" or precio == "-- Seleccionar --":
            return

        self.app.excel_data = {
            "filepath": None,
            "columns": self._columns,
            "rows": self._rows,
            "parte_col": parte,
            "precio_col": precio,
        }
        self.app.show_screen("run")

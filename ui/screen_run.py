import queue
import threading
import csv

from io import BytesIO
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

from automation.browser import init_browser, close_browser
from automation.login import do_login
from automation.navigation import setup_catalog_search
from automation.offer_loop import run_offer_loop
from utils.logger import LogWriter


class ScreenRun(ctk.CTkFrame):
    def __init__(self, app, container):
        super().__init__(container)
        self.app = app
        self.grid_columnconfigure(0, weight=1)

        self._log_lines: list[dict] = []
        self._ok_count = 0
        self._error_count = 0
        self._total = 0
        self._running = False

        # Row 0: Título
        ctk.CTkLabel(
            self, text="Ejecución en Curso",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).grid(row=0, column=0, pady=(20, 8))

        # Row 1: Status
        self.lbl_status = ctk.CTkLabel(
            self, text="Preparando...", font=ctk.CTkFont(size=13)
        )
        self.lbl_status.grid(row=1, column=0, pady=(0, 5))

        # Row 2: Progress
        self.progress = ctk.CTkProgressBar(self, width=500)
        self.progress.grid(row=2, column=0, padx=60, pady=(0, 8), sticky="ew")
        self.progress.set(0)

        # Row 3: Paneles dinámicos (CAPTCHA y Catálogo comparten row)
        self._build_captcha_panel()
        self._build_catalog_panel()

        # Row 4: Log
        self.log_box = ctk.CTkTextbox(self, wrap="word", height=200)
        self.log_box.grid(row=4, column=0, padx=60, pady=(0, 8), sticky="nsew")
        self.log_box.configure(state="disabled")
        self.log_box.tag_config("ok", foreground="#4CAF50")
        self.log_box.tag_config("error", foreground="#F44336")
        self.log_box.tag_config("info", foreground="#BDBDBD")

        self.rowconfigure(4, weight=1)

        # Row 5: Botones
        btn_row = ctk.CTkFrame(self, fg_color="transparent")
        btn_row.grid(row=5, column=0, padx=60, pady=(0, 15), sticky="ew")
        btn_row.grid_columnconfigure(0, weight=1)
        btn_row.grid_columnconfigure(1, weight=1)

        self.btn_stop = ctk.CTkButton(
            btn_row, text="Detener", fg_color="#d32f2f",
            hover_color="#b71c1c", command=self._on_stop
        )
        self.btn_stop.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        self.btn_download = ctk.CTkButton(
            btn_row, text="Descargar Log CSV", state="disabled", command=self._download_log
        )
        self.btn_download.grid(row=0, column=1, padx=(5, 0), sticky="ew")

        self.btn_new = ctk.CTkButton(
            btn_row, text="Nueva ejecución", fg_color="gray", command=self._on_new
        )
        self.btn_new.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="ew")
        self.btn_new.grid_remove()

    # ─── Captcha panel ─────────────────────────────────────────────

    def _build_captcha_panel(self):
        self.captcha_frame = ctk.CTkFrame(self)
        self.captcha_frame.grid(row=3, column=0, padx=60, pady=(0, 8), sticky="ew")
        self.captcha_frame.grid_remove()
        self.captcha_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.captcha_frame, text="CAPTCHA detectado — ingresá el código",
            font=ctk.CTkFont(size=12, weight="bold"),
        ).grid(row=0, column=0, pady=(6, 4))

        self.captcha_img_label = ctk.CTkLabel(self.captcha_frame, text="")
        self.captcha_img_label.grid(row=1, column=0, pady=(0, 6))

        cap_row = ctk.CTkFrame(self.captcha_frame, fg_color="transparent")
        cap_row.grid(row=2, column=0, sticky="ew", pady=(0, 6))
        cap_row.grid_columnconfigure(0, weight=1)
        cap_row.grid_columnconfigure(1, weight=0)

        self.captcha_entry = ctk.CTkEntry(cap_row, placeholder_text="Código", width=180)
        self.captcha_entry.grid(row=0, column=0, padx=(0, 6), sticky="ew")
        self.captcha_entry.bind("<Return>", lambda e: self._on_captcha_submit())

        self.captcha_btn = ctk.CTkButton(
            cap_row, text="Enviar", width=70, command=self._on_captcha_submit
        )
        self.captcha_btn.grid(row=0, column=1)
        self._captcha_img_tk = None

    def _show_captcha(self, image_bytes: bytes):
        img = Image.open(BytesIO(image_bytes))
        img = img.resize((250, 66), Image.LANCZOS)
        self._captcha_img_tk = ctk.CTkImage(light_image=img, dark_image=img, size=(250, 66))
        self.captcha_img_label.configure(image=self._captcha_img_tk)
        self.captcha_entry.delete(0, "end")
        self.captcha_entry.focus_set()
        self._hide_catalog()
        self.captcha_frame.grid()

    def _hide_captcha(self):
        self.captcha_frame.grid_remove()

    def _on_captcha_submit(self):
        code = self.captcha_entry.get().strip()
        if code:
            self.app.captcha_bridge.respond(code)
            self._hide_captcha()
            self._append_log(f"CAPTCHA manual: {code}", "info")

    # ─── Catálogo panel ────────────────────────────────────────────

    def _build_catalog_panel(self):
        self.catalog_frame = ctk.CTkFrame(self)
        self.catalog_frame.grid(row=3, column=0, padx=60, pady=(0, 8), sticky="ew")
        self.catalog_frame.grid_remove()
        self.catalog_frame.grid_columnconfigure(0, weight=1)

        self.lbl_catalog_title = ctk.CTkLabel(
            self.catalog_frame,
            text="Seleccioná las opciones del catálogo",
            font=ctk.CTkFont(size=12, weight="bold"),
        )
        self.lbl_catalog_title.grid(row=0, column=0, pady=(6, 8))

        self.lbl_catalog_step = ctk.CTkLabel(
            self.catalog_frame, text="", anchor="w"
        )
        self.lbl_catalog_step.grid(row=1, column=0, sticky="w", pady=(0, 4))

        self.combo_catalogo_step = ctk.CTkComboBox(
            self.catalog_frame, values=["Cargando..."], state="disabled", width=500
        )
        self.combo_catalogo_step.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        self.catalog_btn = ctk.CTkButton(
            self.catalog_frame, text="Seleccionar →",
            command=self._on_catalog_step_submit, state="disabled"
        )
        self.catalog_btn.grid(row=3, column=0, pady=(0, 6))

    def _show_catalog_step(self, step: str, options: list[dict]):
        labels = {
            "acuerdo": "Acuerdo Marco",
            "catalogo": "Catálogo Electrónico",
            "categoria": "Categoría",
        }
        title = labels.get(step, step)
        self.lbl_catalog_step.configure(text=f"Paso: {title}")

        texts = [f"{o['value']} - {o['text'][:70]}" for o in options]
        self.combo_catalogo_step.configure(values=texts, state="readonly")
        self.combo_catalogo_step.set(texts[0] if texts else "--")
        self.catalog_btn.configure(state="normal", text=f"Seleccionar {title} →")
        self._hide_captcha()
        self.catalog_frame.grid()

    def _hide_catalog(self):
        self.catalog_frame.grid_remove()

    def _on_catalog_step_submit(self):
        text = self.combo_catalogo_step.get()
        value = text.split(" - ")[0].strip() if " - " in text else "0"
        self.app.catalog_bridge.respond_step(value)
        self._append_log(f"Seleccionado: {text}", "info")
        self.catalog_btn.configure(state="disabled", text="Esperando siguiente paso...")
        self.combo_catalogo_step.configure(state="disabled")

    # ─── Flujo principal ───────────────────────────────────────────

    def on_enter(self):
        self._log_lines.clear()
        self._ok_count = 0
        self._error_count = 0
        self._total = 0
        self._running = True
        self.app.stop_event.clear()

        self.lbl_status.configure(text="Iniciando...")
        self.progress.set(0)
        self.btn_stop.configure(state="normal", text="Detener")
        self.btn_download.configure(state="disabled")
        self.btn_new.grid_remove()
        self._hide_captcha()
        self._hide_catalog()
        self.catalog_btn.configure(state="disabled", text="Seleccionar →")

        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")

        thread = threading.Thread(target=self._run_automation, daemon=True)
        thread.start()
        self.poll_queue()

    def _run_automation(self):
        creds = self.app.credentials
        data = self.app.excel_data
        log = LogWriter(self.app.log_queue)
        stop = self.app.stop_event

        pw = None
        browser = None

        try:
            log.info("Iniciando navegador...")
            pw, browser, page = init_browser(headless=creds["headless"])
            log.info("Navegador iniciado")

            success = do_login(
                page, creds["usuario"], creds["password"],
                creds["captcha_key"], log, stop,
                captcha_bridge=self.app.captcha_bridge,
            )
            if not success:
                log.error("Login fallido. Abortando.")
                return
            if stop.is_set():
                return

            # Configurar búsqueda (dropdowns + Iniciar Búsqueda → CatalogoProductoIndex)
            result = setup_catalog_search(
                page, log, self.app.catalog_bridge,
            )
            if not result:
                log.error("Configuración de catálogo fallida. Abortando.")
                return
            if stop.is_set():
                return

            self._total = len(data["rows"])
            log.info(f"Iniciando procesamiento de {self._total} filas...")

            run_offer_loop(
                page, data["rows"], data["parte_col"], data["precio_col"],
                log, stop, creds, creds["captcha_key"],
                creds["usuario"], creds["password"],
                captcha_bridge=self.app.captcha_bridge,
                catalog_bridge=self.app.catalog_bridge,
            )

        except Exception as e:
            log.error(f"Error fatal en automatización: {e}")
        finally:
            if browser and pw:
                try:
                    close_browser(pw, browser)
                    log.info("Navegador cerrado")
                except Exception:
                    pass

    def poll_queue(self):
        if not self._running:
            return
        try:
            while True:
                item = self.app.log_queue.get_nowait()
                self._handle_item(item)
        except queue.Empty:
            pass

        # Verificar CAPTCHA pendiente
        with self.app.captcha_bridge.lock:
            if self.app.captcha_bridge.image_bytes is not None and not self.app.captcha_bridge.event.is_set():
                self._show_captcha(self.app.captcha_bridge.image_bytes)

        # Verificar catálogo pendiente (step by step)
        with self.app.catalog_bridge.lock:
            if self.app.catalog_bridge.options and not self.app.catalog_bridge.event.is_set():
                self._show_catalog_step(
                    self.app.catalog_bridge.step,
                    self.app.catalog_bridge.options,
                )

        self.after(200, self.poll_queue)

    def _handle_item(self, item: dict):
        t = item.get("type")

        if t == "log":
            level = item.get("level", "info")
            msg = item.get("msg", "")
            self._log_lines.append({"level": level, "msg": msg})
            self._append_log(msg, level)

        elif t == "progress":
            current = item.get("current", 0)
            total = item.get("total", 1)
            self._total = total
            self.lbl_status.configure(text=f"Procesando fila {current} de {total}")
            self.progress.set(current / total if total > 0 else 0)

        elif t == "done":
            self._ok_count = item.get("ok", 0)
            self._error_count = item.get("errors", 0)
            self._running = False

            self.lbl_status.configure(
                text=f"Finalizado: {self._ok_count} OK, {self._error_count} errores"
            )
            self.progress.set(1)

            self.btn_stop.configure(state="disabled")
            self.btn_download.configure(state="normal")
            self.btn_new.grid()

    def _append_log(self, msg: str, level: str):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", msg + "\n", level)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def _on_stop(self):
        self.app.stop_event.set()
        self.btn_stop.configure(state="disabled", text="Deteniendo...")
        self._append_log("Detención solicitada por el usuario...", "info")

    def _download_log(self):
        path = filedialog.asksaveasfilename(
            title="Guardar log CSV",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
        )
        if not path:
            return
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Nivel", "Mensaje"])
                for line in self._log_lines:
                    writer.writerow([line["level"], line["msg"]])
        except Exception as e:
            self._append_log(f"Error al guardar CSV: {e}", "error")

    def _on_new(self):
        self.app.show_screen("excel")

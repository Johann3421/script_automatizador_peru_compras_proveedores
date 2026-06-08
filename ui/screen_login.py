import customtkinter as ctk


class ScreenLogin(ctk.CTkFrame):
    def __init__(self, app, container):
        super().__init__(container)
        self.app = app
        self._password_visible = False

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self, text="Peru Compras Bot",
            font=ctk.CTkFont(size=22, weight="bold"),
        ).grid(row=0, column=0, pady=(40, 10))

        ctk.CTkLabel(
            self, text="Credenciales de catalogos.perucompras.gob.pe",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).grid(row=1, column=0, pady=(0, 5), sticky="ew")

        ctk.CTkLabel(
            self, text="El bot iniciará sesión automáticamente en la web oficial",
            font=ctk.CTkFont(size=12),
            text_color="gray",
        ).grid(row=2, column=0, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(
            self, text="resolviendo el CAPTCHA con OCR (Tesseract)",
            font=ctk.CTkFont(size=12),
            text_color="gray",
        ).grid(row=3, column=0, pady=(0, 20), sticky="ew")

        form = ctk.CTkFrame(self, fg_color="transparent")
        form.grid(row=4, column=0, padx=60, sticky="ew")
        form.grid_columnconfigure(0, weight=0)
        form.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(form, text="Usuario / RUC", anchor="w").grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(8, 2)
        )
        self.entry_user = ctk.CTkEntry(form, placeholder_text="Usuario o RUC")
        self.entry_user.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 12))
        self.entry_user.insert(0, "estalin.huamali01")

        ctk.CTkLabel(form, text="Contraseña", anchor="w").grid(
            row=2, column=0, columnspan=2, sticky="w", pady=(8, 2)
        )
        self.entry_pass = ctk.CTkEntry(form, show="*", placeholder_text="Contraseña")
        self.entry_pass.insert(0, "PE/CyG6c&1R4T=")
        self.entry_pass.grid(row=3, column=0, sticky="ew", pady=(0, 12))

        self.btn_eye = ctk.CTkButton(
            form, text="👁", width=36, command=self._toggle_password
        )
        self.btn_eye.grid(row=3, column=1, padx=(6, 0), pady=(0, 12))

        ctk.CTkLabel(form, text="API Key de 2captcha", anchor="w").grid(
            row=4, column=0, columnspan=2, sticky="w", pady=(8, 2)
        )
        self.entry_captcha = ctk.CTkEntry(form, placeholder_text="Opcional - solo si querés usar 2captcha en vez de OCR")
        self.entry_captcha.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(0, 12))

        self.check_headless = ctk.CTkCheckBox(
            form, text="Mostrar navegador durante la ejecución"
        )
        self.check_headless.grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 20))

        self.lbl_error = ctk.CTkLabel(form, text="", text_color="red")
        self.lbl_error.grid(row=5, column=0, columnspan=2, pady=(0, 8))

        self.btn_next = ctk.CTkButton(
            self, text="Siguiente →", height=40, command=self._on_next
        )
        self.btn_next.grid(row=5, column=0, padx=60, pady=(20, 40), sticky="ew")

    def on_enter(self):
        self.lbl_error.configure(text="")

    def _toggle_password(self):
        self._password_visible = not self._password_visible
        if self._password_visible:
            self.entry_pass.configure(show="")
            self.btn_eye.configure(text="🙈")
        else:
            self.entry_pass.configure(show="*")
            self.btn_eye.configure(text="👁")

    def _on_next(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pass.get().strip()
        cap = self.entry_captcha.get().strip()

        if not user or not pwd:
            self.lbl_error.configure(
                text="Usuario y Contraseña son obligatorios."
            )
            return

        self.app.credentials = {
            "usuario": user,
            "password": pwd,
            "captcha_key": cap,
            "headless": not self.check_headless.get(),
        }
        self.app.show_screen("excel")

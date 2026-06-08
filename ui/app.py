import queue
import threading
import customtkinter as ctk

from ui.screen_login import ScreenLogin
from ui.screen_excel import ScreenExcel
from ui.screen_run import ScreenRun


class CaptchaBridge:
    """Permite al thread de automation pedirle al usuario que resuelva el CAPTCHA."""
    def __init__(self):
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.image_bytes: bytes | None = None
        self.user_code: str = ""

    def request(self, image_bytes: bytes) -> str:
        with self.lock:
            self.image_bytes = image_bytes
            self.user_code = ""
            self.event.clear()
        self.event.wait()
        with self.lock:
            return self.user_code

    def respond(self, code: str):
        with self.lock:
            self.user_code = code
            self.image_bytes = None
        self.event.set()


class CatalogBridge:
    """Permite al thread pedir al usuario que seleccione dropdowns en cascada."""
    def __init__(self):
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.step: str = ""           # "acuerdo", "catalogo", "categoria"
        self.options: list[dict] = []  # opciones del dropdown actual
        self.selection: str = ""      # value seleccionado

    def request_step(self, step: str, options: list[dict]) -> str:
        """Bloquea hasta que el usuario seleccione un valor para este paso."""
        with self.lock:
            self.step = step
            self.options = options
            self.selection = ""
            self.event.clear()
        self.event.wait()
        with self.lock:
            return self.selection

    def respond_step(self, value: str):
        with self.lock:
            self.selection = value
            self.options = []
        self.event.set()


class App:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Peru Compras Bot")
        self.root.geometry("880x750")
        self.root.minsize(750, 600)

        self.container = ctk.CTkFrame(root)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)

        self.credentials = {}
        self.excel_data = {
            "filepath": None,
            "columns": [],
            "rows": [],
            "parte_col": None,
            "precio_col": None,
        }
        self.log_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.captcha_bridge = CaptchaBridge()
        self.catalog_bridge = CatalogBridge()

        self.screens: dict[str, ctk.CTkFrame] = {}

        self.screens["login"] = ScreenLogin(self, self.container)
        self.screens["excel"] = ScreenExcel(self, self.container)
        self.screens["run"] = ScreenRun(self, self.container)

        self.current_screen = None
        self.show_screen("login")

    def show_screen(self, name: str):
        if self.current_screen:
            self.screens[self.current_screen].grid_remove()
        screen = self.screens[name]
        screen.grid(row=0, column=0, sticky="nsew")
        screen.on_enter()
        self.current_screen = name
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

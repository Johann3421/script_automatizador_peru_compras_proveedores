"""
ctk_compat.py — Capa de compatibilidad customtkinter → plain tkinter
Reemplaza los widgets CTk con equivalentes tkinter/ttk nativos de Windows.
Misma API pública: .configure(), .get(), .set(), .insert(), .see(), .pack(), .grid()
Los backends existentes no necesitan modificación.

Paleta institucional Peru Compras:
  Azul:  #006CA8  Gris bg: #F0F0F0  Gris panel: #E8E8E8  Blanco: #FFFFFF
"""

import tkinter as tk
from tkinter import ttk
import time

# ── Paleta por defecto (se sobrescribe vía _C en la app) ─────────────
_BG      = "#F0F0F0"
_PANEL   = "#E8E8E8"
_CARD    = "#FFFFFF"
_CARD2   = "#F7F7F7"
_BORDER  = "#C8C8C8"
_TXT     = "#2B2B2B"
_TXT2    = "#555555"
_TXT3    = "#888888"
_AZUL    = "#006CA8"
_AZUL_DK = "#00507E"
_SUCCESS = "#1B6B1B"
_DANGER  = "#8B1A1A"
_SEP     = "#D4D4D4"
_FONT    = ("Segoe UI", 10)
_FONT_B  = ("Segoe UI", 10, "bold")


# ─── Widget Helpers ──────────────────────────────────────────────────

def _ignore(**kw):
    """Descarta kwargs CTk que tkinter no acepta."""
    IGNORED = {"fg_color", "hover_color", "text_color", "border_color", "button_color",
               "corner_radius", "scrollbar_button_color", "progress_color", "dropdown_fg_color",
               "dropdown_hover_color", "dropdown_text_color", "button_hover_color",
               "border_width"}
    return {k: v for k, v in kw.items() if k not in IGNORED}


def _patch_scrollable(master):
    """Si master es un CTkScrollableFrame (o cualquier contenedor con get_inner), redirigir al inner frame."""
    if hasattr(master, "get_inner"):
        return master.get_inner()
    return master


# ─── CTkFont ─────────────────────────────────────────────────────────

class CTkFont:
    def __init__(self, family="Segoe UI", size=10, weight="normal"):
        self._spec = (family, size, weight if weight == "bold" else "")
    def __iter__(self):
        return iter(self._spec)
    def __repr__(self):
        return str(self._spec)


# ─── CTkFrame ────────────────────────────────────────────────────────

class CTkFrame(tk.Frame):
    def __init__(self, master=None, fg_color=None, corner_radius=None,
                 border_width=0, border_color=None, height=None, width=None,
                 scrollbar_button_color=None, **kw):
        p = _patch_scrollable(master)
        bg = fg_color if (fg_color and fg_color != "transparent") else _BG
        super_kw = {}
        if height: super_kw["height"] = height
        if width:  super_kw["width"]  = width
        super().__init__(p, bg=bg, relief="flat", bd=0, **super_kw)
        if border_width and border_color:
            self.configure(highlightbackground=border_color, highlightthickness=1)

    def configure(self, cnf=None, fg_color=None, **kw):
        if cnf is not None and isinstance(cnf, dict):
            kw.update(cnf)
        if fg_color and fg_color != "transparent":
            kw["bg"] = fg_color
        kw.pop("corner_radius", None); kw.pop("border_color", None)
        kw.pop("border_width", None); kw.pop("scrollbar_button_color", None)
        if kw:
            super().configure(**kw)



# ─── CTkScrollableFrame ──────────────────────────────────────────────

class CTkScrollableFrame(tk.Frame):
    """
    Scrollable frame — los widgets hijos se añaden al inner frame.
    Se expone como contenedor normal de grid/pack layout.
    """
    def __init__(self, master=None, fg_color=None, scrollbar_button_color=None, **kw):
        bg = fg_color if (fg_color and fg_color != "transparent") else _BG
        super().__init__(master, bg=bg)
        # Canvas + scrollbar
        self._canvas = tk.Canvas(self, bg=bg, bd=0, highlightthickness=0)
        self._sb = ttk.Scrollbar(self, orient="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self._sb.set)
        self._sb.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)
        # Inner frame where child widgets are placed
        self._inner = tk.Frame(self._canvas, bg=bg)
        self._window = self._canvas.create_window((0, 0), window=self._inner, anchor="nw")
        self._inner.bind("<Configure>", self._on_inner_cfg)
        self._canvas.bind("<Configure>", self._on_canvas_cfg)
        self.bind_all("<MouseWheel>", self._on_wheel, add="+")

    def _on_inner_cfg(self, e):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def _on_canvas_cfg(self, e):
        self._canvas.itemconfig(self._window, width=e.width)

    def _on_wheel(self, e):
        try: self._canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        except Exception: pass

    # ── Proxy geometry config to inner frame ──
    def grid_columnconfigure(self, *a, **kw): self._inner.grid_columnconfigure(*a, **kw)
    def grid_rowconfigure(self, *a, **kw): self._inner.grid_rowconfigure(*a, **kw)

    # ── Make child widgets use self._inner as real parent ──
    # We override the Tk window path so widget creation goes to inner frame.
    # Simpler: we return _inner from a property used by CTk* widgets via _patch_scrollable.
    def get_inner(self): return self._inner


# ─── CTkLabel ────────────────────────────────────────────────────────

class CTkLabel(tk.Label):
    def __init__(self, master=None, text="", font=None, text_color=None,
                 fg_color=None, anchor="center", wraplength=0,
                 corner_radius=None, justify="left", **kw):
        p = _patch_scrollable(master)
        bg = fg_color if (fg_color and fg_color != "transparent") else (
            p.cget("bg") if (p and hasattr(p, "cget")) else _BG)
        fg = text_color or _TXT
        f = tuple(font) if font else _FONT
        super().__init__(p, text=text, bg=bg, fg=fg, font=f,
                         anchor=anchor, wraplength=wraplength, justify=justify)

    def configure(self, cnf=None, text=None, text_color=None, fg_color=None, **kw):
        if cnf is not None and isinstance(cnf, dict):
            kw.update(cnf)
        cfg = {}
        if text is not None: cfg["text"] = text
        if text_color:       cfg["fg"]   = text_color
        if fg_color and fg_color != "transparent": cfg["bg"] = fg_color
        kw.pop("font", None); kw.pop("corner_radius", None)
        cfg.update({k: v for k, v in kw.items() if k not in
                    ("border_color", "border_width", "wraplength")})
        if cfg:
            try: super().configure(**cfg)
            except Exception: pass


# ─── CTkButton ───────────────────────────────────────────────────────

class CTkButton(tk.Button):
    def __init__(self, master=None, text="", font=None, fg_color=None,
                 hover_color=None, text_color=None, border_color=None,
                 border_width=0, corner_radius=None, width=None, height=None,
                 state="normal", anchor="center", command=None, **kw):
        p = _patch_scrollable(master)
        parent_bg = _BG
        try:
            if p and hasattr(p, "cget"): parent_bg = p.cget("bg")
        except Exception:
            pass
        bg = fg_color if (fg_color and fg_color != "transparent") else parent_bg
        fg = text_color if text_color else ("#FFFFFF" if fg_color and fg_color not in ("transparent", "") else _TXT)
        ab = hover_color if (hover_color and hover_color != "transparent") else bg
        f  = tuple(font) if font else _FONT
        opts = dict(text=text, bg=bg, fg=fg, font=f,
                    relief="flat", bd=0, cursor="hand2",
                    state=state, activebackground=ab,
                    activeforeground=fg)
        if command: opts["command"] = command
        super().__init__(p, **opts)
        self._bg = bg
        self._hover = ab
        self.bind("<Enter>", lambda e: self.configure(bg=self._hover))
        self.bind("<Leave>", lambda e: self.configure(bg=self._bg))


    def configure(self, text=None, fg_color=None, text_color=None,
                  state=None, hover_color=None, **kw):
        cfg = {}
        if text is not None: cfg["text"]  = text
        if fg_color:         cfg["bg"]    = fg_color
        if text_color:       cfg["fg"]    = text_color
        if state is not None:cfg["state"] = state
        kw.pop("font", None); kw.pop("corner_radius", None)
        kw.pop("border_width", None); kw.pop("border_color", None)
        kw.pop("width", None); kw.pop("height", None)
        cfg.update({k: v for k, v in kw.items()})
        if cfg:
            try: super().configure(**cfg)
            except Exception: pass


# ─── CTkEntry ────────────────────────────────────────────────────────

class CTkEntry(tk.Entry):
    def __init__(self, master=None, placeholder_text=None, show=None,
                 fg_color=None, border_color=None, text_color=None,
                 height=None, width=None, corner_radius=None, **kw):
        p = _patch_scrollable(master)
        opts = dict(bg=_CARD2, fg=_TXT, font=_FONT,
                    relief="sunken", bd=1,
                    insertbackground=_TXT)
        if show: opts["show"] = show
        if width: opts["width"] = max(1, width // 8)
        super().__init__(p, **opts)
        if placeholder_text and not show:
            self._ph = placeholder_text
            self.insert(0, "")

    def configure(self, show=None, placeholder_text=None, state=None,
                  values=None, **kw):
        cfg = {}
        if show is not None: cfg["show"] = show
        if state is not None: cfg["state"] = state
        kw.pop("fg_color", None); kw.pop("border_color", None)
        kw.pop("text_color", None); kw.pop("corner_radius", None)
        kw.pop("height", None)
        cfg.update({k: v for k, v in kw.items()})
        if cfg:
            try: super().configure(**cfg)
            except Exception: pass


# ─── CTkComboBox / CTkOptionMenu ─────────────────────────────────────

class _ComboBase(ttk.Combobox):
    """Base compartida para CTkComboBox y CTkOptionMenu."""
    def __init__(self, master=None, values=None, state="readonly",
                 command=None, width=None, height=None, **_ignored):
        p = _patch_scrollable(master)
        vals = values or []
        w = max(1, (width or 200) // 8)
        super().__init__(p, values=vals, state=state, font=_FONT, width=w)
        self._cmd = command
        if command:
            self.bind("<<ComboboxSelected>>", lambda e: command(self.get()))
        if vals:
            self.set(vals[0])

    def configure(self, values=None, state=None, command=None, **kw):
        cfg = {}
        if values is not None:
            cfg["values"] = values
        if state is not None:
            cfg["state"] = state
        if command is not None:
            self._cmd = command
            self.bind("<<ComboboxSelected>>", lambda e: command(self.get()))
        kw.pop("fg_color", None); kw.pop("border_color", None)
        kw.pop("text_color", None); kw.pop("button_color", None)
        kw.pop("button_hover_color", None); kw.pop("dropdown_fg_color", None)
        kw.pop("dropdown_hover_color", None); kw.pop("dropdown_text_color", None)
        cfg.update(kw)
        if cfg:
            super().configure(**cfg)
        if values is not None and values:
            self.set(values[0])

    def set(self, value):
        self.delete(0, "end")
        self.insert(0, value if value else "")



class CTkComboBox(_ComboBase):
    pass

class CTkOptionMenu(_ComboBase):
    pass


# ─── CTkCheckBox ─────────────────────────────────────────────────────

class CTkCheckBox(tk.Checkbutton):
    def __init__(self, master=None, text="", font=None, text_color=None,
                 fg_color=None, border_color=None, corner_radius=None, **kw):
        p = _patch_scrollable(master)
        self._var = tk.IntVar(value=0)
        bg = p.cget("bg") if (p and hasattr(p, "cget")) else _BG
        f = tuple(font) if font else _FONT
        super().__init__(p, text=text, variable=self._var,
                         bg=bg, fg=text_color or _TXT,
                         font=f, activebackground=bg,
                         selectcolor=_AZUL)

    def get(self):
        return self._var.get()

    def select(self): self._var.set(1)
    def deselect(self): self._var.set(0)

    def configure(self, **kw):
        kw.pop("fg_color", None); kw.pop("border_color", None)
        kw.pop("font", None); kw.pop("corner_radius", None)
        kw.pop("text_color", None)
        if kw:
            try: super().configure(**kw)
            except Exception: pass


# ─── CTkTextbox ──────────────────────────────────────────────────────

class CTkTextbox(tk.Text):
    def __init__(self, master=None, font=None, fg_color=None, wrap="word",
                 border_width=0, border_color=None, text_color=None,
                 corner_radius=None, **kw):
        p = _patch_scrollable(master)
        bg = fg_color or _CARD
        fg = text_color or _TXT
        f  = tuple(font) if font else ("Consolas", 10)
        super().__init__(p, bg=bg, fg=fg, font=f, wrap=wrap,
                         relief="flat", bd=1,
                         highlightbackground=_BORDER, highlightthickness=1,
                         insertbackground=fg, selectbackground=_AZUL)

    def configure(self, state=None, fg_color=None, text_color=None, **kw):
        cfg = {}
        if state:      cfg["state"]  = state
        if fg_color:   cfg["bg"]     = fg_color
        if text_color: cfg["fg"]     = text_color
        kw.pop("font", None); kw.pop("corner_radius", None)
        kw.pop("border_color", None); kw.pop("border_width", None)
        cfg.update({k: v for k, v in kw.items()})
        if cfg:
            try: super().configure(**cfg)
            except Exception: pass


# ─── CTkProgressBar ──────────────────────────────────────────────────

class CTkProgressBar(ttk.Progressbar):
    """Wrapper: .set(0..1) → ttk.Progressbar value 0..100."""
    def __init__(self, master=None, height=None, fg_color=None,
                 progress_color=None, corner_radius=None, **kw):
        p = _patch_scrollable(master)
        s = ttk.Style()
        s.configure("PC.Horizontal.TProgressbar",
                     troughcolor=_BORDER, background=_AZUL,
                     thickness=height or 6)
        super().__init__(p, orient="horizontal", length=200,
                         mode="determinate", maximum=100,
                         style="PC.Horizontal.TProgressbar")


    def set(self, value):
        """value en rango 0.0 – 1.0"""
        self["value"] = float(value) * 100

    def get(self):
        return self["value"] / 100

    def configure(self, cnf=None, **kw):
        if cnf is not None and isinstance(cnf, dict):
            kw.update(cnf)
        kw.pop("fg_color", None); kw.pop("progress_color", None)
        kw.pop("corner_radius", None); kw.pop("height", None)
        if kw:
            try: super().configure(**kw)
            except Exception: pass


# ─── CTkSlider ───────────────────────────────────────────────────────

class CTkSlider(ttk.Scale):
    def __init__(self, master=None, from_=0, to=1, number_of_steps=10,
                 fg_color=None, progress_color=None, button_color=None,
                 corner_radius=None, command=None, **kw):
        p = _patch_scrollable(master)
        super().__init__(p, from_=from_, to=to, orient="horizontal")
        if command:
            self.configure(command=lambda v: command(float(v)))

    def set(self, value):
        super().set(value)

    def configure(self, cnf=None, command=None, **kw):
        if cnf is not None and isinstance(cnf, dict):
            kw.update(cnf)
        if command:
            super().configure(command=lambda v: command(float(v)))
        kw.pop("fg_color", None); kw.pop("progress_color", None)
        kw.pop("button_color", None); kw.pop("corner_radius", None)
        if kw:
            try: super().configure(**kw)
            except Exception: pass



# ─── CTk (app base) ──────────────────────────────────────────────────

class CTk(tk.Tk):
    def __init__(self):
        super().__init__()
        super().configure(bg=_BG)
        # Apply ttk theme
        s = ttk.Style(self)
        try:
            s.theme_use("clam")
        except Exception:
            pass
        s.configure("TCombobox", fieldbackground=_CARD2, background=_PANEL,
                    selectbackground=_AZUL, selectforeground="#FFFFFF",
                    font=_FONT)
        s.configure("Treeview", font=_FONT, rowheight=22,
                    background=_CARD, foreground=_TXT, fieldbackground=_CARD)
        s.configure("Treeview.Heading", font=_FONT_B,
                    background="#D4D4D4", foreground=_TXT)
        s.map("Treeview", background=[("selected", _AZUL)],
              foreground=[("selected", "#FFFFFF")])

    def configure(self, fg_color=None, **kw):
        if fg_color:
            kw["bg"] = fg_color
        kw.pop("corner_radius", None)
        kw.pop("border_width", None)
        if kw:
            try: super().configure(**kw)
            except Exception: pass


# ─── CTkToplevel ─────────────────────────────────────────────────────

class CTkToplevel(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg=_AZUL)

    def configure(self, fg_color=None, **kw):
        if fg_color: kw["bg"] = fg_color
        kw.pop("corner_radius", None)
        if kw:
            try: super().configure(**kw)
            except Exception: pass


# ─── Helpers de módulo ───────────────────────────────────────────────

def set_appearance_mode(mode): pass   # No-op: always system
def set_default_color_theme(t): pass  # No-op

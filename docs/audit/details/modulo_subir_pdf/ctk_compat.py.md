# Documentación Técnica: `modulo_subir_pdf/ctk_compat.py`

- **Ruta relativa:** `modulo_subir_pdf/ctk_compat.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 452
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `CTkFont` (Línea 53)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, family, size, weight)` (Línea 54): Sin docstring.
  - `def __iter__(self)` (Línea 56): Sin docstring.
  - `def __repr__(self)` (Línea 58): Sin docstring.

#### Clase `CTkFrame` (Línea 64)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, master, fg_color, corner_radius, border_width, border_color, height, width, scrollbar_button_color)` (Línea 65): Sin docstring.
  - `def configure(self, cnf, fg_color)` (Línea 77): Sin docstring.

#### Clase `CTkScrollableFrame` (Línea 91)
- **Docstring:** _Scrollable frame — los widgets hijos se añaden al inner frame.
Se expone como contenedor normal de grid/pack layout._
- **Métodos:**
  - `def __init__(self, master, fg_color, scrollbar_button_color)` (Línea 96): Sin docstring.
  - `def _on_inner_cfg(self, e)` (Línea 112): Sin docstring.
  - `def _on_canvas_cfg(self, e)` (Línea 115): Sin docstring.
  - `def _on_wheel(self, e)` (Línea 118): Sin docstring.
  - `def grid_columnconfigure(self)` (Línea 123): Sin docstring.
  - `def grid_rowconfigure(self)` (Línea 124): Sin docstring.
  - `def get_inner(self)` (Línea 129): Sin docstring.

#### Clase `CTkLabel` (Línea 134)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, master, text, font, text_color, fg_color, anchor, wraplength, corner_radius, justify)` (Línea 135): Sin docstring.
  - `def configure(self, cnf, text, text_color, fg_color)` (Línea 146): Sin docstring.

#### Clase `CTkButton` (Línea 163)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, master, text, font, fg_color, hover_color, text_color, border_color, border_width, corner_radius, width, height, state, anchor, command)` (Línea 164): Sin docstring.
  - `def configure(self, text, fg_color, text_color, state, hover_color)` (Línea 190): Sin docstring.

#### Clase `CTkEntry` (Línea 208)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, master, placeholder_text, show, fg_color, border_color, text_color, height, width, corner_radius)` (Línea 209): Sin docstring.
  - `def configure(self, show, placeholder_text, state, values)` (Línea 223): Sin docstring.

#### Clase `_ComboBase` (Línea 239)
- **Docstring:** _Base compartida para CTkComboBox y CTkOptionMenu._
- **Métodos:**
  - `def __init__(self, master, values, state, command, width, height)` (Línea 241): Sin docstring.
  - `def configure(self, values, state, command)` (Línea 253): Sin docstring.
  - `def set(self, value)` (Línea 272): Sin docstring.

#### Clase `CTkComboBox` (Línea 278)
- **Docstring:** _Sin docstring._

#### Clase `CTkOptionMenu` (Línea 281)
- **Docstring:** _Sin docstring._

#### Clase `CTkCheckBox` (Línea 287)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, master, text, font, text_color, fg_color, border_color, corner_radius)` (Línea 288): Sin docstring.
  - `def get(self)` (Línea 299): Sin docstring.
  - `def select(self)` (Línea 302): Sin docstring.
  - `def deselect(self)` (Línea 303): Sin docstring.
  - `def configure(self)` (Línea 305): Sin docstring.

#### Clase `CTkTextbox` (Línea 316)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, master, font, fg_color, wrap, border_width, border_color, text_color, corner_radius)` (Línea 317): Sin docstring.
  - `def configure(self, state, fg_color, text_color)` (Línea 329): Sin docstring.

#### Clase `CTkProgressBar` (Línea 344)
- **Docstring:** _Wrapper: .set(0..1) → ttk.Progressbar value 0..100._
- **Métodos:**
  - `def __init__(self, master, height, fg_color, progress_color, corner_radius)` (Línea 346): Sin docstring.
  - `def set(self, value)` (Línea 358): value en rango 0.0 – 1.0
  - `def get(self)` (Línea 362): Sin docstring.
  - `def configure(self, cnf)` (Línea 365): Sin docstring.

#### Clase `CTkSlider` (Línea 377)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, master, from_, to, number_of_steps, fg_color, progress_color, button_color, corner_radius, command)` (Línea 378): Sin docstring.
  - `def set(self, value)` (Línea 386): Sin docstring.
  - `def configure(self, cnf, command)` (Línea 389): Sin docstring.

#### Clase `CTk` (Línea 404)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self)` (Línea 405): Sin docstring.
  - `def configure(self, fg_color)` (Línea 424): Sin docstring.

#### Clase `CTkToplevel` (Línea 436)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def __init__(self, master)` (Línea 437): Sin docstring.
  - `def configure(self, fg_color)` (Línea 441): Sin docstring.

### Funciones independientes:

#### `def _ignore()` (Línea 35)
- **Propósito:** Descarta kwargs CTk que tkinter no acepta.
- **Firma:** `def _ignore()`
- **Retorno / Efectos:** Consulta código fuente.

#### `def _patch_scrollable(master)` (Línea 44)
- **Propósito:** Si master es un CTkScrollableFrame (o cualquier contenedor con get_inner), redirigir al inner frame.
- **Firma:** `def _patch_scrollable(master)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def set_appearance_mode(mode)` (Línea 451)
- **Propósito:** Sin docstring.
- **Firma:** `def set_appearance_mode(mode)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def set_default_color_theme(t)` (Línea 452)
- **Propósito:** Sin docstring.
- **Firma:** `def set_default_color_theme(t)`
- **Retorno / Efectos:** Consulta código fuente.

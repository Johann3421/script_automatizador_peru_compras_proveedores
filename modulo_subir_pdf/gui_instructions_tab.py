import customtkinter as ctk

def build_instructions_tab(parent):
    """
    Construye la pestaña de Instrucciones y Señalización de Uso para personal de oficina.
    """
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_rowconfigure(0, weight=1)

    container = ctk.CTkScrollableFrame(parent, fg_color="transparent")
    container.grid(row=0, column=0, padx=16, pady=16, sticky="nsew")
    container.grid_columnconfigure(0, weight=1)

    # ── TÍTULO Y PRESENTACIÓN ──
    title_frame = ctk.CTkFrame(container, fg_color="#252538", corner_radius=8)
    title_frame.pack(fill="x", pady=(0, 12), ipadx=12, ipady=10)

    ctk.CTkLabel(
        title_frame,
        text="Guía de Uso Rápido — Perú Compras Bot",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color="#f8fafc",
    ).pack(anchor="w", padx=12, pady=(4, 2))

    ctk.CTkLabel(
        title_frame,
        text="Manual de operación para automatización de carga de ofertas y fichas técnicas.",
        font=ctk.CTkFont(size=12),
        text_color="#94a3b8",
    ).pack(anchor="w", padx=12, pady=(0, 4))

    # ── SECCIÓN 1: PASOS DE OPERACIÓN ──
    steps_frame = ctk.CTkFrame(container, fg_color="#252538", corner_radius=8)
    steps_frame.pack(fill="x", pady=6, ipadx=12, ipady=10)

    ctk.CTkLabel(
        steps_frame,
        text="Flujo de Trabajo (3 Pasos)",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#2563eb",
    ).pack(anchor="w", padx=12, pady=(4, 6))

    steps = [
        ("1. Credenciales y Archivo Excel", "Ingresar usuario/clave de Perú Compras y seleccionar el archivo .xlsx. El sistema autodetectará las columnas."),
        ("2. Selección de Catálogo", "Elegir el Acuerdo Marco, Catálogo Electrónico y Categoría correspondientes a los productos del Excel."),
        ("3. Iniciar Procesamiento", "Hacer clic en 'Iniciar Procesamiento' en la parte inferior. El bot resolverá el CAPTCHA e iterará las filas."),
    ]

    for title, desc in steps:
        step_box = ctk.CTkFrame(steps_frame, fg_color="#1e1e2e", corner_radius=6)
        step_box.pack(fill="x", padx=12, pady=4, ipadx=8, ipady=6)
        ctk.CTkLabel(
            step_box,
            text=title,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#f8fafc",
        ).pack(anchor="w", padx=8, pady=(2, 0))
        ctk.CTkLabel(
            step_box,
            text=desc,
            font=ctk.CTkFont(size=11),
            text_color="#94a3b8",
            wraplength=700,
            justify="left",
        ).pack(anchor="w", padx=8, pady=(0, 2))

    # ── SECCIÓN 2: FORMATO DEL EXCEL ──
    excel_frame = ctk.CTkFrame(container, fg_color="#252538", corner_radius=8)
    excel_frame.pack(fill="x", pady=6, ipadx=12, ipady=10)

    ctk.CTkLabel(
        excel_frame,
        text="Estructura Requerida del Archivo Excel",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#2563eb",
    ).pack(anchor="w", padx=12, pady=(4, 6))

    ctk.CTkLabel(
        excel_frame,
        text="El archivo .xlsx debe incluir al menos las siguientes dos columnas con cualquier nombre descriptivo:",
        font=ctk.CTkFont(size=11),
        text_color="#94a3b8",
    ).pack(anchor="w", padx=12, pady=(0, 6))

    table_box = ctk.CTkFrame(excel_frame, fg_color="#1e1e2e", corner_radius=6)
    table_box.pack(fill="x", padx=12, pady=4, ipadx=8, ipady=6)

    headers = [("Columna", "Ejemplo de Encabezado", "Descripción")]
    data = [
        ("N° de Parte / Código", "Part Number, N° PARTE, CODIGO", "Código único del producto del fabricante"),
        ("Precio / PDF", "PRECIO, RUTA_PDF, FICHA", "Precio de lista ofertado o ruta local al archivo PDF"),
    ]

    for col, ex, desc in data:
        row_str = f"• {col}: Encabezado típico '{ex}' — {desc}"
        ctk.CTkLabel(
            table_box,
            text=row_str,
            font=ctk.CTkFont(size=11),
            text_color="#f8fafc",
            anchor="w",
        ).pack(anchor="w", padx=8, pady=2)

    # ── SECCIÓN 3: LEYENDA DE COLORES EN RESULTADOS ──
    legend_frame = ctk.CTkFrame(container, fg_color="#252538", corner_radius=8)
    legend_frame.pack(fill="x", pady=6, ipadx=12, ipady=10)

    ctk.CTkLabel(
        legend_frame,
        text="Significado de Colores en Excel Procesado",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#2563eb",
    ).pack(anchor="w", padx=12, pady=(4, 6))

    colors_info = [
        ("🟢 Verde", "Cargado Correctamente", "El precio o PDF se registró con éxito en Perú Compras."),
        ("🟡 Amarillo", "No Encontrado", "El N° de parte no fue ubicado en la categoría seleccionada."),
        ("🔴 Rojo", "Excede Límite Máximo", "El precio ofertado supera el tope máximo permitido por Perú Compras."),
        ("🔵 Azul", "Por debajo de Mínimo", "El precio ofertado está por debajo del límite mínimo permitido."),
    ]

    for tag, title, desc in colors_info:
        c_box = ctk.CTkFrame(legend_frame, fg_color="#1e1e2e", corner_radius=6)
        c_box.pack(fill="x", padx=12, pady=3, ipadx=8, ipady=4)
        ctk.CTkLabel(
            c_box,
            text=f"{tag} — {title}",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#f8fafc",
        ).pack(anchor="w", padx=8, pady=(2, 0))
        ctk.CTkLabel(
            c_box,
            text=desc,
            font=ctk.CTkFont(size=11),
            text_color="#94a3b8",
        ).pack(anchor="w", padx=8, pady=(0, 2))

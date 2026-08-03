import customtkinter as ctk

def build_instructions_tab(parent):
    """
    Construye la vista de Guía e Instrucciones para personal de oficina con paleta corporativa sobria.
    """
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_rowconfigure(0, weight=1)

    container = ctk.CTkScrollableFrame(parent, fg_color="transparent")
    container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    container.grid_columnconfigure(0, weight=1)

    # ── ENCABEZADO DE GUÍA ──
    head_box = ctk.CTkFrame(container, fg_color="#1f2937", corner_radius=8, border_width=1, border_color="#374151")
    head_box.pack(fill="x", pady=(0, 14), ipadx=14, ipady=12)

    ctk.CTkLabel(
        head_box,
        text="Manual de Operación — Perú Compras Bot",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color="#f9fafb",
    ).pack(anchor="w", padx=12, pady=(2, 2))

    ctk.CTkLabel(
        head_box,
        text="Guía paso a paso para la automatización de ofertas, carga de fichas técnicas en PDF y validación de stock.",
        font=ctk.CTkFont(size=12),
        text_color="#9ca3af",
    ).pack(anchor="w", padx=12, pady=(0, 2))

    # ── PASOS DE OPERACIÓN ──
    steps_box = ctk.CTkFrame(container, fg_color="#1f2937", corner_radius=8, border_width=1, border_color="#374151")
    steps_box.pack(fill="x", pady=8, ipadx=14, ipady=12)

    ctk.CTkLabel(
        steps_box,
        text="Flujo de Trabajo Simplificado",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#2563eb",
    ).pack(anchor="w", padx=12, pady=(2, 8))

    steps_data = [
        ("Paso 1: Credenciales y Excel", "Complete el usuario y contraseña de Perú Compras, y seleccione el archivo .xlsx. El sistema detectará las columnas automáticamente."),
        ("Paso 2: Selección de Catálogo", "Indique el Acuerdo Marco, Catálogo y Categoría en los desplegables en cascada."),
        ("Paso 3: Ejecución", "Haga clic en 'Iniciar Procesamiento' en la barra inferior. El bot gestionará el inicio de sesión y la carga de datos."),
    ]

    for title, desc in steps_data:
        card = ctk.CTkFrame(steps_box, fg_color="#111827", corner_radius=6)
        card.pack(fill="x", padx=12, pady=4, ipadx=10, ipady=8)

        ctk.CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#f9fafb",
        ).pack(anchor="w", padx=8, pady=(2, 0))

        ctk.CTkLabel(
            card,
            text=desc,
            font=ctk.CTkFont(size=11),
            text_color="#9ca3af",
            wraplength=680,
            justify="left",
        ).pack(anchor="w", padx=8, pady=(0, 2))

    # ── ESTRUCTURA EXCEL ──
    fmt_box = ctk.CTkFrame(container, fg_color="#1f2937", corner_radius=8, border_width=1, border_color="#374151")
    fmt_box.pack(fill="x", pady=8, ipadx=14, ipady=12)

    ctk.CTkLabel(
        fmt_box,
        text="Requisitos del Archivo Excel (.xlsx)",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#2563eb",
    ).pack(anchor="w", padx=12, pady=(2, 6))

    cols_info = [
        ("N° de Parte / Código", "Part Number, N° PARTE, CODIGO, MPN", "Identificador único de producto"),
        ("Precio Ofertado", "PRECIO, PRECIO LISTA, OFERTA", "Monto numérico a ofertar"),
        ("Ficha Técnica PDF", "RUTA_PDF, PDF, FICHA", "Ruta local completa al archivo PDF a subir"),
    ]

    table_frame = ctk.CTkFrame(fmt_box, fg_color="#111827", corner_radius=6)
    table_frame.pack(fill="x", padx=12, pady=4, ipadx=8, ipady=6)

    for col, typ, dsc in cols_info:
        item_text = f"• {col}: Nombre en Excel '{typ}' ({dsc})"
        ctk.CTkLabel(
            table_frame,
            text=item_text,
            font=ctk.CTkFont(size=11),
            text_color="#f9fafb",
        ).pack(anchor="w", padx=8, pady=3)

    # ── CÓDIGO DE COLORES ──
    color_box = ctk.CTkFrame(container, fg_color="#1f2937", corner_radius=8, border_width=1, border_color="#374151")
    color_box.pack(fill="x", pady=8, ipadx=14, ipady=12)

    ctk.CTkLabel(
        color_box,
        text="Leyenda de Resultados en Excel",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#2563eb",
    ).pack(anchor="w", padx=12, pady=(2, 6))

    legend = [
        ("Verde", "Éxito", "Operación completada en Perú Compras."),
        ("Amarillo", "No Ubicado", "El código de producto no existe en el catálogo."),
        ("Rojo", "Límite Máximo", "El precio superó el tope permitido."),
        ("Azul", "Límite Mínimo", "El precio estuvo por debajo del mínimo."),
    ]

    for color_name, status, detail in legend:
        row_c = ctk.CTkFrame(color_box, fg_color="#111827", corner_radius=6)
        row_c.pack(fill="x", padx=12, pady=3, ipadx=8, ipady=4)

        ctk.CTkLabel(
            row_c,
            text=f"[{color_name}] — {status}: {detail}",
            font=ctk.CTkFont(size=11),
            text_color="#f9fafb",
        ).pack(anchor="w", padx=8, pady=2)

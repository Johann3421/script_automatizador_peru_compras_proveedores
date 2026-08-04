import customtkinter as ctk

_C_DEFAULT = {
    'bg':      '#F4F7FA',
    'card':    '#FFFFFF',
    'card2':   '#F0F4F8',
    'border':  '#C8D6E5',
    'border2': '#DDE4ED',
    'txt':     '#1A2332',
    'txt2':    '#4A6080',
    'txt3':    '#7A90A8',
    'accent':  '#0D6EAA',
    'success': '#1E6E3A',
    'danger':  '#B91C1C',
    'warn':    '#92400E',
    'sep':     '#E2EAF3',
}

def build_instructions_tab(parent, C=None):
    if C is None:
        C = _C_DEFAULT
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_rowconfigure(0, weight=1)
    container = ctk.CTkScrollableFrame(parent, fg_color='transparent', scrollbar_button_color=C['border'])
    container.grid(row=0, column=0, padx=16, pady=12, sticky='nsew')
    container.grid_columnconfigure(0, weight=1)

    def _section_card(title, subtitle=None):
        card = ctk.CTkFrame(container, fg_color=C['card'], corner_radius=8, border_width=1, border_color=C['border'])
        card.pack(fill='x', pady=6)
        card.columnconfigure(0, weight=1)
        header = ctk.CTkFrame(card, fg_color=C['card2'], corner_radius=0)
        header.pack(fill='x')
        ctk.CTkLabel(header, text=title, font=ctk.CTkFont(size=13, weight='bold'), text_color=C['txt'], anchor='w').pack(anchor='w', padx=16, pady=(10, 2 if subtitle else 10))
        if subtitle:
            ctk.CTkLabel(header, text=subtitle, font=ctk.CTkFont(size=11), text_color=C['txt3'], anchor='w').pack(anchor='w', padx=16, pady=(0, 10))
        ctk.CTkFrame(card, fg_color=C['sep'], height=1).pack(fill='x')
        return card

    head = ctk.CTkFrame(container, fg_color=C['accent'], corner_radius=8)
    head.pack(fill='x', pady=(0, 12))
    ctk.CTkLabel(head, text='Manual de Operacion -- Peru Compras Bot', font=ctk.CTkFont(size=16, weight='bold'), text_color='#FFFFFF').pack(anchor='w', padx=16, pady=(14, 2))
    ctk.CTkLabel(head, text='Guia para automatizar la carga de fichas tecnicas PDF, actualizacion de stock y subida de precios en el portal.', font=ctk.CTkFont(size=11), text_color='#C8DFF0', wraplength=760, justify='left').pack(anchor='w', padx=16, pady=(0, 14))

    flow = _section_card('Flujo de Trabajo -- Carga de PDFs', 'Siga estos pasos en orden:')
    steps = [
        ('1. Credenciales', 'Ingrese usuario y contrasena de Peru Compras. La contrasena se puede mostrar/ocultar con el boton.'),
        ('2. Archivo Excel', 'Haga clic en Seleccionar .xlsx, elija el archivo y confirme la pestana y columna de N de Parte.'),
        ('3. Catalogo', 'Seleccione el Catalogo Electronico, Categoria y Estado en los desplegables en cascada.'),
        ('4. Opciones', 'Ajuste la pausa entre productos con el slider. Active Mostrar navegador solo para depuracion.'),
        ('5. Iniciar', 'Presione Iniciar Procesamiento en la barra inferior. El bot gestionara el inicio de sesion y carga automaticamente.'),
    ]
    for i, (step, desc) in enumerate(steps):
        rw = ctk.CTkFrame(flow, fg_color=C['card2'] if i % 2 else C['card'], corner_radius=0)
        rw.pack(fill='x')
        ctk.CTkLabel(rw, text=step, font=ctk.CTkFont(size=11, weight='bold'), text_color=C['accent'], anchor='w').pack(anchor='w', padx=16, pady=(8, 1))
        ctk.CTkLabel(rw, text=desc, font=ctk.CTkFont(size=11), text_color=C['txt2'], anchor='w', justify='left', wraplength=700).pack(anchor='w', padx=16, pady=(0, 8))

    excel_card = _section_card('Formato del Archivo Excel (.xlsx)', 'El archivo debe contener al menos estas columnas:')
    cols = [
        ('N de Parte / Codigo',  'Part Number, N PARTE, CODIGO, MPN',    'Identificador unico del producto'),
        ('Precio Ofertado',       'PRECIO, PRECIO LISTA, OFERTA',          'Monto numerico a ofertar'),
        ('Ficha Tecnica PDF',     'RUTA_PDF, PDF, FICHA',                  'Ruta local al archivo PDF'),
    ]
    hdr = ctk.CTkFrame(excel_card, fg_color=C['border2'], corner_radius=0)
    hdr.pack(fill='x')
    for text, w in [('Campo', 200), ('Nombres aceptados', 280), ('Descripcion', 220)]:
        ctk.CTkLabel(hdr, text=text, font=ctk.CTkFont(size=10, weight='bold'), text_color=C['txt3'], width=w, anchor='w').pack(side='left', padx=8, pady=6)
    for i, (col, names, desc) in enumerate(cols):
        rw = ctk.CTkFrame(excel_card, fg_color=C['card2'] if i % 2 else C['card'], corner_radius=0)
        rw.pack(fill='x')
        ctk.CTkLabel(rw, text=col, font=ctk.CTkFont(size=11, weight='bold'), text_color=C['txt'], width=200, anchor='w').pack(side='left', padx=8, pady=8)
        ctk.CTkLabel(rw, text=names, font=ctk.CTkFont(size=10), text_color=C['txt2'], width=280, anchor='w').pack(side='left', padx=4, pady=8)
        ctk.CTkLabel(rw, text=desc, font=ctk.CTkFont(size=10), text_color=C['txt3'], anchor='w').pack(side='left', padx=4, pady=8)

    ley_card = _section_card('Leyenda de Resultados en el Log')
    legend = [
        (C['success'], 'Exito',          'Operacion completada correctamente.'),
        (C['warn'],    'No Ubicado',      'El codigo de producto no existe en el catalogo.'),
        (C['danger'],  'Limite Maximo',   'El precio ofertado supera el tope maximo permitido.'),
        (C['accent'],  'Limite Minimo',   'El precio ofertado esta por debajo del minimo.'),
        (C['txt3'],    'Omitido',         'El registro fue omitido por no cumplir los filtros.'),
    ]
    for i, (color, status, detail) in enumerate(legend):
        rw = ctk.CTkFrame(ley_card, fg_color=C['card2'] if i % 2 else C['card'], corner_radius=0)
        rw.pack(fill='x')
        badge = ctk.CTkFrame(rw, fg_color=color, corner_radius=4, width=12, height=12)
        badge.pack(side='left', padx=(16, 8), pady=12)
        badge.pack_propagate(False)
        ctk.CTkLabel(rw, text=status, font=ctk.CTkFont(size=11, weight='bold'), text_color=C['txt'], width=110, anchor='w').pack(side='left', padx=(0, 8), pady=10)
        ctk.CTkLabel(rw, text=detail, font=ctk.CTkFont(size=11), text_color=C['txt2'], anchor='w').pack(side='left', pady=10)

    stock_card = _section_card('Modulo -- Analisis de Stock', 'Para actualizar stock, cobertura y plazos:')
    stock_steps = [
        ('Credenciales propias', 'El modulo de stock usa credenciales independientes del modulo PDF.'),
        ('Excel de stock',       'Cargue un Excel con columnas: Parte, Stock, Ficha (numero de ficha en el portal).'),
        ('Plantilla',            'Use Descargar Plantilla para obtener el formato correcto.'),
        ('Filtros del portal',   'Seleccione Acuerdo Marco > Catalogo > Categoria antes de iniciar.'),
    ]
    for i, (step, desc) in enumerate(stock_steps):
        rw = ctk.CTkFrame(stock_card, fg_color=C['card2'] if i % 2 else C['card'], corner_radius=0)
        rw.pack(fill='x')
        ctk.CTkLabel(rw, text=step, font=ctk.CTkFont(size=11, weight='bold'), text_color=C['accent'], width=150, anchor='w').pack(side='left', padx=16, pady=8)
        ctk.CTkLabel(rw, text=desc, font=ctk.CTkFont(size=11), text_color=C['txt2'], anchor='w', wraplength=600).pack(side='left', padx=8, pady=8)

# Script Automatizador Peru Compras - Proveedores

Bot de automatización para carga de ofertas en la plataforma **Catálogos Electrónicos de Peru Compras**.  
Desarrollado en Python con **CustomTkinter** (UI) + **Playwright** (navegador automatizado) + **Tesseract OCR** (CAPTCHA).

---

## Requisitos

| Herramienta | Versión | Descarga |
|---|---|---|
| Python | 3.12.x | https://www.python.org/downloads/ |
| Tesseract OCR | 5.x | https://github.com/UB-Mannheim/tesseract/wiki |
| Git | Cualquiera | https://git-scm.com/downloads |

> **Importante:** Al instalar Python, desactivar el alias de Microsoft Store.  
> Ir a *Configuración > Aplicaciones > Configuración avanzada de aplicaciones > Alias de ejecución de aplicaciones* y desactivar `python.exe` / `python3.exe`.

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Johann3421/script_automatizador_peru_compras_proveedores.git
cd script_automatizador_peru_compras_proveedores

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv
.\venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar navegadores de Playwright
playwright install chromium

# 5. Verificar que Tesseract OCR está instalado y accesible
tesseract --version

# 6. (Opcional) Extraer opciones del catálogo actualizadas
python extract_catalog.py
```

---

## Estructura del proyecto

```
script_automatizador_peru_compras_proveedores/
├── main.py                     # Punto de entrada — UI principal
├── requirements.txt            # Dependencias Python
├── catalog_options.json        # Opciones de catálogo (extraídas con extract_catalog.py)
├── extract_catalog.py          # Script para extraer catálogo actualizado
├── build_exe.py                # Script para compilar a .exe (PyInstaller)
├── automation/
│   ├── browser.py              # Inicialización/cierre de Playwright
│   ├── login.py                # Login + resolución de CAPTCHA (OCR)
│   ├── navigation.py           # Navegación por catálogo (Select2, dropdowns)
│   └── offer_loop.py           # Bucle de procesamiento de ofertas
├── utils/
│   ├── excel_parser.py         # Parseo de Excel (multi-hoja, detección de encabezados)
│   ├── excel_writer.py         # Escritura de Excel coloreado con resultados
│   └── logger.py               # Logger thread-safe con cola
└── .gitignore
```

---

## Uso

### 1. Preparar el archivo Excel

El Excel debe contener al menos dos columnas:

| N° de Parte | Precio |
|---|---|
| ABC123 | 1500 |
| DEF456 | 2000 |

Los encabezados pueden empezar en cualquier fila (fila 7, 8, etc.) — el programa los detecta automáticamente.

### 2. Ejecutar la app

```bash
python main.py
```

### 3. Flujo dentro de la app

1. **Credenciales:** Ingresar usuario y contraseña de Peru Compras.
2. **Archivo Excel:** Seleccionar el `.xlsx`, elegir la **pestaña** correcta y mapear las columnas de *N° de Parte* y *Precio* (se auto-detectan si coinciden con "Part Number" y "PRECIO DE LISTA").
3. **Catálogo:** Seleccionar Acuerdo Marco → Catálogo Electrónico → Categoría.
4. **Iniciar:** Click en *Iniciar Procesamiento*.

### 4. Resultados

Al finalizar, se genera un archivo `*_procesado_YYYYMMDD_HHMMSS.xlsx` con las filas coloreadas:

| Color | Significado |
|---|---|
| 🟢 Verde | Precio cargado correctamente |
| 🟡 Amarillo | Producto no encontrado en el catálogo |
| 🔴 Rojo | Precio excede el límite máximo |
| 🔵 Azul | Precio por debajo del mínimo permitido |

---

## Compilación a .exe (para distribuir sin Python)

```bash
python build_exe.py
```

El ejecutable se genera en la carpeta `dist/`.  
Para crear un instalador con Inno Setup, usar el script `installer.iss`.

> **Nota:** El .exe incluye Chromium (~300 MB) y Tesseract (~100 MB), por lo que el resultado pesa ~1.5 GB.

---

## Dependencias principales

```
customtkinter          # UI moderna
playwright             # Automatización de navegador
openpyxl               # Lectura/escritura de Excel
pytesseract            # OCR para CAPTCHA
Pillow                 # Procesamiento de imágenes
```

Ver `requirements.txt` para la lista completa.

---

## Solución de problemas

### "No se encontró Python"
Desactivar alias de Microsoft Store (ver Requisitos).

### "Tesseract not found"
Instalar Tesseract OCR 5.x y agregarlo al PATH del sistema.

### "Playwright browsers not found"
Ejecutar `playwright install chromium` en la terminal.

### Error de CAPTCHA
El sistema intenta resolverlo automáticamente con OCR (5 intentos). Si falla, se muestra un panel para ingreso manual.

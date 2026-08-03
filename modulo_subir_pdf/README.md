# Módulo: Subir PDF — Peru Compras

## Propósito

Este módulo es **completamente independiente** del flujo principal y del módulo
`modulo_modificar_productos/`. No modifica ningún archivo del proyecto principal.

Su objetivo es automatizar **únicamente la subida del PDF** de ficha técnica en
las fichas de producto de Peru Compras. El flujo se detiene después de guardar
los cambios — **no agrega certificaciones ISO 9001/14001**.

Si necesitás subir PDFs + agregar certificaciones, usá `modulo_modificar_productos/`.
Si solo necesitás subir PDFs (las certificaciones ya están), usá este módulo.

---

## Estructura del Módulo

```
modulo_subir_pdf/
├── README.md                  ← Este archivo
├── run_subir_pdf.py           ← Launcher: `python run_subir_pdf.py`
├── main_subir_pdf.py          ← Entry point: UI + orquestación
├── combinaciones_computadoras.json  ← Datos de dropdowns en cascada
├── automation_mod/
│   ├── __init__.py
│   ├── bulk_subir_pdf.py      ← Flujo masivo vía API + navegación directa
│   └── navegacion_productos.py← Funciones de navegación (login, dropdowns, PDF)
├── utils_mod/
│   ├── __init__.py
│   ├── excel_parser_mod.py    ← Parser Excel con detección de headers
│   ├── excel_writer_mod.py    ← Escritor de Excel coloreado
│   └── logger_mod.py          ← Logger thread-safe
└── docs/
    └── FLUJO_MODIFICAR.md     ← Documentación del flujo
```

---

## Flujo General

```
1. Login en Peru Compras
2. Navega a t_CatalogoProductoMarca
3. Aplica dropdowns en cascada (Acuerdo → Catálogo → Categoría → Estado)
4. Por cada fila del Excel:
   a. Busca el producto por N° de Parte (vía API o UI)
   b. Abre la ficha de edición
   c. Sube el PDF de ficha técnica
   d. Guarda los cambios
   e. Retorna a la lista
5. Escribe resultados de vuelta al Excel (coloreado)
```

---

## Diferencias con `modulo_modificar_productos/`

| Aspecto                | modulo_modificar_productos  | modulo_subir_pdf (este)         |
|------------------------|----------------------------|---------------------------------|
| Sube PDF               | ✓                          | ✓                               |
| Agrega ISO 9001/14001  | ✓                          | ✗ (no lo hace)                  |
| Credentials por defecto| ✓                          | ✓ (mismas)                      |
| Interfaz               | Idéntica                   | Idéntica                        |

---

## Cómo empezar

```bash
# Desde la raíz del proyecto:
cd modulo_subir_pdf
python run_subir_pdf.py
```

> **Nota**: Este módulo usa las mismas dependencias del proyecto principal
> (Playwright, customtkinter, openpyxl). No requiere instalar nada adicional.

### Credenciales por defecto

- **Usuario**: `almerco.03`
- **Contraseña**: `4lm3rKenYa@#`

(Pueden sobrescribirse en la UI antes de iniciar.)

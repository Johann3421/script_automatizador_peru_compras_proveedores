# Módulo: Modificar Productos — Peru Compras

## Propósito

Este módulo es **completamente independiente** del flujo de subida de precios (`main.py`).
No modifica ningún archivo del proyecto principal.

Su objetivo es automatizar la **modificación de fichas de producto** en Peru Compras:
1. Subir un nuevo PDF de ficha técnica
2. Agregar/actualizar certificaciones del producto
3. Guardar los cambios

Funciona con una **cuenta diferente** y accede a una sección distinta del portal.

---

## Estructura del Módulo

```
modulo_modificar_productos/
├── README.md                  ← Este archivo
├── main_modificar.py          ← Entry point: UI + orquestación
├── automation/
│   ├── __init__.py
│   ├── login_mod.py           ← Login para esta cuenta (reutiliza lógica del proyecto)
│   ├── navegacion_productos.py← Navega a la sección de gestión de productos
│   └── modificar_loop.py      ← Bucle: por cada producto → sube PDF + cert + guarda
├── utils/
│   ├── __init__.py
│   ├── excel_parser_mod.py    ← Lee el Excel con la lista de productos a modificar
│   └── logger_mod.py          ← Logger thread-safe
└── docs/
    └── FLUJO_MODIFICAR.md     ← Documentación del flujo de este módulo
```

---

## Flujo General

```
Usuario configura en UI:
  - Credenciales (cuenta diferente)
  - Archivo Excel con lista de productos (N° Parte + ruta PDF + certificaciones)
  - Modo headless o visible

Bot ejecuta:
  1. Login en Peru Compras (misma URL, diferente cuenta)
  2. Navega a la sección de GESTIÓN DE PRODUCTOS del proveedor
     (diferente al catálogo de precios)
  3. Por cada fila del Excel:
     a. Busca el producto por N° de Parte
     b. Abre la ficha de edición
     c. Sube el PDF de ficha técnica (si se especifica)
     d. Agrega/actualiza certificaciones (si se especifica)
     e. Guarda los cambios
  4. Escribe resultados de vuelta al Excel
```

---

## Diferencias con el flujo principal (precios)

| Aspecto              | Flujo Principal (precios)         | Este Módulo (modificar productos) |
|----------------------|-----------------------------------|-----------------------------------|
| Cuenta               | Proveedor A                       | Proveedor B (diferente)           |
| Sección del portal   | t_ProductoOfertadoAmp (catálogo)  | Gestión/fichas de productos       |
| Acción               | Llenar precio en input            | Subir PDF + certificaciones       |
| Método               | HTTP inject (Inserta_ProductoOfertadoTMP) | Playwright (upload de archivos) |
| Archivos modificados | offer_loop.py, navigation.py      | **NINGUNO** (módulo independiente)|

---

## HTTP Endpoints Conocidos (del interceptor del proyecto principal)

Los siguientes endpoints ya fueron descubiertos y pueden ser útiles de referencia:

| Endpoint | Descripción |
|----------|-------------|
| `/AccesoGeneral` | Login (form-encoded con __RequestVerificationToken) |
| `/t_ProductoOfertadoAmp/_CatalogoProductoIndexJson` | DataTables de productos (form-encoded) |
| `/t_ProductoOfertadoAmp/Inserta_ProductoOfertadoTMP` | Inserta precio temporal (form-encoded) |
| `/General/ListaJ_CatalogoAcuerdo` | Lista catálogos por acuerdo (JSON) |
| `/General/ListaJ_CategoriaCatalogo` | Lista categorías por catálogo (JSON) |

Los endpoints para modificación de fichas (PDF + certificaciones) son **aún por descubrir**
mediante el interceptor (`intercept_payload.py`) en la sesión de esta cuenta.

---

## Cómo empezar

```bash
# Desde la raíz del proyecto principal:
cd modulo_modificar_productos
python main_modificar.py
```

> **Nota**: Este módulo usa las mismas dependencias del proyecto principal
> (Playwright, customtkinter, openpyxl). No requiere instalar nada adicional.

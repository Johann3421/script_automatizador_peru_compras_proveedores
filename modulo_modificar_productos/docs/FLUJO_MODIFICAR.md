# FLUJO: Módulo Modificar Productos — Peru Compras

## 1. PROPÓSITO

Automatizar la **modificación de fichas de producto** en Peru Compras para
una **cuenta diferente** a la del bot de precios. Las acciones por producto son:
1. Subir un nuevo PDF de ficha técnica
2. Agregar/actualizar certificaciones
3. Guardar los cambios

---

## 2. DIFERENCIA CON EL FLUJO PRINCIPAL (PRECIOS)

| | Bot de Precios (proyecto raíz) | Este módulo |
|---|---|---|
| Cuenta | Proveedor A | Proveedor B (diferente) |
| Sección portal | `/t_ProductoOfertadoAmp` | `/t_CatalogoProducto` (estimado) |
| Acción | Llenar precio en input | Subir PDF + certificaciones |
| Método de subida | HTTP inject (`Inserta_ProductoOfertadoTMP`) | Playwright (upload files) |
| Trigger de datos | `#btn_enviarOferta2` | `#btnGuardar` (estimado) |

---

## 3. FLUJO PASO A PASO

```
Excel (.xlsx)
  └── Columnas: N° Parte | Ruta PDF | Certificaciones

  ▼ parse_excel()

rows = [{"parte": "ABC123", "pdf": "C:/fichas/abc123.pdf", "certs": "ISO 9001"}, ...]

  ▼ init_browser(headless)

  ▼ login_y_navegar()
    → do_login() (reutiliza automation/login.py del proyecto raíz)
    → CAPTCHA OCR automático (mismo mecanismo)
    → Navega a sección de gestión de productos

  ▼ run_modificar_loop(rows)
    POR CADA FILA:
      1. buscar_producto(parte)   → localiza en la tabla
      2. abrir_edicion()          → click en botón editar
      3. subir_pdf(ruta_pdf)      → set_input_files() de Playwright
      4. agregar_certificaciones(certs) → fill en textarea
      5. guardar_cambios()        → click en #btnGuardar
      6. volver_a_lista()         → go_back()
      7. sleep(1.5s)

  ▼ Resultados
    ok            → producto modificado
    no_encontrado → parte no está en la tabla
    error_pdf     → archivo PDF no existe o no se pudo subir
    error_certs   → no se pudo escribir en el campo de certificaciones
    error_guardar → click en Guardar falló
    error         → excepción general
```

---

## 4. ENDPOINTS HTTP CONOCIDOS (del interceptor del proyecto raíz)

Estos endpoints son del catálogo de **precios** (flujo principal).
Los endpoints de **modificación de fichas** son diferentes y deben
descubrirse con `intercept_modificar.py`.

### Para descubrir:
1. Ejecutar: `python intercept_modificar.py`
2. Completar USUARIO/PASSWORD con las credenciales de esta cuenta
3. Navegar manualmente a la sección de gestión de productos
4. Editar un producto y guardar
5. Revisar `captured_modificar.json`

### Endpoints esperados (a confirmar):
- `POST /t_CatalogoProducto/Edit` — guardar cambios de la ficha
- `POST /t_CatalogoProducto/UploadPDF` — subir archivo PDF
- `POST /t_CatalogoProducto/GuardarCertificaciones` — guardar certs

---

## 5. ESTRUCTURA DE ARCHIVOS

```
modulo_modificar_productos/
├── README.md
├── main_modificar.py          ← UI customtkinter + orquestación
├── intercept_modificar.py     ← Interceptor para descubrir endpoints
├── automation/
│   ├── __init__.py
│   ├── login_mod.py           ← Reutiliza do_login() del proyecto raíz
│   ├── navegacion_productos.py← Búsqueda + edición en tabla de productos
│   └── modificar_loop.py      ← Bucle 1x1 por fila del Excel
├── utils/
│   ├── __init__.py
│   ├── excel_parser_mod.py    ← Lee Excel (parte + pdf + certs)
│   └── logger_mod.py          ← Logger thread-safe
└── docs/
    └── FLUJO_MODIFICAR.md     ← Este archivo
```

---

## 6. CÓMO EJECUTAR

```bash
# Desde la raíz del proyecto:
python modulo_modificar_productos/main_modificar.py

# O desde dentro de la carpeta del módulo:
cd modulo_modificar_productos
python main_modificar.py
```

---

## 7. PRÓXIMOS PASOS

1. **[ ] Descubrir endpoints** — ejecutar `intercept_modificar.py` y navegar manualmente
2. **[ ] Confirmar selectores DOM** — ajustar los `SEL_*` en `navegacion_productos.py`
3. **[ ] Confirmar URL de gestión** — actualizar `GESTION_PRODUCTOS_URL` en `login_mod.py`
4. **[ ] Probar con 1 producto** antes de procesar el Excel completo
5. **[ ] Agregar escritura de resultados al Excel** (similar a `excel_writer.py`)

# Auditoría de Funciones: `modulo_modificar_productos/automation_mod/login_mod.py`

- **Lenguaje:** `python`
- **Líneas de código:** 78
- **Hash SHA256:** `9dea2dc311f6`
- **Estrategia de Análisis:** Pasada directa

---

## 🔍 Inventario de Funciones y Bloques Lógicos

### `def login_y_navegar(page, usuario, password, log, stop_event, captcha_bridge)`
- **Línea inicial:** 32 | **Línea final:** 78
- **Firma completa:** `def login_y_navegar(page, usuario, password, log, stop_event, captcha_bridge)`
- **Propósito:** Hace login en Peru Compras y navega a la sección de gestión de productos.
Retorna True si todo OK, False si falla.

Reutiliza do_login() del proyecto principal (misma URL de login, mismo CAPTCHA).
La diferencia es la cuenta (usuario/password diferentes) y la URL de destino.
- **Efectos Secundarios:** Navegación / Red HTTP
- **Dependencias / Invocaciones:** `do_login, info, goto, error, sleep, ok, warn`
- **Nivel de Complejidad:** `BAJA` (Ramas lógicas: 3)

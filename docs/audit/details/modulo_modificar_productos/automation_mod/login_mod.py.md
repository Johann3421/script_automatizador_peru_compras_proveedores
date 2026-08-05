# Documentación Técnica: `modulo_modificar_productos/automation_mod/login_mod.py`

- **Ruta relativa:** `modulo_modificar_productos/automation_mod/login_mod.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 78
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!CAUTION]
> **CRÍTICO - NÚCLEO DE AUTOMATIZACIÓN (NO TOCAR)**
> Este archivo pertenece a la capa del backend de automatización o comunicación con el portal Perú Compras.
> **Regla:** Queda prohibido modificar contratos de login, selectores XPath/CSS o peticiones HTTP a Perú Compras sin autorización explícita.

## 📋 Estructura Interna del Archivo

### Funciones independientes:

#### `def login_y_navegar(page, usuario, password, log, stop_event, captcha_bridge)` (Línea 32)
- **Propósito:** Hace login en Peru Compras y navega a la sección de gestión de productos.
Retorna True si todo OK, False si falla.

Reutiliza do_login() del proyecto principal (misma URL de login, mismo CAPTCHA).
La diferencia es la cuenta (usuario/password diferentes) y la URL de destino.
- **Firma:** `def login_y_navegar(page, usuario, password, log, stop_event, captcha_bridge)`
- **Retorno / Efectos:** Consulta código fuente.

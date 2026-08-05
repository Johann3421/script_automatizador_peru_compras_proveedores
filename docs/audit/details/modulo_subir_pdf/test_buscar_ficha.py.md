# Documentación Técnica: `modulo_subir_pdf/test_buscar_ficha.py`

- **Ruta relativa:** `modulo_subir_pdf/test_buscar_ficha.py`
- **Tipo de archivo:** `.py`
- **Líneas de código:** 246
- **Fecha de inspección:** 2026-08-05 18:37:53

---

## 🛠️ Reglas de Modificación (Qué tocar y qué NO tocar)

> [!NOTE]
> **MODULO DE INTERFAZ / UTILIDAD (MODIFICABLE CON PRECAUCIÓN)**
> Este archivo gestiona la presentación, puente PyWebView o formateo de reportes.
> **Regla:** Se pueden hacer mejoras estéticas, agregar eventos de UI o ajustar layouts cuidando no romper la comunicación con el backend.

## 📋 Estructura Interna del Archivo

### Clases definidas:

#### Clase `PrintLog` (Línea 36)
- **Docstring:** _Sin docstring._
- **Métodos:**
  - `def info(self, m)` (Línea 37): Sin docstring.
  - `def warn(self, m)` (Línea 38): Sin docstring.
  - `def error(self, m)` (Línea 39): Sin docstring.
  - `def ok(self, m)` (Línea 40): Sin docstring.

### Funciones independientes:

#### `def probar_api_con_param(page, nombre, params, log)` (Línea 43)
- **Propósito:** Probar el API con un set de params y reportar resultado.
- **Firma:** `def probar_api_con_param(page, nombre, params, log)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def interceptar_busqueda_real(page, log)` (Línea 81)
- **Propósito:** Interceptar la búsqueda real que hace la UI cuando se busca por N° de parte.
- **Firma:** `def interceptar_busqueda_real(page, log)`
- **Retorno / Efectos:** Consulta código fuente.

#### `def main()` (Línea 135)
- **Propósito:** Sin docstring.
- **Firma:** `def main()`
- **Retorno / Efectos:** Consulta código fuente.

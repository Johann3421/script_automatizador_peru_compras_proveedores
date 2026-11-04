# 2026-10-09 — Generación de Instalador Windows Standalone Oficial

- **Fecha:** 2026-10-09
- **Tipo:** Empaquetado / Despliegue / Build
- **Estado:** Completado y Verificado
- **Módulo:** `installer/` y `build_exe.py`

---

## 🎯 Contexto y Objetivo
Crear y compilar un instalador ejecutable de Windows (`Script_Peru_Compras_Setup.exe`) completamente auto-contenido, de modo que cualquier usuario pueda instalarlo y ejecutarlo en una computadora nueva sin tener instalado Python, librerías, Tesseract ni navegadores previos.

---

## 🛠️ Arquitectura de Distribución Implementada

### 1. Entorno Standalone Embebido (PyInstaller)
- Empaqueta el intérprete de Python, las dependencias de interfaz (`pywebview`, `customtkinter`), controladores de automatización (`playwright`), procesadores de datos (`pandas`, `numpy`, `openpyxl`, `PIL`) y lógica institucional.
- **Tesseract OCR Portable Embebido:** Se incluyeron los binarios y datos de entrenamiento de `tesseract/` directamente en el paquete, garantizando resolución automática de captchas sin instalación adicional.
- **Navegador Chromium Standalone:** Se integró la distribución local de Chromium en `browsers/` para ejecución inmediata sin requerir descargas pesadas.
- **Módulos y UI Web:** Se empaquetó `ui_web/` (con todos los nuevos estilos y soporte Excel/JSON) y `modulo_subir_pdf/`.

### 2. Instalador de Windows Oficial (Inno Setup 6)
- Script de instalación: `installer/setup.iss`.
- Compilador: `C:\InnoSetup6\ISCC.exe` integrado automáticamente al flujo de build en `build_exe.py`.
- Generación de archivo único distribuible:
  `installer/Output/Script_Peru_Compras_Setup.exe`.
- **Características para PCs Nuevas:**
  - Asistente de instalación moderno en español con elevación UAC estándar.
  - Creación automática de accesos directos en Escritorio y Menú Inicio con icono institucional `icon.ico`.
  - Detección inteligente de navegador: si ya cuenta con Chromium portable local o Edge, omite descargas de red para instalación ultrarrápida.
  - Registro de desinstalador limpio en "Agregar o quitar programas" de Windows.

---

## 📁 Archivos Modificados y Generados
- `build_exe.py`: Orquestador unificado que compila PyInstaller y ejecuta Inno Setup automáticamente.
- `installer/setup.iss`: Optimizado para salto de descargas si el navegador ya está empaquetado.
- `build.bat`: Script batch de un solo clic para compilar instaladores.
- `installer/Output/Script_Peru_Compras_Setup.exe`: Archivo instalador distribuible listo para entrega (422.8 MB, 100% autocontenido).
- `notes/INDEX.md`

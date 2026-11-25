# Compilación de Paquete Standalone e Instalador Oficial de Distribución

- **Fecha:** 2026-11-18
- **Tipo:** Compilación / Empaquetado / Distribución Standalone
- **Estado:** Completado Exitosamente

---

## 1. Objetivo
Generar un instalador oficial autocontenido (`Script_Peru_Compras_Setup.exe`) y paquete standalone ejecutable para que cualquier usuario pueda utilizar el sistema en cualquier equipo con Windows 10/11 sin necesidad de instalar Python, Tesseract, Chromium ni ninguna dependencia adicional.

---

## 2. Componentes Empaquetados en el Build
1. **Python Embebido y Librerías Compiladas:**
   - `pywebview` + .NET/WebView2 runtime.
   - `playwright` 1.58 + bindings de automatización.
   - `pandas`, `openpyxl`, `Pillow`, `pytesseract`.
2. **Motor de Navegación Nativo (Chromium 1208):**
   - Se empaquetó el motor `chromium-1208` (393 MB) correspondiente a Playwright 1.58 dentro de la carpeta `browsers/`.
   - Se limpiaron versiones obsoletas no coincidentes (`chromium-1223`).
3. **Motor OCR Local:**
   - Binarios completos de `tesseract/` con modelos de entrenamiento para resolución de CAPTCHA sin llamadas a APIs externas.
4. **Interfaz de Usuario Web:**
   - Recursos completos de `ui_web/` sincronizados tanto en el directorio raíz como en `_internal/ui_web/`.
5. **Instalador Oficial Windows (Inno Setup 6):**
   - Script `installer/setup.iss` configurado para compilar con `ISCC.exe` en `installer/Output/Script_Peru_Compras_Setup.exe`.
   - Genera accesos directos en Escritorio y Menú Inicio, con permisos de administrador e integración completa de desinstalación.

---

## 3. Artefactos de Distribución Generados

| Tipo | Ruta del Archivo | Tamaño | Propósito |
|---|---|---|---|
| **Instalador Oficial Único** | `installer/Output/Script_Peru_Compras_Setup.exe` | **419.8 MB** | Instalador ejecutable estándar de Windows. Instala la app completa, accesos directos y desinstalador. Cero dependencias previas requeridas. |
| **Paquete Standalone Portable** | `dist/PeruComprasBot/PeruComprasBot.exe` | Carpeta (58.9 MB exe) | Carpeta portable directa. Se puede copiar en una memoria USB o disco y ejecutar sin instalación. |
| **Lanzador Directo .BAT** | `dist/Iniciar PeruComprasBot.bat` | Script | Lanzador alternativo para iniciar el ejecutable sin consola. |

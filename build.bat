@echo off
setlocal EnableDelayedExpansion
title Peru Compras Bot - Compilador de Instalador v1.4

:: ═══════════════════════════════════════════════════════════════════════
:: build.bat  —  Orquestador de Compilación y Distribución
:: ───────────────────────────────────────────────────────────────────────
:: Propósito: Generar los binarios ejecutables distribuibles (.exe)
:: para compartir la aplicación con otros usuarios sin requerir Python.
::
:: PROCESO DE COMPILACIÓN EN 2 FASES:
::   1. build_exe.py: Genera el paquete Standalone en dist/PeruComprasBot/
::      (PyInstaller --onedir con todas las DLLs, Python empaquetado, etc.)
::   2. build_installer.py: Genera el Instalador Web Liviano (~15 MB)
::      en dist/Instalar_PeruComprasBot_v1.4.exe
::
:: FASE FINAL (Instalador Windows Standalone con Inno Setup):
::   Para generar un archivo instalador único Script_Peru_Compras_Setup.exe:
::   Ejecutar en la carpeta installer/: ISCC.exe setup.iss
:: ═══════════════════════════════════════════════════════════════════════

:: PASO 0: Determinar ruta raíz absoluta del proyecto
set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"

echo ============================================================
echo   COMPILACION Y GENERACION DE INSTALADOR: PERU COMPRAS BOT
echo ============================================================
echo Directorio Raiz: %ROOT%
echo.

:: PASO 1: Compilar paquete standalone y generar Instalador Windows Oficial
:: Ejecuta build_exe.py -> genera dist/PeruComprasBot/ y compila installer/Output/Script_Peru_Compras_Setup.exe
echo [1/1] Compilando ejecutable standalone y generando Instalador Windows Oficial (build_exe.py)...
python "%ROOT%\build_exe.py"
if errorlevel 1 (
    echo.
    echo ❌ ERROR: Fallo build_exe.py durante la compilacion.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   BUILD COMPLETADO EXITOSAMENTE
echo   El Instalador Final Listo para Distribuir se encuentra en:
echo   %ROOT%\installer\Output\Script_Peru_Compras_Setup.exe
echo ============================================================
echo.
pause

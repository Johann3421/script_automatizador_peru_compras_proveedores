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

:: PASO 1: Compilar paquete standalone con PyInstaller
:: Ejecuta build_exe.py -> genera dist/PeruComprasBot/ (Standalone)
echo [1/2] Compilando ejecutable principal (build_exe.py)...
python "%ROOT%\build_exe.py"
if errorlevel 1 (
    echo.
    echo ❌ ERROR: Fallo build_exe.py durante la compilacion PyInstaller.
    pause
    exit /b 1
)

:: PASO 2: Compilar instalador liviano auto-contenido
:: Ejecuta build_installer.py -> genera dist/Instalar_PeruComprasBot_v1.4.exe (~15 MB)
echo.
echo [2/2] Compilando instalador liviano distribuible (build_installer.py)...
python "%ROOT%\build_installer.py"
if errorlevel 1 (
    echo.
    echo ❌ ERROR: Fallo build_installer.py
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   BUILD COMPLETADO EXITOSAMENTE
echo   Los archivos generados se encuentran en:
echo   %ROOT%\dist\
echo
echo   Para compilar el Instalador Windows (.exe unico con Inno Setup):
echo     1. Ir a la carpeta: %ROOT%\installer\
echo     2. Ejecutar: ISCC.exe setup.iss
echo     3. El instalador final estara en: %ROOT%\installer\Output\
echo ============================================================
echo.
pause

@echo off
setlocal EnableDelayedExpansion
title Peru Compras Bot - Compilador de Instalador v1.4

set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"

echo ============================================================
echo   COMPILACION Y GENERACION DE INSTALADOR: PERU COMPRAS BOT
echo ============================================================
echo Directiorio: %ROOT%
echo.

:: 1. Compilar ejecutable principal y carpeta dist
echo [1/2] Compilando ejecutable principal (build_exe.py)...
python "%ROOT%\build_exe.py"
if errorlevel 1 (
    echo.
    echo ERROR: Fallo build_exe.py
    pause
    exit /b 1
)

:: 2. Compilar instalador liviano auto-contenido (.exe)
echo.
echo [2/2] Compilando instalador liviano distribuible (build_installer.py)...
python "%ROOT%\build_installer.py"
if errorlevel 1 (
    echo.
    echo ERROR: Fallo build_installer.py
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   BUILD COMPLETADO EXITOSAMENTE
echo   Los archivos generados se encuentran en:
echo   %ROOT%\dist\
echo ============================================================
echo.
pause

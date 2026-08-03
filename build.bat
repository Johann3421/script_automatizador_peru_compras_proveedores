@echo off
setlocal EnableDelayedExpansion

:: ── Configuración ───────────────────────────────────────────────────────────
set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"
set "VENV=%ROOT%\venv_build"
set "PYTHON=%VENV%\Scripts\python.exe"
set "PIP=%VENV%\Scripts\pip.exe"
set "PYINSTALLER=%VENV%\Scripts\pyinstaller.exe"
set "DIST_DIR=%ROOT%\dist\PeruComprasBot"
set "SETUP_EXE=%ROOT%\installer\Output\Script_Peru_Compras_Setup.exe"

:: ── Crear venv si no existe ─────────────────────────────────────────────────
if not exist "%VENV%\Scripts\python.exe" (
    echo [build] Creando entorno virtual en %VENV% ...
    python -m venv "%VENV%"
    if errorlevel 1 (
        echo ERROR: No se pudo crear el entorno virtual. Asegurate de tener Python instalado.
        exit /b 1
    )
)

:: ── Activar venv e instalar dependencias ────────────────────────────────────
echo [build] Instalando/actualizando dependencias ...
call "%VENV%\Scripts\activate.bat"
"%PIP%" install --upgrade pip
"%PIP%" install -r "%ROOT%\requirements.txt"
"%PIP%" install pyinstaller

:: ── Buscar Inno Setup Compiler ──────────────────────────────────────────────
set "ISCC="
for %%i in (iscc.exe) do set "ISCC=%%~$PATH:i"
if not defined ISCC (
    if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
        set "ISCC=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
    )
)
if not defined ISCC (
    if exist "%ROOT%\installer_tmp\InnoSetup6\ISCC.exe" (
        set "ISCC=%ROOT%\installer_tmp\InnoSetup6\ISCC.exe"
    )
)
if not defined ISCC (
    echo.
    echo [build] Inno Setup no encontrado. Intentando descarga local con winget ...
    echo.
    winget download --id JRSoftware.InnoSetup -e -d "%ROOT%\installer_tmp" >nul 2>&1
    if exist "%ROOT%\installer_tmp\Inno Setup 6_*_inno_en-US.exe" (
        for %%f in ("%ROOT%\installer_tmp\Inno Setup 6_*_inno_en-US.exe") do (
            echo [build] Instalando Inno Setup localmente ...
            "%%f" /VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP- /CURRENTUSER /DIR="%ROOT%\installer_tmp\InnoSetup6"
        )
        if exist "%ROOT%\installer_tmp\InnoSetup6\ISCC.exe" (
            set "ISCC=%ROOT%\installer_tmp\InnoSetup6\ISCC.exe"
        )
    )
)
if not defined ISCC (
    echo.
    echo [build] AVISO: No se pudo obtener ISCC.exe ^(Inno Setup^).
    echo [build] Se generara la carpeta dist/ pero NO el instalador .exe.
    echo [build] Descarga Inno Setup 6 desde https://jrsoftware.org/isdl.php
    echo.
)

:: ── Descargar Tesseract si hace falta ───────────────────────────────────────
if not exist "%ROOT%\tesseract\tesseract.exe" (
    echo [build] Descargando Tesseract OCR ...
    "%PYTHON%" "%ROOT%\scripts\download_tesseract.py"
    if errorlevel 1 (
        echo ERROR: No se pudo obtener Tesseract. Corregi el problema y volve a ejecutar build.bat.
        exit /b 1
    )
) else (
    echo [build] Tesseract ya existe.
)

:: ── Generar icono si no existe ──────────────────────────────────────────────
if not exist "%ROOT%\resources\icon.ico" (
    echo [build] Generando icono placeholder ...
    "%PYTHON%" "%ROOT%\scripts\create_icon.py"
)

:: ── Limpiar archivos de debug/output que alargan rutas innecesariamente ─────
echo [build] Limpiando directorios de debug/output ...
if exist "%ROOT%\modulo_subir_pdf\output_extract" rmdir /s /q "%ROOT%\modulo_subir_pdf\output_extract"
if exist "%ROOT%\modulo_subir_pdf\discovery_output" rmdir /s /q "%ROOT%\modulo_subir_pdf\discovery_output"
if exist "%ROOT%\modulo_subir_pdf\discovery_v2_output" rmdir /s /q "%ROOT%\modulo_subir_pdf\discovery_v2_output"
if exist "%ROOT%\modulo_modificar_productos\output_extract" rmdir /s /q "%ROOT%\modulo_modificar_productos\output_extract"
if exist "%ROOT%\modulo_modificar_productos\discovery_output" rmdir /s /q "%ROOT%\modulo_modificar_productos\discovery_output"
if exist "%ROOT%\modulo_modificar_productos\discovery_v2_output" rmdir /s /q "%ROOT%\modulo_modificar_productos\discovery_v2_output"
:: Eliminar xlsx de prueba/procesados que no se usan en runtime
del /q "%ROOT%\modulo_subir_pdf\*.xlsx" 2>nul
del /q "%ROOT%\modulo_modificar_productos\*.xlsx" 2>nul

:: ── Ejecutar PyInstaller ────────────────────────────────────────────────────
echo [build] Ejecutando PyInstaller ...
"%PYINSTALLER%" --clean -y "%ROOT%\PeruComprasBot.spec"
if errorlevel 1 (
    echo ERROR: PyInstaller fallo.
    exit /b 1
)

:: ── Compilar instalador con Inno Setup ──────────────────────────────────────
if defined ISCC (
    echo [build] Compilando instalador con Inno Setup ...
    > "%ROOT%\installer\setup_config.iss" echo #define SourceDir "%ROOT%\dist\PeruComprasBot"
    "%ISCC%" /Qp "%ROOT%\installer\setup.iss"
    if errorlevel 1 (
        echo ERROR: Inno Setup fallo.
        exit /b 1
    )
)

:: ── Resumen ─────────────────────────────────────────────────────────────────
echo.
echo ==========================================
echo  BUILD COMPLETADO
echo ==========================================
echo Carpeta de la app: %DIST_DIR%
if exist "%SETUP_EXE%" (
    echo Instalador:        %SETUP_EXE%
) else (
    echo Instalador:        NO GENERADO ^(falta Inno Setup^)
)
echo.
pause

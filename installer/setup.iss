; Inno Setup script para PeruComprasBot
; Compilar con ISCC.exe desde el directorio del proyecto o con build.bat

; setup_config.iss es generado por build.bat con la ruta absoluta al dist.
; Si no existe, se usa la ruta relativa por defecto.
#ifexist "setup_config.iss"
  #include "setup_config.iss"
#endif
#ifndef SourceDir
  #define SourceDir "..\dist\PeruComprasBot"
#endif

#define MyAppName "PeruComprasBot"
#define MyAppVersion "1.4"
#define MyAppPublisher "THE KING COMPUTER E.I.R.L."
#define MyAppExeName "PeruComprasBot.exe"
#define MyAppIcon "icon.ico"

[Setup]
AppId={{F4C8E1A2-9B3D-4E5F-8A7C-1D2E3F4A5B6C}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=Output
OutputBaseFilename=Script_Peru_Compras_Setup
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=admin
PrivilegesRequiredOverridesAllowed=dialog
UninstallDisplayIcon={app}\_internal\resources\{#MyAppIcon}
SetupIconFile=..\resources\icon.ico
LicenseFile=license.txt
WizardStyle=modern
; Forzar sobreescritura completa al reinstalar
CloseApplications=force

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "{#SourceDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Excludes: "playwright_browsers\*"

[Icons]
; Todos los shortcuts apuntan explicitamente al .ico dentro de _internal\resources
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\_internal\resources\{#MyAppIcon}"; WorkingDir: "{app}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\_internal\resources\{#MyAppIcon}"; Tasks: desktopicon; WorkingDir: "{app}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\_internal\resources\{#MyAppIcon}"; WorkingDir: "{app}"

[Run]
; 1. Limpiar cache de iconos de Windows para que el nuevo icono se muestre inmediatamente
Filename: "cmd.exe"; Parameters: "/c ie4uinit.exe -show"; StatusMsg: "Actualizando iconos del sistema..."; Flags: runhidden waituntilterminated
; 2. Instalar Chromium para Playwright en C:\ProgramData\PeruComprasBot\ms-playwright (compartido para TODOS los usuarios de la PC)
Filename: "cmd.exe"; Parameters: "/c ""set PLAYWRIGHT_BROWSERS_PATH={commonappdata}\PeruComprasBot\ms-playwright&& ""{app}\_internal\playwright\driver\node.exe"" ""{app}\_internal\playwright\driver\package\cli.js"" install chromium"""; Description: "Descargando motor Chromium (necesario para automatización)..."; StatusMsg: "Instalando motor Chromium para Playwright en la PC, espere..."; Flags: runhidden waituntilterminated; Check: NeedsChromiumInstall

; Abrir la aplicación al finalizar la instalación
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#MyAppName}}"; Flags: nowait postinstall skipifsilent

[Code]
function NeedsChromiumInstall: Boolean;
var
  NodeExe, CliJs: String;
begin
  NodeExe := ExpandConstant('{app}\_internal\playwright\driver\node.exe');
  CliJs   := ExpandConstant('{app}\_internal\playwright\driver\package\cli.js');
  Result := FileExists(NodeExe) and FileExists(CliJs);
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  CachePath, Cmd: String;
  ResultCode: Integer;
begin
  if CurStep = ssPostInstall then
  begin
    { Eliminar archivos de cache de iconos de Windows para forzar regeneracion }
    CachePath := ExpandConstant('{localappdata}\Microsoft\Windows\Explorer');
    Exec('cmd.exe', '/c del /f /q "' + CachePath + '\iconcache*" 2>nul', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    Exec('cmd.exe', '/c del /f /q "' + CachePath + '\thumbcache*" 2>nul', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    { Reiniciar el explorador para que recargue iconos frescos }
    Exec('cmd.exe', '/c taskkill /f /im explorer.exe & start explorer.exe', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  end;
end;

[InstallDelete]
; Limpiar instalacion anterior completamente antes de copiar archivos nuevos
Type: filesandordirs; Name: "{app}\_internal"

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

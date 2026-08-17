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
UninstallDisplayIcon={app}\{#MyAppExeName}
LicenseFile=license.txt
WizardStyle=modern


[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "{#SourceDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Excludes: "playwright_browsers\*"

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon; WorkingDir: "{app}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"

[Run]
; Instalar Chromium para Playwright en C:\ProgramData\PeruComprasBot\ms-playwright (compartido para TODOS los usuarios de la PC)
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

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

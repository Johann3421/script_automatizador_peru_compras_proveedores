import os
import shutil

def get_writable_path(filename="dropdowns_precios.json", default_dir=""):
    """
    Retorna una ruta de archivo que sea escribible por el usuario actual.
    Si la carpeta de instalación (default_dir) es de solo lectura (por ejemplo, en Program Files),
    creará y retornará una ruta en el directorio AppData/Local de Windows, copiando
    el archivo pre-empaquetado si existiese.
    """
    local_path = os.path.join(default_dir, filename)
    try:
        # Intentamos abrir/crear el archivo en modo append para verificar permisos
        if os.path.exists(local_path):
            with open(local_path, "a", encoding="utf-8"):
                pass
        else:
            with open(local_path, "w", encoding="utf-8") as f:
                f.write("[]")
        return local_path
    except (PermissionError, OSError):
        # Si da error de permisos (Program Files), usamos LOCALAPPDATA
        appdata = os.environ.get("LOCALAPPDATA", os.path.expanduser("~"))
        bot_dir = os.path.join(appdata, "PeruComprasBot")
        os.makedirs(bot_dir, exist_ok=True)
        appdata_path = os.path.join(bot_dir, filename)
        
        # Si el archivo local existe pero en AppData no, lo copiamos para no perder la configuración empaquetada
        if os.path.exists(local_path) and not os.path.exists(appdata_path):
            try:
                shutil.copy(local_path, appdata_path)
            except Exception:
                pass
        return appdata_path

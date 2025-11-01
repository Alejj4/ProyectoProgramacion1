import json
from .utils import manejar_apertura_archivo

def obtener_diccionario_autos():
    archivo_autos = manejar_apertura_archivo("autos.json", "rt", "archivos")
    autos_data = json.load(archivo_autos)

    archivo_autos.close()
    return autos_data
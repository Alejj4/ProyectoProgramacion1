import json
from .utils import manejar_apertura_archivo, mostrar_opciones_disponibles, verificar_numero_valido

def obtener_diccionario_autos():
    archivo_autos = manejar_apertura_archivo("autos.json", "rt", "archivos")
    autos_data = json.load(archivo_autos)

    archivo_autos.close()
    return autos_data

def obtener_datos_modelos():
    """Funcion unicamente dedicada a obtener los datos (marca y tipo) referentes a los que el admin quiere acceder para realizar una operacion"""
    marca_seleccionada = None
    tipo_seleccionado = None

    autos_data = obtener_diccionario_autos()

    marcas_disponibles = list(autos_data.keys())

    mostrar_opciones_disponibles(marcas_disponibles)
    marca_indice = verificar_numero_valido("Ingrese la marca de auto que desea modificar o ingrese -1 para volver: ", rango=range(len(marcas_disponibles)), opciones_disponibles=marcas_disponibles, retornar_indice=True)

    if marca_indice != -1:
        marca_seleccionada = marcas_disponibles[marca_indice]
        tipos_disponibles = list(autos_data[marca_seleccionada].keys())

        mostrar_opciones_disponibles(tipos_disponibles)
        tipo_indice = verificar_numero_valido("Ingrese el tipo de auto al que desea acceder: ", rango=range(len(tipos_disponibles)),opciones_disponibles=tipos_disponibles, retornar_indice=True)

        tipo_seleccionado = tipos_disponibles[tipo_indice]

    return marca_seleccionada, tipo_seleccionado
import json
from .utils import manejar_apertura_archivo, mostrar_opciones_disponibles, verificar_numero_valido, imprimir_separador

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


def cargar_auto():
    """Funcion para que el admin pueda cargar autos al archivo autos.json"""
    autos_data = obtener_diccionario_autos()

    while True:
        marca_seleccionada, tipo_seleccionado = obtener_datos_modelos()

        nombre = input(f"Ingrese un nombre para el nuevo modelo a registrar en {marca_seleccionada} - {tipo_seleccionado}: ").capitalize()

        if nombre == "" or nombre.isdigit():
            print("Se debe ingresar un nombre de modelo para continuar")
            continue
        
        imprimir_separador()
        equipamientos_disponibles = [1,2,3]
        mostrar_opciones_disponibles(equipamientos_disponibles)
        equipamiento = verificar_numero_valido("Ingrese el numero de equipamiento que desee asignar: ", rango=range(len(equipamientos_disponibles)),opciones_disponibles=equipamientos_disponibles)

        precio_min, precio_max = 20, 100
        precio = verificar_numero_valido("Ingrese el precio del modelo: ",rango=range(precio_min, precio_max), mensaje_error=f"El precio ingresado está fuera de rango (entre {precio_min} y {precio_max})")

        autos_data[marca_seleccionada][tipo_seleccionado].append({"nombre":nombre, "equipamiento": equipamiento, "precio":precio})

        print("Modelo registrado con exito!")


        with open("archivos/autos.json", "wt", encoding="UTF-8") as archivo_autos:
            texto_json = json.dumps(autos_data, indent=4) # Serializar el diccionario para escribir el texto en el archivo de autos
            archivo_autos.write(texto_json)


        print("¿Desea añadir un nuevo modelo?")
        opciones_disponibles = ["Sí", "No (salir)"]
        mostrar_opciones_disponibles(opciones_disponibles)
        opcion = verificar_numero_valido("Ingrese la opcion que desee: ", rango=range(2), opciones_disponibles=opciones_disponibles)

        if opcion == 2:
            print("Volviendo al menu")
            break
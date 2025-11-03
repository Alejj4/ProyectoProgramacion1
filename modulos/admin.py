import json
from .utils import manejar_apertura_archivo, mostrar_opciones_disponibles, verificar_numero_valido, imprimir_separador, crear_registro
from .informes import obtener_3_autos_mas_vendidos, obtener_3_autos_mas_vendidos_marca, obtener_ventas_por_marca, obtener_ventas_por_auto

def obtener_diccionario_autos():
    archivo_autos = manejar_apertura_archivo("autos.json", "rt", "archivos")
    autos_data = json.load(archivo_autos)

    archivo_autos.close()
    return autos_data

def obtener_rango_precios():
    """Funcion que retorna los precios minimos y maximos que puede tener un vehiculo"""
    return 1, 200

def obtener_datos_modelos():
    """Funcion unicamente dedicada a obtener los datos (marca y tipo) referentes a los que el admin quiere acceder para realizar una operacion"""
    marca_seleccionada = None
    tipo_seleccionado = None

    autos_data = obtener_diccionario_autos()

    marcas_disponibles = list(autos_data.keys())

    mostrar_opciones_disponibles(marcas_disponibles)
    marca_numero = verificar_numero_valido("Ingrese la marca de auto que desea modificar o ingrese -1 para volver: ", rango=range(1, len(marcas_disponibles) + 1), opciones_disponibles=marcas_disponibles)

    if marca_numero != -1:
        marca_seleccionada = marcas_disponibles[marca_numero - 1]
        crear_registro(f"Marca seleccionada ({marca_seleccionada})")
        tipos_disponibles = list(autos_data[marca_seleccionada].keys())

        mostrar_opciones_disponibles(tipos_disponibles)
        tipo_numero = verificar_numero_valido("Ingrese el tipo de auto al que desea acceder: ", rango=range(1, len(tipos_disponibles) + 1),opciones_disponibles=tipos_disponibles)
        if tipo_numero != -1:
            tipo_seleccionado = tipos_disponibles[tipo_numero - 1]
            crear_registro(f"Tipo ({tipo_seleccionado})")
        else:
            tipo_numero = None

    return marca_seleccionada, tipo_seleccionado


def registrar_auto():
    """Funcion para que el admin pueda cargar autos al archivo autos.json"""
    autos_data = obtener_diccionario_autos()

    salir = False
    marca_seleccionada, tipo_seleccionado = obtener_datos_modelos()

    if not (marca_seleccionada and tipo_seleccionado):
        salir= True

    while not salir:

        nombre = input(f"Ingrese un nombre para el nuevo modelo a registrar en {marca_seleccionada} - {tipo_seleccionado}: ").capitalize()

        if nombre == "" or nombre.isdigit() or nombre == "-1":
            print("Se debe ingresar un nombre de modelo para continuar")
            continue
        crear_registro(f"Nombre modelo ({nombre})")
        imprimir_separador()
        equipamientos_disponibles = [1,2,3]
        mostrar_opciones_disponibles(equipamientos_disponibles)
        equipamiento = verificar_numero_valido("Ingrese el numero de equipamiento que desee asignar: ", rango=range(1, len(equipamientos_disponibles) + 1),opciones_disponibles=equipamientos_disponibles)
        crear_registro(f"Equipamiento ({equipamiento})")
        precio_min, precio_max = obtener_rango_precios()
        precio = verificar_numero_valido("Ingrese el precio del modelo: ",rango=range(precio_min, precio_max + 1), mensaje_error=f"El precio ingresado está fuera de rango (entre {precio_min} y {precio_max})")
        crear_registro(f"Precio ({precio})")
        autos_data[marca_seleccionada][tipo_seleccionado].append({"nombre":nombre, "equipamiento": equipamiento, "precio":precio})

        print("Modelo registrado con exito!")


        with open("archivos/autos.json", "wt", encoding="UTF-8") as archivo_autos:
            texto_json = json.dumps(autos_data, indent=4) # Serializar el diccionario para escribir el texto en el archivo de autos
            archivo_autos.write(texto_json)


        print("¿Desea añadir un nuevo modelo?")
        opciones_disponibles = ["Sí", "No (salir)"]
        mostrar_opciones_disponibles(opciones_disponibles)
        opcion = verificar_numero_valido("Ingrese la opcion que desee: ", rango=range(1, len(opciones_disponibles) + 1), opciones_disponibles=opciones_disponibles)
        crear_registro("Agregar nuevo modelo")
        if opcion == 2:
            print("Volviendo al menu")
            crear_registro("Salir")
            break


def modificar_precios():
    """Funcion en la que un admin puede modificar los precios de un modelo especifico"""
    modelo_seleccionado_indice = -1
    precio_min, precio_max = obtener_rango_precios()

    marca_seleccionada, tipo_seleccionado = obtener_datos_modelos()
    autos_data = obtener_diccionario_autos()

    modelos_disponibles = autos_data[marca_seleccionada][tipo_seleccionado]

    if len(modelos_disponibles) > 0:
        print(f"{marca_seleccionada} - {tipo_seleccionado} cuenta con los siguientes modelos")

        mostrar_opciones_disponibles(modelos_disponibles)

        modelo_seleccionado_indice = verificar_numero_valido("Ingrese el modelo al que desea cambiarle el precio o ingrese -1 para volver: ", rango=range(1, len(modelos_disponibles) + 1),opciones_disponibles=modelos_disponibles)

        if modelo_seleccionado_indice != -1:
            modelo_seleccionado = modelos_disponibles[modelo_seleccionado_indice - 1]
            crear_registro(f"Modificar precio ({modelo_seleccionado['nombre']})")
            print("Modelo seleccionado: ")
            print(f"{modelo_seleccionado['nombre']}, precio: {modelo_seleccionado['precio']}")

            nuevo_precio = verificar_numero_valido("Ingrese un nuevo precio para este modelo: ", rango=range(precio_min, precio_max + 1), mensaje_error=f"El precio es invalido, debe ser un numero entero entre {precio_min} y {precio_max}")
            crear_registro("Nuevo precio")
            autos_data[marca_seleccionada][tipo_seleccionado][modelo_seleccionado_indice - 1]["precio"] = nuevo_precio

            archivo_autos = manejar_apertura_archivo("autos.json", "wt", "archivos")
            archivo_autos.write(json.dumps(autos_data, indent=4))
            archivo_autos.close()

            print(f"Precio del modelo '{modelo_seleccionado['nombre']}' actualizado a {nuevo_precio} con éxito.")
            print("Volviendo al menu principal")
    else:
        print(f"{marca_seleccionada} - {tipo_seleccionado} aun no cuenta con modelos disponibles")

def obtener_informes():
    informes_a_consultar = ["Los 3 autos mas vendidos", "Los 3 autos mas vendidos (por marca)", "Ventas por marca", "Ventas totales por auto"]

    salir = False

    while not salir:
        print("Como administrador tiene acceso a los siguientes informes del sistema:")
        mostrar_opciones_disponibles(informes_a_consultar)

        informe_seleccionado = verificar_numero_valido("Ingrese la opcion que desee o -1 para volver al menu principal: ",rango=range(1, len(informes_a_consultar) + 1), opciones_disponibles=informes_a_consultar)

        imprimir_separador()

        if informe_seleccionado == 1:
            crear_registro("Ver informe (3 autos más vendidos)")
            obtener_3_autos_mas_vendidos()
        elif informe_seleccionado == 2:
            crear_registro("Ver informe ( 3 autos mas vendidos por marca)")
            obtener_3_autos_mas_vendidos_marca()
        elif informe_seleccionado == 3:
            crear_registro("Ver informe (ventas por marca)")
            obtener_ventas_por_marca()
        elif informe_seleccionado == 4:
            crear_registro("Ver informe (ventas por auto)")
            obtener_ventas_por_auto()
        else:
            break
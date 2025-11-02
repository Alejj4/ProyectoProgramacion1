from modulos.utils import manejar_apertura_archivo, mostrar_opciones_disponibles, verificar_numero_valido, imprimir_separador, crear_registro, mostrar_matriz

import json, random

def completar_archivo_stock():

    archivo_autos = manejar_apertura_archivo("autos.json", "rt")

    archivo_stock = manejar_apertura_archivo("stock.csv", "wt")

    if archivo_autos is not None:

        archivo_stock.write("marca, modelo, stock\n")

        autos = json.load(archivo_autos)
        marcas = list(autos.keys())

        for marca in marcas:
            tipos = autos[marca]
            for tipo in tipos:
                modelos = autos[marca][tipo]

                for modelo in modelos:
                    stock_disponible = random.randint(1, 5)
                    archivo_stock.write(f"{marca}, {modelo['nombre']}, {stock_disponible}\n")
    
    archivo_stock.close()
    archivo_autos.close()


def calcular_precios_promedios_tipo():
   
    archivo_autos = manejar_apertura_archivo("autos.json", "rt")
    
    archivo_precios_promedios = manejar_apertura_archivo("precios_promedios.csv", "wt", "archivos")

    archivo_precios_promedios.write("marca, tipo, promedio\n")

    if archivo_autos is not None:
        autos = json.load(archivo_autos)
        
        matriz_precios_promedios = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
        ]

        marcas = list(autos.keys())
        
        for fila, marca in enumerate(marcas):
            tipos = autos[marca]
            for columna, tipo in enumerate(tipos):
                suma_precios = sum(modelo["precio"] for modelo in autos[marca][tipo])
                
                try:
                    promedio = suma_precios / len(autos[marca][tipo])
                except ZeroDivisionError:
                    promedio = 0

                matriz_precios_promedios[fila][columna] = round(promedio, 2)
                archivo_precios_promedios.write(f"{marca}, {tipo}, {promedio}\n")

        archivo_precios_promedios.close()
        return matriz_precios_promedios


def pedir_dato_de_autos(mensaje_input, opciones_disponibles):
    """Funcion dedicada a pedirle un dato al usuario para luego
       poder mostrarle al usuario las opciones de modelos en base
       a lo ingresado"""
    mostrar_opciones_disponibles(opciones_disponibles)
    dato = verificar_numero_valido(mensaje_input, rango=range(1, len(opciones_disponibles) + 1), opciones_disponibles=opciones_disponibles)
    
    dato = -1 if dato == -1 else dato - 1

    return dato

        
def pedir_datos_compra():
    """Funcion encargada de pedir los datos de la marca, el tipo y modelo exacto deseados por el usuario"""

    marcas_disponibles = ["Toyota", "Schipani", "Chevrolet", "Ford"]

    marca_indice = pedir_dato_de_autos("Ingrese la marca que desea visualizar, para salir, simplemente ingrese -1: ", marcas_disponibles)

    imprimir_separador()
    if not marca_indice == -1:
        nombre_marca = marcas_disponibles[marca_indice]
        crear_registro("Marca_seleccionada", nombre_marca)
        tipos_disponibles = ["Hatchback", "Sedan", "SUV", "Pick-up"]
        tipo_indice = pedir_dato_de_autos("Ingrese el tipo de auto que desea visualizar, para salir, simplemente ingrese -1: ", tipos_disponibles)
        nombre_tipo = tipos_disponibles[tipo_indice] if tipo_indice != -1 else -1
        crear_registro("Tipo_seleccionado", nombre_tipo)
    else:
        nombre_marca, nombre_tipo = -1, -1 #Se sale automaticamente

    return nombre_marca, nombre_tipo


def obtener_modelos_disponibles(nombre_marca, nombre_tipo):
    """Funcion hecha para obtener los modelos que se encuentran registrados y disponibles en base a los dos argumentos que se les pasan (nombre_marca y nombre_tipo)"""
    archivo_autos = manejar_apertura_archivo("autos.json", "rt")
    archivo_stock = manejar_apertura_archivo("stock.csv", "r")
    disponibles = []

    autos = json.load(archivo_autos)
    stock_data = {}
    
    for i, linea in enumerate(archivo_stock):
        if i != 0:
            partes = linea.strip().split(",")
            marca = partes[0].strip()
            modelo = partes[1].strip()

            try:
                stock = int(partes[2].strip())
            except ValueError:
                stock = 0
            stock_data[(marca.lower(), modelo.lower())] = stock

    modelos = autos[nombre_marca][nombre_tipo]
    for m in modelos:
        nombre_modelo = m["nombre"].strip()
        equipamiento = m["equipamiento"]
        precio = m["precio"]
        stock = stock_data.get((nombre_marca.lower(), nombre_modelo.lower()), 0)

        if stock > 0:
            disponibles.append({
                "marca":nombre_marca,
                "nombre":nombre_modelo, 
                "equipamiento":equipamiento, 
                "precio":precio, 
                "stock":stock
            })


    total_disponibles = contar_modelos_disponibles(disponibles)
    imprimir_separador()
    print(f"Total de modelos disponibles en {nombre_marca} - {nombre_tipo}: {total_disponibles}")
    imprimir_separador()

    
    archivo_stock.close()
    archivo_autos.close()
    return disponibles


def contar_modelos_disponibles(modelos, i=0):
    #funcion recursiva
    if i==len(modelos):
        return 0
    stock = modelos[i].get("stock", 0)
    subtotal=contar_modelos_disponibles(modelos, i + 1)
    if stock>0:
        return 1+subtotal
    else:
        return subtotal


def mostrar_modelos_disponibles(nombre_marca, nombre_tipo, modelos_disponibles):
    """Funcion para mostrar los modelos que disponibles segun los datos que se le pasen"""

    print(f"Autos disponibles de {nombre_marca} - {nombre_tipo}:\n")
    print("Modelos".ljust(25), "Equipamiento".ljust(15), "Precio".ljust(20), "Stock")
    for modelo in modelos_disponibles:
        print(
            str(modelo["nombre"]).ljust(25),
            str(modelo["equipamiento"]).ljust(15),
            str(modelo["precio"]).ljust(20),
            str(modelo["stock"])
        )
    imprimir_separador()


def desplegar_menu_de_catalogo():
    
    matriz_precios_promedios = calcular_precios_promedios_tipo()
    
    mostrar_matriz(matriz_precios_promedios)

import random as rn

import json

import random
from faker import Faker
def verificar_numero_valido(mensaje_input, rango=None):
    """Funcion que maneja la excepcion ValueError cuando en un input se espera un numero y no otra cosa"""
    
    while True:
        try:
            dato = int(input(mensaje_input)) - 1

            if rango is not None and not dato in rango:
                raise IndexError("Opcion no disponible, por favor intente de nuevo")

            dato += 1
            break
        except ValueError:
            imprimir_separador()
            print("El dato ingresado es inválido, el mismo debe ser un número")
            imprimir_separador()
        except IndexError as e:
            print(e)
            imprimir_separador()

    return dato


def imprimir_separador():
    print("-"*78)


def mostrar_matriz(matriz):
    esquina = 'Marcas/Tipo'
    columnas = ['Hatchback', 'Sedan', 'Suv', 'PickUp']
    filas = ['Toyota', 'Schipani', 'Chevrolet', 'Ford']
    ancho = 15

    # encabezado
    print(esquina.ljust(ancho), end='')
    for col in columnas:
        print(col.ljust(ancho), end='')
    print()

    # filas
    for i in range(len(filas)):
        print(filas[i].ljust(ancho), end='')
        for fil in matriz[i]:
            print(str(fil).ljust(ancho), end='')
        print()


def mostrar_opciones_disponibles(datos):
    for i, dato in enumerate(datos):
        print(f"{i + 1} - {dato}")


def desplegar_menu_informes():
    informes_disponibles = ["Los 3 autos más caros y baratos.", "Los autos más y menos vendidos.", "DNI de los clientes."]

    print("A continuación se presentan los distintos informes que puede consultar:")
    for i, informe in enumerate(informes_disponibles):
        print(f"{i + 1} - {informe}")

def completar_clientes():
    archivo = open("clientes.csv", "wt", encoding="UTF-8")

    fake = Faker('es_AR')

    archivo.write("dni, nombre, contraseña\n")
    
    for i in range(10):
        dni = random.randint(10000000, 99999999)
        
        nombre = fake.name() if (i != 0 and i != 1) else ("Tiziano Schipani" if i == 0 else "Alfonso Schipani")
        password = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)

        archivo.write(f"{dni}, {nombre}, {password}\n")

    archivo.close()

def manejar_apertura_archivo(direccion, modo_apertura):
    try:
        archivo = open(direccion, modo_apertura, encoding="UTF-8") 
    except FileNotFoundError:
        print("El archivo no ha sido encontrado, suspendiendo operacion...")
        return None
    
    return archivo


def completar_archivo_stock():

    archivo_autos = manejar_apertura_archivo("autos.json", "rt")

    archivo_stock = open("stock.csv", "wt", encoding="UTF-8")

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
    archivo_precios_promedios = open("precios_promedios.csv", "wt", encoding="UTF-8")

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

    while True:
        try:
            mostrar_opciones_disponibles(opciones_disponibles)
            dato = int(input(mensaje_input))

            resultado = None

            if dato == -1:
                resultado = -1
            elif (dato - 1) in range(len(opciones_disponibles)):
                resultado = dato - 1

            if not (resultado in range(len(opciones_disponibles)) or resultado == -1):
                raise IndexError("El numero ingresado es inválido")


            imprimir_separador()
            break
        except ValueError:
            imprimir_separador()
            print("El dato ingresado debe ser un numero")
            print("Por favor intente nuevamente")
            imprimir_separador()
        except IndexError as e:
            imprimir_separador()
            print(e)
            print("Por favor intente nuevamente")
            imprimir_separador()

    return resultado

def pedir_datos_compra():
    """Funcion encargada de pedir los datos de la marca, el tipo y modelo exacto deseados por el usuario"""

    marcas_disponibles = ["Toyota", "Schipani", "Chevrolet", "Ford"]

    marca_indice = pedir_dato_de_autos("Ingrese la marca que desea visualizar, para salir, simplemente ingrese -1: ", marcas_disponibles)

    if not marca_indice == -1:
        nombre_marca = marcas_disponibles[marca_indice]
        
        tipos_disponibles = ["Hatchback", "Sedan", "SUV", "Pick-up"]
        tipo_indice = pedir_dato_de_autos("Ingrese el tipo de auto que desea visualizar, para salir, simplemente ingrese -1: ", tipos_disponibles)

        nombre_tipo = tipos_disponibles[tipo_indice] if tipo_indice != -1 else -1

    else:
        nombre_marca, nombre_tipo = -1, -1 #Se sale automaticamente

    return nombre_marca, nombre_tipo

def obtener_modelos_disponibles(nombre_marca, nombre_tipo):
    """Funcion hecha para obtener los modelos que se encuentran registrados y disponibles en base a los dos argumentos que se les pasan (nombre_marca y nombre_tipo)"""
    archivo_autos = manejar_apertura_archivo("autos.json", "rt")
    archivo_stock = manejar_apertura_archivo("stock.csv", "r")
    disponibles = []

    autos = json.load(archivo_autos)
    archivo_autos.close()
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
                "nombre":nombre_modelo, 
                "equipamiento":equipamiento, 
                "precio":precio, 
                "stock":stock
            })

    archivo_stock.close()
    return disponibles


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


def mostrar_resumen(encargo_data):
    imprimir_separador()
    
    print("Resumen de su compra: ")

    for i, auto in enumerate(encargo_data["modelos_seleccionados"]):
        nombre, precio, color = auto["nombre"], auto["precio"], auto["color"]
        print(f"{i + 1}) nombre: {nombre} - color: {color} - precio: ${precio}")

    print(f"Monto acumulado: ${encargo_data['monto_total']}")

    imprimir_separador()

def encargar_autos():
    """Funcion que maneja todo lo referido al encargo de los autos que un usuario va a comprar"""

    finalizar_compra = False

    encargo_data = {
        "modelos_seleccionados":[],
        "monto_total": 0
    }
    
    while not finalizar_compra:
        print("Catalogo disponible: ")
        desplegar_menu_de_catalogo() # Despliegue del catalogo

        imprimir_separador()


        #---------------------- Seleccion de marca y tipo --------------------------------------------

        nombre_marca, nombre_tipo = pedir_datos_compra() # Funcion para pedir datos para realizar una compra

        if nombre_marca == -1:
            finalizar_compra = True
            continue
        elif nombre_tipo == -1:
            continue

        #---------------------- Obtencion de modelos disponibles --------------------------------------------

        modelos_disponibles = obtener_modelos_disponibles(nombre_marca, nombre_tipo)

        if len(modelos_disponibles) > 0:
            mostrar_modelos_disponibles(nombre_marca, nombre_tipo, modelos_disponibles)

        else:    
            print(f"No hay modelos en stock para {nombre_marca} - {nombre_tipo}.")
            imprimir_separador()

            continue

        #---------------------- Seleccion de modelo --------------------------------------------

        modelo_seleccionado_indice = pedir_dato_de_autos("Seleccione el modelo que mas le interese. Si desea volver al menú de inicio, ingrese -1: " , opciones_disponibles=[modelo["nombre"] for modelo in modelos_disponibles])

        # Vuelve al menú del inicio
        if modelo_seleccionado_indice == -1:
            continue

        # ------------------------- Seleccion de color --------------------------------------------

        colores_disponibles = ["Verde", "Azul", "Rojo", "Gris", "Blanco", "Negro", "Marron", "Amarillo"]
        mostrar_opciones_disponibles(colores_disponibles)
        color_indice = verificar_numero_valido("Seleccione alguno de los colores con los que contamos: ", rango=range(len(colores_disponibles))) - 1
        color_seleccionado = colores_disponibles[color_indice]
        
        #---------------------- Confirmacion de compra --------------------------------------------
        
        modelo_seleccionado = modelos_disponibles[modelo_seleccionado_indice]
        modelo_seleccionado["color"] = color_seleccionado

        encargo_data["modelos_seleccionados"].append(modelo_seleccionado)
        encargo_data["monto_total"] += modelo_seleccionado["precio"]
        print(f"Se agregó exitosamente el siguiente modelo al resumen: {modelo_seleccionado['nombre']} - {nombre_marca} - {nombre_tipo}")

        

        mostrar_opciones_disponibles(["Ver resumen", "Finalizar operacion"])
        decision = verificar_numero_valido("Ingrese la opcion deseada: ", rango=range(2))

        if decision == 1:
            mostrar_resumen(encargo_data)

            print("¿Desea pasar a finalizar la operacion? ")
            mostrar_opciones_disponibles(["Sí", "No (Encargar un nuevo vehiculo)"])
            
            respuesta = verificar_numero_valido("Ingrese la opcion deseada: ", rango=range(2))

            finalizar_compra = respuesta == 1
        else:
            finalizar_compra = True # Pasa a la parte de finalizar compra si el usuario ingresa 2

    return encargo_data


def aplicar_descuento_precio_final():
       """Funcion que se basa en un juego donde si el usuario gana, obtiene un descuento sobre el monto final de la compra"""

       aplicar_descuento = False

       print("¿Desea participar de un juego para conseguir un descuento del 20% para la compra de su auto?")
       des = verificar_numero_valido("Ingrese 1 si quiere y 2 si no quiere: ", rango=range(2))

       if des == 2: 
              print("Como usted desee.")
       else: 
              print("Nos alegra que haya querido participar. El juego trata de que tiene que elegir un numero del 1 al 5, si su numero es igual al que eligio el programa usted se gana el descuento asi de facil.")
              ran = rn.randint(1,5)
              
              numran = verificar_numero_valido("Ingrese un numero del 1 al 5: ", rango=range(5))
              
              if numran != ran:
                    print("Lo lamentamos, pero su numero no coincide, el numero correcto era:", ran)
              else:
                    print("¡Felicitaciones! Su numero coicide, usted se gano un descuento del 20%.")
                    aplicar_descuento = True
       return aplicar_descuento
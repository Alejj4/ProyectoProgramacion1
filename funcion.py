import matrices as mt
import random as rn

import json

import random
from faker import Faker

def verificar_numero_valido(mensaje_input):
    """Funcion que maneja la excepcion ValueError cuando en un input se espera un numero y no otra cosa"""
    
    while True:
        try:
            dato = int(input(mensaje_input))

            break
        except ValueError:
            print("El dato ingresado es inválido, el mismo debe ser un número")

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


def mostrar_autos(fila, columna):
    modelos, equipamientos, precios = mt.obtener_datos_de_modelos()
    indices_marcas = mt.obtener_indices_marcas()
    modelo_indice = indices_marcas[fila - 1][columna - 1]

    nombres = modelos[modelo_indice]
    equip = equipamientos[modelo_indice]
    prec = precios[modelo_indice]

    if len(nombres) == 0:
        print("Actualmente no hay stock disponible.")
    else:
        ancho = 20
        print("\ncaracterísticas/nombre".ljust(ancho), end='')
        for nombre in nombres:
            print(nombre.ljust(ancho), end='')
        print("\n")

        info = ["equipamiento", "precio"]
        datos = [equip, prec]

        for i in range(len(info)):
            etiqueta = info[i]
            fila_datos = datos[i]

            print(etiqueta.ljust(ancho), end='')
            for dato in fila_datos:
                print(str(dato).ljust(ancho), end='')
            print("\n")



def mostrar_opciones_disponibles(datos):
    for i, dato in enumerate(datos):
        print(f"{i + 1} - {dato}")


def comprar_auto(fila, columna, matriz_compras):
    """
    Permite al usuario comprar un auto de la marca (fila) y tipo (columna) elegido.
    """
    total = 0
    modelos, equipamientos, precios = mt.obtener_datos_de_modelos()
    indices_marcas = mt.obtener_indices_marcas()
    marca_indice = indices_marcas[fila - 1][columna - 1]

    nombres = modelos[marca_indice]
    precios = precios[marca_indice]

    if len(nombres) == 0: # Si no hay modelos disponibles
        print("No hay autos disponibles en esta categoría.")
    else:
    # ------------------------------------------------------------------------------------------------------------------
    # ELECCION DEL MODELO
        print("\nAutos disponibles:")
        for i in range(len(nombres)):
            print(f"{i+1}. {nombres[i]} - Precio: {precios[i]}")
            
        modelo_seleccionado_indice = verificar_numero_valido("\nSeleccione el número del auto que desea comprar: ") - 1
        while not modelo_seleccionado_indice in range(len(nombres)):
            imprimir_separador()
            print("Opcion no disponible, por favor ingrese un numero válido")
            mostrar_opciones_disponibles(nombres)
            modelo_seleccionado_indice = verificar_numero_valido("Seleccione alguno de los mismos: ") - 1
        imprimir_separador()
        
    # ------------------------------------------------------------------------------------------------------------------
    # ELECCIÓN DE COLOR
        colores_disponibles = ["Verde", "Azul", "Rojo", "Gris", "Blanco", "Negro", "Marron", "Amarillo"]
        mostrar_opciones_disponibles(colores_disponibles) # Mostramos los colores disponibles uno abajo del otro
        color_indice = verificar_numero_valido("Seleccione alguno de los colores con los que contamos: ") - 1 # Se resta 1 al numero para despues acceder al color por el indice de la lista
        imprimir_separador()
        while color_indice not in range(len(colores_disponibles)):
            print("Opcion no disponible, por favor ingrese un numero válido")
            mostrar_opciones_disponibles(colores_disponibles) # Mostramos los colores disponibles uno abajo del otro
            color_indice = verificar_numero_valido("Seleccione alguno de los mismos: ") - 1
            imprimir_separador()
            
# ------------------------------------------------------------------------------------------------------------------
        
        modelo_seleccionado = nombres[modelo_seleccionado_indice]
        color = colores_disponibles[color_indice]
        precio_modelo = precios[modelo_seleccionado_indice]  # precio base del modelo
        
        total += precio_modelo

        #PARTE FINAL DE LA COMPRA (CONFIRMACION)
        print(f"Usted seleccionó el modelo {modelo_seleccionado} de color {color}")
        
        opciones_de_confirmacion = ["Sí","No"]
        
        print("¿Desea confimar la compra? S/N: ")
        mostrar_opciones_disponibles(opciones_de_confirmacion)
        confirmacion = input("Ingrese la opción que desee: ")
        
        while not confirmacion.lower() in ["s", "n", "si", "sí", "no","1", "2"]: # Se verifica que el usuario haya ingresado una respuesta valida a la confirmacion
            imprimir_separador()
            print("Disculpe, no se ingresó una respuesta valida")
            
            print("¿Desea confimar la compra? S/N: ")
            mostrar_opciones_disponibles(opciones_de_confirmacion)
            confirmacion = input("Ingrese la opción que desee: ")

        if confirmacion.lower() in ["s", "si", "sí", "1"]: # El usuario confirma la compra
            matriz_compra_actualizada = mt.actualizar_matriz_compra(fila, columna, matriz_compras)
            
            print("matriz compra actualizada")
            imprimir_separador()
            mostrar_matriz(matriz_compra_actualizada)
        else: # El usuario cancela la compra
            print("Cancelando compra...")
            return 0
        return total
    
def verificar_marca(marca):
    while marca not in (range(1,5)):
        print("Opción incorrecta! Intente de nuevo.")
        marca = int(input('Ingrese 1 para Toyota, 2 para Honda, 3 para Chevrolet y 4 para Ford: '))
        imprimir_separador()
    return marca

def verificar_modelo(modelo):
    while modelo not in (range(1,5)):
        print("Opción incorrecta! Intente de nuevo.")
        modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
    return modelo


def descuento_auto():
       descuento = 0
       des = verificar_numero_valido("¿Desea participar de un juego para conseguir un descuento del 20% para la compra de su auto? Ingrese 1 si quiere y 2 si no quiere: ")
       while des != 1 and des != 2:
              des = verificar_numero_valido("Su respuesta es incorrecta. Ingrese 1 si quiere participar y 2 si no quiere: ")
       if des == 2: 
              print("Como usted desee. Nos vemos!")
       else: 
              print("Nos alegra que haya querido participar. El juego trata de que tiene que elegir un numero del 1 al 5, si su numero es igual al que eligio el programa usted se gana el descuento asi de facil.")
              ran = rn.randint(1,5)
              numran = verificar_numero_valido("Ingrese un numero del 1 al 5: ")
              while numran < 1 or numran > 5:
                     numran = verificar_numero_valido("Número fuera de rango, ingrese un numero entre 1 y 5: ")
              if numran != ran:
                    print("Lo lamentamos, pero su numero no coincide, el numero correcto era:", ran)
              else:
                    print("¡Felicitaciones! Su numero coicide, usted se gano un descuento del 20%.")
                    descuento += 1
       return descuento


def desplegar_menu_informes():
    informes_disponibles = ["Los 3 autos más caros y baratos.", "Los autos más y menos vendidos.", "DNI de los clientes."]

    print("A continuación se presentan los distintos informes que puede consultar:")
    for i, informe in enumerate(informes_disponibles):
        print(f"{i + 1} - {informe}")

def max_min_autos():
    modelos, _, precios = mt.obtener_datos_de_modelos()
    
    nombres_modelos = []
    fila_precios = []
    columna_precios = []
    lista_precios = []
    
    # Armamos listas planas
    for i in range(len(precios)):
        for j in range(len(precios[i])):
            nombres_modelos.append(modelos[i][j])
            fila_precios.append(i)
            columna_precios.append(j)
            lista_precios.append(precios[i][j])
    
    # Ordenamos los índices según los precios
    indices_ordenados = sorted(range(len(lista_precios)), key=lambda k: lista_precios[k])
    
    # Usamos slicing para quedarnos con los 3 más baratos y 3 más caros
    indices_menores = indices_ordenados[:3]
    indices_mayores = indices_ordenados[-3:]
    
    print("------------------------------------------------------------------------------")
    print("Autos más baratos son: \n")
    for k in indices_menores:
        print(f"{nombres_modelos[k]}: {lista_precios[k]}")
    print("------------------------------------------------------------------------------")
    
    print("Los autos más caros son: \n")
    for k in indices_mayores:
        print(f"{nombres_modelos[k]}: {lista_precios[k]}")
    print("------------------------------------------------------------------------------")
    
    return indices_menores, indices_mayores

def obtener_marca_mas_vendida(vehiculos_comprados_matriz):
    marcas = ["Toyota", "Schipani", "Chevrolet", "Ford"]
    lista_autos_comprados = [sum(marca_autos) for marca_autos in vehiculos_comprados_matriz]

    maximo = max(lista_autos_comprados)
    posicion_max = lista_autos_comprados.index(maximo)

    imprimir_separador()
    print("La marca de autos más vendida es", marcas[posicion_max], "con", maximo, "unidades vendidas")
    imprimir_separador()

# def norep(dato,lista):
#     #revisa que no haya un dato repetido en una lista
#     flag = 0
#     if dato in lista:
#         flag = 1
#     return flag


# def dni_Clientes(lista):
#     j = 1
#     imprimir_separador()
#     for i in lista:
#         print (f"Cliente {j}: {i} \n")
#         j += 1
#     imprimir_separador()

#

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
                    stock_disponible = random.randint(0, 5)
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


        return matriz_precios_promedios
    

def ingreso_de_autos(mensaje_input, opciones_disponibles):
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
    marcas_disponibles = ["Toyota", "Schipani", "Chevrolet", "Ford"]

    marca_indice = ingreso_de_autos("Ingrese la marca que desea visualizar, para finalizar, simplemente ingrese -1: ", marcas_disponibles)

    tipos_disponibles = ["Hatchback", "Sedan", "SUV", "Pick-up"]

    tipo_indice = ingreso_de_autos("Ingrese el tipo de auto que desea visualizar, para finalizar, simplemente ingrese -1: ", tipos_disponibles)

    nombre_marca = marcas_disponibles[marca_indice]
    nombre_tipo = tipos_disponibles[tipo_indice]

    return nombre_marca, nombre_tipo

# REHACER SIN EL READLINES()
def obtener_modelos_disponibles(nombre_marca, nombre_tipo):
    archivo_autos = manejar_apertura_archivo("autos.json", "rt")
    archivo_stock = manejar_apertura_archivo("stock.csv", "r")
    disponibles = []

    autos = json.load(archivo_autos)
    archivo_autos.close()
    stock_data = {}
    lineas = archivo_stock.readlines()
    
    archivo_stock.close()
    for linea in lineas[1:]:
        partes = linea.strip().split(",")
        if len(partes) != 3:
            continue
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

    return disponibles


def mostrar_modelos_disponibles(nombre_marca, nombre_tipo, modelos_disponibles):

    if not modelos_disponibles:
        print(f"No hay modelos disponibles para {nombre_marca} - {nombre_tipo}.")
        imprimir_separador()
        return

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
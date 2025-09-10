import matrices as mt
import random as rn


def imprimir_separador():
    print("-"*78)


def mostrar_matriz(matriz):
    esquina = 'Marcas/Autos'
    columnas = ['Hatchback', 'Sedan', 'Suv', 'PickUp']
    filas = ['Toyota', 'Schipani', 'Chevrolet', 'Ford']
    ancho = 15

    print(esquina.ljust(ancho), end='')
    for col in columnas:
        print(col.ljust(ancho), end='')
    print()

    for nombre, fila in zip(filas, matriz):
        print(nombre.ljust(ancho), end='')
        for fil in fila:
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
        ancho = 30
        print("\ncaracterísticas/nombre".ljust(ancho), end='')
        for nombre in nombres:
            print(nombre.ljust(ancho), end='')
        print("\n")

        info = ["equipamiento", "precio"]
        for etiqueta, fila_datos in zip(info, [equip, prec]):
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
            
        modelo_seleccionado_indice = int(input("\nSeleccione el número del auto que desea comprar: ")) - 1
        while not modelo_seleccionado_indice in range(len(nombres)):
            imprimir_separador()
            print("Opcion no disponible, por favor ingrese un numero válido")
            mostrar_opciones_disponibles(nombres)
            modelo_seleccionado_indice = int(input("Seleccione alguno de los mismos: ")) - 1
        imprimir_separador()
        
    # ------------------------------------------------------------------------------------------------------------------
    # ELECCIóN DE COLOR
        colores_disponibles = ["Verde", "Azul", "Rojo", "Gris", "Blanco", "Negro", "Marron", "Amarillo"]
        mostrar_opciones_disponibles(colores_disponibles) # Mostramos los colores disponibles uno abajo del otro
        color_indice = int(input("Seleccione alguno de los colores con los que contamos: ")) - 1 # Se resta 1 al numero para despues acceder al color por el indice de la lista
        imprimir_separador()
        while color_indice not in range(len(colores_disponibles)):
            print("Opcion no disponible, por favor ingrese un numero válido")
            mostrar_opciones_disponibles(colores_disponibles) # Mostramos los colores disponibles uno abajo del otro
            color_indice = int(input("Seleccione alguno de los mismos: ")) - 1
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
       des = int(input("¿Desea participar de un juego para conseguir un descuento del 20% para la compra de su auto? Ingrese 1 si quiere y 2 si no quiere: "))
       while des != 1 and des != 2:
              des = int(input("Su respuesta es incorrecta. Ingrese 1 si quiere participar y 2 si no quiere: "))
       if des == 2: 
              print("Como usted desee. Nos vemos!")
       else: 
              print("Nos alegra que haya querido participar. El juego trata de que tiene que elegir un numero del 1 al 5, si su numero es igual al que eligio el programa usted se gana el descuento asi de facil.")
              ran = rn.randint(1,5)
              numran = int(input("Ingrese un numero del 1 al 5: "))
              while numran < 1 or numran > 5:
                     numran = int(input("Número fuera de rango, ingrese un numero entre 1 y 5: "))
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

def norep(dato,lista):
    #revisa que no haya un dato repetido en una lista
    flag = 0
    if dato in lista:
        flag = 1
    return flag


def dni_Clientes(lista):
    j = 1
    imprimir_separador()
    for i in lista:
        print ('Cliente',str(j).ljust(2), str(i).ljust(5), ': ', end='' '\n')
        j += 1
    imprimir_separador()
    

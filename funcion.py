import matrices as mt
import random as rn

def imprimir_separador():
    print("------------------------------------------------------------------------------")

def mostrar_matriz(matriz):
    esquina = 'Marcas/Autos'
    columnas = ['Hatchback','Sedan','Suv','PickUp']
    filas = ['Toyota', 'Schipani', 'Chevrolet', 'Ford']
    ancho = 15
    
    print(esquina.ljust(ancho), end='')
    for col in columnas:
        print(col.ljust(ancho),end = '')
    print()
    
    for nombre,fila in zip(filas, matriz):
        print(nombre.ljust(ancho),end='')
        for fil in fila:
            print(str(fil).ljust(ancho),end ='')
        print()

# CORREGIR
def mostrar_autos(fila, columna):
    """
    Muestra los autos disponibles de una marca y tipo específico.
    Usa los índices de la estructura homogénea.
    """
    modelos, equipamientos, precios = mt.obtener_datos_de_modelos() # Obtengo las 3 matrices de los datos de los autos
    indices_marcas = mt.obtener_indices_marcas() # Lista de los indices de las matrices
    modelo_indice = indices_marcas[fila - 1][columna - 1] # Obtengo el indice del modelo que necesito

    nombres = modelos[modelo_indice]
    equipamientos = equipamientos[modelo_indice]
    precios = precios[modelo_indice]

    if len(nombres) == 0:
        print("Actualmente no hay stock disponible.")
    else:
        ancho = 30
        print("\ncaracterísticas/nombre".ljust(ancho), end='')
        for nombre in nombres:
            print(nombre.ljust(ancho), end='')
        print("\n")

        info = ["equipamiento", "precio"]
        for etiqueta, fila_datos in zip(info, [equipamientos, precios]):
            print(etiqueta.ljust(ancho), end='')
            for dato in fila_datos:
                print(str(dato).ljust(ancho), end='')
            print("\n")
    

def mostrar_opciones_disponibles(datos): # datos tiene que ser una lista de strings unicamente
    """
    Funcion para mostrar enumeradamente los datos de una lista.
    Se puede usar para elegir entre modelos disponibles y para la eleccion de colores de un auto durante el proceso de compra
    """
    for i, dato in enumerate(datos): # Accedo a cada dato individual y lo imprimo con su posicion en la lista, recorro cada uno e imprimo las opciones
        print(f"{i + 1} - {dato}")

# CORREGIR
def comprar_auto(fila, columna, matrizcompra):
    """
    Permite al usuario comprar un auto de la marca (fila) y tipo (columna) elegido.
    """
    total = 0
    modelos, equipamientos, precios = mt.obtener_datos_de_modelos()
    indices_marcas = mt.obtener_indices_marcas()
    modelo_indice = indices_marcas[fila - 1][columna - 1]

    nombres = modelos[modelo_indice]
    precios = precios[modelo_indice]

    if len(nombres) == 0:
        print("No hay autos disponibles en esta categoría.")
    else:
        print("\nAutos disponibles:")
        for i in range(len(nombres)):
            print(f"{i+1}. {nombres[i]} - Equipamiento: {equipamientos[i]} - Precio: {precios[i]}")

        mostrar_opciones_disponibles(nombres)
        opcion = int(input("\nSeleccione el número del auto que desea comprar: "))

        if opcion < 1 or opcion > len(nombres):
            print("Opción inválida. No se realizó la compra.")
        else:
            # actualización del equipamiento en la posición elegida
            equipamientos[opcion - 1] = equipamientos[opcion - 1] + 1
            equipamientos[modelo_indice] = equipamientos
            print(f"Compra realizada con éxito: {nombres[opcion - 1]}")

'''def comprar_auto(fila, columna, matrizcompra):
    """
    funcion encargada del proceso de compra de un auto
    """
    total = 0
    datos_auto = mt.obtener_matriz_especifica(fila, columna) # Obtengo los datos del tipo de auto que el usuario eligió

    cant_modelos = len(datos_auto[0]) # Saco la longitud de cualquiera de las 3 filas de la matriz de los datos del auto (Todas deben tener la misma cantidad de datos)

    if cant_modelos == 1: # Si solo hay un modelo de auto disponible para el tipo y marca elegidos
        modelo_indice = 0
        unico_disponible = datos_auto[0][0] # Accedo a la fila de nombres y al unico disponible
        print(f"Actualmente solo contamos con el modelo: {unico_disponible}")
    else:
        print("Seleccione el modelo que prefiera: ")
        mostrar_opciones_disponibles(datos_auto[0]) # Mostramos los nombres disponibles uno abajo del otro
        
    
        
        # ELECCION DE MODELO
        modelo_indice = int(input("Seleccione alguno de los mismos: ")) - 1 # Se resta 1 al numero para despues acceder al modelo por el indice con el que aparece en la fila de la matriz
        
        while modelo_indice not in range(len(datos_auto[0])):
            print("Opcion no disponible, por favor ingrese un numero válido")
            mostrar_opciones_disponibles(datos_auto[0])
            modelo_indice = int(input("Seleccione alguno de los mismos: ")) - 1 # Con este indice ya se puede acceder a los datos especificos de lo que el usuario quiere
            imprimir_separador()
        imprimir_separador()
    
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

    nombre_modelo = datos_auto[0][modelo_indice] # Saco el nombre por el indice de la fila
    color = colores_disponibles[color_indice]
    precio_modelo = datos_auto[2][modelo_indice]  # precio base del modelo
    print(f"El precio base del modelo seleccionado es: {precio_modelo}") 
    total += precio_modelo
    #PARTE FINAL DE LA COMPRA (CONFIRMACION)
    print(f"Usted seleccionó el modelo {nombre_modelo} de color {color}")
    confirmacion = input("¿Desea confimar la compra? S/N: ")
    while not confirmacion.lower() in ["s", "n", "si", "sí", "no"]: # Se verifica que el usuario haya ingresado una respuesta valida a la confirmacion
        imprimir_separador()
        print("Disculpe, no se ingresó una respuesta valida")
        confirmacion = input("¿Desea confimar la compra? S/N: ")

    if confirmacion.lower() in ["s", "si", "sí"]:
        matriz_compra_actualizada = mt.actualizar_matriz_compra(fila, columna, matrizcompra)
        
        
        print("matriz compra actualizada")
        imprimir_separador()
        mostrar_matriz(matriz_compra_actualizada)
    return total
'''
    

    
def verificar_marca():
    marca = int(input('Ingrese 1 para Toyota, 2 para Honda, 3 para Chevrolet y 4 para Ford: '))
    while marca not in (range(1,5)):
        print("Opción incorrecta! Intente de nuevo.")
        marca = int(input('Ingrese 1 para Toyota, 2 para Honda, 3 para Chevrolet y 4 para Ford: '))
    return marca
def verificar_modelo():
    modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
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
                     numran = int(input("Su numero es incorrecto, ingrese un numero entre 1 y 5: "))
              if numran != ran:
                    print("Lo lamentamos, pero su numero no coincide, el numero correcto era:", ran)
              else:
                    print("¡Felicitaciones! Su numero coicide, usted se gano un descuento del 20%.")
                    descuento += 1
       return descuento

def desplegar_menu_informes():
    informes_disponibles = ["Los 3 autos mas caros y baratos.", "Los autos mas y menos vendidos"]
    
    print("A continuación se presentan los distintos informes que puede consultar:")
    
    for i, informe in enumerate(informes_disponibles):
        print(f"{i + 1} - {informe}")
        
# CORREGIR
def max_min_autos():
       info_autos=mt.obtener_datos_de_modelos()
       listaprecio=[]
       for autos in info_autos: 
           if len(autos)>0:
               nombres=autos[0]
               precios=autos[2]
               for i in range(len(nombres)):
                   listaprecio.append([nombres[i], precios[i]])
        
       lista_ordenada= sorted(listaprecio, key=lambda x: x[1])
       los_3_baratos=lista_ordenada[:3]
       print("------------------------------------------------------------------------------")
       print("Autos mas baratos\n")   
       for n,p in los_3_baratos:
        print(f"{n}: {p}")
       print("------------------------------------------------------------------------------")
       los_3_caros=lista_ordenada[-3:]
       print("Autos mas caros\n")
       for n,p in los_3_caros:
            print(f"{n}: {p}")
       print("------------------------------------------------------------------------------")
       return (los_3_baratos,los_3_caros)

def obtener_marca_mas_vendida(vehiculos_comprados_matriz):
    """
    Funcion encargada de mostrar un mensaje con la marca que más ventas tuvo
    """
    marcas=["Toyota", "Schipani", "Chevrolet","Ford"]
    lista_autos_comprados=[]
    for marca_autos in vehiculos_comprados_matriz:
        lista_autos_comprados.append(sum(marca_autos))
        
    maximo=max(lista_autos_comprados)
    # minimo=min(lista_autos_comprados)
    
    posicion_max=lista_autos_comprados.index(maximo)
    # posicion_mini=lista_autos_comprados.index(minimo)
    
    imprimir_separador()
    print("La marca de autos mas vendida es",marcas[posicion_max],"con",maximo, "unidades vendidas")
    # print("La marca de autos menos vendida es",marcas[posicion_mini],"con",minimo, "unidades vendidas")
    imprimir_separador()
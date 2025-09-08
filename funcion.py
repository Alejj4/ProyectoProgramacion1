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
 
def mostrar_autos(datos_de_auto_matriz): # Ej de datos (no vacios): [['schipani uade Seminuevo', 'Schipani Schiziano'], [1, 2], [28, 35]]
    """Funcion que printea la matriz del auto y marca seleccionado"""

    # Palabras que van a estar en cada submatriz
    info = ['equipamiento', 'precio']
    esquina = 'caracteristicas/nombre'
    nombres = datos_de_auto_matriz[0] 
    
    ancho = 30 #ancho que quiero que haya entre cada palabra
    print('')
    print(esquina.ljust(ancho), end ='')#printea esquina con espacio de 30 a su derecha y que lo siguiente lo anote al lado
    for col in nombres:#Selecciona la lista de nombres que va a usar en base a lo ingresado por el usuario
        print(col.ljust(ancho), end='')#printea los nombres igual que la esquina
    print()
    print('')

    # Se imprimen datos de equipamiento y precio
    for infom,fila in zip(info, datos_de_auto_matriz[1:]):# nos permite printear primero el dato de la lista info y a su lado con el siguiente for los datos requeridos por el usuario
        print(infom.ljust(ancho),end='')
        for fil in fila:
            print(str(fil).ljust(ancho),end ='')
        print()
        print('')

def mostrar_opciones_disponibles(datos): # datos tiene que ser una lista de strings unicamente
    """
    Funcion para mostrar enumeradamente los datos de una lista.
    Se puede usar para elegir entre modelos disponibles y para la eleccion de colores de un auto durante el proceso de compra
    """
    for i, dato in enumerate(datos): # Accedo a cada dato individual y lo imprimo con su posicion en la lista, recorro cada uno e imprimo las opciones
        print(f"{i + 1} - {dato}")


def comprar_auto(fila, columna, matrizcompra):
    """
    funcion encargada de comprar autos
    """
    
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
    
    # ELECCION DE COLOR
    colores_disponibles = ["verde", "azul", "rojo", "gris", "blanco", "negro", "rojo", "amarillo"]
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
              print("Como usted desee, el precio final del auto es el siguiente: ")
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









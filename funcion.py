import matrices as mt
import random as rn


def imprimir_separador():
    print("------------------------------------------------------------------------------")


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


def comprar_auto(fila, columna, matrizcompra):
    total = 0
    modelos, equipamientos, precios = mt.obtener_datos_de_modelos()
    indices_marcas = mt.obtener_indices_marcas()
    modelo_indice = indices_marcas[fila - 1][columna - 1]

    nombres = modelos[modelo_indice]
    prec = precios[modelo_indice]

    if len(nombres) == 0:
        print("No hay autos disponibles en esta categoría.")
    else:
        print("\nAutos disponibles:")
        for i in range(len(nombres)):
            print(f"{i+1}. {nombres[i]} - Precio: {prec[i]} mil dólares")

        mostrar_opciones_disponibles(nombres)
        opcion = int(input("\nSeleccione el número del auto que desea comprar: "))

        if opcion < 1 or opcion > len(nombres):
            print("Opción inválida. No se realizó la compra.")
        else:
            print(f"Compra realizada con éxito: {nombres[opcion - 1]}")
            total = prec[opcion - 1]
            matrizcompra[fila - 1][columna - 1] += 1

    return total


def verificar_marca():
    marca = int(input('Ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))
    while marca not in (range(1, 5)):
        print("Opción incorrecta! Intente de nuevo.")
        marca = int(input('Ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))
    return marca


def verificar_modelo():
    modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
    while modelo not in (range(1, 5)):
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
        print("El juego trata de que tiene que elegir un número del 1 al 5.")
        ran = rn.randint(1, 5)
        numran = int(input("Ingrese un número del 1 al 5: "))
        while numran < 1 or numran > 5:
            numran = int(input("Su número es incorrecto, ingrese un número entre 1 y 5: "))
        if numran != ran:
            print("Lo lamentamos, el número correcto era:", ran)
        else:
            print("¡Felicitaciones! Usted se ganó un descuento del 20%.")
            descuento = 1
    return descuento


def desplegar_menu_informes():
    informes_disponibles = ["Los 3 autos más caros y baratos.", "Los autos más y menos vendidos"]

    print("A continuación se presentan los distintos informes que puede consultar:")
    for i, informe in enumerate(informes_disponibles):
        print(f"{i + 1} - {informe}")


def max_min_autos():
    modelos, equipamientos, precios = mt.obtener_datos_de_modelos()
    listaprecio = []
    for i in range(len(modelos)):
        for j in range(len(modelos[i])):
            listaprecio.append([modelos[i][j], precios[i][j]])

    lista_ordenada = sorted(listaprecio, key=lambda x: x[1])
    los_3_baratos = lista_ordenada[:3]
    los_3_caros = lista_ordenada[-3:]

    imprimir_separador()
    print("Autos más baratos\n")
    for n, p in los_3_baratos:
        print(f"{n}: {p}")
    imprimir_separador()
    print("Autos más caros\n")
    for n, p in los_3_caros:
        print(f"{n}: {p}")
    imprimir_separador()

    return los_3_baratos, los_3_caros


def obtener_marca_mas_vendida(vehiculos_comprados_matriz):
    marcas = ["Toyota", "Schipani", "Chevrolet", "Ford"]
    lista_autos_comprados = [sum(marca_autos) for marca_autos in vehiculos_comprados_matriz]

    maximo = max(lista_autos_comprados)
    posicion_max = lista_autos_comprados.index(maximo)

    imprimir_separador()
    print("La marca de autos más vendida es", marcas[posicion_max], "con", maximo, "unidades vendidas")
    imprimir_separador()



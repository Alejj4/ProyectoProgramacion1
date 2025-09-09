import random as schipani
import funcion
import matrices as mt

def imprimir_separador():
    print("------------------------------------------------------------------------------")

def desplegar_menu_de_catalogo():
    
    #matriz display para el usuario
    matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,4,5],
    [3,5,6,8]
    ]
    
    matriz_precios_promedios = mt.calcular_precios_promedio(matriz)
    funcion.mostrar_matriz(matriz_precios_promedios)

def main():
    
    vehiculos_comprados_matriz =[
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    Vtoyota = []
    Vschipani = []
    VChevrolet =[]
    Vford =[]
    
    print('Bienvenido a Schipani Motors Sport esta es nuestra disponibilidad. ')
    desplegar_menu_de_catalogo()
    
    marca = 0
    precio_total = 0
    while marca != -1:

        imprimir_separador()
        print('Seleccione la marca que le gustaria ver')
        print("Para salir simplemente ingrese -1")
        marca = int(input('Ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))
        imprimir_separador()
        

        if marca == -1:
            print('Compra finalizada.')

        else:
            while marca not in (range(1,5)):
                print("Opción incorrecta! Intente de nuevo.")
                marca = int(input('Ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))
                imprimir_separador()
            print('Ahora seleccione los modelos que quiere ver.')
            modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
            imprimir_separador()
            while modelo not in (range(1,5)):
                print("Opción incorrecta! Intente de nuevo.")
                modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
                imprimir_separador()

            datos_de_auto_matriz = mt.obtener_matriz_especifica(marca, modelo)
            


            while len(datos_de_auto_matriz) == 0: # Esto quiere decir que no hay stock de la marca y modelo elegido
                print("\nDisculpe, actualmente no hay stock disponible. Puede probar con otro modelo")
                imprimir_separador()                
                modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
                datos_de_auto_matriz = mt.obtener_matriz_especifica(marca, modelo)
                

            funcion.mostrar_autos(datos_de_auto_matriz)
            imprimir_separador()
             
            precio_total += funcion.comprar_auto(marca, modelo, vehiculos_comprados_matriz)  # Se pasan marca y modelo como posiciones tal cual como las ingresa el usuario (no como indices)
            print("\nTotal de la compra hasta ahora:", precio_total, "mil dolares.")
            dscto = funcion.descuento_auto()
            if dscto == 1:
                print("El precio final con el descuento del 20% aplicado es de:", int(precio_total*0.80), "mil dolares.")

    
    opcion = int(input("¿Le gustaría ver los informes obtenidos? (1=Sí | -1=No): "))

    while opcion != 1 and opcion != -1:
        print("Opción incorrecta. Por favor, ingrese 1 para sí o -1 para no.")
        opcion = int(input("¿Le gustaría ver los informes obtenidos? (1=Sí | -1=No): "))

    while opcion != -1:
        funcion.desplegar_menu_informes()
        opcion = int(input("Seleccione el informe que desea visualizar (-1 para salir): "))

        if opcion == 1:
            funcion.max_min_autos()
        else:
            print("Opción inválida. Intente de nuevo.")
            
    print("Muchas gracias por venir a Schipani Motors, ¡nos vemos!")
main()
    
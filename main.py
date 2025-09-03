import random as schipani
import funcion
import matrices as mt







def main():

    matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,4,5],
    [3,5,6,8]
    ]
    print('Bienvenido a Schipani Motors Sport esta es nuestra disponibilidad. ')
    funcion.mostrar_matriz(matriz)
    marca = 0
    while marca != -2:
        print('Seleccione la marca que le gustaria ver')
        marca = int(input('Ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))
        while marca not in (range(1,5)):
            print("Opción incorrecta! Intente de nuevo.")
            marca = int(input('ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))
        marca = marca - 1
        print('Ahora seleccione los modelos que quiere ver.')
        modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
        while modelo not in (range(1,5)):
            print("Opción incorrecta! Intente de nuevo.")
            modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
        modelo = modelo -1
        funcion.mostrar_autos(marca,modelo)
        

main()
    
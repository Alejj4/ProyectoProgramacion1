import random as schipani
import funcion



matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,4,5],
    [3,5,6,8]
]



def main():
    print('Bienvenido a schipani motors sport esta es nuestra disponibilidad ')
    funcion.mostrar_matriz(matriz)
    #Alejo va a hacer la verificacion de datos
    print('Seleccione la marca que le gustaria ver')
    marca = int(input('ingrese 1 para Toyota, 2 para Honda, 3 para Chevrolet y 4 para Ford '))
    print('ahora seleccione los modelos que quiere ver')
    modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp '))
    


main()
    
import random as schipani
from funcion import verificar_marca,mostrar_matriz,verificar_modelo







def main():
    matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,4,5],
    [3,5,6,8]
    ]
    print('Bienvenido a Schipani Motors Sport esta es nuestra disponibilidad. ')
    mostrar_matriz(matriz)
    print('Seleccione la marca que le gustaria ver')
    verificar_marca()
    print('Ahora seleccione los modelos que quiere ver.')
    verificar_modelo()


main()
    
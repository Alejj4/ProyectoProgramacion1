import random as schipani
import funcion
import matrices as mt



def main():
    #matriz display para el usuario
    matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,4,5],
    [3,5,6,8]
    ]
    vehiculos_comprados=[[0,0,0,0],
                         [0,0,0,0],
                         [0,0,0,0],
                         [0,0,0,0]]
    Vtoyota = []
    Vschipani = []
    VChevrolet =[]
    Vford =[]
    
    print('Bienvenido a Schipani Motors Sport esta es nuestra disponibilidad. ')
    funcion.mostrar_matriz(matriz)
    marca = 0
    
    while marca != -1:
        print('Seleccione la marca que le gustaria ver')
        print("Para salir simplemente ingrese -1")
        marca = int(input('Ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))

        if marca == -1:
            print('programa finalizado')
        else:
            while marca not in (range(1,5)):
                print("Opción incorrecta! Intente de nuevo.")
                marca = int(input('Ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))

            print('Ahora seleccione los modelos que quiere ver.')
            modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))

            while modelo not in (range(1,5)):
                print("Opción incorrecta! Intente de nuevo.")
                modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))

            matriz = mt.llamar_matriz(marca, modelo)


            while len(matriz) == 0: # Esto quiere decir que no hay stock de la marca y modelo elegido
                print("\nDisculpe, actualmente no hay stock disponible. Puede probar con otro modelo")
                print("----------------------------------------------")
                
                modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
                matriz = mt.llamar_matriz(marca, modelo)
                print(matriz)

            funcion.mostrar_autos(marca, modelo)
                
            funcion.compra_auto(marca, modelo, vehiculos_comprados)
            
                

            # Una vez salido del bucle queria hacer listas con datos tipo cantidad de plata que hizo cada marca. autos vendidos(ya que hice una funcion para sacar el nombre individual de cada auto comprado podemos hacer una lista de cuantos autos de cada tipo se vendio etc y demas cosas)
            #no use lambda todavia
            #soy medio autista
            #solo 2 personas sabian como hice el codigo, dios y yo, ahora solo lo sabe dios, asi que si no entienden algo preguntenle a chatgtp
    


main()
    
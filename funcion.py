import matrices as mt
def mostrar_matriz(matriz):
    esquina = 'Marcas/Autos'
    columnas = ['Hatchback','Sedan','Suv','PickUp']
    filas = ['Toyota', 'Honda', 'Chevrolet', 'Ford']
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

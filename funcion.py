import matrices as mt
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

def mostrar_autos(columna,fila):
    matriz = mt.llamar_matriz(columna ,fila)
    
    # Nombre de los diferentes tipos de autos
    info = ['equipamento', 'precio']
    esquina = 'caracteristicas/nombre'
    ToHa = ['Yaris xs', 'Yaris xls', 'Yaris s']
    ToSe = []
    ToSu = ['Cross xli', 'Cross seG']
    ToPi = ['Hilux dx4x4','Hiluxsr4x4']
    ScHa = []
    ScSe = ['schipani uade Seminuevo','Schipani Schiziano']
    ScSu = ['schipani chipa', 'schipani bochoQuemado']
    ScPi = ['Schipani Pipani']
    ChHa = []
    ChSe = ['Onixplus']
    ChSu = ['Spring', 'Tracker']
    ChPi = ['Montana', 'S10', 'Silverado']
    FoHa = []
    FoSe = []
    FoSu = ['Territory', 'Kuga Hybrid', 'Everest']
    FoPi = ['Maverick', 'Rnager Raptor', 'F-150 Lariat Hybrid']




    nombres = [[ToHa,ToSe,ToSu,ToPi],
               [ScHa,ScSe,ScSu,ScPi],
               [ChHa,ChSe,ChSu,ChPi],
               [FoHa,FoSe,FoSu,FoPi]]
    ancho = 30
    print('')
    print(esquina.ljust(ancho), end ='')
    for col in nombres[columna][fila]:
        print(col.ljust(ancho), end='')
    print()
    print('')
    for nombre,fila in zip(info, matriz):
        print(nombre.ljust(ancho),end='')
        for fil in fila:
            print(str(fil).ljust(ancho),end ='')
        print()
        print('')

    
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

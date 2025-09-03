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
#Funcion que printea la matriz del auto y marca seleccionado 
def mostrar_autos(columna,fila):
    matriz = mt.llamar_matriz(columna ,fila)
    
    # Palabras que van a estar en cada submatriz

    info = ['equipamento', 'precio']
    # Nombre de los diferentes tipos de autos, las vacias es porque no tiene stock
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



    #Matriz de nombres declarados previamente
    nombres = [[ToHa,ToSe,ToSu,ToPi],
               [ScHa,ScSe,ScSu,ScPi],
               [ChHa,ChSe,ChSu,ChPi],
               [FoHa,FoSe,FoSu,FoPi]]
    ancho = 30 #ancho que quiero que haya entre cada palabra
    print('')
    print(esquina.ljust(ancho), end ='')#printea esquina con espacio de 30 a su derecha y que lo siguiente lo anote al lado
    for col in nombres[columna][fila]:#Selecciona la lista de nombres que va a usar en base a lo ingresado por el usuario
        print(col.ljust(ancho), end='')#printea los nombres igual que la esquina
    print()
    print('')
    for infom,fila in zip(info, matriz):# nos permite printear primero el dato de la lista info y a su lado con el siguiente for los datos requeridos por el usuario
        print(infom.ljust(ancho),end='')
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

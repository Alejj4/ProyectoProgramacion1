import matrices as mt

def modelos_de_autos():
    #rearmar esto en el archivo matrices
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
    return nombres

def precios(matriz):
    for columna in range(4):
        for fila in range(4):
            promedio_autos = mt.llamar_matriz(columna, fila)
            if len(promedio_autos)>1:
                preciospromedios=sum(promedio_autos[1])//len(promedio_autos[1])
            else:
                preciospromedios = 0
            matriz[columna][fila]=preciospromedios
    return matriz


def mostrar_matriz(matriz):
    matriz2 = precios(matriz)
    esquina = 'Marcas/Autos'
    columnas = ['Hatchback','Sedan','Suv','PickUp']
    filas = ['Toyota', 'Schipani', 'Chevrolet', 'Ford']
    ancho = 15
    print(esquina.ljust(ancho), end='')
    for col in columnas:
        print(col.ljust(ancho),end = '')
    print()
    for nombre,fila in zip(filas, matriz2):
        print(nombre.ljust(ancho),end='')
        for fil in fila:
            print(str(fil).ljust(ancho),end ='')
        print()
#Funcion que printea la matriz del auto y marca seleccionado 
def mostrar_autos(columna,fila):
    matriz = mt.llamar_matriz(columna ,fila)
    
    # Palabras que van a estar en cada submatriz

    info = ['equipamento', 'precio']
    esquina = 'caracteristicas/nombre'
    nombres = modelos_de_autos()



    #Matriz de nombres declarados previamente
    
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

def nomAu(columna, fila, eleccion):
   # Cuando se llama a un vehiculo cuya lista esta vacia da error, hay que corregir eso
    # Esta funcion funciona igual que mostrar matriz solo que sin la parte de mostrarla, te busca los nombres en base a lo eleigod por el usuario y luego agarra el auto en la posicion que eligio el usuario
    
    nombres = modelos_de_autos()



    #Matriz de nombres declarados previamente
   
    elegido = nombres[columna][fila]
    elegidoNom = elegido[eleccion -1]
    return(elegidoNom)


def compra_auto(columna,fila,matrizcompra):

    # funcion para compra de autos
    matriz = mt.llamar_matriz(columna, fila)#llamo la matriz de vehiculos que quise comprar

    

    for i in range(len(matriz[1])):
        i += 1
         
    if i == 1:#aca abria que poner un verificador que el usuario no ponga cosas mal y algo que permita volver para atras
       aux = int(input('desea comprar el vehiculo? ingrese 1 para si'))
    if i == 2:
        aux = int(input('ingrese 1 para comprar la primera opcion, 2 para la opcion 2 '))
    if i == 3:
        aux = int(input('ingrese 1 para la primera opcion, 2 para el segundo o 3 para el tercero '))
    print('')
    color = input('por ultimo elegi el color entre verde, azul, rojo, gris, blanco negro, rojo o amarillo ')#hacer una verificacion que ponga esos colores(usen una lista con un not in)
    auto_elegido = nomAu(columna,fila,aux) # me da el nombre del auto

    print('')
    
    print('usted eligio un ',auto_elegido, 'color ', color, '.')
    compra = input(('Desea comprarlo? SI/NO '))
    
    if compra.lower() == 'si':
        print('usted compro su auto')
        print(mt.matriz_compra(columna,fila,matrizcompra))

    # hay que meter una opcion de que pasa si pongo no y un verificador para que si pongo ni no ni si funque igual



    
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

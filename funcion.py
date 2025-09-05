import matrices as mt


# REVISAR
#Funcion que printea la matriz del auto y marca seleccionado 
def mostrar_autos(datos_de_auto_matriz): # Ej: [['schipani uade Seminuevo', 'Schipani Schiziano'], [1, 2], [28, 35]]

    # Palabras que van a estar en cada submatriz

    info = ['equipamiento', 'precio']
    esquina = 'caracteristicas/nombre'
    nombres = datos_de_auto_matriz[0] 

    #Matriz de nombres declarados previamente
    
    ancho = 30 #ancho que quiero que haya entre cada palabra
    print('')
    print(esquina.ljust(ancho), end ='')#printea esquina con espacio de 30 a su derecha y que lo siguiente lo anote al lado
    for col in nombres:#Selecciona la lista de nombres que va a usar en base a lo ingresado por el usuario
        print(col.ljust(ancho), end='')#printea los nombres igual que la esquina
    print()
    print('')

    # Se imprimen datos de equipamiento y precio
    for infom,fila in zip(info, datos_de_auto_matriz[1:]):# nos permite printear primero el dato de la lista info y a su lado con el siguiente for los datos requeridos por el usuario
        print(infom.ljust(ancho),end='')
        for fil in fila:
            print(str(fil).ljust(ancho),end ='')
        print()
        print('')

# REVISAR
def nomAu(fila, columna, eleccion):
   # Cuando se llama a un vehiculo cuya lista esta vacia da error, hay que corregir eso
    # Esta funcion funciona igual que mostrar matriz solo que sin la parte de mostrarla, te busca los nombres en base a lo eleigod por el usuario y luego agarra el auto en la posicion que eligio el usuario
    
    nombres = mt.modelos_de_autos()



    #Matriz de nombres declarados previamente
   
    elegido = nombres[columna][fila]
    elegidoNom = elegido[eleccion -1]
    return(elegidoNom)

# REVISAR
def compra_auto(fila, columna, matrizcompra):

    # funcion para compra de autos
    matriz = mt.obtener_matriz_especifica(fila, columna)#llamo la matriz de vehiculos que quise comprar

    

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

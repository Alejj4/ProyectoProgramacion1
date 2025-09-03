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

def mostrar_autos(columna,fila):
    
    toyota_hatchback = [[1,2,3],
                        [ 28,31,33]]  #xs xls s
    matriz = toyota_hatchback
    # Nombre de los diferentes tipos de autos
    info = ['equipamento', 'precio']
    esquina = 'caracteristicas/nombre'
    ToHa = ['yaris xs', 'yaris xls', 'yaris s']
    ToSe = []
    ToSu =['cross xli', 'cross sed']
    nombres = [[ToHa,ToSe,ToSu]]
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

    

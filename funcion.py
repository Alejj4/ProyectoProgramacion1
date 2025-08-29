def mostrar_matriz(matriz):
    esquina = 'Marcas/Autos'
    columnas = ['Hatchback','Sedan','Suv','PickUp']
    filas = ['Toyota', 'Honda', 'chevrolet', 'ford']
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
# la idea aca es guardar todas las matrices de marca/modelo
# Esta funcion lo que hace es en base a una fila dada y una columna dada(marca y modelo elegido por el usuario) nos devuelve la sub matriz de vehiculos requerida


def obtener_datos_de_modelos():
    """
    FORMATO DE LAS MATRICES:
    
    nombre_variable = [
        [modelo1, modelo2, modelo3],
        [equipamiento1, equipamiento2, equipamiento3],
        [precio1, precio2, precio3],
    ]
    
    PARA MODELOS SIN STOCK: nombre_variable = [] 
    """
    
    ToHa = [['Yaris xs', 'Yaris xls', 'Yaris s'],
            [1,2,3],
            [28,31,33]]
    ToSe = []
    ToSu = [['Cross xli', 'Cross seG'],
            [1,3],
            [44,52]]
    ToPi = [['Hilux dx4x4','Hiluxsr4x4'],
            [1,3],
            [53,61]]
    ScHa = []
    ScSe = [['schipani uade Seminuevo','Schipani Schiziano'],
            [1,2],
            [28,35]]
    ScSu = [['schipani chipa', 'schipani bochoQuemado'],
            [2,3],
            [25,30]]
    ScPi = [['Schipani Pipani'],
            [3],
            [48]]
    ChHa = []
    ChSe = [['Onixplus'],
            [2],
            [27]]
    ChSu = [['Spring', 'Tracker'],
            [1,2],
            [31,32]]
    ChPi = [['Montana', 'S10', 'Silverado'],
            [1,2,3],
            [34,43,102]]
    FoHa = []
    FoSe = []
    FoSu = [['Territory', 'Kuga Hybrid', 'Everest'],
            [2,3,3],
            [43,76,85]]
    FoPi = [['Maverick', 'Rnager Raptor', 'F-150 Lariat Hybrid'],
            [2,3,3],
            [51,116, 124]]
    
    return [ToHa, ToSe, ToSu, ToPi, ScHa, ScSe, ScSu, ScPi, ChHa, ChSe, ChSu, ChPi, FoHa, FoSe, FoSu, FoPi]
    

def obtener_matriz_completa():
    # Devuelve una matriz con los datos de todos los tipos, marcas y modelos

    ToHa, ToSe, ToSu, ToPi, ScHa, ScSe, ScSu, ScPi, ChHa, ChSe, ChSu, ChPi, FoHa, FoSe, FoSu, FoPi = obtener_datos_de_modelos()
    
    matriz_completa = [
        [ToHa,ToSe,ToSu,ToPi],
        [ScHa,ScSe,ScSu,ScPi],
        [ChHa,ChSe,ChSu,ChPi],
        [FoHa,FoSe,FoSu,FoPi]
    ]
    return matriz_completa

def obtener_matriz_especifica(fila,columna): 
    
    # Devuelve los datos segun la marca (fila) y tipo de auto (columna) que se le especifique
    # Se tiene que pasar el número que ingresa el usuario en consola
    
    matriz_completa = obtener_matriz_completa()

    return matriz_completa[fila - 1][columna - 1]

def matriz_compra(fila, columna, matriz):
    # llama la matriz compravehiculos que la arrastre y suma 1 cuando hay una venta en base a lo ingresado por el usuario

    matriz[fila][columna] += 1
    return(mostrar_matriz(matriz))

def calcular_precios_promedio(matriz):
    
    for fila in range(4): # fila = marca
        for columna in range(4): # columna = tipo
            promedio_autos = obtener_matriz_especifica(fila,columna)
            print(promedio_autos)
            calcular_promedio = lambda lista: sum(lista) // len(lista)
            precios_promedios = calcular_promedio(promedio_autos[2]) if len(promedio_autos) > 0 else 0
            
            """
            # Codigo equivalente a:
            if len(promedio_autos)>1:
                precios_promedios=sum(promedio_autos[1])//len(promedio_autos[1])
                # print(precios_promedios)
            else:
                precios_promedios = 0
            """
            
            matriz[fila][columna]=precios_promedios
    return matriz
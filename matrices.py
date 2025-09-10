def obtener_datos_de_modelos():
    modelos = [
        ['Yaris xs', 'Yaris xls', 'Yaris s'],   # ToHa
        [],                                     # ToSe
        ['Cross xli', 'Cross seG'],             # ToSu
        ['Hilux dx4x4','Hiluxsr4x4'],           # ToPi
        [],                                     # ScHa
        ['schipani uade Seminuevo','Schipani Schiziano'],  # ScSe
        ['schipani chipa', 'schipani bochoQuemado'],       # ScSu
        ['Schipani Pipani'],                    # ScPi
        [],                                     # ChHa
        ['Onixplus'],                           # ChSe
        ['Spring', 'Tracker'],                  # ChSu
        ['Montana', 'S10', 'Silverado'],        # ChPi
        [],                                     # FoHa
        [],                                     # FoSe
        ['Territory', 'Kuga Hybrid', 'Everest'],# FoSu
        ['Maverick', 'Rnager Raptor', 'F-150 Lariat Hybrid'] # FoPi
    ]

    equipamientos = [
        [1,2,3],    # ToHa
        [],         # ToSe
        [1,3],      # ToSu
        [1,3],      # ToPi
        [],         # ScHa
        [1,2],      # ScSe
        [2,3],      # ScSu
        [3],        # ScPi
        [],         # ChHa
        [2],        # ChSe
        [1,2],      # ChSu
        [1,2,3],    # ChPi
        [],         # FoHa
        [],         # FoSe
        [2,3,3],    # FoSu
        [2,3,3]     # FoPi
    ]

    precios = [
        [28,31,33],   # ToHa
        [],           # ToSe
        [44,52],      # ToSu
        [53,61],      # ToPi
        
        [],           # ScHa
        [28,35],      # ScSe
        [25,30],      # ScSu
        [48],         # ScPi
        
        [],           # ChHa
        [27],         # ChSe
        [31,32],      # ChSu
        [34,43,102],  # ChPi
        
        [],           # FoHa
        [],           # FoSe
        [43,76,85],   # FoSu
        [51,116,124]  # FoPi
    ]

    return modelos, equipamientos, precios


def obtener_indices_marcas():
    lista_indices = [
        [0, 1, 2, 3],    # Toyota
        [4, 5, 6, 7],    # Schipani
        [8, 9, 10, 11],  # Chevrolet
        [12, 13, 14, 15] # Ford
    ]
    return lista_indices

def actualizar_matriz_compra(fila, columna, matriz_compra):
    """
    Función encargada de actualizar el número de unidades que una marca
    vendió de determinado tipo
    """
    
    matriz_compra[fila - 1][columna - 1] += 1 # Se suma 1 en la posición del tipo de la marca que se vendió

    return matriz_compra

def calcular_precios_promedio():
    indices_marcas = obtener_indices_marcas()
    _, _, precios = obtener_datos_de_modelos()

    precios_promedios = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]  # Se construye una matriz con ceros para poder añadir los precios promedios

    for fila in range(len(indices_marcas)): # Realiza una vuelta por cada fila (correspondiente a cada marca)
        for columna in range(len(indices_marcas[fila])): #Recorremos los indices de cada tipo de auto
            indice = indices_marcas[fila][columna]
            lista_precios = precios[indice] # Obtenemos la lista de precios que corresponde al indice
            if lista_precios:
                promedio = sum(lista_precios) // len(lista_precios)
            else:
                promedio = 0
            precios_promedios[fila][columna] = promedio

    return precios_promedios


def obtener_matriz_especifica(marca, modelo):
    modelos, equipamientos, precios = obtener_datos_de_modelos()
    indices_marcas = obtener_indices_marcas()
    indice = indices_marcas[marca - 1][modelo - 1]
    return modelos[indice]



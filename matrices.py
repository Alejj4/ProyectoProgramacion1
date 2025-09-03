# la idea aca es guardar todas las matrices de marca/modelo
def llamar_matriz(fila,columna):
    toyota_hatchback = [[1,2,3],
                        [ 28,31,33]]  #yaris-xs, yaris-xls yaris-s
    toyota_sedan = [[0]]
    toyota_suv =[[1,3],  #cross xli, cross seg
                [44,52]]
    toyota_pickup =[[1,3],   #hilux dx4x4, hiluxsr4x4
                    [53,61]]
    honda_hatchback = [[0]]
    honda_sedan = [[3], #honda civic
                [28]] 
    honda_suv=[[2,3],   #hr-v, cr-v
            [25,30]]
    honda_pickup=[[3],   #ridgeline
                [48]]
    chevrolet_hatchback = [[0]]
    chevrolet_sedan = [[2], #onixplus
                    [27]]
    chevrolet_suv = [[1,2],  #sping, tracker
                    [31,32]]
    chevrolet_pickup = [[1,2,3],  #montana, S10, silverado
                        [34,43,102]]
    ford_hatchback = [[0]]
    ford_sedan = [[0]]
    ford_suv =[[2,3,3],   #nueva territory, kuga hibrido, nueva Everest
            [43,76,85]]
    ford_pickup =[[2,3,3],      #nueva maverick, ranger raptor, f150 lariat hibrido
                [51,116, 124]]

    Matriz_principal =[[toyota_hatchback,toyota_sedan,toyota_suv,toyota_pickup],
                    [honda_hatchback, honda_sedan, honda_suv, honda_pickup],
                    [chevrolet_hatchback, chevrolet_sedan, chevrolet_suv, chevrolet_pickup],
                    [ford_hatchback, ford_sedan, ford_suv, ford_pickup]]
    return Matriz_principal[fila][columna]
# la idea aca es guardar todas las matrices de marca/modelo
# Esta funcion lo que hace es en base a una fila dada y una columna dada(marca y modelo elegido por el usuario) nos devuelve la sub matriz de vehiculos requerida
import funcion as fn
# en este archivo las filas y columnas estan bien
def llamar_matriz(fila,columna):
    toyota_hatchback = [[1,2,3],
                        [ 28,31,33]]  #yaris-xs, yaris-xls yaris-s
    toyota_sedan = [[0]]
    toyota_suv =[[1,3],  #cross xli, cross seg
                [44,52]]
    toyota_pickup =[[1,3],   #hilux dx4x4, hiluxsr4x4
                    [53,61]]
    schipani_hatchback = [[0]]
    schipani_sedan = [[1,2], #schipani uade Seminuevo, Schipani Schiziano
                [28,35]] 
    schipani_suv=[[2,3],   #schipani chipa, schipani bochoQuemado
            [25,30]]
    schipani_pickup=[[3],   #Schipani Pipani
                [48]]
    chevrolet_hatchback = [[0]]
    chevrolet_sedan = [[2], #onixplus
                    [27]]
    chevrolet_suv = [[1,2],  #spring, tracker
                    [31,32]]
    chevrolet_pickup = [[1,2,3],  #montana, S10, silverado
                        [34,43,102]]
    ford_hatchback = [[0]]
    ford_sedan = [[0]]
    ford_suv =[[2,3,3],   # territory, kuga hibrido,  Everest
            [43,76,85]]
    ford_pickup =[[2,3,3],      # maverick, ranger raptor, f150 lariat hibrido
                [51,116, 124]]
        #Gran matriz con todas las submatrices
    Matriz_principal =[[toyota_hatchback,toyota_sedan,toyota_suv,toyota_pickup],
                    [schipani_hatchback, schipani_sedan, schipani_suv, schipani_pickup],
                    [chevrolet_hatchback, chevrolet_sedan, chevrolet_suv, chevrolet_pickup],
                    [ford_hatchback, ford_sedan, ford_suv, ford_pickup]]
    return Matriz_principal[fila][columna]

def matriz_compra(fila, columna,matriz):
    # llama la matriz compravehiculos que la arrastre y suma 1 cuando hay una venta en base a lo ingresado por el usuario
    matriz[fila][columna] += 1
    return(fn.mostrar_matriz(matriz))
    
#def carga_ventas():
    
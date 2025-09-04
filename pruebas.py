# Archivo de pruebas para experimentar fuera de los archivos principales
# Borrar cuando el proyecto este terminado
import matrices as mt

matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,4,5],
    [3,5,6,8]
    ]


def precios(matriz):
       for columna in range(4):
              for fila in range(4):
                     promedio_autos = mt.llamar_matriz(columna ,fila)
                     if len(promedio_autos)>1:
                            preciospromedios=sum(promedio_autos[1])//len(promedio_autos[1])
                     else:
                            preciospromedios = 0
                     matriz[columna][fila]=preciospromedios
       return matriz

print(precios(matriz))
# Schipani Motors Sport 🚗

## Algunas aclaraciones importantes
1 - Tener cuidado al querer acceder a los datos de una matriz, corroborar si hay que pasarle la posicion tal cual o los indices (que arrancan desde el 0,0)

2 - En las matrices se accede primero a la marca (fila) y despues a al tipo de auto (columna)

3 - Los modelos de autos que estén cargados en las matrices siempre tienen que tener misma cantidad de columnas en sus filas (Nombre, equipamiento, precio)

## Convenciones para el codigo
1 - Usar triples comillas (""" """) para comentarios sobre el funcionamiento general de un modulo o funcion (para las funciones agreguenlas abajo de la linea del def, antes de escribir toda la logica)

2 - Usar el # para comentarios de lineas puntuales para especificar cosas como qué hace, qué datos recibe determinada funcion, mostrar un ejemplo de lo que deberia retornar algo, etc

3 - Al crear una funcion o variable, siempre darle un nombre lo mas especifico posible

4 - Intentar que una funcion no haga muchas cosas al mismo tiempo, si es necesario y hay logica que pueda tener que usarse mas adelante, separenla en otra funcion aparte

5 - Para evitar posibles conflictos de importes en la ejecucion hagamos así, main.py solo importa funcion.py y funcion.py solo importa matrices.py. Que no haya ningun otro importe en un orden o direccion diferente

### Tareas pendientes (Agregar en caso de que haga falta)
1 - Agregar la sentencia lambda al codigo

2 - Agregar slicing

3 - Mejorar la visualizacion del menu en la consola (Agregando separadores, espacios y demás)

4 - Hay que pasar los numeros de las matrices de los datos de autos a texto ¿?

5 - Hacer que el menú de los autos (que aparece al inicio) salga cada vez que el usuario tiene que volver a ingresar datos de autos desde el principio

6 - Al finalizar el programa, ver como mostrar la informacion de los autos que se vendieron ¿?

7 - Agregar un mensaje para el caso donde el usuario cancele una compra, como "Cancelando..." o algo así

8 - Manejar los casos donde el usuario ingrese otra cosa que no sea un numero cuando el programa espera especificamente ese tipo de dato

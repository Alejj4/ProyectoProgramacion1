import datetime
import os

def imprimir_separador():
    print("-"*78)


def obtener_datos_de_usuario_autenticado():
    usuario_data = None

    try:
        with open("archivos/usuario_autenticado.csv", "r", encoding="UTF-8") as archivo:
            for i, linea in enumerate(archivo):
                if i != 0:
                    dni, nombre, contraseña, es_admin = linea.split(",")

                    usuario_data = {
                        "dni":str(dni).strip(), 
                        "nombre":str(nombre).strip(), 
                        "contraseña":str(contraseña).strip(), 
                        "es_admin":str(es_admin).strip()
                    }
                    
    except FileNotFoundError:
        print("No se encontró el archivo con los datos del usuario logueado")

    return usuario_data


def mostrar_opciones_disponibles(datos):
    for i, dato in enumerate(datos):
        print(f"{i + 1} - {dato.capitalize()}")
        

def verificar_numero_valido(mensaje_input, rango=None, mensaje_error="Opcion no disponible, por favor intente de nuevo", opciones_disponibles=None, retornar_indice=False):
    """Funcion que maneja la excepcion ValueError cuando en un input se espera un numero y no otra cosa"""
    
    while True:
        try:
            dato = int(input(mensaje_input))

            if dato != -1 and (rango is not None and not (dato - 1) in rango):
                raise IndexError(mensaje_error)


            break
        except ValueError:
            imprimir_separador()
            print("El dato ingresado es inválido, el mismo debe ser un número")
            imprimir_separador()

            if opciones_disponibles:
                mostrar_opciones_disponibles(opciones_disponibles)
        except IndexError as e:
            imprimir_separador()
            print(e)

            if opciones_disponibles:
                mostrar_opciones_disponibles(opciones_disponibles)

    if dato != -1 and retornar_indice:
        dato -= 1

    return dato


def manejar_apertura_archivo(nombre_archivo, modo_apertura, directorio="archivos"):
    try:
        archivo = open(f"{directorio}/{nombre_archivo}", modo_apertura, encoding="UTF-8") 
    except FileNotFoundError:
        archivo = None
    
    return archivo


def crear_registro(accion,valor):
    usuario = obtener_datos_de_usuario_autenticado()
    
    registro = manejar_apertura_archivo("log.txt","a")
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro_entrada = f"Fecha: [{fecha_actual}] | Usuario: {usuario["nombre"] if usuario is not None else "Usuario anonimo"} | {accion}: {valor} \n"
    registro.write(f"{registro_entrada} \n")
    registro.close()
    return usuario,accion,valor


def mostrar_matriz(matriz):
    esquina = 'Marcas/Tipo'
    columnas = ['Hatchback', 'Sedan', 'Suv', 'PickUp']
    filas = ['Toyota', 'Schipani', 'Chevrolet', 'Ford']
    ancho = 15

    # encabezado
    print(esquina.ljust(ancho), end='')
    for col in columnas:
        print(col.ljust(ancho), end='')
    print()

    # filas
    for i in range(len(filas)):
        print(filas[i].ljust(ancho), end='')
        for fil in matriz[i]:
            print(str(fil).ljust(ancho), end='')
        print()


def desplegar_menu_informes():
    informes_disponibles = ["Los 3 autos más caros y baratos.", "Los autos más y menos vendidos.", "DNI de los clientes."]

    print("A continuación se presentan los distintos informes que puede consultar:")
    for i, informe in enumerate(informes_disponibles):
        print(f"{i + 1} - {informe}")


def generar_directorio(nombre_directorio):
    
    # Obteniendo la ruta actual del archivo
    ruta_actual = os.getcwd()

    # Obteniendo la ruta completa donde deberia estar el archivo
    ruta_completa = os.path.join(ruta_actual, nombre_directorio)
    
    # Verificar que si el archivo ya existe
    directorio_existente = os.path.exists(ruta_completa)

    if not directorio_existente:
        os.makedirs(ruta_completa, exist_ok=True)
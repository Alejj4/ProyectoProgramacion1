import random

from faker import Faker

from modulos.utils import imprimir_separador, manejar_apertura_archivo, mostrar_opciones_disponibles, crear_registro, verificar_numero_valido


def rango_documento():
    return 1000000, 100000000

def register():
    
    while True:
        dni,dni_existentes=dni_existe()
        if str(dni) in dni_existentes:
            print("Este DNI ya esta registrado. Intente iniciar sesión o use otro DNI.")
        else:
            break
    imprimir_separador()
    usuario_nombre = input("Ingrese su nombre: ")
    imprimir_separador()
    password = input("Ingrese su contraseña: ")
    imprimir_separador()
    archivo = manejar_apertura_archivo("usuarios.csv", "at")
    archivo.write(f"{dni}, {usuario_nombre}, {password}, {0}\n")
    print("Su registro ha sido exitoso, disfrute de su compra")
    imprimir_separador()
    archivo.close()

    usuario_data = {
        'dni':str(dni).strip(), 
        'nombre':str(usuario_nombre).strip(), 
        'contraseña':str(password).strip(), 
        'es_admin':str(0)
    }

    return usuario_data

def login():
    usuario_data = None
    encontrado=False
    archivo_usuarios = None
    
    while True:
        dni_ingreso,_ = dni_existe()
        imprimir_separador()
        if int(dni_ingreso) != -1:
            contraseña=input("Ingrese su contraseña: ").strip()
            imprimir_separador()
            archivo_usuarios=manejar_apertura_archivo("usuarios.csv", "r")
            
            for i, linea in enumerate(archivo_usuarios):
                if i == 0:
                    continue

                partes = linea.strip().split(",")
                dni, nombre, contraseña_actual, es_admin = [p.strip() for p in partes]
                if dni == str(dni_ingreso) and contraseña_actual == contraseña:
                    encontrado=True
                    usuario_data = {
                        'dni':str(dni).strip(), 
                        'nombre':str(nombre).strip(), 
                        'contraseña':str(contraseña).strip(), 
                        'es_admin': str(es_admin)
                    }

                    with open("archivos/usuario_autenticado.csv", "a", encoding="UTF-8") as archivo_login:
                        archivo_login.write(f"{usuario_data['dni']}, {usuario_data['nombre']}, {usuario_data['contraseña']}, {usuario_data['es_admin']}")


            if not encontrado:  
                print("DNI o contraseña incorrectos. Intente nuevamente.")
                imprimir_separador()
                continue 
            break

        if archivo_usuarios:
            archivo_usuarios.close()
    return usuario_data

def dni_existe():
    dni_existentes = []
    try:
        archivo=manejar_apertura_archivo("usuarios.csv", "r")
        for i,linea in enumerate(archivo):
            if i != 0:
                partes = linea.strip().split(",")
                dni_existentes.append(partes[0].strip())      
        archivo.close()
    except FileNotFoundError:
        print("No se encontró el archivo usuarios.csv.")
    while True:
        dni_min, dni_max = rango_documento()
        dni = verificar_numero_valido("Ingrese su DNI o -1 para volver: ", rango=range(dni_min, dni_max + 1), mensaje_error="Documento invalido")
        break
    return str(dni),dni_existentes


def cambiar_contrasena(): 
    usuarios_lista = [] 
    usuario_actualizado = None
    dni_min, dni_max = rango_documento()
    dni_buscado = verificar_numero_valido('Ingrese su dni para actualizar su contraseña o -1 para salir: ', rango=range(dni_min, dni_max + 1), mensaje_error="El documento ingresado es invalido")
    
    if dni_buscado != -1:
        archivo_usuarios = manejar_apertura_archivo('usuarios.csv','r') 
        for i, linea in enumerate(archivo_usuarios): 
            if i != 0: 
                datauser = linea.split(',') 
                usuarios_lista.append({
                    'dni':datauser[0].strip(), 
                    'nombre':datauser[1].strip(), 
                    'contraseña':datauser[2].strip(), 
                    'es_admin':datauser[3].strip()
                })    
        archivo_usuarios.close()


        for usuario in usuarios_lista:
            if usuario['dni'] == str(dni_buscado):
                while True:
                    try:
                        nueva_contra = input('Ingrese su nueva contraseña: ').strip()
                        confirmacion = input('Ingrese de nuevo su contraseña: ').strip()

                        if "" in [nueva_contra, confirmacion]:
                            raise ValueError("Los campos de contraseña no pueden ser vacíos")

                        if nueva_contra != confirmacion:
                            raise ValueError('Las contraseñas no coinciden, intente nuevamente')

                        usuario['contraseña'] = nueva_contra
                        usuario_actualizado = usuario
                        break

                    except ValueError as e:
                        print(e)
                    
    if usuario_actualizado is not None:

        archivo_usuarios = manejar_apertura_archivo("usuarios.csv", "wt")
        archivo_usuarios.write('dni, nombre, contraseña, es_admin\n')
        
        for usuario in usuarios_lista:
            archivo_usuarios.write(f"{usuario['dni']}, {usuario['nombre']}, {usuario['contraseña']}, {usuario['es_admin']}\n")
        
        print('Su contraseña fue cambiada con éxito')
        archivo_usuarios.close()

    imprimir_separador()
    return usuario_actualizado


def completar_usuarios():
    archivo = manejar_apertura_archivo("usuarios.csv", "wt", "archivos")

    fake = Faker('es_AR')

    archivo.write("dni, nombre, contraseña, es_admin\n")
    
    for i in range(10):
        
        if i == 2:
            dni = 45684868
            nombre = "Lautaro Gomez"
            password = "a"
            es_admin = 0
        else:
            dni = random.randint(10000000, 99999999)

            nombre = fake.name() if (i != 0 and i != 1) else ("Tiziano Schipani" if i == 0 else "Alfonso Schipani")
            password = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)
            es_admin = 1 if i <= 1 else 0

        archivo.write(f"{dni}, {nombre}, {password},{es_admin}\n")

    archivo.close()


def actualizar_clientes(dni_usuario: str):
    archivo = manejar_apertura_archivo("clientes.csv", "r")
    clientes_dic = {}

    if archivo is not None:
        for i, linea in enumerate(archivo):
            if i == 0:  
                continue
            partes = linea.strip().split(",")
            if len(partes) == 2 and partes[0] != "":
                dni_leido = partes[0].strip()
                compras = int(partes[1].strip())
                clientes_dic[dni_leido] = compras
        archivo.close()

    if dni_usuario in clientes_dic:
        clientes_dic[dni_usuario] = clientes_dic[dni_usuario] + 1
    else:
        clientes_dic[dni_usuario] = 1

    clientes = manejar_apertura_archivo("clientes.csv", "w")
    clientes.write("dni,compras\n")
    for clave in clientes_dic:
        valor = clientes_dic[clave]
        clientes.write(f"{clave},{valor}\n")
    clientes.close()



def menu_inicio():
    with open("archivos/usuario_autenticado.csv", "wt", encoding="UTF-8") as archivo_login:
        archivo_login.write("dni, nombre, contraseña, es_admin\n")
    
    while True:
        print('Bienvenido a Schipani Motors Sport, elija una opcion.')

        opciones_disponibles = ["Registrarse","Loguearse",'Cambiar contraseña','salir']
        mostrar_opciones_disponibles(opciones_disponibles)

        opcion = verificar_numero_valido("Ingrese una opción: ", rango=range(1, len(opciones_disponibles) + 1),opciones_disponibles=opciones_disponibles)

        imprimir_separador()

        if opcion == 1:
            usuario = register()
            crear_registro("Registro", "OK")
        elif opcion == 2:
            usuario = login()
            crear_registro("Login","OK")
            break       
        elif opcion == 3:
            usuario = cambiar_contrasena()
            crear_registro("Cambio contraseña", "OK" if usuario is not None else "WARNING")
        elif opcion == 4:
            usuario = None
            break
        else:
            print("Opcion no disponible, por favor intente de nuevo")
            imprimir_separador()

    return usuario
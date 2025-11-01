import random

from faker import Faker

from modulos.utils import imprimir_separador, manejar_apertura_archivo, mostrar_opciones_disponibles, crear_registro, verificar_numero_valido


def rango_documento():
    return range(1000000,99999999)

def register():
    
    while True:
        dni,dni_existentes=dni_existe()
        if str(dni) in dni_existentes:
            print("Este DNI ya esta registrado. Intente iniciar sesión o use otro DNI.")
        else:
            break
    imprimir_separador()
    nombre_de_usuario = input("Ingrese su nombre de usuario: ")
    imprimir_separador()
    password = input("Ingrese su contraseña: ")
    imprimir_separador()
    archivo = manejar_apertura_archivo("usuarios.csv", "at")
    archivo.write(f"{dni}, {nombre_de_usuario}, {password}, {0}\n")
    print("Su registro ha sido exitoso, disfrute de su compra")
    imprimir_separador()
    archivo.close()

    usuario_data = {
        'dni':str(dni).strip(), 
        'nombre':nombre_de_usuario.strip(), 
        'contraseña':password.strip(), 
        'es_admin':0
    }

    return usuario_data

def login():
    usuario_data = None
    
    while True:
        dni_ingreso,_ = dni_existe()
        imprimir_separador()
        if int(dni_ingreso)==-1:
            menu_inicio()
            break
            
        
        contraseña=input("Ingrese su contraseña: ").strip()
        imprimir_separador()
        archivo=manejar_apertura_archivo("usuarios.csv", "r")
        encontrado=False
        
        for i, linea in enumerate(archivo):
                if i == 0:
                    continue

                partes = linea.strip().split(",")

                dni, nombre, contraseña_actual, es_admin = [p.strip() for p in partes]

                if dni == str(dni_ingreso) and contraseña_actual == contraseña:
                    encontrado=True
                    usuario_data = {
                        'dni':dni.strip(), 
                        'nombre':nombre.strip(), 
                        'contraseña':contraseña.strip(), 
                        'es_admin': es_admin
                    }

                    break
                else:
                    encontrado = False
                    usuario_data = None    


        if not encontrado:  
            print("DNI o contraseña incorrectos. Intente nuevamente.")
            imprimir_separador()
            continue 
        break

    

    archivo.close()
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
        dni = verificar_numero_valido("Ingrese su DNI o -1 para volver para atras: ", rango=rango_documento(), mensaje_error="Documento invalido")
        break
    return dni,dni_existentes


def cambiar_contrasena(): 
    usuarios_lista = [] 
    dni_buscado = verificar_numero_valido('Ingrese su dni: ', rango=rango_documento(), mensaje_error="Documento invalido")
    
    archivo = manejar_apertura_archivo('usuarios.csv','r') 
    for i, linea in enumerate(archivo): 
        if i != 0: 
            datauser = linea.split(',') 
            usuarios_lista.append({
                'dni':datauser[0].strip(), 
                'nombre':datauser[1].strip(), 
                'contraseña':datauser[2].strip(), 
                'es_admin':datauser[3].strip()
            })    
    archivo.close()

    usuario_actualizado = None

    for usuario in usuarios_lista:
        if usuario['dni'] == dni_buscado:
            while True:
                try:
                    contraseña = input('Ingrese su nueva contraseña: ').strip()
                    confirmacion_contraseña = input('Ingrese de nuevo su contraseña: ').strip()


                    if "" in [contraseña, confirmacion_contraseña]:
                        raise ValueError("Los campos de contraseña no pueden ser vacias")

                    if contraseña != confirmacion_contraseña:
                        raise ValueError('Las contraseñas no coinciden, intente nuevamente')
                    
                    
                    usuario['contraseña'] = contraseña
                    usuario_actualizado = usuario
                    print('Su contraseña fue cambiada con éxito')
                    
                    break
                except ValueError as e:
                    print(e)
                    
    if usuario_actualizado is not None:

        archivo_usuarios = manejar_apertura_archivo("usuarios.csv", "wt", "informes")
        archivo_usuarios.write('dni, nombre, contraseña, es_admin\n')
        
        for usuario in usuarios_lista:
            archivo_usuarios.write(f'{usuario['dni']}, {usuario['nombre']}, {usuario['contraseña']}, {usuario['es_admin']}\n')
        
        archivo_usuarios.close()

        usuario = usuario_actualizado
    else:
        usuario = None

    return usuario


def completar_clientes():
    archivo = manejar_apertura_archivo("usuarios.csv", "wt", "archivos")

    fake = Faker('es_AR')

    archivo.write("dni, nombre, contraseña, es_admin\n")
    
    for i in range(10):
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
    while True:
        print('Bienvenido a Schipani Motors Sport, elija una opcion.')
        opciones_disponibles = ["Registrarse","Loguearse",'Cambiar contraseña','salir']
        mostrar_opciones_disponibles(opciones_disponibles)
        opcion = verificar_numero_valido("Ingrese una opción: ", rango=range(len(opciones_disponibles)))
        imprimir_separador()
        if opcion == 1:
            usuario = register()
            crear_registro(usuario,"Registro", "OK")
            break
        elif opcion == 2:
            usuario = login()
            crear_registro(usuario,"Login","OK")
            break       
        elif opcion == 3:
            usuario = cambiar_contrasena()
            crear_registro(usuario, "Cambio contraseña", "OK" if usuario is not None else "WARNING")
            break
        elif opcion == 4:
            usuario = None
            break

    return usuario
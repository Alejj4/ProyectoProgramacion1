import random

from faker import Faker

from modulos.utils import imprimir_separador, manejar_apertura_archivo, mostrar_opciones_disponibles, crear_registro, verificar_numero_valido




def register():
    
    while True:
        dni,dni_existentes=dni_existe()
        if str(dni) in dni_existentes:
            print("Este DNI ya esta registrado. Intente iniciar sesión o use otro DNI.")
        else:
            break
    imprimir_separador()
    usuario = input("Ingrese su nombre de usuario: ")
    imprimir_separador()
    password = input("Ingrese su contraseña: ")
    imprimir_separador()
    archivo = manejar_apertura_archivo("usuarios.csv", "at")
    archivo.write(f"{dni}, {usuario}, {password}, {0}\n")
    print("Su registro ha sido exitoso, disfrute de su compra")
    imprimir_separador()
    archivo.close()
    return usuario,dni

def login():
    usuario = None
    dni_user = None
    while True:
        dni_ingreso,dni_existentes=dni_existe()
        imprimir_separador()
        if int(dni_ingreso)==-1:
             menu_inicio()
             break
            
        
        contra=input("Ingrese su contraseña: ").strip()
        imprimir_separador()
        archivo=manejar_apertura_archivo("usuarios.csv", "r")
        encontrado=False
        
        for i, linea in enumerate(archivo):
                if i == 0:
                    continue

                partes = linea.strip().split(",")

                dni, nombre, contraseña, es_admin = [p.strip() for p in partes]

                if dni == str(dni_ingreso) and contraseña == contra:
                    usuario = nombre
                    dni_user = dni
                    encontrado=True
                    if es_admin == "1":
                        print(f"🔥😎 PANEL DE ADMINISTRADOR ({nombre}) 😎🔥")
                        imprimir_separador()
                    else:
                        print(f"Bienvenido/a nuevamente, {nombre}")
                        imprimir_separador()
                    break
                    
        archivo.close()
        if not encontrado:  
            print("DNI o contraseña incorrectos. Intente nuevamente.")
            imprimir_separador()
            continue 
        break
    return usuario, dni_user

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
        dni = verificar_numero_valido("Ingrese su DNI o -1 para volver para atras: ", rango = range(1000000,99999999))
        break
    return dni,dni_existentes


def cambiar_contrasena(): 
    usuarios = [] 
    dniabuscar = int(input('ingrese su dni ')) 
    contra_vieja = input('Ingrese su contrasena vieja ') 
    archivo = manejar_apertura_archivo('usuarios.csv','r') 
    for i, linea in enumerate(archivo): 
        if i != 0: 
            datauser = linea.split(',') 
            usuarios.append({ 'dni':datauser[0].strip(), 
                            'nombre':datauser[1].strip(), 
                            'contraseña':datauser[2].strip(), 
                            'es_admin':datauser[3].strip() })    
    archivo.close()

    usuario_actualizado = None

    for usuario in usuarios:
        if usuario['dni'] == dniabuscar:
            while True:
                try:
                    contraseña = input('Ingrese su nueva contraseña: ').strip()
                    confirmacion_contraseña = input('Ingrese de nuevo su contraseña: ').strip()

                    if contraseña != confirmacion_contraseña:
                        raise ValueError
                    
                    
                    usuario['contraseña'] = contraseña
                    usuario_actualizado = usuario
                    print('Su contraseña fue cambiada con éxito')
                    
                    break
                except ValueError:
                    print('Las contraseñas no coinciden, intente nuevamente')
                    
    if usuario_actualizado is not None:

        archivo_usuarios = manejar_apertura_archivo("usuarios.csv", "wt", "informes")
        archivo_usuarios.write('dni, nombre, contraseña, es_admin\n')
        
        for usuario in usuarios:
            archivo_usuarios.write(f'{usuario['dni']}, {usuario['nombre']}, {usuario['contraseña']}, {usuario['es_admin']}\n')
        
        archivo_usuarios.close()

        usuario, dni = usuario_actualizado['nombre'], usuario_actualizado['dni']
    else:
        usuario, dni = None, None

    return usuario, dni


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
        opciones_disponibles = ["Registrarse","Logearse",'Cambiar contraseña','salir']
        print('Bienvenido a Schipani Motors Sport, elija una opcion.')
        mostrar_opciones_disponibles(opciones_disponibles)
        opcion = verificar_numero_valido("Ingrese una opción: ", rango=range(len(opciones_disponibles)))
        imprimir_separador()
        if opcion == 1:
            usuario,dni = register()
            crear_registro(usuario,"Registro", "OK")
            break
        elif opcion == 2:
            usuario,dni = login()
            crear_registro(usuario,"Login","OK")
            break       
        elif opcion == 3:
            usuario, dni = cambiar_contrasena()
            crear_registro(usuario, "Cambio contraseña", "OK" if usuario is not None else "WARNING")
            break
        elif opcion == 4:
            usuario,dni = None, None
            break

    return usuario,dni
  
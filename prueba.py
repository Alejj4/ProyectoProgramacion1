import funcion as fn
import os
def cambiar_contrasena():
    dni = int(input('ingrese su dni '))
    contra_vieja = input('Ingrese su contrasena vieja ')
    archivo = fn.manejar_apertura_archivo('usuarios.csv','r')
    dnilista = []
    contrasenaLista = []
    mod = []
    linea = archivo.readline()
    while linea:
        linea = archivo.readline().strip()
        dni3 = linea.split(', ')
        if len(dni3)>=3:
            
            dnilista.append(int(dni3[0]))
            
            contrasenaLista.append(dni3[2])
            mod.append(dni3)
    print(mod)

    while True: 
        if dni not in dnilista:
            try:
                opcion = int(input('su dni no se encuentra ingresado, ingrese 1 para login, 2 para volver a escribir su DNI '))
                if opcion == 2:
                    dni = int(input('ingrese su dni '))
                    contra_vieja = input('Ingrese su contrasena vieja ')
                    continue
                elif opcion == 1:
                    None
                else:
                    raise ValueError()
            except  ValueError:
                print('ingrese un numero valido')
        
        indice = dnilista.index(int(dni))
        if contra_vieja != contrasenaLista[indice]:
            print('su contrasena no coincide')

        else:
            break
    try:
        contraNueva = input('ingrese su nueva contrasena ')
        contraCheq = input('ingrese de nuevo su contrasena ')
        if contraNueva == contraCheq:
            #preguntarle a lauti
          
            mod[indice][2] = contraNueva
            for i in (mod):
                for j in mod[i]:
                    aux = aux + str(mod[j])
                print(aux)
            
        else:
            raise ValueError()
    except ValueError:
        print('su contrasena no coincide')
        
encargo_data = {
        "modelos_seleccionados":[],
        "monto_total": 0
    }



cambiar_contrasena()
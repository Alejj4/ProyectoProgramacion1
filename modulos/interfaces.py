from modulos.compras import aplicar_descuento_precio_final, encargar_autos
from modulos.admin import cargar_auto
from modulos.utils import imprimir_separador, manejar_apertura_archivo, obtener_datos_de_usuario_autenticado, mostrar_opciones_disponibles, verificar_numero_valido


def modificar_precios():
    pass

def obtener_informes():
    pass



def interfaz_admin():
    usuario_data = None

    try:
        usuario_data = obtener_datos_de_usuario_autenticado()

        if usuario_data is None:
            raise ValueError("No se encontró el archivo con los datos del usuario logueado")

        while True:
            print(f"PANEL DE ADMINISTRADOR ({usuario_data.get('nombre')})")
            imprimir_separador()
            print("Opciones de panel de admin")
            opciones_disponibles = ["Cargar nuevo vehiculo", "Modificar precios", "Obtener informes", "Salir"]
            
            mostrar_opciones_disponibles(opciones_disponibles)
            opcion_seleccionada = verificar_numero_valido("Ingrese la opcion que desea: ", rango=range(1, len(opciones_disponibles) + 1), opciones_disponibles=opciones_disponibles)

            if opcion_seleccionada == 1:
                cargar_auto()
            elif opcion_seleccionada == 2:
                modificar_precios()
            elif opcion_seleccionada == 3:
                obtener_informes()
            elif opcion_seleccionada == -1:
                imprimir_separador()
                print("Opcion no disponible, por favor intente de nuevo")
                imprimir_separador()
            else:
                break    
    
    except KeyError:
        print("Se produjo un error en los datos del usuario.")
    except ValueError as e:
        print(e)

def interfaz_usuario():

    encargo_data = encargar_autos() # La totalidad de autos que el usuario seleccionó y va a comprar
    
    print("Finalizando operacion")
    
    imprimir_separador()
    
    if len(encargo_data["modelos_seleccionados"]) > 0:
        aplicar_descuento = aplicar_descuento_precio_final()
        
        if aplicar_descuento:
            monto_final = round(encargo_data["monto_total"]*0.80, 2)
            encargo_data["monto_total"] = monto_final

            print(f"El precio final con el descuento del 20% aplicado es de: {monto_final} mil dolares.")
        
        ventas_archivo = manejar_apertura_archivo("ventas.csv", "a", "archivos")
        for modelo in encargo_data["modelos_seleccionados"]:
            ventas_archivo.write(f"{modelo['nombre']},{modelo['equipamiento']},{modelo['precio']},{modelo['color']} \n")
        ventas_archivo.close()
        
    else:
        print("No se realizó ningún pedido")
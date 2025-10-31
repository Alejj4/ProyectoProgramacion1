import random as rn

from modulos.utils import imprimir_separador, verificar_numero_valido, mostrar_opciones_disponibles, crear_registro
from modulos.autos import desplegar_menu_de_catalogo, pedir_datos_compra, obtener_modelos_disponibles, mostrar_modelos_disponibles, pedir_dato_de_autos
from modulos.usuarios import actualizar_clientes



def mostrar_resumen(encargo_data):
    imprimir_separador()
    
    print("Resumen de su compra: ")

    for i, auto in enumerate(encargo_data["modelos_seleccionados"]):
        nombre, precio, color = auto["nombre"], auto["precio"], auto["color"]
        print(f"{i + 1}) nombre: {nombre} - color: {color} - precio: ${precio}")

    print(f"Monto acumulado: ${encargo_data['monto_total']}")

    imprimir_separador()

def encargar_autos(usuario,dni):
    """Funcion que maneja todo lo referido al encargo de los autos que un usuario va a comprar"""
    finalizar_compra = False

    encargo_data = {
        "modelos_seleccionados":[],
        "monto_total": 0
    }
    
    while not finalizar_compra:
        print("Catalogo disponible: ")
        desplegar_menu_de_catalogo() # Despliegue del catalogo

        imprimir_separador()


        #---------------------- Selección de marca y tipo --------------------------------------------

        nombre_marca, nombre_tipo = pedir_datos_compra(usuario) # Funcion para pedir datos para realizar una compra

        if nombre_marca == -1:
            finalizar_compra = True
            continue
        elif nombre_tipo == -1:
            continue

        #---------------------- Obtención de modelos disponibles --------------------------------------------

        modelos_disponibles = obtener_modelos_disponibles(nombre_marca, nombre_tipo)

        if len(modelos_disponibles) > 0:
            mostrar_modelos_disponibles(nombre_marca, nombre_tipo, modelos_disponibles)

        else:    
            print(f"No hay modelos en stock para {nombre_marca} - {nombre_tipo}.")
            imprimir_separador()

            continue

        #---------------------- Selección de modelo --------------------------------------------

        modelo_seleccionado_indice = pedir_dato_de_autos("Seleccione el modelo que mas le interese. Si desea volver al menú de inicio, ingrese -1: " , opciones_disponibles=[modelo["nombre"] for modelo in modelos_disponibles])
        imprimir_separador()
        # Vuelve al menú del inicio
        if modelo_seleccionado_indice == -1:
            continue

        # ------------------------- Selección de color --------------------------------------------

        colores_disponibles = ["Verde", "Azul", "Rojo", "Gris", "Blanco", "Negro", "Marron", "Amarillo"]
        mostrar_opciones_disponibles(colores_disponibles)
        color_indice = verificar_numero_valido("Seleccione alguno de los colores con los que contamos: ", rango=range(len(colores_disponibles))) - 1
        imprimir_separador()
        color_seleccionado = colores_disponibles[color_indice]
        
        #---------------------- Confirmación de compra --------------------------------------------
        
        modelo_seleccionado = modelos_disponibles[modelo_seleccionado_indice]
        crear_registro(usuario,"Modelo_seleccionado", modelo_seleccionado["nombre"])
        modelo_seleccionado["color"] = color_seleccionado
        crear_registro(usuario,"Color_seleccionado", color_seleccionado)
        encargo_data["modelos_seleccionados"].append(modelo_seleccionado)
        encargo_data["monto_total"] += modelo_seleccionado["precio"]
        print(f"Se agregó exitosamente el siguiente modelo al resumen: {modelo_seleccionado['nombre']} - {nombre_marca} - {nombre_tipo}")

        mostrar_opciones_disponibles(["Ver resumen", "Finalizar operación"])
        decision = verificar_numero_valido("Ingrese la opción deseada: ", rango=range(2))

        if decision == 1:
            mostrar_resumen(encargo_data)
            crear_registro(usuario, "Ver resumen", "Sí")
            print("¿Desea pasar a finalizar la operación? ")
            mostrar_opciones_disponibles(["Sí", "No (Encargar un nuevo vehículo)"])
            
            respuesta = verificar_numero_valido("Ingrese la opcion deseada: ", rango=range(2))

            finalizar_compra = respuesta == 1
            crear_registro(usuario, "Finalizar compra", "Sí" if finalizar_compra else "No")
            if finalizar_compra and len(encargo_data["modelos_seleccionados"]) > 0:
                    actualizar_clientes(dni)
        else:
            crear_registro(usuario, "Ver resumen", "No")
            finalizar_compra = True
            crear_registro(usuario, "Finalizar compra", "Sí")
            if len(encargo_data["modelos_seleccionados"]) > 0:
                actualizar_clientes(dni)
    return encargo_data

def aplicar_descuento_precio_final(usuario):
       """Función que se basa en un juego donde si el usuario gana, obtiene un descuento sobre el monto final de la compra"""

       aplicar_descuento = False

       print("¿Desea participar de un juego para conseguir un descuento del 20% para la compra de su auto?")
       des = verificar_numero_valido("Ingrese 1 si quiere y 2 si no quiere: ", rango=range(2))

       if des == 2: 
              print("Como usted desee.")
              crear_registro(usuario,"Descuento", "No")
       else: 
              print("Nos alegra que haya querido participar. El juego trata de que tiene que elegir un numero del 1 al 5, si su numero es igual al que eligió el programa usted se gana el descuento asi de facil.")
              ran = rn.randint(1,5)
              crear_registro(usuario,"descuento", "Sí")
              numran = verificar_numero_valido("Ingrese un numero del 1 al 5: ", rango=range(5))
              
              if numran != ran:
                    print("Lo lamentamos, pero su numero no coincide, el numero correcto era:", ran)
              else:
                    print("¡Felicitaciones! Su numero coincide, usted se gano un descuento del 20%.")
                    aplicar_descuento = True
       return aplicar_descuento


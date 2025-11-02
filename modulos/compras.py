import random as rn

from modulos.utils import imprimir_separador, verificar_numero_valido, mostrar_opciones_disponibles, crear_registro, obtener_datos_de_usuario_autenticado, manejar_apertura_archivo
from modulos.autos import desplegar_menu_de_catalogo, pedir_datos_compra, obtener_modelos_disponibles, mostrar_modelos_disponibles, pedir_dato_de_autos
from modulos.usuarios import actualizar_clientes

def actualizar_stock(marca_elegida, modelo_elegido):
    archivo_stock_lectura = manejar_apertura_archivo("stock.csv", "r")

    texto_actualizado = []
    
    for i, linea in enumerate(archivo_stock_lectura):
        if i == 0:
            texto_actualizado.append(linea.strip())
        else:
            marca_linea, modelo_linea, stock_linea = linea.strip().split(",")

            modificar_linea = marca_linea.lower().strip() == marca_elegida.lower().strip() and modelo_linea.lower().strip() == modelo_elegido.lower().strip()

            if modificar_linea:
                stock_linea = int(stock_linea.strip()) - 1
                
            
            linea = f"{marca_linea.strip()}, {modelo_linea.strip()}, {str(stock_linea).strip()}"


            texto_actualizado.append(linea.strip())

    archivo_stock_lectura.close()

    archivo_stock_escritura = manejar_apertura_archivo("stock.csv", "wt")
    for linea in texto_actualizado:
        archivo_stock_escritura.write(linea + "\n")
    archivo_stock_escritura.close()

def mostrar_resumen(encargo_data):
    imprimir_separador()
    
    print("Resumen de su compra: ")

    for i, auto in enumerate(encargo_data["modelos_seleccionados"]):
        nombre, precio, color = auto["nombre"], auto["precio"], auto["color"]
        print(f"{i + 1}) nombre: {nombre} - color: {color} - precio: ${precio}")

    print(f"Monto acumulado: ${encargo_data['monto_total']}")

    imprimir_separador()

def encargar_autos():
    """Funcion que maneja todo lo referido al encargo de los autos que un usuario va a comprar"""
    usuario_data = obtener_datos_de_usuario_autenticado()
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

        nombre_marca, nombre_tipo = pedir_datos_compra() # Funcion para pedir datos para realizar una compra

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
        color_numero = verificar_numero_valido("Seleccione alguno de los colores con los que contamos: ", rango=range(1, len(colores_disponibles) + 1), opciones_disponibles=colores_disponibles)
        imprimir_separador()
        color_seleccionado = colores_disponibles[color_numero - 1]
        
        #---------------------- Confirmación de compra --------------------------------------------
        
        modelo_seleccionado = modelos_disponibles[modelo_seleccionado_indice]
        crear_registro("Modelo_seleccionado", modelo_seleccionado["nombre"])
        modelo_seleccionado["color"] = color_seleccionado
        crear_registro("Color_seleccionado", color_seleccionado)
        encargo_data["modelos_seleccionados"].append(modelo_seleccionado)
        encargo_data["monto_total"] += modelo_seleccionado["precio"]

        actualizar_stock(nombre_marca, modelo_seleccionado["nombre"])

        print(f"Se agregó exitosamente el siguiente modelo al resumen: {modelo_seleccionado['nombre']} - {nombre_marca} - {nombre_tipo}")

        opciones = ["Ver resumen", "Finalizar operación"]
        mostrar_opciones_disponibles(opciones)
        decision = verificar_numero_valido("Ingrese la opción deseada: ", rango=range(1, len(opciones) + 1),opciones_disponibles=opciones)

        if decision == 1:
            mostrar_resumen(encargo_data)
            crear_registro( "Ver resumen", "Sí")
            print("¿Desea pasar a finalizar la operación? ")

            respuestas_validas = ["Sí", "No (Encargar un nuevo vehículo)"]
            mostrar_opciones_disponibles(respuestas_validas)
            
            respuesta = verificar_numero_valido("Ingrese la opcion deseada: ", rango=range(1, len(respuestas_validas) + 1), opciones_disponibles=respuestas_validas)

            finalizar_compra = respuesta == 1
            crear_registro( "Finalizar compra", "Sí" if finalizar_compra else "No")
            if finalizar_compra and len(encargo_data["modelos_seleccionados"]) > 0:
                actualizar_clientes(usuario_data["dni"])
        else:
            crear_registro("Ver resumen", "No")
            finalizar_compra = True
            crear_registro("Finalizar compra", "Sí")
            if len(encargo_data["modelos_seleccionados"]) > 0:
                actualizar_clientes(usuario_data["dni"])
    return encargo_data

def aplicar_descuento_precio_final():
    """Función que se basa en un juego donde si el usuario gana, obtiene un descuento sobre el monto final de la compra"""

    

    aplicar_descuento = False

    print("¿Desea participar de un juego para conseguir un descuento del 20% para la compra de su auto?")
    des = verificar_numero_valido("Ingrese 1 si quiere y 2 si no quiere: ", rango=range(1, 3))

    if des == 2: 
        print("Como usted desee.")
        crear_registro("Descuento", "No")
    else: 
        print("Nos alegra que haya querido participar. El juego trata de que tiene que elegir un numero del 1 al 5, si su numero es igual al que eligió el programa usted se gana el descuento asi de facil.")
        ran = rn.randint(1,5)
        crear_registro("descuento", "Sí")
        numran = verificar_numero_valido("Ingrese un numero del 1 al 5: ", rango=range(1, 6))
          
        if numran != ran:
            print("Lo lamentamos, pero su numero no coincide, el numero correcto era:", ran)
        else:
            print("¡Felicitaciones! Su numero coincide, usted se gano un descuento del 20%.")
            aplicar_descuento = True
    return aplicar_descuento

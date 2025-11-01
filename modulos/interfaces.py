from modulos.compras import aplicar_descuento_precio_final, encargar_autos
from modulos.utils import imprimir_separador, manejar_apertura_archivo


def interfaz_usuario():

    ventas_archivo = manejar_apertura_archivo("ventas.csv", "a", "archivos")

    encargo_data = encargar_autos() # La totalidad de autos que el usuario seleccionó y va a comprar
    
    print("Finalizando operacion")
    
    imprimir_separador()
    
    if len(encargo_data["modelos_seleccionados"]) > 0:
        aplicar_descuento = aplicar_descuento_precio_final()
        
        if aplicar_descuento:
            monto_final = round(encargo_data["monto_total"]*0.80, 2)
            encargo_data["monto_total"] = monto_final

            print(f"El precio final con el descuento del 20% aplicado es de: {monto_final} mil dolares.")
        for modelo in encargo_data["modelos_seleccionados"]:
            ventas_archivo.write(f"{modelo['nombre']},{modelo['equipamiento']},{modelo['precio']},{modelo['color']} \n")
        
    else:
        print("No se realizó ningún pedido")
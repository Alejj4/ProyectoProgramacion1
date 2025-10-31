from modulos.autos import calcular_precios_promedios_tipo, completar_archivo_stock
from modulos.compras import aplicar_descuento_precio_final, encargar_autos
from modulos.usuarios import completar_clientes, menu_inicio
from modulos.utils import generar_directorio, imprimir_separador, manejar_apertura_archivo




def main():
    
    generar_directorio("archivos")
    generar_directorio("informes")

    ventas_archivo = manejar_apertura_archivo("ventas.csv", "wt", "archivos")
    ventas_archivo.write(f"Nombre, Equipamiento, Precio, Color \n")
    completar_clientes()

    completar_archivo_stock()

    calcular_precios_promedios_tipo()

    imprimir_separador()
    usuario,dni = menu_inicio()
    encargo_data = encargar_autos(usuario,dni) # La totalidad de autos que el usuario seleccionó y va a comprar
    
    print("Finalizando operacion")
    
    imprimir_separador()
    
    if len(encargo_data["modelos_seleccionados"]) > 0:
        aplicar_descuento = aplicar_descuento_precio_final(usuario)
        
        if aplicar_descuento:
            monto_final = round(encargo_data["monto_total"]*0.80, 2)
            encargo_data["monto_total"] = monto_final

            print(f"El precio final con el descuento del 20% aplicado es de: {monto_final} mil dolares.")
        for modelo in encargo_data["modelos_seleccionados"]:
            ventas_archivo.write(f"{modelo['nombre']},{modelo['equipamiento']},{modelo['precio']},{modelo['color']} \n")
        
    else:
        print("No se realizó ningún pedido")
    
    ventas_archivo.close()

if __name__ == "__main__":
    main()

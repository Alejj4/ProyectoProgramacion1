import funcion
import os

def generar_directorio(nombre_directorio):
    
    # Obteniendo la ruta actual del archivo
    ruta_actual = os.getcwd()

    # Obteniendo la ruta completa donde deberia estar el archivo
    ruta_completa = os.path.join(ruta_actual, nombre_directorio)
    
    # Verificar que si el archivo ya existe
    directorio_existente = os.path.exists(ruta_completa)

    if not directorio_existente:
        os.makedirs(ruta_completa, exist_ok=True)

def main():
    
    generar_directorio("archivos")
    generar_directorio("reportes")

    ventas = funcion.manejar_apertura_archivo("ventas.csv", "wt", "archivos")
    ventas.write(f"Nombre, Equipamiento, Precio, Color \n")
    funcion.completar_clientes()

    funcion.completar_archivo_stock()

    funcion.calcular_precios_promedios_tipo()

    funcion.imprimir_separador()
    usuario,dni = funcion.menu_inicio()
    encargo_data = funcion.encargar_autos(usuario,dni) # La totalidad de autos que el usuario seleccionó y va a comprar
    
    print("Finalizando operacion")
    
    funcion.imprimir_separador()
    
    if len(encargo_data["modelos_seleccionados"]) > 0:
        aplicar_descuento = funcion.aplicar_descuento_precio_final(usuario)
        
        if aplicar_descuento:
            monto_final = round(encargo_data["monto_total"]*0.80, 2)
            encargo_data["monto_total"] = monto_final

            print(f"El precio final con el descuento del 20% aplicado es de: {monto_final} mil dolares.")
        for modelo in encargo_data["modelos_seleccionados"]:
            ventas.write(f"{modelo['nombre']},{modelo['equipamiento']},{modelo['precio']},{modelo['color']} \n")
    else:
        print("No se realizó ningún pedido")

if __name__ == "__main__":
    main()

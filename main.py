import funcion

def main():
    
    ventas = open("ventas.csv", "wt", encoding="UTF-8")
    ventas.write(f"Nombre, Equipamiento, Precio, Color \n")
    funcion.completar_clientes()

    funcion.completar_archivo_stock()

    funcion.calcular_precios_promedios_tipo()

    funcion.imprimir_separador()
    while True:
        opciones_disponibles = ["Registrarse","Logearse"]
        print('Bienvenido a Schipani Motors Sport, elija una opcion.')
        funcion.mostrar_opciones_disponibles(opciones_disponibles)
        opcion = funcion.verificar_numero_valido("Ingrese una opción: ", rango=range(2))
        
        if opcion == 1:
            funcion.register()
            break
        elif opcion == 2:
            funcion.login()
            break
    encargo_data = funcion.encargar_autos() # La totalidad de autos que el usuario seleccionó y va a comprar
    
    print("Finalizando operacion")
    
    funcion.imprimir_separador()
    
    if len(encargo_data["modelos_seleccionados"]) > 0:
        aplicar_descuento = funcion.aplicar_descuento_precio_final()
        
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

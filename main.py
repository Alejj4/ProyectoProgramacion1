import funcion
import matrices as mt

def main():
    
    ventas = open("ventas.csv", "wt", encoding="UTF-8")

    funcion.completar_clientes()

    funcion.completar_archivo_stock()

    funcion.calcular_precios_promedios_tipo()

    funcion.imprimir_separador()
    print('Bienvenido a Schipani Motors Sport, esta es nuestra disponibilidad.')

    encargo_data = funcion.encargar_autos() # La totalidad de autos que el usuario seleccionó y va a comprar
        
    print(encargo_data)
    #         # comprar auto
    #         precio_total += funcion.comprar_auto(marca, modelo, vehiculos_comprados_matriz)
    #         print("\nTotal de la compra hasta ahora:", precio_total, "mil dólares.")

    #         descuento = funcion.descuento_auto()
    #         if descuento == 1:
    #             print("El precio final con el descuento del 20% aplicado es de:", int(precio_total*0.80), "mil dolares.")
            
    #         funcion.imprimir_separador()
    #         print('Porfavor, ingrese su DNI a la base de datos de cientes. ')
    #         numero = funcion.verificar_numero_valido(input('Ingrese su DNI aca: '))
    #         if funcion.norep(numero,dni_clientes) == 0:
    #             dni_clientes.append(numero)
    #             print('Su DNI se ha guardado, vuelva pronto.')
    #         else:
    #             print('Gracias por comprar nuevamente, vuelva pronto')
    # opcion = funcion.verificar_numero_valido(input("¿Le gustaría ver los informes obtenidos? (1=Sí | -1=No): "))

    # while opcion != 1 and opcion != -1:
    #     print("Opción incorrecta. Por favor, ingrese 1 para sí o -1 para no.")
    #     opcion = funcion.verificar_numero_valido(input("¿Le gustaría ver los informes obtenidos? (1=Sí | -1=No): "))

    # while opcion != -1:
    #     funcion.desplegar_menu_informes()
    #     opcion = funcion.verificar_numero_valido(input("Seleccione el informe que desea visualizar (-1 para salir): "))

    #     if opcion == 1:
    #         funcion.max_min_autos()
    #     elif opcion == 2:
    #         funcion.obtener_marca_mas_vendida(vehiculos_comprados_matriz)
    #     elif opcion == 3:
    #         funcion.dni_Clientes(dni_clientes)      
    #     else:
    #         print("Opción inválida. Intente de nuevo.")

    # print("Muchas gracias por venir a Schipani Motors, ¡nos vemos!")


if __name__ == "__main__":
    main()

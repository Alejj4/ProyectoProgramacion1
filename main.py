import funcion
import matrices as mt


def desplegar_menu_de_catalogo():
    
    matriz_precios_promedios = mt.calcular_precios_promedio()
    
    funcion.mostrar_matriz(matriz_precios_promedios)


def main():
    
    vehiculos_comprados_matriz = [
        [0,0,0,0],  # Toyota
        [0,0,0,0],  # Schipani
        [0,0,0,0],  # Chevrolet
        [0,0,0,0]   # Ford
    ]

    dni_clientes = []

    funcion.imprimir_separador()
    print('Bienvenido a Schipani Motors Sport, esta es nuestra disponibilidad.')
    desplegar_menu_de_catalogo()

    marca = 0
    
    while marca != -1:
        precio_total = 0
        funcion.imprimir_separador()
        print('Seleccione la marca que le gustaría ver')
        print("Para salir simplemente ingrese -1")
        marca = int(input('Ingrese 1 para Toyota, 2 para Schipani, 3 para Chevrolet y 4 para Ford: '))
        funcion.imprimir_separador()

        if marca == -1:
            print('Compra finalizada.')
        else:
            funcion.verificar_marca(marca)
            
                
            print('Ahora seleccione los modelos de qué tipo quiere ver.')
            
            modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
            
            if modelo != -1:
                funcion.imprimir_separador()
                funcion.verificar_modelo(modelo)
            
            modelos, _, _ = mt.obtener_datos_de_modelos()
            indices_marcas = mt.obtener_indices_marcas()
            
            modelo_indice = indices_marcas[marca - 1][modelo - 1]
            

            while len(modelos[modelo_indice]) == 0: # Si no hay stock de la marca y modelo elegido
                print("\nDisculpe, actualmente no hay stock disponible. Puede probar con otro modelo")
                funcion.imprimir_separador()
                modelo = int(input('Ingrese 1 para Hatchback, 2 para Sedan, 3 para Suv y 4 para PickUp: '))
                modelo_indice = indices_marcas[marca - 1][modelo - 1]    

            # Mostrar autos disponibles
            funcion.mostrar_autos(marca, modelo)
            funcion.imprimir_separador()
             
            # comprar auto
            precio_total += funcion.comprar_auto(marca, modelo, vehiculos_comprados_matriz)
            print("\nTotal de la compra hasta ahora:", precio_total, "mil dólares.")

            descuento = funcion.descuento_auto()
            if descuento == 1:
                print("El precio final con el descuento del 20% aplicado es de:", int(precio_total*0.80), "mil dolares.")
            
            funcion.imprimir_separador()
            print('Porfavor, ingrese su DNI a la base de datos de cientes. ')
            numero = int(input('Ingrese su DNI aca: '))
            if funcion.norep(numero,dni_clientes) == 0:
                dni_clientes.append(numero)
                print('Su DNI se ha guardado, vuelva pronto.')
            else:
                print('Gracias por comprar nuevamente, vuelva pronto')
    opcion = int(input("¿Le gustaría ver los informes obtenidos? (1=Sí | -1=No): "))

    while opcion != 1 and opcion != -1:
        print("Opción incorrecta. Por favor, ingrese 1 para sí o -1 para no.")
        opcion = int(input("¿Le gustaría ver los informes obtenidos? (1=Sí | -1=No): "))

    while opcion != -1:
        funcion.desplegar_menu_informes()
        opcion = int(input("Seleccione el informe que desea visualizar (-1 para salir): "))

        if opcion == 1:
            funcion.max_min_autos()
        elif opcion == 2:
            funcion.obtener_marca_mas_vendida(vehiculos_comprados_matriz)
        elif opcion == 3:
            funcion.dni_Clientes(dni_clientes)      
        else:
            print("Opción inválida. Intente de nuevo.")

    print("Muchas gracias por venir a Schipani Motors, ¡nos vemos!")


if __name__ == "__main__":
    main()

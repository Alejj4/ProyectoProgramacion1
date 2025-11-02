from .utils import verificar_numero_valido, manejar_apertura_archivo

def obtener_3_autos_mas_vendidos():
    archivo_ventas = manejar_apertura_archivo("ventas.csv", "rt", "archivos")

    if archivo_ventas:
        ventas_lista = []
        for i, linea in enumerate(archivo_ventas):
            if i == 0:
                pass
            
            linea_partes = linea.split(",")

            if len(linea_partes) < 2:
                continue
            
            marca = linea_partes[0].strip()
            nombre = linea_partes[1].strip()

            
            encontrado = False
            for venta in ventas_lista:
                if venta["marca"] == marca and venta["nombre"] == nombre:
                    venta["ventas"] += 1
                    encontrado = True

            if not encontrado:
                ventas_lista.append({
                    "marca": marca,
                    "nombre": nombre,
                    "ventas": 1
                })

        if len(ventas_lista) > 0:
            ventas_lista.sort(key=lambda x: x["ventas"], reverse=True)

            # Tomar los 3 primeros o los que haya
            autos_mas_vendidos = ventas_lista[:3]

            archivo_salida = manejar_apertura_archivo("top_3_autos.csv", "wt", "informes")
            archivo_salida.write("Marca,Nombre,Ventas\n")
            for auto in autos_mas_vendidos:
                archivo_salida.write(f"{auto['marca']},{auto['nombre']},{auto['ventas']}\n")
            archivo_salida.close()
        else:
            print("No se registraron ventas aun")

    else:
        print("No se encontró el archivo necesario para este informe (ventas.csv)")


def obtener_autos_mas_vendidos_marca():
    archivo_ventas = manejar_apertura_archivo("ventas.csv", "rt", "archivos")

    if archivo_ventas:

        print("Estas son las marcas que puede consultar")
        marcas_disponibles = ['Hatchback', 'Sedan', 'Suv', 'PickUp']

        marca_elegida = verificar_numero_valido("Ingrese una marca para obtener el informe correspondiente o -1 para salir: ", rango=(1, len(marcas_disponibles) + 1), opciones_disponibles=marcas_disponibles)

        if marca_elegida != -1:
            ventas_lista = []

            for i, linea in enumerate(archivo_ventas):
                if i == 0:
                    continue

                linea_partes = linea.strip().split(",")
                if len(linea_partes) < 2:
                    continue

                marca = linea_partes[0].strip()

                if marca.lower() != str(marca_elegida).lower():
                    continue

                encontrado = False
                for venta in ventas_lista:
                    if venta["marca"] == marca:
                        venta["ventas"] += 1
                        encontrado = True

                if not encontrado:
                    ventas_lista.append({
                        "marca": marca,
                        "ventas": 1
                    })

            if len(ventas_lista) > 0:
                ventas_lista.sort(key=lambda x: x["ventas"], reverse=True)
                top_3 = ventas_lista[:3]

                archivo_salida = manejar_apertura_archivo(f"top_3_autos_{marca_elegida}.csv", "wt", "informes")
                archivo_salida.write("Marca,Nombre,Ventas\n")
                for auto in top_3:
                    archivo_salida.write(f"{auto['marca']},{auto['nombre']},{auto['ventas']}\n")
                archivo_salida.close()
            else:
                print(f"No se registraron ventas para la marca {marca_elegida}")
                
        else:
            print("Saliendo")


    else:
        print("No se encontró el archivo necesario para este informe (ventas.csv)")


def obtener_ventas_por_marca():
    archivo_ventas = manejar_apertura_archivo("ventas.csv", "rt", "archivos")

    if archivo_ventas:
        pass
    else:
        print("No se encontró el archivo necesario para este informe (ventas.csv)")


def obtener_ventas_por_auto():
    archivo_ventas = manejar_apertura_archivo("ventas.csv", "rt", "archivos")

    if archivo_ventas:
        pass
    else:
        print("No se encontró el archivo necesario para este informe (ventas.csv)")

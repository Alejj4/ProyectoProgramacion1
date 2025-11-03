from .utils import verificar_numero_valido, manejar_apertura_archivo, mostrar_opciones_disponibles, imprimir_separador, crear_registro


def mostrar_mensaje_exitoso():
    print("Informe generado con exito, puede consultarlo en la carpeta de informes")

def obtener_3_autos_mas_vendidos():
    """Funcion para obtener los 3 autos mas vendidos sin discriminar por ningun criterio"""
    archivo_ventas = manejar_apertura_archivo("ventas.csv", "rt", "archivos")

    if archivo_ventas:
        ventas_lista = []
        for i, linea in enumerate(archivo_ventas):
            if i == 0:
                continue
            
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
            mostrar_mensaje_exitoso()
        else:
            print("No se registraron ventas aun")

    else:
        print("No se encontró el archivo necesario para este informe (ventas.csv)")


def obtener_3_autos_mas_vendidos_marca():
    """Funcion para obtener los 3 autos mas vendidos en base a la marca indicada por el admin"""
    archivo_ventas = manejar_apertura_archivo("ventas.csv", "rt", "archivos")

    if archivo_ventas:

        print("Estas son las marcas que puede consultar")
        marcas_disponibles = ['Hatchback', 'Sedan', 'Suv', 'Pick-Up']
        mostrar_opciones_disponibles(marcas_disponibles)

        marca_elegida = verificar_numero_valido("Ingrese una marca para obtener el informe correspondiente o -1 para salir: ", rango=(1, len(marcas_disponibles) + 1), opciones_disponibles=marcas_disponibles)
        crear_registro("Ver informe (3 autos mas vendidos)")
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
            crear_registro("Salir")
            print("Saliendo")


    else:
        print("No se encontró el archivo necesario para este informe (ventas.csv)")


def obtener_ventas_por_marca():
    """Funcion para obtener cuanto vendió cada marca"""
    archivo_ventas = manejar_apertura_archivo("ventas.csv", "rt", "archivos")

    if archivo_ventas:
        
        ventas_por_marca = []

        for i, linea in enumerate(archivo_ventas):
            if i == 0:
                continue

            linea_partes = linea.strip().split(",")
            if len(linea_partes) < 2:
                continue

            marca = linea_partes[0].strip()

            encontrado = False
            for venta in ventas_por_marca:
                if venta["marca"] == marca:
                    venta["ventas"] += 1
                    encontrado = True

            if not encontrado:
                ventas_por_marca.append({
                    "marca": marca,
                    "ventas": 1
                })

        marcas = ['Hatchback', 'Sedan', 'Suv', 'Pick-Up']

        # Agregar marcas sin ventas
        for marca in marcas:
            existe = False
            for venta in ventas_por_marca:
                if venta["marca"].lower().strip() == marca.lower().strip():
                    existe = True
                    break
            if not existe:
                ventas_por_marca.append({
                    "marca": marca,
                    "ventas": 0
                })        

        if len(ventas_por_marca) > 0:
            archivo_salida = manejar_apertura_archivo("ventas_por_marca.csv", "wt", "informes")
            archivo_salida.write("Marca,Total_Vendido\n")
            for venta in ventas_por_marca:
                archivo_salida.write(f"{venta['marca']},{venta['ventas']}\n")
            archivo_salida.close()
            mostrar_mensaje_exitoso()
        else:
            print("No se encontraron autos vendidos")
            imprimir_separador()
        

    else:
        print("No se encontró el archivo necesario para este informe (ventas.csv)")


def obtener_ventas_por_auto():
    """Genera un informe de ventas por modelo, incluyendo los que no tuvieron ventas (con 0)."""
    archivo_ventas = manejar_apertura_archivo("ventas.csv", "rt", "archivos")

    if archivo_ventas:
        
        autos_lista = []  # Lista para almacenar los autos y sus ventas

        for i, linea in enumerate(archivo_ventas):
            if i == 0:
                continue  # Saltar encabezado

            partes = linea.strip().split(",")
            if len(partes) < 2:
                continue  # Saltar líneas mal formateadas

            marca = partes[0].strip()
            nombre = partes[1].strip()

            # Buscar si el auto ya está en la lista
            encontrado = False
            for auto in autos_lista:
                if auto["marca"] == marca and auto["nombre"] == nombre:
                    auto["ventas"] += 1
                    encontrado = True
                    break

            # Si no estaba, agregarlo
            if not encontrado:
                autos_lista.append({
                    "marca": marca,
                    "nombre": nombre,
                    "ventas": 1
                })

        archivo_ventas.close()

        if len(autos_lista) > 0:
            # Ordenar por cantidad de ventas descendente
            autos_lista.sort(key=lambda x: x["ventas"], reverse=True)

            archivo_salida = manejar_apertura_archivo("ventas_por_auto.csv", "wt", "informes")
            archivo_salida.write("Marca,Nombre,Ventas\n")

            for auto in autos_lista:
                archivo_salida.write(f"{auto['marca']},{auto['nombre']},{auto['ventas']}\n")

            archivo_salida.close()
            mostrar_mensaje_exitoso()
        else:
            print("No se encontraron autos vendidos")
            imprimir_separador()
    else:
        print("No se encontraron datos de ventas ni modelos para generar el informe.")
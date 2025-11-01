from modulos.autos import calcular_precios_promedios_tipo, completar_archivo_stock
from modulos.usuarios import completar_clientes, menu_inicio
from modulos.utils import generar_directorio, imprimir_separador, manejar_apertura_archivo
from modulos.interfaces import interfaz_usuario, interfaz_admin


def main():
    
    generar_directorio("archivos")
    generar_directorio("informes")

    archivo_log = manejar_apertura_archivo("log.txt", "wt")
    archivo_log.close()

    ventas_archivo = manejar_apertura_archivo("ventas.csv", "wt", "archivos")
    ventas_archivo.write("Nombre, Equipamiento, Precio, Color \n")
    completar_clientes()
    ventas_archivo.close()

    completar_archivo_stock()

    calcular_precios_promedios_tipo()

    imprimir_separador()
    
    while True:
        usuario = menu_inicio()


        if usuario is None: # Finaliza el programa
            print("Finalizando el programa")
            break

        elif int(usuario["es_admin"]) == 1: # Inicia sesion un admin
            interfaz_admin()
            
            imprimir_separador()

        elif int(usuario["es_admin"]) == 0: # Inicia sesion un usuario normal
            print(f"Bienvenido/a nuevamente, {usuario["nombre"]}")
            interfaz_usuario()
            imprimir_separador()
    



if __name__ == "__main__":
    main()

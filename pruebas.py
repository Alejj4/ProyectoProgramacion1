

def max_min_autos():
       info_autos=mt.obtener_datos_de_modelos()
       listaprecio=[]
       for autos in info_autos: 
              if len(autos)>0:
                     nombres=autos[0]
                     precio=autos[2]
                     for i in range(len(nombres)):
                            listaprecio.append([nombres[i],precio[i]])
       lista_ordenada= sorted(listaprecio, key=lambda x: x[1])
       los_3_baratos=lista_ordenada[:3]
       print("------------------------------------------------------------------------------")
       print(los_3_baratos)
       print("------------------------------------------------------------------------------")
       los_3_caros=lista_ordenada[-3:]
       print(los_3_caros)
       print("------------------------------------------------------------------------------")
       return (los_3_baratos,los_3_caros)


       








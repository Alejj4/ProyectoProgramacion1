# Archivo de pruebas para experimentar fuera de los archivos principales
# Borrar cuando el proyecto este terminado

columna = 0
fila = 0
aux = 2

ToHa = ['Yaris xs', 'Yaris xls', 'Yaris s']
ToSe = []
ToSu = ['Cross xli', 'Cross seG']
ToPi = ['Hilux dx4x4','Hiluxsr4x4']
ScHa = []
ScSe = ['schipani uade Seminuevo','Schipani Schiziano']
ScSu = ['schipani chipa', 'schipani bochoQuemado']
ScPi = ['Schipani Pipani']
ChHa = []
ChSe = ['Onixplus']
ChSu = ['Spring', 'Tracker']
ChPi = ['Montana', 'S10', 'Silverado']
FoHa = []
FoSe = []
FoSu = ['Territory', 'Kuga Hybrid', 'Everest']
FoPi = ['Maverick', 'Rnager Raptor', 'F-150 Lariat Hybrid']



#Matriz de nombres declarados previamente
nombres = [[ToHa,ToSe,ToSu,ToPi],
       [ScHa,ScSe,ScSu,ScPi],
       [ChHa,ChSe,ChSu,ChPi],
       [FoHa,FoSe,FoSu,FoPi]]
elegido = nombres[columna][fila]
elegidoNom = elegido[aux]
print(elegidoNom)
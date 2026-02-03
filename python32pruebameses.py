# Esto es para descargar oracle en Mac
# https://fjtoscano.medium.com/instalar-oracle-database-xe-en-mac-m1-d5d2d17fc00c
from class32mes import Mes
print("Trabajando con clases")
# --------------------------------------------------------
# Primer ejercicio
# enero=Mes()
# enero.nombre="Enero"
# enero.temperaturaMaxima=9
# enero.temperaturaMinima=-2
# print("Media Enero ", enero.getTemperaturaMedia())
# mes2=Mes()
# mes2.nombre="Febrero"
# mes2.temperaturaMaxima=12
# mes2.temperaturaMinima=4
# print("Media Febrero ", mes2.getTemperaturaMedia())
# ---------------------------------------------------------
# Segundo ejercicio
# primero creamos una lista para guardar los datos
listaMeses=[]
for i in range(3):
    # Aquí creamos un nuevo mes
    mes=Mes()
    print("Introduzca el mes ", (i+1))
    mes.nombre=(input())
    print("Temperatura máx :")
    mes.temperaturaMaxima=int(input())
    print("Temperatura min :")
    mes.temperaturaMinima=int(input())
    listaMeses.append(mes)
# Recorremos los meses
for dato in listaMeses:
    print(dato.nombre+", Maxima"+ str(dato.temperaturaMaxima))
    print("Mínima "+ str(dato.temperaturaMinima))
    print("Media "+ dato.getTemperaturaMedia())
    mediaAnual=mediaAnual+dato.getTemperaturaMedia()
    #  esto está mal habría que dividir por toda la lista
print("Media anual ",mediaAnual)
print("Fin del programa")
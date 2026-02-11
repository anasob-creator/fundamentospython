# Nos olvidamos de BBDD.
# Solo quiero mostrar un menú con los oficios que vamos
# a crear manualmente
# después mostramos un menú al usuario par que seleccione un oficio
# mediante un número de opciones
import oracledb
connection=oracledb.connect(user="SYSTEM", password="oracle"
                            ,dsn="localhost/FREEPDB1")
cursor=connection.cursor()
# Necesitamos una lista de oficios
listaOficios=[]
# Agregamos oficios
listaOficios.append("ANALISTA")
listaOficios.append("DIRECTOR")
listaOficios.append("PROGRAMATOR")
listaOficios.append("VENDEITOR")
listaOficios.append("SUBDIRECTOR")
# Para mostrar un menú, recorremos la lista
# Creamos un contador
contador=1
for ofi in listaOficios:
    print(f"{contador}.- {ofi}")
    contador=contador+1
print("Seleccione una opción: ")
opcion=int(input())
oficioSeleccionado=listaOficios[opcion - 1]
print(f"Opción seleccionada: {oficioSeleccionado}")
# Consultamos los empleados con el oficio oficioSeleccionado
sql="select * from EMP where OFICIO=:oficio"
cursor.execute(sql, (oficioSeleccionado,))
print("----- LISTA  EMPLEADOS -----")
for row in cursor:
    print(f" - {row[1]}, Salario: {row[5]}")
cursor.close()
connection.close()
print("Fin del programa")

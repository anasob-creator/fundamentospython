# Quiero un menú con las funciones de la plantilla
# El usuario seleccionará una función y mostramos 
# los apellidos de la función seleccionada
# 1. Interino
# 2. Enfermera
# 3. Enfermera
# seleccione una opción:
import oracledb
connection=oracledb.connect(user="SYSTEM", password="oracle"
                            ,dsn="localhost/FREEPDB1")
cursor=connection.cursor()
# Necesitamos una lista de oficios
listaFuncion=[]
# Agregamos oficios
sql="select distinct FUNCION from PLANTILLA"
cursor.execute(sql)
# recorremos y por cada oficio append
for row in cursor:
    # Agregamaos cada oficio
    listaFuncion.append(row[0])
    # Creamos un contador
contador=1
for ofi in listaFuncion:
    print(f"{contador}.- {ofi}")
    contador=contador+1
print("Seleccione una opción: ")
opcion=int(input())
funcionSeleccionada=listaFuncion[opcion - 1]
print(f"Opción seleccionada: {funcionSeleccionada}")
# Consultamos los empleados con la función funcionSeleccionada
sql="select * from PLANTILLA where FUNCION=:funcion"
cursor.execute(sql, (funcionSeleccionada,))
print("----- PLANTILLA -----")
for row in cursor:
    print(f" - {row[3]}, Salario: {row[6]}")
cursor.close()
connection.close()
print("Fin del programa")
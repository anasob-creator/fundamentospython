# Vamos a mostrar de la plantilla de los empleados d
# de un turno que nos diga el usuario, 
# Empezamos importando la BBDD.
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
print ("Conectado")
print ("Dame un truno (T;M;N)")
turno=input()
sql="select APELLIDO, FUNCION from PLANTILLA where TURNO='" + turno+"'"
print(sql) # PINTAR LA CONSULTA PARA VER FALLOS
cursor=connection.cursor()
cursor.execute(sql)
for row in cursor:
    apellido=row[0]
    funcion=row[1]
    print(apellido +","+funcion)
cursor.close()
connection.close()
print("Fin del programa")
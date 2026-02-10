# Vamos a eliminar un enfermo por su identificador
# Empezamos importando la BBDD.
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
# antes creamos un solo cursor para primero mostrar enfermos y luego eliminar
cursor=connection.cursor()
# antes mostramos los enfermos (apellido e inscr)
sql="select APELLIDO, INSCRIPCION from ENFERMO"
cursor.execute(sql)
#recorremos
for row in cursor:
    print (row[0] + ", Inscripcion: " + str(row[1]))
# Tengo que limpiar el cursor
# cursor.close()
print ("Introduzca inscripción a eliminar:")
dato=input()
sql="delete from ENFERMO where INSCRIPCION="+dato
print(sql)
cursor.execute(sql)
# como es una consulta de acción hay que hacer un commit o un rollback incluso con un if...
connection.commit()
afectados=cursor.rowcount
print("Registros eliminados: " + str(afectados))
cursor.close()
connection.close()
print ("Fin del programa")
# si necesitamos hacer 2 consultas, necesitamos 2 cursores, pero si se puede hacer 
# una detrás de la otra, con 1 cursor basta.
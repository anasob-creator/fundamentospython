# Vamos a eliminar un enfermo por su identificador
# Empezamos importando la BBDD.
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
print ("Conectado")
print ("Introduzca inscripción a eliminar:")
dato=input()
sql="delete from ENFERMO where INSCRIPCION="+dato
print(sql)
cursor=connection.cursor()
cursor.execute(sql)
# como es una consulta de acción
afectados=cursor.rowcount
print("Registros eliminados: " + str(afectados))
cursor.close()
connection.close()
print ("Fin del programa")
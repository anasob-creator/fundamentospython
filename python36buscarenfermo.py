# Debemos buscar un enfermo por su inscripción
# igual que el dpto.
# Pediremos la inscripción al usuario y si existe 
# dibujamos los datos y si no indicamos que el enfermo
# no existe. 
# Datos: Apellido y dirección
########################### Comenzamos ########################
# Empezamos importando la BBDD.
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
print ("Conectado")
# Queremos el apellido y y dirección, me voy a oracle a ver qué quiero
# pedimos el id de dpto
print("Introduce un tu número de inscripción:")
dato=input()
sql="select APELLIDO, DIRECCION from ENFERMO where INSCRIPCION= "+dato
print(sql)
cursor=connection.cursor()
cursor.execute(sql)
row=cursor.fetchone()
if (row==None):
     print ("El num. de inscripción no existe")
else:
    apellido=row[0] #APELLIDO
    direccion=row[1] #DIRECCION
    print(apellido+","+direccion)
cursor.close()
connection.close()
print ("Fin del programa")
# si nos vamos a comprobar a la base de datos, no se grabará 
# hasta que introduzcamos commit o rollback en nuestras acciones. 
# Por lo tanto, hay que darle un commit o rollback


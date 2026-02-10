# En el siguiente ejemplo vamos a realizar un buscador de un dpto. por su id
# pediremos al usuario que nos diga el id del dpto.
# después mostramos los datos
# Empezamos importando la BBDD.
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
print ("Conectado")
# ############ dinámico
# pedimos el id de dpto.
print("Introduce un ID de dpto:")
iddpartamento=input()
sql="select * from DEPT where DEPT_NO:"+iddpartamento
print(sql)
cursor=connection.cursor()
cursor.execute(sql)
row=cursor.fetchone() 
if (row==None):
     print("NO existe el Dpto")
else:
     #Recuperamos los datos
     nombre=row[1] #DNOMBRE
     localidad=row[2] #LOC
     print(nombre+","+localidad)
# Necesitamos una consulta
# liberamos los recurso
cursor.close()
# # Cerramos conexión
connection.close()
print("Fin del programa")
# ############ estático
#Ahora necesitamos una consulta. Si no me acuerdo voy al archivo de test.sql, donde
# # la pruebo y me la traigo
# # Ahora necesitamos una consulta. Si no me acuerdo voy al archivo de test.sql, donde
# # la pruebo y me la traigo
# sql="select * from DEPT where DEPT_NO=10"
# # Ahora creamos un cursor. Lo hacemos con un método, para que me devuelva un objeto "cursor"
# cursor=connection.cursor()
# # Ahora ya si, ejecutamos para traernos los datos de la consulta con execute
# cursor.execute(sql)
# # Ahora recuperamos la primera fila
# row=cursor.fetchone() 
# # en este caso es estático, el 10, luego lo haremos dinámico
# # Comprobamos si tenemos datos o no en la fila
# if (row==None):
#     print("NO existe el Dpto")
# else:
#     #Recuperamos los datos
#     nombre=row[1] #DNOMBRE
#     localidad=row[2] #LOC
#     print(nombre+","+localidad)
# # liberamos los recurso
# cursor.close()
# # Cerramos conexión
# connection.close()
# print("Fin del programa")


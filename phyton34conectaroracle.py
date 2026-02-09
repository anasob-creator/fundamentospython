import oracledb
print ("Conectando Oracle")
# Tenemos un objeto connection que nos pedirá
# (user, password, system)
connetion=oracledb.connect(user="SYSTEM"
                           , password="oracle"
                           , dsn="localhost/FREEPDB1")
print("Estamos conectados!!!")
# cursor=connetion.cursor() OOJOOO QUE ME HE EQUIVOCADO
# cursor.execute(SQL)
sql="select * from DEPT"
print("Estamos conectados!!!")
#creamos un cursor para la consulta
cursor=connetion.cursor()
# ahora esto es una consulta vacía, debemos ejecutar la consulta para 
# que nos devuelva los datos de ORacle y para ello usamos execute
cursor.execute(sql)
# aquí ya están los datos
# una vez que tenemos el cursor (ahora ya lo tenemos aquí), 
# solo tenemos que leer los datos.
# tenemos un método llamado fetchone() que se mueve una fila 
# cada vez que lo ejecutamos 
# y nos devuelve dicha fila en la que estamos posicionados
row = cursor.fetchone() #primera fila, vamos a pintarla
print(row)
row = cursor.fetchone()#segunda fila, vamos a pintarla
print(row)
row = cursor.fetchone()#tercera fila
print(row)
row = cursor.fetchone()#cuarta fila
print(row)
# qué sucede si paso de fila a la siguiente? si no hay más filas
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
# pinta none, que es el null de python
# siempre que finalicemos las acciones, debemos 
# liberar los recursos
# si quiero reutilizarlo hay que liberar los cursores.
# Hay que cerrar el cursor
cursor.close()
# cerrar la conexión de la base de datos
connetion.close()
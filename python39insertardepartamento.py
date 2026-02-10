# Insertaremos un nuevo dpto pidiendo los datos al usuario
# y después mostraremos los datos insertados
# Empezamos importando la BBDD.
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
# Creamos cursor para las consultas:
cursor=connection.cursor()
print("Id del departamento")
id=input() #88
print("Nombre del departamento")
nombre=input() #NUEVO
print("Localidad del departamento")
localidad=input() #LOC
# insert into DEPT values (88, 'NUEVO', 'NUEVO')
# se puede hacer así, a manija:
# sql="insert into DEPT values("+id+", '"+nombre+", '"+localidad+"')"
# Pero En python tenemos una forma de concatenar 
# usando solamente un string, sin + 
# para ello se usa la letra f fuera del string 
# y cada variable irá entre llaves dentro del string
sql=f"insert into DEPT values ({id}, '{nombre}', '{localidad}')"
print(sql)
# realizamos la acción de insertar
cursor.execute(sql)
# Como voy a mostrar la tabla con los hospitales...
# realizo también el commit y lo dejo permanente.
connection.commit()
# Ahora nos traemos todos los datos de los hospitales
sql="select * from DEPT"
cursor.execute(sql)
# recorremos los regsistros
for row in cursor:
    num=row[0]
    nom=row[1]
    loc=row[2]
    print(f"Id {num}, Nombre {nom}, Localidad {loc}")
cursor.close()
connection.close()
print("Fin del programa")


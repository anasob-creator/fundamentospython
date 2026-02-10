# Programa que inserte un nuevo hospital.
# Le pedimos los datos al usuario 
# mostramos los hospitales
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
# Creamos cursor para las consultas:
cursor=connection.cursor()
# pedimos los datos
print("Codigo del hospital")
cod=input() #49
print("Nombre del hospital")
nombre=input() #la luz
print("Dirección del hospital")
dir=input() #reina victoria
print("Teléfono del hospital")
tel=input() #la luz
print("Número de camas")
camas=input() #reina victoria
sql=f"insert into HOSPITAL values ({cod}, '{nombre}', '{dir}','{tel}',{camas})"
print(sql)
# realizamos la acción de insertar
cursor.execute(sql)
# Como voy a mostrar la tabla con los depts...
# realizo también el commit y lo dejo permanente.
connection.commit()
# Ahora nos traemos todos los datos de los hospitales
sql="select * from HOSPITAL"
cursor.execute(sql)
# recorremos los regsistros
for row in cursor:
    cod=row[0]
    nom=row[1]
    dir=row[2]
    tel=row[3]
    camas=row[4]
    print(f"Cod {cod}, Nombre {nom}, Dirección {dir}, Teléfono{tel}, Camas {camas}")
cursor.close()
connection.close()
print("Fin del programa")
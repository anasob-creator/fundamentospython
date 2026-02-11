# Realizar una práctica para incrementar el salario de los empleados por un OFICIO
# Pediremos el oficio y el incremento al usuario
# Una vez incrementado mostrar el num de empleados que han sido incrementados
# y también los datos de los empleados
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
# Creamos cursor para las consultas:
cursor=connection.cursor()
# pedimos los datos
print("Oficio del empleado: ")
oficio=str(input())
print("Dame el incremento del sueldo: ")
incremento=int(input())
# Realizamos la acción de update el salario
sql="update EMP set SALARIO=SALARIO+:aumento where OFICIO=:ofi"
print(sql)
cursor.execute(sql, (incremento,oficio,))
registros=cursor.rowcount
connection.commit()
print(registros)
print(f"Empleados afectados: {registros}")
sql="select * from EMP where OFICIO=:ofi"
cursor.execute(sql, (oficio,))
for row in cursor:
     print(f"Apellido: {row[1]}, Salario: {row[5]}")
cursor.close()
connection.close()
print("Fin programa")
# Realizar un ejemplo para incrementar el salario 
# de los empleados de la plantilla
# de un hospital
# pediremos el hospital y el incremento
# y mostraremos el num de empleados afectados
# APELLIDO, SALARIO y HOSPITAL de los empleados afectados 
# por la consulta
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
# Creamos cursor para las consultas:
cursor=connection.cursor()
# pedimos los datos
print("Hospital del empleado: ")
hospital=input()
print("Dame el incremento del sueldo: ")
incremento=int(input())
# Realizamos la acción de update el salario
sql="update PLANTILLA set SALARIO=SALARIO+:aumento where HOSPITAL_COD=:codigo"
print(sql)
cursor.execute(sql, (incremento, hospital,))
registros=cursor.rowcount
connection.commit()
print(f"Empleados afectados: {registros}")
sql="select * from PLANTILLA where HOSPITAL_COD=:codigo"
print(sql)
cursor.execute(sql, (hospital,))
for row in cursor:
    print(f"Apellido: {row[3]}, Nuevo Salario: {row[6]}")
cursor.close()
connection.close()

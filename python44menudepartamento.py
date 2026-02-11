# Quiero mostrar los empleados de un dpto por su id
# El problema está en que no me acuerdo de los números 
# de dpto que tenemos.. 
# Mostrar los dptos, que el usuario lo viera y pueda 
# seleccionar
import oracledb
connection=oracledb.connect(user="SYSTEM", password="oracle"
                            ,dsn="localhost/FREEPDB1")
cursor=connection.cursor()
sql="select DEPT_NO FROM DEPT"
cursor.execute(sql)
print("----- Menú Departamentos -----")
for row in cursor:
    print(row[0])
print("Seleccione un departamento: ")
iddept=int(input())
sql="select APELLIDO, OFICIO from EMP where DEPT_NO=:iddpet"
cursor.execute(sql, (iddept,))
print("----- Empledos Departamentos -----")
for ape, ofi in cursor:
    print(f"{ape}, Oficio: {ofi}")
cursor.close()
connection.close()
print("Fin del programa")
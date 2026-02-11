# Vamos a realizar un ejemplo en el que mostraremos datos de 
# empleados de un departamento
# Pediremos al usuario el número de departamento
import oracledb
# Creamos la conexión a oracle
connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
# Creamos cursor para las consultas:
cursor=connection.cursor()
# pedimos los datos
print("Id del departamento")
id=input() #88
sql=f"select APELLIDO, OFICIO, DEPT_NO from EMP where DEPT_NO={id}"
cursor.execute(sql)
for APELLIDO, OFICIO, DEPT_NO in cursor:
    print(f"Apellido: {APELLIDO}, Oficio: {OFICIO}, Departamento: {DEPT_NO}")
cursor.close()
connection.close()
print("Fin programa")


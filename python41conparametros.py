# Igual que el anterior, pero con parámetros
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
numero=int(input())
sql=f"select APELLIDO, OFICIO, DEPT_NO from EMP where DEPT_NO=:deptno"
print(sql)
cursor.execute(sql,(numero,))
for APELLIDO, OFICIO, DEPT_NO in cursor:
    print(f"Apellido: {APELLIDO}, Oficio: {OFICIO}, Departamento: {DEPT_NO}")
cursor.close()
connection.close()
print("Fin programa")
# Quiero que cuando nos pidan un dpto. pongamos lo siguiente:
# 0 or 1=1
# Lo que estamos realizando es: 
# sql=f"select APELLIDO, OFICIO, DEPT_NO from EMP where DEPT_NO={id}or 1=1" 
# Estos se llama sql injection que es una medida de acceso a las aplicaciones
# Es una medida de hacking
# Nuestras apps están expuestas si utilizamos las consultas sql tal y como lo hemos 
# hecho en Python
# En lugar de concatenar textos/variables, se utiliza parametros
# las consultas. 
# Los parámetros impiden SQL Injection. 
# En lugar de incluir valores dentro de la consulta SQL, 
# se usan palabras clave que son sustituidas posteriormente. 
# Lo único que tenemos que saber , debemos enviar el tipo de dato 
# que necesita la consulta.
# Está mal porque es un tipo de dato String, por lo que habría que enviar:
# id=int(input())
# Si voy a enviar un texto tengo que convertirlo.
# Los parámetros ya no son visibles en la consulta
# Si pintamos la instrucción en sql ya no los veremos.
# Los nombres de parámetro dependen de la BBDD:
# En oracle, los parámetros se declaran con
# :nombreparametro
# # EN SQL Server: @nombreparametro
# Entonces la consulta será sustituyendo el id por :nombreinventado
# sql=f"select * from EMP where DEPT_NO=:iddepartamento"
# en SQL Server será sql=f"select * from EMP where DEPT_NO=@iddepartamento"
# tendríamos que pasarle en el execute del cursor los parámetros así:
# cursor.execute(sql, (parametros))
# Vamos a modificar en nuestro ejemplo porque a partir de ahora sin parámetros



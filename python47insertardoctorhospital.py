# Vamos a realizar un programa para insertar un Doctor
# Vamos a pedir 
# ID doctor, Apellido, Especialidad, Salario
# Una vez que pedimos los datos mostraremos un menú para que 
# el usuario selecciones a qué hospital quiere llevar al Doctor
# 1. La Paz.
# 2. San Carlos.
import oracledb
connection=oracledb.connect(user="SYSTEM", password="oracle"
                            ,dsn="localhost/FREEPDB1")
cursor=connection.cursor()
# Pedimos los datos al usuario
apellido=input("Introduzca el apellido: ")
iddoctor=input("Id del Doctor:")
espe=input("Especialidad: ")
salario=input("Salario: ")
# Necesitamos mostrar los hospitales
print("Debe seleccionar un Hospital: ")
sql="select NOMBRE, HOSPITAL_COD from HOSPITAL"
cursor.execute(sql)
# Necesitamos una lista de códigos hospitales
listaCodigos=[]
contador=1
for row in cursor:
    print(f"{contador}.- {row[0]}")
    listaCodigos.append(row[1])
    contador=contador+1
print("Seleccione un Hospital: ")
opcion=int(input())
idhospital=listaCodigos[opcion-1]
sql="insert into DOCTOR values(:hosp, :id, :ape, :espe, :sal)"
cursor.execute(sql, (idhospital, iddoctor, apellido, espe, salario,))
connection.commit()
registros=cursor.rowcount
print(f"Doctores insertados: {registros}")
cursor.close()
connection.close()
print ("Fin del programa")

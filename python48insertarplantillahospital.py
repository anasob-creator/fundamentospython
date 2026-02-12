# Insertar una persona en la Plantilla
# el id de la plantilla lo generamos dentro del programa
# pediremos al usuario Apellido, Función, Turno y salario y cod. sala
# Mostraremos un menú con los hospitales
import oracledb
connection=oracledb.connect(user="SYSTEM", password="oracle"
                            ,dsn="localhost/FREEPDB1")
cursor=connection.cursor()
# Generarmos el id de plantilla
sql="select max(EMPLEADO_NO)+1 as MAXIMO from PLANTILLA"
cursor.execute(sql)
row=cursor.fetchone()
idempleado=row[0]
# Pedimos el resto de datos al usuario
codsala=input("Código de la sala: ")
apellido=input("Introduzca el apellido del empleado: ")
funcion=input("Función del empleado:")
turno=input("Turno: ")
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
sql="insert into PLANTILLA values(:hosp, :sala, :idempleado, :ape, :funcion, :turno, :salario)"
cursor.execute(sql, (idhospital,codsala,idempleado,apellido,funcion,turno,salario,))
connection.commit()
registros=cursor.rowcount
print(f"Doctores insertados: {registros}")
cursor.close()
connection.close()
print ("Fin del programa")

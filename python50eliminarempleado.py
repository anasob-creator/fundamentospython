# Una aplicación para eliminar empleados igual que antes
# eliminar enfermos
# 1. clase de datos oracle50 empleado
# 2. clase programa: python50eliminarempleado.py
from oracle50empleados import OracleEmpleados
# Creamos nuestra clase OracleEnfermos
oracle=OracleEmpleados()
print("Programa eliminar empleado")
print("Introduzca un id de empleado")
dato=int(input())
# Le paso el dato que usuario ha introducido y me devuelve el num de regs eliminados
# recuperamos los registros que queramos eliminar y los pasamos a la variable registros
registros=oracle.eliminarEmpleados(dato)
print(f"Empleados eliminados: {registros}")
print("Fin de programa")
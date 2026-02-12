# Una aplicación para eliminar empleados igual que antes
# eliminar enfermos
# 1. clase de datos oracle50 empleado
# 2. clase programa: python50eliminarempleado.py
from oracle50empleados import OracleEmpleados
print("Programa eliminar empleado")
# Creamos nuestra clase OracleEnfermos
oracle=OracleEmpleados()
print("Introduzca un id de empleado")
dato=int(input())
# Le paso el dato que usuario ha introducido y me devuelve el num de regs eliminados
registros=oracle.eliminarEmpleados(dato)
print(f"Empleados eliminados: {registros}")
print("Fin de programa")
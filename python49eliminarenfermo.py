from oracle49enfermos import OracleEnfermos
print("Programa eliminar enfermo")
# Creamos nuestra clase OracleEnfermos
oracle=OracleEnfermos()
print("Introduzca una inscripción")
dato=int(input())
registros=oracle.eliminarEnfermo(dato)
print(f"Enfermo eliminado: {registros}")
print("Fin de programa")
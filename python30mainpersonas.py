###### manejo de personas ########
# Lo primero traer lo que vayas a necesitar
# En este caso me traigo personas
from class30persona import Persona
print("Manejando clases de persona")
# Creamos una persona
persona1=Persona()
persona1.nombre="Roger"
persona1.apellidos="Rabbit"
persona1.anyonacimiento=1989
persona1.pais="EEUU"
print(persona1.getNombreCompleto())
print("Edad persona 1", persona1.getEdad())
persona2=Persona()
print("Persona país ", persona2.pais)
print("Fin del programa")

############# CLASES ########################
class Persona:
    # Declaramos propiedades aquí
    # Asignamos valores
    nombre=""
    apellidos=""
    email=""
    anyonacimiento=0
    pais="loquesea"
# El constructor es un método para iniciar, 
# El primer código que utiliza cualquier programa con mi clase persona
# (valores por defecto???)
# Se le llama init
def __init__(self):
    self.pais="Francia"
    # así todas las personas tendrán pais Francia de inicio
    # Se indica self. siempre
    # También se podría indicar el valor por defecto al declararlo arriba
# Esto ya podría estar, epero el objeto podría tener
# métodos: acciones sobre la clase persona
# p.e.: cumplir años, si tuviera una edad, le sumo
def getEdad(self):
    return 2026 - self.anyonacimiento
def getNombreCompleto(self):
    return self.nombre + " " + self.apellidos

#  Los métodos los podemos dividir en 2 grupos
#Los métodos de acción: ejecutan una serie de acciones
# Los métodos return: ejecutan una serie de acciones y devuelven un valor después de ejecutar dichas acciones
#  Método de acción: print() (hace algo)
#  Método de return: len(). (devuelve algo)
# # # # # # # # # # METODOS RETURN # # # # # # # # # # # # # 
# Este método convierte a mayúsculas y nos devuelve texto a mayúsculas
def convertirMayusculas(texto):
    return texto.upper()
# Este método convierte a minusculas
def convertirMinusculas(texto):
    return texto.lower()
# concatenar
def concatenar(texto1,texto2):
    resultado=texto1+texto2
    return resultado



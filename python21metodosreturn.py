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
# un método de acción
def mostrarMenu():
    print("Seleccione una opción: ")
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    print("3. Concatenar")
# Aquí hacemos el programa MAIN
print("Ejemplos de método return")
print("Introduce un texto: ")
valor=input()
mostrarMenu()
opcion=int(input())
resultado=""
if (opcion ==1):
    resultado=convertirMayusculas(valor)
elif(opcion==2):
    resultado=convertirMinusculas(valor)
elif(opcion==3):
    print("dame otro texto")
    otro_texto=input()
    resultado=concatenar(valor,otro_texto)
print("resultado")
print("Fin de programa")
# Tengo que guardar el valor del return para poder mostrarlo


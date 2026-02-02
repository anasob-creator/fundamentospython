# RETO
# 1) Necesito un programa para averiguar si un número es narcisita
# Un número narcisista es aquel que la suma de sus potencias elevada a su 
# longitud nos devuelve el mismo número
# Ejemplo:  153
# 1x1x1= 1
# 5x5x5=125
# 3x3x3=27
# 1 + 125+27 = 153
# 2) Llevar la lógica a un método def en una librería
# 3) Crear un programa en el que el usuario introduce un rango y 
# le mostramos los números narcisistas en ese rango con nuestro método 
# Pedimos un rango de números al usuario
print("Fin del programa")


#1. pido rango de números
#2. los meto en una lista
#3. la voy recorriendo
#4. elevo a la potencia 
# 5. creo una suma para sumar la longitud de la cadena
# 6. comparo con el número inicial y si es igual, es narcisista
# Con esto tendríamos la primera parte del reto narcisista,
#######
# 1. Ahora hay que llevarlo a una librería
# 2. Con un código base se crea el librería29narcisista.py para que vaya a la par
# Ahí crearé el def con un cálculo que me diga true o false a la pregunta de si es narcisita y me lo devuelva
# En el def no querré el print
# Necesito que mi número narcisista sea texto y lo convierto a texto. 
######
#1. Lo siguiente, en Python29narcisita elimino todo y me traigo solo la librería
import libreria29narcisista
print("Numero narcista")
print("Introduce un numero iniciar")
inicial = int(input())
print("Introduzca numero final")
final = int(input())
for inicial in range(inicial, final):
    if (libreria29narcisista.numeroNarcisista(inicial) == True):
        print(inicial)
print("Fin de programa")
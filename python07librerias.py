######### Librerías #########
# Una librería es un conjunto de funcionalidades
# Python tiene muchas librerías ya instaladas que nos ayudan  con los códigos
# Algunas librerías son estándar y vienen con la instalación de Python
## Existen dos tipos de librerías
#1. Librerías estándar: vienen con la instalación de Python, integradas dentro del lenguaje, no puedo utilizarlas a no ser que las llame
#2.  Librerías externas: son librerías creadas por terceros, que no vienen con la instalación de Python, y que tenemos que instalar para poder utilizarlas
# Estas son (pip)
# Para conocerlo vamos a crear un simple programa que utlizará la librería math para saber cómo se utilizaría los métodos.
# Tenemos dos métodos, son iguales pero con diferentes sintaxis
# 1.
# import libreria
# libreria.metodo1()
# libreria.metodo2()
# tenemos otra sintaxix donde nos traemos directamente los métodos de la librería
# 2.
# from liberia import metodo1(), metodo2()
# vamos a ver un ejemplo con la librería math, para utilizar funciones matemáticas (redondear, raíz cuadrada, potencia...
print("Librerías Python")
# Necesitamos la parte entera del resultado
resultado=int(7/3)
print(resultado)
print("fin del programa")
# Si queremos redondear al alza la parte entera, Python no trae de serie nada para hacer operaciones matetemáticas complejas es utilizar clases herramientas (liberías)
print("Librerías Python")
import math
# Necesitamos la parte entera del resultado
resultado=(7/3)
print(resultado)
print("Floor", math.floor(resultado))
print("Ceil", math.ceil(resultado))
print("sqrt", math.sqrt(25))    
print("fin del programa")
# En python.org hay una lista de librerías estándar
# https://docs.python.org/3/library/
# Con la otra sintaxis
print("Librerías Python")
from math import floor, ceil, sqrt
# Necesitamos la parte entera del resultado
resultado=(7/3)
print(resultado)
print("Floor", floor(resultado))
print("Ceil", ceil(resultado))
print("sqrt", sqrt(25))    
print("fin del programa")
# otro ejemplos
print("Librerías Python")
from math import floor, ceil
num1=7
num2=3
resultado=num1/num2
celi=ceil(resultado)
flora=floor(resultado)
print(resultado)
print("Floor", floor(resultado))
print("Ceil", ceil(resultado)) 
print("fin del programa")
## # # # # #  Depuración de aplicaciones # # # # #
# Nos permite qué pasa en nuestro programa en tiempo de ejecución, cuando nedesitamos saber el valor que tienen las variables en el código mientras se ejecuta
# Nos sirve sobre todo para errores lógicos
# VAmos a visualizar cómo podemos averiguar qué está pasando cuando ejecutamos.
# En la parte ida del código ponemos un punto de interrupción (breakpoint) y cuando el programa llega a ese punto se para y podemos ver el valor de las variables en ese momento
# Ejecutamos con run and debug. 
# Ponemos un breakpoint en la línea que queremos parar haciendo clic a la izquierda del número de línea
# Cuando el programa llega a ese punto se para y podemos ver el valor de las variables nos tenemos que ir a pestaña del debub y ejecutar el archivo corriente entonces se parará
# Podemos ver el valor de las variables en la pestaña de VARIABLES
# Podemos seguir ejecutando línea a línea con F10 o continuar la ejecución normal con F5
# Podemos quitar los breakpoints haciendo clic en el punto rojo
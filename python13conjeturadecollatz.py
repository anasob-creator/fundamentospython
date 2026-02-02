####### Conjetura de Collatz #######
# Todo número entero positivo siempres llegará a ser 1 siguiendo dos concidiones:
# 1. Si el número es par se divide por 2
# 2. Si el número es impar se multiplica por 3 y se le suma 1
# Ejemplo: 6 es par, 6/2=3, 3 es impar, 3*3+1=10, 10 es par, 10/2=5, 5 es impar, 5*3+1=16, 16 es par, 16/2=8, 8 es par, 8/2=4, 4 es par, 4/2=2, 2 es par, 2/2=1
# El programa pedirá un número y mostrará la secuencia hasta llegar a 1
# No se puede hacer con un for, porque no sabemos el número de repeticiones, usaremos un while
# Pedimos el número al usuario
# Introducimos while y le ponemos la condición de salida,que será cuando el número sea diferente de 1.
print("Conjetura Collatz")
print("Introduzca un numero")
numero = int(input())
while (numero != 1):
    if (numero % 2 == 0):
        numero = int(numero / 2)
    else:
        numero = numero * 3 + 1
    print(numero)
print("Fin de programa")
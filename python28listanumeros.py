# Programa que pida números hasta que el usuario meta -1
# después mostraremos los siguientes
# Suma total de números
# Números introducidos: 9
# Números pares: 3
# Números impares: 6
# Suma Pares:
# Suma impares: 99
print("#########Lista números##########")
# Pedimos el número al usuario
listaNumeros = []
# Creamos las variables
total_numeros=0
total_pares=0
total_impares=0
suma_numeros=0
suma_numeros_pares=0
suma_numeros_impares=0
numero=0
# Mientras el número sea diferente de -1 seguiremos pidiendo números. Usaremos while porquen no sabemos el número de repeticiones
while (numero != -1):
    print("Dime un número: ")
    numero = int(input())
    listaNumeros.append(numero)
    # Incrementamos el contador de números para el total de números
    total_numeros=total_numeros+1
    # Sumamos el número a la suma total
    suma_numeros=suma_numeros+numero
    if (numero%2==0):
        #es par
        # Incrementamos el contador de números para el total de números pares
        total_pares=total_pares+1
        # Sumamos el número a la suma total de pares
        suma_numeros_pares=suma_numeros_pares+numero
    else: 
        # Incrementamos el contador de números para el total de números impares
        total_impares=total_impares+1
         # Sumamos el número a la suma total de impares
        suma_numeros_impares=suma_numeros_impares+numero
# Mostramos los resultados
print(listaNumeros)
print("Has introducido un total de: ", total_numeros, " números.")
print("Has introducido un total de números pares: ", total_pares, " números.")
print("Has introducido un total de números impares: ", total_impares, " números.")
print("La suma de todos los números introducidos es: ", suma_numeros)
print("La suma de todos los números pares introducidos es: ", suma_numeros_pares)
print("La suma de todos los números impares introducidos es: ", suma_numeros_impares)
print("Fin del programa")
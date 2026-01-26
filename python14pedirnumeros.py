# Necesito un programa que pedirá números al usuario hasta que introduzca un cero.
# El resultado del programa será:
# Número introducidos: 6
# La suma de todos los números que el usuario haya escrito
print("#########Suma de los números introducidos##########")
# Pedimos el número al usuario
numero=int(input("Dame un número: "))
# Creamos las variables
total_numeros=0
suma_numeros=0
# Mientras el número sea diferente de cero seguiremos pidiendo números. Usaremos while porquen no sabemos el número de repeticiones
while (numero!=0):
    # Incrementamos el contador de números
    total_numeros=total_numeros+1
    # Sumamos el número a la suma total
    suma_numeros=suma_numeros+numero
    # Pedimos otro número
    numero=int(input("Dame otro número (introduce 0 si quieres salir): "))
# Mostramos los resultados
print("Has introducido un total de: ", total_numeros, " números.")
print("La suma de todos los números introducidos es: ", suma_numeros)
print("Fin del programa")
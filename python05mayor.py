# Ejemplo 1, pedir dos número al usuario.
# con esos dos número decir cual es mayor y si los número son iguales
# creamos un programa pyton05mayor.py
print("Mayor/meno/igual")
print("Dame un número")
num1=int(input())
print("Dame otro número")
num2=int(input())
if (num1>num2):
    print("El número mayor es: ", num1)
elif (num1==num2):
    print("Los números son iguales")
else:
    print("El número mayor es: ", num2)
print("Fin del programa")
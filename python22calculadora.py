# En el main
# Pediremos dos números al usuario
# Mostraremos un menú con las siguientes opciones
# 1.- Sumar
# 2.- Restar
# 3.- Multiplicar
# Tendremos cuatro funciones, tres return con las operaciones y otra para mostrar el menú
# Primero creamos los métodos
#Sumar
def sumar(num1,num2):
    suma=num1+num2
    return suma
#restar. Se puede hacer sin guardar también
def restar(num1,num2):
    return num1-num2
def multiplicar(num1,num2):
    return num1*num2
# un método de acción
def mostrarMenu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("Seleccione una opción: ")
# Aquí hacemos el programa MAIN
print("Ejemplos de método return")
print("Introduce un número: ")
numero1=int(input())
print("Introduce otro número: ")
numero2=int(input())
mostrarMenu()
opcion=int(input())
resultado=0
if (opcion==1):
    resultado=sumar(numero1,numero2)
elif(opcion==2):
    resultado=restar(numero1,numero2)
elif(opcion==3):
    resultado=multiplicar(numero1,numero2)
else:
    print("opción no válida")
print("Operación:", resultado)
print("Fin del programa")
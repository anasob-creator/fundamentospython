# Versión 23 de la calculadora
# Si el usuario no mete ningún número pedimos números hasta que sea correcto
# Creamos otra opció má para que el usurio pueda introducir nuevos números
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
    print("0. Salir")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("Introducir nuevos números: ")
    print("Seleccione una opción: ")
#Creamos un método que devolverá el método introducido, con un bucle infinito hasta que nos de un número
def getNumero():
    print("Introduzca su número: ")
    #  almacenamos lo que escriba el usuario en una variable string
    aux=input()
    # Entramos en un bucle mientras no sean números
    while(aux.isdigit()==False):
        print("Eso no es un número")
        print("Introducir nuevos números: ")
        aux=input()
    #convertimos el texto a número
    num=int(aux)
    # Devolvemos en número de este método
    return num
# Aquí hacemos el programa MAIN
print("Ejemplos de método return versión 3")
# Aquí metemos el método que recoge el número
numero1=getNumero()
numero2=getNumero()
# Quiero mostrar el menú hasta que elija salir
# CUando el usuario elija el 0 salimos del bucle
# primero le damos valor a opción para que entre en el bucle
opcion=-1
while(opcion!=0):
    mostrarMenu()
    opcion=int(input())
    resultado=0
    if(opcion==1):
        resultado=sumar(numero1,numero2)
    elif(opcion==2):
        resultado=restar(numero1,numero2)
    elif(opcion==3):
        resultado=multiplicar(numero1,numero2)
    elif(opcion==4):
        numero1=getNumero()
        numero2=getNumero()
    else:
        print("opción no válida")
        print("Operación:", resultado)
        print("Fin del programa")

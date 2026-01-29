# # # # # #  Fichero de Metodos # # # # # # 
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
# Creamos un nuevo programa con el 23 a juego

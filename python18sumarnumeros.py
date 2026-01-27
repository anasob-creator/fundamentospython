# Necesitamos un programa que pida una cifra de números
# Comprobar que nos han dado números. 
# 1. Si no son números, mostramos un mensaje de error
# 2. Si son números mostramos la suma de cada número del texto
#  1+2+3+4=10 Cada elemento.
#  Tipo de dato
#  En este caso nos interesa el número convertido a string
print("Sumar números")
numero_string=str(input("Escribe un número: "))
print(numero_string)
if numero_string.isdigit() ==False:
    print("No son números, escribe números")
else:
    print("son números")
    # para sumar los números lo que voy a necesitar es una suma. Declaro la suma
    suma=0
    # recorro cada caracter
    for i in range(len(numero_string)):
       #necesito cada letra del texto
       letra=numero_string[i]
       # convertimos la letra a numero
       numero=int(letra) 
       suma=suma+numero
print("la suma de "+ numero_string + "es" + str(suma))
print("fin del programa")
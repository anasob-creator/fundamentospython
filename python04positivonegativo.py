print("Positivo/Negativo/Cero")
numero=0
if (numero>0):
    print("Positivo")
else:
# volvemos a preguntar
    if (numero==0):
        print ("Cero")
    else:
        print("Negativo")
print("Fin del programa")
# Tenemos otra sintaxis para cuando queremos preguntar sobre una misma variable. Dicha sintaxis es else if, seguir preguntando
#Modificamos el código anterior usando elif.
print("Positivo/Negativo/Cero")
numero=0
if (numero>0):
    print("Positivo")
elif (numero==0):
    print ("Cero")
else:
    print("Negativo")
print("Fin del programa")

# volvemos a preguntar
if (numero==0):
        print ("Cero")
else:
        print("Negativo")
print("Fin del programa")
# hacer dinámico pedir el número al usuario
print("Positivo/negativo/cero")
print("Dame un número")
num=int(input())
if (num>0):
    print("Positivo")
elif (num==0):
    print("Cero")
else:
    print("Negativo")
print("Fin del programa")
# Ejemplo 1, pedir dos número al usuario.
# con esos dos número decir cual es mayor y si los número son iguales
# creamos un programa pyton05mayor.py
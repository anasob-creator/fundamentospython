# RETO
# 1) Necesito un programa para averiguar si un número es narcisita
# Un número narcisista es aquel que la suma de sus potencias elevada a su 
# longitud nos devuelve el mismo número
# Ejemplo:  153
# 1x1x1= 1
# 5x5x5=125
# 3x3x3=27
# 1 + 125+27 = 153
# 2) Llevar la lógica a un método def en una librería
# 3) Crear un programa en el que el usuario introduce un rango y 
# le mostramos los números narcisistas en ese rango con nuestro método 


# Pedimos un rango de números al usuario
inicial=int(input("Dame el número inicial del rango: "))
numero_final=int(input("Dame el número final del rango: "))
while (inicial<=numero_final):
    if (inicial%2==0):
        print(inicial)
        #incrementamos el inicial
    inicial=inicial+1
print("Fin del programa")

#calculo narcisista

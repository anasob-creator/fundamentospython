# vamos a realizar un programa que muestre los número pares que se encuentren en un rango
# Pedimos al usuario el rango
print("Rango de número pares")
inicio=6
numero_final=20
# que tipo de bucle podríamos utlizar? Cualquiera, pero es más sencillo con un bucle for 
# porque sabemos el número de repeticiones
print("Números pares entre ", inicio, " y ", numero_final)
for i in range(inicio, numero_final+1):
    # preguntamos si el número es par
    if (i%2==0):
        # Estamos en un par
        print(i)
# con un while sería así
print("Números pares entre ", inicio, " y ", numero_final, " con while")
# Pedimos los datos al usuario
inicial=int(input("Dame el número inicial del rango: "))
numero_final=int(input("Dame el número final del rango: "))
while (inicial<=numero_final):
    if (inicial%2==0):
        print(inicial)
        #incrementamos el inicial
    inicial=inicial+1
print("Fin del programa")
# Todo dependerá del tipo de bucle que queramos usar, si nosotros sabemos el número de repeticiones, usaremos for, si no lo sabemos usaremos while

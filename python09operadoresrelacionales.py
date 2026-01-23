#### Operadores relacionales ####
## Los operadores relacionales son aquellos que permiten comparar dos valores.
# Tenemos dos palabras clave para utilizarlos: and y or
# and: Todas las condiciones deben cumplirse. devuelve True si ambas condiciones son verdaderas
# Ej: para rangos
# # or: Cualquier condicion haría cumplirse. Devuelve True si al menos una condición es verdadera
# Ej:para valores de variables
# ejemplo: Pedimos 3 número y mostraremos el menor, mayor y el intermedio
print("Mayor de tres números")
# directamente pedimos y guardamos los tres números
num1=int(input("Dame el primer número: "))
num2=int(input("Dame el segundo número: "))
num3=int(input("Dame el tercer número: "))
# qué número es mayor
# Tengo algo para guardar el número mayor?? Nunca declararé la variable dentro del if. 
#  Si la variable está tabulada en un ámbito solo existirá dentro de ese ámbito
# Las variables no estará por ahí tiradas deben declararse arriba
mayor=0 # inicializo la variable mayor con un valor cualquiera
menor=0 # inicializo la variable menor con un valor cualquiera
intermedio=0 # inicializo la variable intermedio con un valor cualquiera
if (num1>num2 and num1):
    mayor=num1
elif (num2>num1 and num2>num3):
    mayor=num2
else:
    mayor=num3
# qué número es menor
if (num1<num2 and num1<num3):
    menor=num1
elif (num2<num1 and num2<num3):
    menor=num2
else:
    menor=num3
# qué número es intermedio
if (num1!=mayor and num1!=menor):
    intermedio=num1
elif (num2!=mayor and num2!=menor):
    intermedio=num2 
else:
    intermedio=num3
print("El número mayor es: ", mayor)
print("El número intermedio es: ", intermedio)
print("El número menor es: ", menor)
print("Fin del programa")
# otra forma sería sumar todos los números y restar el menor y el mayor.
suma=num1+num2+num3
intermedio2=suma-mayor-menor
print("El número intermedio calculado es: ", intermedio2)
print("Fin del programa")
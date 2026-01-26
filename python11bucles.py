# Secuencia de código que se repite n veces mediante instrucciones
#### Bucles ####
# Tenemos dos tipos de bucles en Python
# 1. Bucle while: Es condicional, se repite mientras hasta que se cumpla una condición
# Sintaxis: 
# while (condicion==True):
    # instrucciones a repetir
    # codigo para False
# 2. Bucle for: Es un bucle definido, se repite un número determinado de veces, le indicamos le principio y el final y el bucle entra en ese inicio y finaliza en ese final.. Aquí estamos protegidos del bucle infinito.
# La variable se declara dentro del propio nucleo y solo tendrá visibilidad dentro del mismo bucle.
# Sintaxis:
# for contador in range(final):
    # instrucciones a repetir
# AQUÍ CONTADOR NO EXISTE
# La variable contador siempre será cero con esta sintaxix.
# Tenemos otra sintaxis en la que podemos iniciar el contador con otro valor
# for contador in range(inicio, final):
    # instrucciones a repetir
# AQUÍ CONTADOR NO EXISTE
######### EJEMPLOS #########
print("####### Ejemplos de Bucles #######")
print("Bucle while")
# Declaramos la variable fuera del bucle
# Para nuestra condición de salida del bucle
contador=0
# Bucle while que se repite mientras contador sea menor que 5   
while (contador<=5):
    print("Contador: ", contador)
    # Incrementamos el contador para que llegue a la condición de salida
    contador=contador+1
# En el bucle FOR, se declara la variable dentro del propio bucle
print("Bucle for")
# Dicha variable suele llamarse i, z, k, 
# vamos a hacer un bucle for de 0 a 5
for i in range(5+1):
    print("Valor de i: ", i)
# Siempre hay que poner el valor final +1 porque el rango es exclusivo (cuenta como un menor que)
# Tenemos la posibilidad de iniciar el contador en otro valor
# Un número final 2--8
print("Bucle for con inicio y final")
for z in range(2, 8+1):
    print("Valor de z: ", z)
print("Fin del programa")
   
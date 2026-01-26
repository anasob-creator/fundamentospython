# Pedimos el número al usuario y el programa nos muestra la tabla de multiplicar de ese número del 1 al 10
print("#########Tabla de multiplicar##########")
# utilizaremos un bucle for porque sabemos el número de repeticiones. Pedimos el número
numero=int(input("Dame un número para mostrar su tabla de multiplicar: "))
print("Tabla de multiplicar del número ", numero)
total=1
for i in range(1, 10+1):
    # multiplicamos
    total=int(numero*i)
    # mostramos el resultado
    print(str(numero), "x", str(i), "=", str(total))
    #sumamos a la variable total
    total=total+1
print("Fin del programa")
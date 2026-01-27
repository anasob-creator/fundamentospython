########## VALIDACIÓN ISBN ############
# Pedir un isbn y ver si está correcto
# Se descomponen la cadena y se multiplica por la posición en la que está
# 1. primera posición por 1, segunda posición por 2, tercera posición por 3
# 2. La suma de todas esas multiplicaciones se divide entre 11 y si el resto es cero el num ISBN es correcto
# Pedimos un isbn
print("---------- Validar ISBN -----------")
isbn=str(input("Escribe un número: "))
print(isbn)
 #Declaramos la variable aquí para que sume
suma=0
if isbn.isdigit() ==False:
    print("No son números, escribe números")
else:
    print("son números")
    # para multiplicar los números lo que voy a necesitar es una variable. Declaro el producto
    producto=0
     # vamos a necesitar una suma para el 2.
    for i in range(len(isbn)):
        # necesito cada letra del texto
        letra=isbn[i]
         # convertimos la letra a numero
        numero=int(letra)
        producto=numero*(i+1)
        suma=producto+suma
    print(suma)
    if suma % 11 == 0:
        print("El ISBN es correcto")
    else:
        print("El ISBN es correcto")
print("fin del programa")




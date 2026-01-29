# librería de métodos
########## VALIDACIÓN ISBN ############
# Pedir un isbn y ver si está correcto
# Se descomponen la cadena y se multiplica por la posición en la que está
# 1. primera posición por 1, segunda posición por 2, tercera posición por 3
# 2. La suma de todas esas multiplicaciones se divide entre 11 y si el resto es cero el num ISBN es correcto
# Pedimos un isbn
def validarISBN(ISBN):
    if(len(isbn) !=10):
        print("el ISBN debe tener 10 caracteres")
    else:
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
            if (suma % 11 == 0):
                return"El ISBN es correcto"
            else:
                return"El ISBN no es correcto"
# vamos a separar la capa visual de la capa lógica
# def validarDni(dni):
#     resultado=dni/23
#     if (resultado==1):
#        return"T"
# Realizar una aplicación para conocer la letra del Documento Nacional de Identidad a través del número de DNI. 
# La fórmula para calcular la letra del número del DNI se halla de la siguiente manera:
# Se calcula el valor de la siguiente resta 
# ( nº DNI - (ENTERO(nº DNI / 23) * 23
# Se mira la equivalencia en la siguiente tabla cambios
def validarDni(dni):
    numero=dni - (int(dni/23)*23)
    if (numero==0):
        return"T"
    elif (numero==1):
        return"R"
    elif (numero==2):
        return"W"
    elif (numero==3):
        return"A"
    elif (numero==4):
        return"G"
    elif (numero==5):
        return"M"
    elif (numero==6):
        return"Y"
    elif (numero==7):
        return"F"
    elif (numero==8):
        return"P"
    elif (numero==9):
        return"D"
    elif (numero==10):
        return"X"
    elif (numero==11):
        return"B"
    elif (numero==12):
        return"N"
    elif (numero==13):
        return"J"
    elif (numero==14):
        return"Z"
    elif (numero==15):
        return"S"
    elif (numero==16):
        return"Q"
    elif (numero==17):
        return"V"
    elif (numero==18):
        return"H"   
    elif (numero==19):
        return"L"
    elif (numero==20):
        return"C"
    elif (numero==21):
        return"K"
    elif (numero==22):
        return"E"
    elif (numero==23):
        return"T"
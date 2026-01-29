def validarISBN(isbn):
    if (len(isbn) != 10):
        return False
    else:
        suma = 0
        for i in range(len(isbn)):
            #recuperamos cada caracter
            caracter = isbn[i]
            #convertimos a numero el caracter
            numero = int(caracter)
            multi = numero * (i + 1)
            suma = suma + multi
        #Preguntamos si la suma es divisible entre 11
        if (suma % 11 == 0):
            return True
        else:
            return False
def validarDNI(dni):
    #( nº DNI - (ENTERO(nº DNI / 23) * 23
    resultado = dni - ((dni / 23) * 23)
    if (resultado == 0):
        return"T"
    elif (resultado == 1):
        return"R"
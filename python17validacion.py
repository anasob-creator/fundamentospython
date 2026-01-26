# Escribiremos un email se lo pedimos al usuario
#  Debemos indicar si tiene algún error
#  que contenga @
#  que el email contenga un punto
#  @ ni al principio ni al final (starswith)
#  que solamente contenga 1 @
#  Que exista un punto después de la @
#  Que el dominio sea de 2 a 3 caracteres (es/com/org)
# Pedimos el email al usuario
email=input("Escribe tu email: ")
contiene_arroba=email.find("@")
print("El email contiene @: ", contiene_arroba)
contiene_punto=email.find(".")
print("El email contiene un punto: ", contiene_punto)
comienza_arroba=email.startswith("@")
print("El email comienza @: ", comienza_arroba)
termina_arroba=email.endswith("@")
print("El email termina @: ", termina_arroba)
contador_a=email.count("a")
print("La letra a aparece este número de veces: ", contador_a)
#busco el índice de la arroba
print("find(@, index):", email.find("@", 1))
#busco la subcadena a partir de al arroba
subcadena=email[3:]
print("email [3:]", subcadena)
tras_arroba_contiene_punto=subcadena.find(".")
print("El email contiene un punto tras la arroba: ", tras_arroba_contiene_punto)

# a partir del punto extraigo subcadena dominio
#busco el índice del punto
print("find(., index):", email.find(".", 1))
#busco la subcadena a partir del punto
dominio=email[3:]
print("email [3:]", dominio)



if contiene_arroba ==-1:
    print("El email no contiene @: ")
elif contiene_punto ==-1:
    print("El email no contiene .: ")
elif comienza_arroba==True:
    print("El email comienza con @, corrígelo: ")
elif termina_arroba==True:
    print("El email termina con @, corrígelo: ")







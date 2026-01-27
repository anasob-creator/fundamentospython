# Escribiremos un email se lo pedimos al usuario
#  Debemos indicar si tiene algún error
#  que contenga @
#  que el email contenga un punto
#  @ ni al principio ni al final (starswith)
#  que solamente contenga 1 @
#  Que exista un punto después de la @
#  Que el dominio sea de 2 a 3 caracteres (es/com/org)
# Pedimos el email al usuario
print("Validación email")
email=input("Escribe tu email: ")
print("------------------ ERRORES ----------------")
if email.find("@") ==-1:
    print("no existe @")
elif email.count("@") ==0:
    print("no existe @ en el email")
elif email.find(".") ==-1:
    print("no existe .")
elif email.startswith("@") or email.endswith("@"):
    print("no existe @")
elif (email.find("@") != email.rfind("@")):
    print ("existe más de una @")
elif (email.rfind(".")>email.find(".")):
    print ("Debe existir solo un punto después de la @")
else:
    ultimo_punto=email.rfind(".")
    dominio=email[ultimo_punto+1:]
    longitud_dominio=len(dominio)
    if(longitud_dominio>=2 and longitud_dominio<=3):
        print("email correcto")
    else:
        print("El dominio debe ser de 2 o 4 caracteres")
print (" fin del programa")
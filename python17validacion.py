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
print("------------------ ERRORES ----------------")
if contiene_arroba ==-1:
    print("OJO!! -------- El email no contiene ARROBA")
elif contiene_punto ==-1:
    print("OJO!! --------  El email no contiene PUNTO")
elif comienza_arroba==True:
    print("OJO!! --------  El email comienza con @, corrígelo")
elif termina_arroba==True:
    print("OJO!! --------  El email termina con @, corrígelo: ")
elif posicion_punto==True:
    print("OJO!! --------  El email termina con @, corrígelo: ")

def validar_punto_post_arroba(email):
    # 1. Buscamos la posición de la arroba
    posicion_arroba = email.find("@")
    
    # 2. Buscamos la posición del último punto
    posicion_punto = email.rfind(".")

    # VALIDACIONES:
    # Si no hay arroba, find devuelve -1
    if posicion_arroba == -1:
        return False
    
    # Si el punto está antes de la arroba o no existe (-1)
    elif posicion_punto < posicion_arroba:
        return False
    
    # Si el punto está inmediatamente después de la arroba (ej: u@.com)
    # y queremos evitarlo
    elif posicion_punto == posicion_arroba + 1:
        return False

    else:
        return True

# Pruebas
print(validar_punto_post_arroba("usuario@dominio.com"))  # True
print(validar_punto_post_arroba("usuario.nombre@dominio")) # False (punto antes)
print(validar_punto_post_arroba("usuario@dominio"))      # False (sin punto)




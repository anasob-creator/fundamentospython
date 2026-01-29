from unittest import result
import libreria24validaciones
print("Main de validaciones")
print("Introduzca ISBN")
isbn = input()
respuesta = libreria24validaciones.validarISBN(isbn) #???
if (respuesta == True):
    print("El ISBN esta BIEN")
else:
    print("El isbn no es correcto")
print("Fin del programa Main")
print("Main de DNI")
print("Calcular letra NIF")
print("Introduzca numero DNI")
dni = int(input())
respuesta=libreria24validaciones.validarDNI(dni)
print(respuesta)
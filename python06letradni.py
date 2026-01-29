# practicas de sintaxis

# Realizar una aplicación para conocer la letra del Documento Nacional de Identidad a través del número de DNI. 
# La fórmula para calcular la letra del número del DNI se halla de la siguiente manera:
# Se calcula el valor de la siguiente resta 
# ( nº DNI - (ENTERO(nº DNI / 23) * 23
# Se mira la equivalencia en la siguiente tabla cambios

print("Encuentra la letra del DNI")
print("Dame tu número del DNI")
dni=int(input())
numero=dni - (int(dni/23)*23)
if (numero==0):
    print("la letra es: T ")
elif (numero==1):
    print("la letra es: R ")
elif (numero==2):
    print("la letra es: W ")
elif (numero==3):
    print("la letra es: A ")
elif (numero==4):
    print("la letra es: G ")
elif (numero==5):
    print("la letra es: M ")
elif (numero==6):
    print("la letra es: Y ")
elif (numero==7):
    print("la letra es: F ")
elif (numero==8):
    print("la letra es: P ")
elif (numero==9):
    print("la letra es: D ")
elif (numero==10):
    print("la letra es: X ")
elif (numero==11):
    print("la letra es: B ")
elif (numero==12):
    print("la letra es: N ")
elif (numero==13):
    print("la letra es: J ")
elif (numero==14):
    print("la letra es: Z ")
elif (numero==15):
    print("la letra es: S ")
elif (numero==16):
    print("la letra es: Q ")
elif (numero==17):
    print("la letra es: V ")
elif (numero==18):
    print("la letra es: H ")
elif (numero==19):
    print("la letra es: L ")
elif (numero==20):
    print("la letra es: C ")
elif (numero==21):
    print("la letra es: K ")
elif (numero==22):
    print("la letra es: E ")
elif (numero==23):
    print("la letra es: T")
print("Fin del programa")

#otra forma de hacerlo

print("Calcular letra NIF")
print("Introduzca numero DNI")
dni = int(input())
#( nº DNI - (ENTERO(nº DNI / 23) * 23
resultado = dni - ((dni / 23) * 23)
print(resultado)
if (resultado == 0):
    print("T")
elif (resultado == 1):
    print("R")
elif (resultado == 2):
    print("W")
elif (resultado == 3):
    print("A")
elif (resultado == 4):
    print("G")
elif (resultado == 5):
    print("M")
elif (resultado == 6):
    print("Y")
elif (resultado == 7):
    print("F")
elif (resultado == 8):
    print("P")
elif (resultado == 9):
    print("D")
elif (resultado == 10):
    print("X")
elif (resultado == 11):
    print("B")
elif (resultado == 12):
    print("N")
elif (resultado == 13):
    print("J")
elif (resultado == 14):
    print("Z")
elif (resultado == 15):
    print("S")
elif (resultado == 16):
    print("Q")
elif (resultado == 17):
    print("V")
elif (resultado == 18):
    print("H")
elif (resultado == 19):
    print("L")
elif (resultado == 20):
    print("C")
elif (resultado == 21):
    print("K")
elif (resultado == 22):
    print("E")
elif (resultado == 23):
    print("T")
print("Fin de programa")
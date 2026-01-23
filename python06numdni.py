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

print("Encuentra la letra del DNI")
print("Dame tu número del DNI")
dni=int(input())
numero=dni - (int(dni/23)*23)
letra=""
if (numero==0):
    letra="T"
elif (numero==1):
    letra="R"
elif (numero==2):
    letra="W"
elif (numero==3):
    letra="A"
elif (numero==4):
    letra="G"
elif (numero==5):
    letra="M"
elif (numero==6):
    letra="Y"
elif (numero==7):
    letra="F"
elif (numero==8):
    letra="P"
elif (numero==9):
    letra="D"
elif (numero==10):
    letra="X"
elif (numero==11):
    letra="B"
elif (numero==12):
    letra="N"
elif (numero==13):
    letra="J"
elif (numero==14):
    letra="Z"
elif (numero==15):
    letra="S"
elif (numero==16):
    letra="Q"
elif (numero==17):
    letra="V"
elif (numero==18):
    letra="H"   
elif (numero==19):
    letra="L"
elif (numero==20):
    letra="C"
elif (numero==21):
    letra="K"
elif (numero==22):
    letra="E"
elif (numero==23):
    letra="T"
print("Letra "+letra)
print("Fin del programa")
######## Pedir fecha ala usuario y decir que día de la semana es ########
# Pido el día y el número mes y el año
print("Dime el día")
dia=int(input())
print("Dime el número del mes")
mes=int(input())
print("Dime el año")
ano=int(input())
#  A partir de esto datos hay que calcular lo siguiente para averiguar el día de la semana de nacimiento:
# Ejemplo 15/06/1997
# 1. Si el mes es enero es 13 si es febrero 14
if mes==1:
    mes=13
elif mes==2:
    mes=14
# 2. Multiplicamos el mes más 1 por 3 y dividimos entre 5
mes_calculo=int((mes+1)*3/5)
# 3. Dividir el año entre 4 y coger la parte entera
ano_calculo1=int(ano/4)
# 4. Dividir el año entre 100
ano_calculo2=int(ano/100)
# 5. Dividir el año entre 400
ano_calculo3=int(ano/400)
# 6. Sumar el dia, el doble del mes, el año, el resultado de la operación 1, el resultado de la operación 2, menos el resultado de la operación 3 más la operación 4 más 2.
resultado=dia + (mes*2) + ano + mes_calculo + ano_calculo1 - ano_calculo2 + ano_calculo3 + 2
print("Resultado:", resultado)
# 7. Dividir el resultado entre 7
resto=int(resultado/7)
print("Resto:", resto)
# Restar el número del paso 5 con el número del paso 6 multiplicado por 7
paso7=resultado - (resto*7)
print("Paso 7:", paso7)
if paso7==0:
    print("El día de la semana es sábado")
elif paso7==1:
    print("El día de la semana es domingo")
elif paso7==2:
    print("El día de la semana es lunes")
elif paso7==3:
    print("El día de la semana es martes")
elif paso7==4:
    print("El día de la semana es miércoles")
elif paso7==5:
    print("El día de la semana es jueves")
elif paso7==6:
    print("El día de la semana es viernes")
print("Fin del programa")
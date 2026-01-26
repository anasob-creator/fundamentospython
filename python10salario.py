######## SALARIOS ########
#Realizar una aplicación que obtenga el salario neto de los empleados de una empresa teniendo en cuenta el número de horas trabajadas, el importe a pagar por hora y el lugar al que ha sido destinado el trabajador (establecido en Km).
##Cada hora extra se pagará 1.5€ más que las normales, (la hora extra comienza a computarse a partir de la 36 hora semanal trabajada)
##Sobre el salario base anterior, si el destino del empleado está:
#Entre 101 Km y 900Km: La dieta será “NACIONAL”
#Por encima de 900Km: Dieta “INTERNACIONAL”
#Por debajo de 101 Km  Dieta “PROVINCIAL”
##Sobre el precio final obtenido del salario: Cantidades menores o iguales a 250 € no soportan retención 0%Cantidades por encima de 250 € y menores o iguales a 500 € la retención es del 20%Cantidades por encima de 500 € la retención es del 50%
##Aplicaremos el IVA (16%) al salario bruto y se lo restaremos para conseguir el salario neto del trabajador.
##Al final debemos mostrar el siguiente informe:
##INTRODUZCA HORAS SEMANALES        INTRODUZCA IMPORTE HORA:        INTRODUZCA KILOMETROS:                                      
## Solicitamos los datos al usuario
horas_trabajadas=int(input("Introduzca las horas trabajadas en la semana: "))
importe_hora=float(input("Introduzca el importe por hora trabajada: "))
kilometros=int(input("Introduzca los kilómetros: ")) 
# Declaramos las variables
horas_extra=0
destino=""
retencion=""
salario_base=0.0
salario_extras=0.0
salario_bruto=0.0
iva=0.16
salario_total=0.0
if (horas_trabajadas>36):
    horas_extra=horas_trabajadas-36
    salario_extras=horas_extra*(importe_hora*1.5)
    salario_base=(horas_trabajadas*importe_hora)
else:
    salario_base=horas_trabajadas*importe_hora
# Calculamos el destino
if (kilometros>900):
    destino="INTERNACIONAL"
elif (kilometros>=101 and kilometros<=900):
    destino="NACIONAL"
else:
    destino="PROVINCIAL"
# Calculamos el salario bruto
salario_bruto=salario_base+salario_extras
# Pintaamos la retención
if (salario_bruto>500):
    retencion=("50%")
elif (salario_bruto>250 and salario_bruto<=500):
    retencion=("20%")
else:
    retencion=("0%")
# Calculamos el iva
iva=salario_bruto*0.16
# Calculamos el salario total
salario_total=salario_bruto-iva
# Mostramos el informe
print("------- INFORME DE SALARIO -------")
print("Horas trabajadas: ", horas_trabajadas)
print("Horas extras: ", horas_extra)
print("Importe por hora: ", importe_hora)
print("Distancia en kilómetros: ", kilometros)
print("Destino: ", destino)
print("Retención: ", retencion)
print("Salario base: ", salario_base)
print("Salario  horas extras: ", salario_extras)
print("Salario bruto: ", salario_bruto)
print("IVA 16%: ", iva)
print("------------------------------------------")
print("Salario total: ", salario_total)
print("Fin de programa")

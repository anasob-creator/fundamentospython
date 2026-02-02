from class33mascotas import Mascota
print("Trabajando con clases")
listaMascotas=[]
ron=Mascota()
ron.nombre = "Ron"
ron.raza = "Teckel"
ron.anyoNacimiento = 2000
ron.anyoAdopcion=2001
print("Años adopción: ", ron.getAnyosAdoptada())
listaMascotas.append(ron)
milton=Mascota()
milton.nombre = "Milton"
milton.raza = "Braco"
milton.anyoNacimiento = 2005
milton.anyoAdopcion=2007
print("Años adopción: ", milton.getAnyosAdoptada())
listaMascotas.append(milton)
mus=Mascota()
mus.nombre = "Mus"
mus.raza = "Teckel"
mus.anyoNacimiento = 2010
mus.anyoAdopcion=2015
print("Años adopción: ", mus.getAnyosAdoptada())
listaMascotas.append(mus)


######### Listas y tuplas ###########
print("Listas en Python")
listaNumeros=[3,5,7,112,9,88]
# Podemos dibuar idrectamente las listas
#print(listaNumeros)
#podemos ordenar de forma ascendente
# listaNumeros.sort()
# print(listaNumeros)
#podemos ordenar de forma descendente
# print(listaNumeros)
#  Podemos recorrer todos los elementos del conjunto 1 a 1 con un for (Todo empieza en CERO)
for i in range (len(listaNumeros)):
               print(listaNumeros[i])
# Listas pueden ser cualquier tipo
listaNombres=["Ana", "María","Adrián","Lucía", "Diana"]
# Accedemos a los nombre por si índice
print("Nombre[2]: ", listaNombres[2])
print("Nombre[2]: ", listaNombres[4])
# Append añade nuevo elemento al final de las listas. Si queremos meter más de un elemento, con bucles
listaNombres.append("El nuevo")
# Existe otra opción para insertar un nuevo elemento en una posición concreta: insert
listaNombres.insert(1, "Infiltrado")
# El método remove elimina el primer elemento que se encuentra
#listaNombres.remove("Adrián")  # No elimina los dos, solo el primero que encuentre
# Podemos eliminar por índice(posición)
listaNombres.pop(6) 
# Imaginamos que borro una posición que no existe: Error. Debe de existir
# SI queremos elminar dos, tienen que ser dos instrucciones
# podemos borrar RANGOS con del
del listaNombres[0:2]
# podemos preguntar por elementos dentro del conjunto
respuesta="Diana" in listaNombres
print(listaNombres)
print(respuesta)
# podemos recorrer cada elemento
for i in range (len(listaNombres)):
        print (listaNombres[i])
# podemos borrar toda la lsitalista con clear
listaNombres.clear()
print (listaNombres)
# # # # # # #  Tuplas # # # # # # # # 
print("Tuplas")
#  Elementos que son estáticos. NO se pueden modificar
tupla=("Leche", "Cacao", "Avellanas", "Azucar")
print(tupla)
#  dibujo un elemento
print("tupla[1] :", tupla[1])
# la tupla no se puede modificar
print(tupla)
#  Son útiles para manejar múltiples objetos de un golpe


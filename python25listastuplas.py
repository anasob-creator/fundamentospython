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
# # # Diccionarios
provincias=dict()
provincias={
        924: "Badajoz",
        956:"Alicante",
        976:"Zaragoza"
}
# Podemos recuperar solas claves (keys()) o solo los values())
for claves in provincias.keys():
        print("Prefijo: ", claves)
        print("------------------------")
for valores in provincias.values():
        print("Provincias: ", valores)
#  setdefault inserta
provincias.setdefault
# pop elimina un elemento en el diccionario por su key
provincias.pop(956)
print(provincias)
# clear elimina todo el diccionario
provincias.clear()
print(provincias)
# Cuando hablamos de objetos conjuntos existe un tercer tipo de bucle llamado referencia
# En lugar de recorrer por una condición o contador lo realiza una a una, mostrando cada elemento del conjunto
for i in range(len(tupla)):
        elem=tupla[i]
        print(elem)
# En este bucle estamos recorriendo con un contador y almacenando cada elemento dentro de una variable llamada Elem"
# La variable elem es una variable de referencia, porque hace referencia a un elemento del conjunto.
# Los bucles de referencia se utilizan cuando no me importa el contador, solo el contenido.
# Quiero recorrer cada elemento de la tupla
for elem in tupla:
        print(elem)
# en este último no coges la posición en la que estén.
# Vale para las listas, para todos los conjuntos

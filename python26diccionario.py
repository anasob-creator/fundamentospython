print("Diccionarios")
#Creamos el diccionario
provincias=dict()
provincias={
        924:"Badajoz",
        956:"Alicante",
        976:"Zaragoza",
        91:"Madrid",
        93:"Barcelona",
        959:"Huelva"
}
print(provincias)
# Recuperar el value de un elemento por su KEY
# si no existe devuelve None
print(provincias.get(9591))
# Recorrer cada Key, Value mediante items
for clave, valor in provincias.items():
    print("key "+ str(clave) + ", Value: "+valor)
print(provincias)
# Al igual que hemos recorrido los items podemos recorrer o solo claves o solo valores (values)
for clave in provincias.keys():
    print(clave)
for valor in provincias.values():
    print(valor)
# Podemos añadir con setdefault
provincias.setdefault(925,"Toledo")
# No podemos repetir una Key
# Se puede repetir el value
# Se puede eliminar por la clave con pop por su KEY
provincias.pop(924)
print(provincias)
#  la clave debe existir o tendremos error
#  Para eliminar todo el diccionario
provincias.clear()
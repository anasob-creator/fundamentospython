######## CLASE STRING ########
# Una clase es la definición de un objeto, en este caso un string
# Una clase está compuesta por propiedades y métodos.
# Las propiedades son características del objeto, en el caso de los strings una propiedad es la longitud del string
# Dependiendo del tipo de clase tendremos unos métodos u otros, que serán herramientas para manejar dicho objeto.
# La clase STRING es la que permite almacenar y manejar textos en Python
# Por ejemplo podemos convertir un texto a mayúsculas, minúsculas, buscar una palabra dentro del texto, etc
# Un string no deja de ser un conjunto de caracteres almacenados en una variable.
# Podemos averiguar el tampaño de un conjunto mediante la función o propiedad LEN
print("######## Ejemplos de clase STRING ########")
# String diferente mayúsculas y minúsculas
texto="Lenguaje Python"
longitudtexto=len(texto)
# los strings siempre comienzan en la posición 0
# cada letra estará en una posición, la primera letra en la posición 0, la segunda en la posición 1, etc la última letra será len-1
# todo funciona por índices, por lo que tenemos la posibilidad la posición de cada letra por su índice. 
# Cogemos el objeto string y le decimos la posición entre corchetes
#texto[0]="L"
#texto[1]="e"
# Tenemos una serie de métodos para manejar los strings
# Mayúsculas upper()
texto_mayusculas=texto.upper()
print("Texto en mayúsculas: ", texto_mayusculas)
# Minúsculas lower()
texto_minusculas=texto.lower()
print("Texto en minúsculas: ", texto_minusculas)
# Buscar una palabra dentro del texto find()
posicion_palabra=texto.find("Python")
print("La palabra Python comienza en la posición: ", posicion_palabra) # si no lo encuentra devolverá -1
# Reemplazar una palabra por otra replace()
texto_reemplazado=texto.replace("Python", "Java")
print("Texto reemplazado: ", texto_reemplazado)
# rfind() busca de derecha a izquierda (busca la primera e índice que encuentra empezando por la derecha)
texto2="Lenguaje Python y lenguaje C++ y lenguaje Java"
posicion_palabra_rfind=texto2.rfind("lenguaje")
# Dentro de python tenemos programación orientada a objetos (POO), por lo que podemos usar métodos de dicha programación, como el polimorfismo.
# el polimorfismo es varias formas para un método, por ejemplo el método replace puede sustituir una palabra por otra en un string, 
# #pero también puede sustituir caracteres por otros caracteres.

# Ejemplo polimorfismo con find y rfind
texto3="abacadaeafagahaiajakalamanaoapaqarasatauavaaxaayaza"
posicion_a_find=texto3.find("a") # buscará la primera a desde la izquierda
posicion_a_rfind=texto3.rfind("a") # buscará la primera a desde la derecha
print("Posición de la primera 'a' con find: ", posicion_a_find)
print("Posición de la primera 'a' con rfind: ", posicion_a_rfind)
print("Fin del programa")
# startswith() y endswith() devuelve True si el stringo comienza con un texto o termina con un texto determinado
texto4="Hola, bienvenido al lenguaje Python"
comienza_con_hola=texto4.startswith("Hola")
termina_con_python=texto4.endswith("Python")
print("¿El texto comienza con 'Hola'? ", comienza_con_hola)
print("¿El texto termina con 'Python'? ", termina_con_python)
print("Fin del programa")
# ejemplo de replace con polimorfismo
texto5="abracadabra"
# reemplazamos la palabra abra por xyz
texto_reemplazado1=texto5.replace("abra", "xyz")
print("Texto reemplazado 1: ", texto_reemplazado1)
# reemplazamos la letra a por o
texto_reemplazado2=texto5.replace("a", "o")
print("Texto reemplazado 2: ", texto_reemplazado2)
print("Fin del programa")
# ejemplo con count() cuenta cuántas veces aparece una subcadena dentro del string
texto6="abracadabra"
contador_a=texto6.count("a")
contador_abra=texto6.count("abra")
print("La letra 'a' aparece ", contador_a, " veces en el texto")
print("La subcadena 'abra' aparece ", contador_abra, " veces en el texto")
print("Fin del programa")
# ejemplo con isalpha() devuelve True si todos los caracteres del string son letras (no números ni espacios ni símbolos)
texto7="Python"
texto8="Python3"
es_texto7_alpha=texto7.isalpha()
es_texto8_alpha=texto8.isalpha()
print("¿El texto7 es solo letras? ", es_texto7_alpha)
print("¿El texto8 es solo letras? ", es_texto8_alpha)
print("Fin del programa")
# ejemplo con isdigit() devuelve True si todos los caracteres del string son dígitos (números) del 0 al 9
texto9="12345"
texto10="123a45"
es_texto9_digit=texto9.isdigit()
es_texto10_digit=texto10.isdigit()
print("¿El texto9 es solo dígitos? ", es_texto9_digit)
print("¿El texto10 es solo dígitos? ", es_texto10_digit)
print("Fin del programa")
# algunos métodos más de la clase string
isupper=texto.isupper() # devuelve True si el string está en mayúsculas
islower=texto.islower() # devuelve True si el string está en minúsculas
titulo=texto.title()   # convierte la primera letra de cada palabra en mayúscula
# Dentro de python tenemos la posibilidad de extraer subcadenas de un texto. 
##### PYTHON SLICING #######
texto="primer python"
# tenemos dos posibilidadas
# 1. Queremos la subcadena desde una posición concreta
# texto[8:] -->  yton
# 2. Queremos una subcadena desde una posición inical hasta una posición final ... será 
# # objeto [inicio:final]
# texto[0:2] ---->pr
print("------------------------ EJEMPLOS ------------------------------ ")
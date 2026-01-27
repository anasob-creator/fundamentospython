####### FUNCIONES / METODOS DE PYTHON ##############
# Una función es un método y un método es una función, es lo mismo
# Son herramientas que contienen los programas de Python y sus clases también
# Un método de una clase de Python: (string) (upper())
# Una función de Python: len(texto)
# Cualquier programa se ejecuta y utiliza funciones/métodos de Python
# Los métodos o funciones hacen que nuestro código no sea lineal, además podemos reutilizar las funciones
# Actualmente hemos validado un email, dni o un isbn.
# Si queremos validar un email, usaremos el método que hayamos creado
# El código lo separaremos en diferentes programas. 
# Tendremos programas con métodos con ejecución/llamadas de dichos métodos
# También podremos tener un mismo programa, métodos y también la parte principal de la ejecución
# Por un lado nuestro programa principal es Python, será el mail
####### NUestro programa en Python (MAIN)
# print("Validación de email")
# print("Dame un email")
# email=input()
#LLamada a un método o función (en lugar de los if, elif.....)
# me lo invento: validaremail()
###### En otro lugar de nuestro CODIGO/FICHERO
# En otro lugar tendremos la llamada:
# # validaremail(emailrecibido):
# # #Aquí Comprobamos las cosas
# En python para declarar métodos se utiliza la palabra clave def y a continuación el nombre del método.
# Los métodos pueden estar en el mismo fichero o en otro
# Si están en el mismo lo primero que se escriben son dichos métodos.
# Los métodos o funciones pueden recibir parámetros
# (el email recibido es un parámetro.)
####################### SINTAXIS ##################################
# Si voy a poner los métodos en el mismo fichero, lo primero los métodos
# La sintaxis de los métodos se escriben con la segunda inicial y siguientes en mayúscula
# primer()
# primerMetodo()
# Declaración del método
def primerMetodo():
    # Este código jamás se ejecuta
    print("Primer metodo")
def segundoMetodo():
    # Este código jamás se ejecuta
    print("Segundo metodo")
print("Ejemplo de métodos")
# ahora si se ejecuta solo ejecutará el print, a no ser que lo llamemos
#  Para llamarlo solo se le llama
primerMetodo()
segundoMetodo()
print("Fin del programa")
## # # # # # #  Parámetros en los métodos # # # # # # # # # # # 
#  Un método puede recibir parámetros, info que necesita el método para poder ser ejecutado.
#  Se reciben dentro de los parámetros, si recibimos más de uno, irán separados por comas
#  Las variables que enviamos y las que declaramos NO tienen que coincidir, son distintos nombres.
#  Los parámetros solamente se pueden utilizar dentro del método.
# Creamos un nuevo programa.

#  Los métodos los podemos dividir en 2 grupos
#Los métodos de acción: ejecutan una serie de acciones
# Los métodos return: ejecutan una serie de acciones y devuelven un valor después de ejecutar dichas acciones
#  Método de acción: print() (hace algo)
#  Método de return: len(). (devuelve algo)



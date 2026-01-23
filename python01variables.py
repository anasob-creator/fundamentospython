# Comentarios en Python
# Option derecha + 3
# Dibujar por pantalla es ocn string/texto
print("mi primer python")
# Cada instrucción en una línea
# Si queremos declarar variables: simplemente nos inventamos un nombre
nombre="Paco"
numero=14
numero="catorce"
print (nombre)
print (numero)
#podemos representar variables junto al texto literal
print("su nombre es " + nombre)
print ("su nombre es ",numero)
# Las variables tienen un tipo de dato interno (número, string....) que se establece en el momento de asignar un valor, y dependiendo del tipo podrán realizar unas acciones u otras
# Una variable de tipo número (int, float... puede realizar operaciones matemáticas, por lo que tenemos operadores matemáticos
# El símbolo más suma, pero también hay un Concatenar para sumar dos textos, pero también sirve para sumar
# si concatenamos un texto con un número usando el +
print("su número es "+numero)
# tenemos 3 tipos de errores
# 1. Errores de compilación, escribimos mal 
# 2. Errores en ejecución, está bien escrito pero no hemos tenido en cuenta algo de nuestro código y nos falla al ejecutar
# 3. Errores lógicos. Todo está bien escrito, todo funciona, no nos da error, pero el programa no ejecuta lo que queremos.
############ Conversiones: Funciones ############
# str (valor): convierte un valor a string
# int(string): convierte un texto a int (si el texto no es numérico no funcionará)
# float(string): convierte un texto a decimal
nombre="Paco"
numero=14
numero2="6"
suma=numero+int(numero2)
print(suma)
# operadores
numero=14
numero2=6
suma=numero+numero2
resta=numero-numero2
multi=numero*numero2
divide=numero/numero2
print ("Suma: ", suma)
print ("Resta: ", resta)
print ("División: ", divide)
print ("Multiplica: ", multi)
####### Pedir información al usuario
# Utilización de valore estáticos dentro de la svariables. 
# Para preguntar al usuario y que nos de un valor para nuestro programa se utiliza input() y se almacena en string
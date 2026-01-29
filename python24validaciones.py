# programa main validaciones
# Tendremos un métdodo qu eserá validar el isbn tru/false
# 2. un método que recibirá el número de dni y nos devolverá la letra
# 3. Tendremos un met. que nos dirá si un dni es correcto. Enviaremos todo el DNI: 12344555X y nos dirá si es true o false.
# programa main
from libreria24validaciones import validarDni
print("Programa de validaciones")
print("Encuentra la letra del DNI")
print("Dame tu número del DNI")
dni=int(input())
validarDni()
print("Fin del progrma")

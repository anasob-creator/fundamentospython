from class31coche import Coche
from class31deportivo import Deportivo
print("Conduciendo...")
car=Coche()
print("Vel. Max:", car.getVelocidadMaxima())
depor=Deportivo()
print("Vel. Max:", depor.getVelocidadMaxima())
depor.arrancar()
depor.acelerar()
depor.turbo()
car.marca="Pontiac"
car.modelo="Firebird"
print(car.marca+" "+car.modelo)
car.arrancar()
car.acelerar()
car.acelerar()
car.acelerar()
car.frenar()

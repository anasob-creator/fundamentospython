from class31coche import Coche

class Deportivo(Coche):
    def turbo(self):
        self.velocidad+=100
        print("Turbo a tope!!!", self.velocidad)
    def acelerar(self):
        self.velocidad+=45
        print("Aceleranto en deportivo!! ", self.velocidad)
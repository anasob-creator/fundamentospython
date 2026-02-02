class Coche:
    # Declaramos las propiedades en el constructor
    def __init__(self):
        self.marca=""
        self.modelo=""
        self.velocidad=0
        self.estado=False
    
    def arrancar(self):
        self.estado=True
        print("Coche arrancado")

    def getVelocidadMaxima(self):
        return 180

    def detener(self):
        self.estado=False
        self.velocidad=0
        print("Coche parado")

    def acelerar(self):
        if(self.estado == False):
            print("El coche está parado. Debe arrancar antes")
        else:
            self.velocidad=self.velocidad + 20
            print("Su velocidad es de ",self.velocidad)

    def frenar(self):
        if(self.velocidad == 0):
            print("Si ya estás parado...")
        else:
            self.velocidad=self.velocidad - 10
            print("Su velocidad es de ", self.velocidad)
class Mascota:
    #Declaramos las propiedades en el constructor
    def __init__(self):
        self.nombre = ""
        self.raza = ""
        self.anyoNacimiento = 0
        self.anyoAdopcion=0
    
    def getAnyosAdoptada(self):
        anyoadopcion=(self.anyoAdopcion-self.anyoNacimiento)
        return anyoadopcion
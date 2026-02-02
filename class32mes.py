class Mes:
    #Declaramos las propiedades en el constructor
    def __init__(self):
        self.nombre = ""
        self.temperaturaMinima = 0
        self.temperaturaMaxima = 0
    
    def getTemperaturaMedia(self):
        media=(self.temperaturaMaxima+self.temperaturaMinima)/2
        return media
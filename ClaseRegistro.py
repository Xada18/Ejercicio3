class Registro:
    __temperatura = 0.0
    __humedad = 0.0
    __presion = 0.0

    def __init__(self, temp, hume, pres):
        self.__temperatura = float(temp)
        self.__humedad = float(hume)
        self.__presion = float(pres)

    
    
    def getTemperatura(self):
        return self.__temperatura
    
    def getHumedad(self):
        return self.__humedad
    
    def getPresion(self):
        return self.__presion
    

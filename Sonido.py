class Sonido:
    def __init__(self,velocidad):
        self.setVelocidad(velocidad)

    def devuelveRetrasoCalculado(self,distancia):
        """
        OBJ: devuelve tiempo en segundos
        PRE: distancia>0 en metros
        """
        return distancia/self.getVelocidad()

    #def devuelveFrecuenciaCalculada(self,
    #                                frecuencia):
                
    def setVelocidad(self,velocidad):
        """
        PRE: velocidad en metros por segundo
        """
        self.velocidad=velocidad

    def getVelocidad(self):
        """
        OBJ: devuelve velocidad en metros por
             segundo
        """
        return self.velocidad

    def toString(self):
        return "{Sonido: velocidad="+\
               str(self.getVelocidad())+" m/s}"

"""
#PROBADOR
velocidadSonidoAire=340 #mps
velocidadSonidoVacio=0
velocidadSonidoAgua=1400 #4*aire
distancia=1000 #m
sonido=Sonido(velocidadSonidoAire)
print(round(sonido.devuelveRetrasoCalculado(\
      distancia),2),"debe ser 2.94 s")
print(sonido.toString())
"""

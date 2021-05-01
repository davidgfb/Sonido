class Frecuencia:
    def __init__(self,valor):
        self.setValor(valor)

    def devuelveLongitudOndaCalculada(self,
                                      velocidad):
        return velocidad.getValor()/self.getValor()#self.getVelocidad

    def setValor(self,valor):
        """PRE: valor en herzios"""
        self.valor=valor

    def getValor(self):
        """OBJ: devuelve valor en herzios"""
        return self.valor

    def toString(self):
        return "{Frecuencia: valor="+\
               str(self.getValor())+" hz}"

"""
#PROBADOR
from Velocidad import Velocidad
velocidad=Velocidad(340)
frecuencia=Frecuencia(20)
print(frecuencia.devuelveLongitudOndaCalculada(\
      velocidad),"debe ser 17 metros")
print(frecuencia.toString())
"""

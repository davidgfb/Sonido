class Velocidad:
    def __init__(self,valor):
        self.setValor(valor)

    def setValor(self,valor):
        """PRE: valor deben ser metros por segundo"""
        self.valor=valor

    def getValor(self):
        """OBJ: devuelve valor en metros por segundo"""
        return self.valor

    def toString(self):
        return "{Velocidad: valor="+\
               str(self.getValor())+" m/s}"

'''
#PROBADOR
velocidad=Velocidad(340)
print(velocidad.toString())
'''

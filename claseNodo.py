class Nodo:
    __vehiclo=None
    __siguiente=None


    def __init__(self,vehiculo):
        self.__vehiclo=vehiculo
        self.__siguiente=None


    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente


    def getDato(self):
        return self.__vehiclo


    def hola(self):
        print("hola")


    def __gt__(self, other):
        vehiculo=other.getDato()
        valor=True
        print("estoy dentro de gt")
        if (int(self.__vehiclo.calcularImporte())>int(vehiculo.calcularImporte())):
            print("valor {}".format(valor))
            return valor
        else:
            valor=False
            print("valor {}".format(valor))
            return valor



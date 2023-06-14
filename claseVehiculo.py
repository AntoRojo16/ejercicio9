
import json
class Vehiculo:
    __modelo=""
    __cantPuertas=0
    __color=""
    __precioBase=0



    def __init__(self,modelo,cant,color,precio):
        self.__modelo=modelo
        self.__cantPuertas=cant
        self.__color=color
        self.__precioBase=precio




    def calcularImporte(self):
        pass

    def getCantidadPuertas(self):
        return self.__cantPuertas


    def getColor(self):
        return self.__color

    def getModelo(self):
        return self.__modelo

    def getPrecioBase(self):
        return int(self.__precioBase)


    def modificarP(self, precio):
        self.__precioBase=precio


    def mostrar(self):
        print("Modelo {}, cantidad de puertas {}, color {}, precion base {}".format(self.__modelo,self.__cantPuertas,self.__color,self.__precioBase))


    def mostrarEjercicio(self):
        print("Modelo: {}, Cantidad: {}".format(self.__modelo,self.__cantPuertas))


    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=self.__modelo,
                cantidadPuertas=self.__cantPuertas,
                color=self.__color,
                precioBase=self.__precioBase

            )
        )
        return d

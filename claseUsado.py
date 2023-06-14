from claseVehiculo import Vehiculo


class Usado(Vehiculo):
    __marca=""
    __patente=""
    __año=0
    __kilometraje=0



    def __init__(self,modelo,cant,color,precio,marca,patente,año,kilometraje):
        super().__init__(modelo,cant,color,precio)
        self.__marca=marca
        self.__patente=patente
        self.__año=año
        self.__kilometraje=kilometraje



    def calcularImporte(self):
        año=2023
        calculo=año-int(self.__año)
        porcentaje=(super().getPrecioBase()*calculo)/100
        calculo2=0
        if self.__kilometraje>200000:
            calculo2=(super().getPrecioBase()*2)/100

        impore=super().getPrecioBase()-porcentaje-calculo2
        return impore


    def mostrar(self):
        super().mostrar()
        print("Marca {}, patente {}, año {}, kilometraje {}".format(self.__marca,self.__patente,self.__año,self.__kilometraje))
        print("suimporte es {}".format(self.calcularImporte()))
    def getPatente(self):
        return self.__patente

    def modificarPrecio(self):
        precio=input("Ingrese el nuevo precio del vehiculo {}".format(self.__marca))
        super().modificarP(precio)

    def mostrarEjercicio(self):
        super().mostrarEjercicio()
        print("El importe de venta es: {}".format(self.calcularImporte()))


    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo=super().getModelo(),
                cantidadPuertas=super().getCantidadPuertas(),
                color=super().getColor(),
                precioBase=super().getPrecioBase(),
                marca=self.__marca,
                patente=self.__patente,
                año=self.__año,
                kilometraje=self.__kilometraje
            )
        )

        return d




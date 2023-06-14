from claseVehiculo import Vehiculo

class Nuevo(Vehiculo):
    __version=""
    marca="Ford"


    def __init__(self,modelo,cant,color,precio,version):
        super().__init__(modelo,cant,color,precio)
        self.__version=version


    @classmethod
    def getMarca(cls):
        return cls.marca



    def calcularImporte(self):
        calculo=(super().getPrecioBase()*10)/100
        calculo2=0
        if self.__version=="full":
            calculo2=(super().getPrecioBase()*2)/100
        importe=super().getPrecioBase()+calculo+calculo2

        return importe


    def mostrar(self):
        super().mostrar()
        print("Version {}, marca {} ".format(self.__version,self.getMarca()))
        print("suimporte es {}".format(self.calcularImporte()))

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
                version=self.__version,
                marca=self.getMarca()
            )
        )

        return d




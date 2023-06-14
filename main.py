from claseColeccionVehiculos import Coleccion
from claseDecodificador import ObjetEncoder
import json
from claseVehiculo import Vehiculo
from claseNuevo import Nuevo
from claseUsado import Usado
if __name__=="__main__":
    unVehiculoUsado=Usado("Focus",4,"rojo",2000000,"ford","123ale",2011,5000)
    unVehiculoNuevo=Nuevo("Palio",3,"negro mate",30000000,"base")
    VehiculoUsado=Usado("Seat Leon",4,"azul",2000000,"Volkswagen ","156ale",2015,10000)
    unVehiculo=Usado("Sun",4,"azul",2000000,"Volkswagen ","156ale",2015,10000)
    unUsado=Usado("Leon",4,"azul",2000000,"Volkswagen ","156ale",2015,10000)
    listaVehiculos=Coleccion()
    listaVehiculos.agregarVehiculo(VehiculoUsado)
    listaVehiculos.agregarVehiculo(unUsado)
    listaVehiculos.agregarVehiculo(unVehiculo)
    listaVehiculos.agregarVehiculo(unVehiculoUsado)
    listaVehiculos.insertarElemento(unVehiculoNuevo)
    print("######datos ingresados########")
    listaVehiculos.mostrarDatos()
    #listaVehiculos.mostrarElemento()
    #listaVehiculos.modificarPrecioBase()
    listaVehiculos.mostrarVehiculomasEconomico()
    print("todos los vehiculos son")
    listaVehiculos.mostrarTodos()
    json=ObjetEncoder()
    diccionario=listaVehiculos.toJSON()
    json.guardarJSONarchivo(diccionario,"DatosVehiculos.json")




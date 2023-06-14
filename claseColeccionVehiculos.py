from claseNodo import Nodo
from claseinterfaz import Interfaz
from claseNuevo import Nuevo
from claseUsado import Usado
import json
import os
from zope.interface import implementer
@implementer(Interfaz)
class Coleccion:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0



    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def getTope(self):
        return self.__tope


    def agregarVehiculo(self,vehiculo):
        try:

            if type(vehiculo)==Nuevo or type(vehiculo)==Usado:#podria preguntar si es de clase vehiculo directamente?
                unNodo=Nodo(vehiculo)
                if self.__comienzo==None:
                    unNodo.setSiguiente(self.__comienzo)
                    self.__comienzo=unNodo
                    self.__actual=unNodo
                    self.__tope+=1
                else:
                    aux=self.__comienzo
                    siguiente=self.__comienzo.getSiguiente()
                    while(siguiente!=None):
                        aux=siguiente
                        siguiente=aux.getSiguiente()
                    unNodo.setSiguiente(siguiente)
                    aux.setSiguiente(unNodo)
                    self.__tope+=1
            else: 
                raise TypeError
        except TypeError:
            print("No es una clase de tipo vehiculo")

    def insertarElemento(self,vehiculo):
        posicion=int(input("ingrese la posicion en la que desea agregar el vehiculo"))
        print(self.__tope)
        print(posicion-1)
        try:
            if (posicion>=0) and (posicion<=self.__tope):
                unNodo=Nodo(vehiculo)
                if posicion==0:
                    unNodo.setSiguiente(self.__comienzo)
                    self.__comienzo=unNodo
                    self.__tope+=1
                else:
                    cont=1
                    aux=self.__comienzo
                    siguiente=aux.getSiguiente()
                    while(siguiente!=None)and(cont!=posicion):
                        aux=siguiente
                        siguiente=aux.getSiguiente()
                        cont+=1
                    if cont==posicion:
                        unNodo.setSiguiente(siguiente)
                        aux.setSiguiente(unNodo)
                        self.__tope+=1
            else:
                raise IndexError
        except IndexError:
            print("Error:  se ingreso un numero menor que 0 o el valor ingresado supera la cantidad de datos almacenados en la coleccion")



    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def mostrarDatos(self):
        aux=self.__comienzo
        while(aux!=None):
            aux.getDato().mostrar()
            if type(aux)==Nuevo:
                aux.getDato().getMarca()
            aux=aux.getSiguiente()

    def mostrarElemento(self):
        posicion=int(input("ingrese la posicion de el elemento que desea mostrar"))
        cont=0
        aux=self.__comienzo
        #siguiente=aux.getSiguiente()
        #while cont!=posicion and siguiente!=None:
        while (cont!=posicion) and (aux!=None):
            aux=aux.getSiguiente()
        #    aux=siguiente
        #    siguiente=siguiente.getSiguiente()
            cont+=1
        if posicion==cont:
            aux.getDato().mostrar()


    def modificarPrecioBase(self):
        patente=input("ingrese la patente del vehiculo usado")
        band=False
        aux=self.__comienzo
        #siguiente=aux.getSiguiente()
        while(band==False)and(aux!=None):
            aux.getDato().mostrar()
            if type(aux.getDato())==Usado:
                if (aux.getDato().getPatente()==patente):
                    band=True
                else:
                    aux=aux.getSiguiente()
            else:
                aux=aux.getSiguiente()
        if band==True:
            aux.getDato().modificarPrecio()
            print("su importe es {}" .format(aux.getDato().calcularImporte()))


    def mostrarVehiculomasEconomico(self):
        aux=None
        minimo=100000000000000000
        for vehiculo in self:
            valor=vehiculo.calcularImporte()
            print("el valor de importe {}".format(valor))
            if int(valor) <minimo:
                minimo=valor
                aux=vehiculo
                print("hola")
        print("los datos del vehiculo con menor importe es:")
        (aux.mostrar())

    def mostrarTodos (self):
        for vehiculo in self:
            vehiculo.mostrarEjercicio()

    def toJSON(self):
        vehiculos=[]
        for v in self:
            vehiculos.append(v.toJSON())
        dic=dict(__class__=self.__class__.__name__,datos=vehiculos)
        return dic







                    




    

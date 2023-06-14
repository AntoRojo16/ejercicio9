import json
from pathlib import Path
class ObjetEncoder(object):
    def decodificarDiccionario(self,d):
        if "__calss__"not in d:
            return d
        else:
            class_name=d=["__class__"]
            class_=eval(class_name)
            if class_name=="Coleccion":
                vehiculos=d["vehiculo"]
                coleccion=class_()
                for i in range(len(vehiculos)):
                    dVehiculo=vehiculos[i]
                    class_name=dVehiculo.pop('__class__')
                    class_=eval(class_name)
                    atributos=dVehiculo['__atributos__']
                    unVehiculo=class_(**atributos)
                    coleccion.agregarVehiculo(unVehiculo)
        return coleccion



    def guardarJSONarchivo(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="utf-8")as destino:
            json.dump(diccionario,destino,ident=4)
            destino.close()

    def leerArchivoJSON(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario

    def convertirTextoADiccinario(self,texto):
        return json.loads(texto)


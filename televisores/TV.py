class TV:
    numTV = 0
    def __init__(self, marca, estado:bool):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        self.__control = None   ##Con NONE se puede asignar despues el valor
        TV.numTV += 1
#### Marca
    def getterMarca(self):
        return self.__marca

    def setterMarca(self, new_marca):
        self.__marca = new_marca
####canal
    def getterCanal(self):
        return self.__canal

    def setterCanal(self, new_canal):
        self.__canal = new_canal
####precio
    def getterPrecio(self):
        return self.__precio

    def setterPrecio(self, new_precio):
        self.__precio = new_precio
####    volumen
    def getterVolumen(self):
        return self.__volumen

    def setterVolumen(self, new_volumen):
        self.__volumen = new_volumen
####    control
    def getterControl(self):
        return self.__control
    
    def setterControl(self, new_control):
        self.__control = new_control
    
    @classmethod
    def conteo_numTV(cls):
        return cls.numTV
    def getEstado(self):
        return self.__estado


    def turnOn(self):
        if self.__estado is False:
            self.__estado = True
        else:
            self.__estado = True

    def turnOff(self):
        if self.__estado is True:
            self.__estado = False
        else:
            self.__estado = False
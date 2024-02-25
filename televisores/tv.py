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
    def getMarca(self):
        return self.__marca

    def setMarca(self, new_marca):
        self.__marca = new_marca
####canal
    def getCanal(self):
        return self.__canal

    def setCanal(self, new_canal):
        self.__canal = new_canal
####precio
    def getPrecio(self):
        return self.__precio

    def setPrecio(self, new_precio):
        self.__precio = new_precio
####    volumen
    def getVolumen(self):
        return self.__volumen

    def setVolumen(self, new_volumen):
        self.__volumen = new_volumen
####    control
    def getControl(self):
        return self.__control
    
    def setControl(self, new_control):
        self.__control = new_control
    
    @classmethod
    def setNumTV(cls, numero):
         cls.numTV = numero
    @classmethod
    def getNumTv(cls):
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

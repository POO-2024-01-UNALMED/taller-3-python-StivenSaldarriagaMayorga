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
        if (self.__estado is True and 1 < new_canal <= 120):
            self.__canal = new_canal
####precio
    def getPrecio(self):
        return self.__precio

    def setPrecio(self, new_precio):
        self.__precio = new_precio
####    volumen
    
    @classmethod
    def setNumTV(cls, numero):
         cls.numTV = numero
    @classmethod
    def getNumTV(cls):
        return cls.numTV

    def getEstado(self):
        return self.__estado

##############################################################################
    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def canalUp(self):
        if self.__estado and self.__canal < 120:
            self.__canal += 1

    def canalDown(self):
        if self.__estado and self.__canal > 1:
            self.__canal -= 1

    def volumenUp(self):
        if self.__estado and self.__volumen <= 7:
            self.__volumen += 1
    
    def volumenDown(self):
        if self.__estado and self.__volumen > 0:
            self.__volumen -= 1

    def getVolumen(self):
        return self.__volumen

    def setVolumen(self, volumen):
        if 0 <= volumen <= 7 and self.__estado:
            self.__volumen = volumen
####    control
    def getControl(self):
        return self.__control
    
    def setControl(self, new_control):
        self.__control = new_control
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
###Get
    def getEstado(self):
        return self.__estado

    def getControl(self):
        return self.__control
    
    def getMarca(self):
        return self.__marca

    def getPrecio(self):
        return self.__precio

    def getCanal(self):
        return self.__canal

    def getVolumen(self):
        return self.__volumen
##set

    
    @classmethod
    def setNumTV(cls, numero):
         cls.numTV = numero
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    def setCanal(self, new_canal):
        if self.__estado is True and 1 < new_canal <= 120:
            self.__canal = new_canal

    def setPrecio(self, new_precio):
        self.__precio = new_precio

    def setControl(self, new_control):
        self.__control = new_control

    def setVolumen(self, volumen):
        if 0 <= volumen <= 7 and self.__estado is True:
            self.__volumen = volumen

    def setMarca(self, new_marca):
        self.__marca = new_marca
##############################################################################
    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def canalUp(self):
        if self.__estado and self.__canal < 120 and self.__canal >= 1:
            self.__canal += 1

    def canalDown(self):
        if self.__estado and self.__canal > 1 and self.__canal <= 120:
            self.__canal -= 1

    def volumenUp(self):
        if self.__estado is True and self.__volumen < 7 and self.__volumen >= 0:
            self.__volumen += 1
    
    def volumenDown(self):
        if self.__estado is True and self.__volumen > 0 and self.__volumen <= 7:
            self.__volumen -= 1

####    control
    
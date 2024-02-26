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
    def getNumTV(cls):
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

    def canalDown(self):
        self.__tv = self.__tv.getCanal -1
        while 1 <= self.__tv.canal <=120:
            if self.__tv.estado is True:
                self.__tv.canal += 1
    
    def canalUp(self):
        while 1 <= self.__tv.canal <=120:
            if self.__tv.estado is True:
                self.__tv.canal += 1

    def volumenUp(self):
         while 0 <= self.__tv.volumen <= 7:  
            if self.__tv.estado is True:
                self.__tv.volumen += 1
            else:
                print("Está apagado")
    
    def volumenDown(self):
         while 0 <= self.__tv.volumen <= 7:  
            if self.__tv.estado is True:
                self.__tv.volumen -= 1
            else:
                print("Está apagado")
   
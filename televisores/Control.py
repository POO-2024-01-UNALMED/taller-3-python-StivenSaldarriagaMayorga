from televisores import *

class Control:
    def __init__(self, tv):
        self.__tv=tv

    @property
    def tv(self):
        return self.__tv
    @tv.setter
    def tv(self, new_tv):
        self.__tv = new_tv
    
    def canalUp(self):
        while 1 <= self.__tv.canal <=120:
            if self.__tv.estado is True:
                self.__tv.canal += 1
            else:
                print("Está apagado")

    def canalDown(self):
        while 1 <= self.__tv.control <=120: 
            if self.__tv.estado is True:
                self.__tv.control -= 1
            else:
                print("Está apagado")

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

    def enlazar(self, tv):
        if self.__tv is not None:
            self.__tv.control = None
        
        self.__tv = tv

        if tv is not None:
            tv.control = self
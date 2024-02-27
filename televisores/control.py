from televisores.tv import *

class Control:
    def __init__(self):
        self.__tv=None


    def enlazar(self, tv:TV):
        self.__tv = tv
        tv.setControl(self)

    def getTv(self):
        return self.__tv

    def setTv(self, new_tv):
        self.__tv = new_tv

#############################################################
    def canalDown(self):
       if self.__tv:
            self.__tv.canalDown()
    
    def canalUp(self):
        if self.__tv:
            self.__tv.canalUp()

    def volumenUp(self):
         if self.__tv:
            self.__tv.volumenUp()
    
    def volumenDown(self):
         if self.__tv:
            self.__tv.volumenDown()
   
    def getCanal(self):
        self.__tv.getCanal()

    def setCanal(self, new_canal):
        if self.__tv:
            self.__tv.setCanal(new_canal)

    def getVolumen(self):
        self.__tv.getVolumen()

    def setVolumen(self, new_volumen):
        self.__tv.setVolumen(new_volumen)

    def turnOff(self):
        if self.__tv:
            self.__tv.turnOff()

    def turnOn(self):
        if self.__tv:
            self.__tv.turnOff()

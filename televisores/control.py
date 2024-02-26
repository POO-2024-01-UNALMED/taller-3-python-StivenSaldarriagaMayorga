from televisores.tv import *

class Control:
    def __init__(self, tv=TV):
        self.__tv=tv

    def enlazar(self, tv:TV):
        self.__tv = tv
        tv.setControl(self)

    def getTv(self):
        return self.__tv

    def setTv(self, new_tv):
        self.__tv = new_tv

#############################################################
    def canalDown(self):
        self.__tv.canalDown()
    
    def canalUp(self):
        self.__tv.canalUp()

    def volumenUp(self):
         self.__tv.canalDown()
    
    def volumenDown(self):
         self.__tv.canalDown()
   
    def getCanal(self):
        self.__tv.getCanal()

    def setCanal(self, new_canal):
        self.__tv.setCanal(new_canal)

    def getVolumen(self):
        self.__tv.getVolumen()

    def setVolumen(self, new_volumen):
        self.__tv.setVolumen(new_volumen)



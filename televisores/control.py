
class Control:
    def __init__(self, tv=None):
        self.__tv=tv


    def getTv(self):
        return self.__tv

    def setTv(self, new_tv):
        self.__tv = new_tv
    
    def canalDown(self):
        self.__tv.setCanal()
        
    def canalUp(self):
        while 1 <= self.__tv.canal <=120:
            if self.__tv.estado is True:
                self.__tv.canal += 1
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
        self.__tv = tv
        tv.setControl(self)

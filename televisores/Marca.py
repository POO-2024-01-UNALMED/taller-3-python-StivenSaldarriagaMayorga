
class marca:
    def __init__(self, nombre:str):
        self.__nombre = nombre

    @property
    def getterNombre(self):
        return self.__nombre

    def setterNombre(self, new_nombre):
        self.__nombre = new_nombre

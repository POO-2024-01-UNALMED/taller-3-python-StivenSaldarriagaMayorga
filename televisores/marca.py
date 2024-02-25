
class Marca:
    def __init__(self, nombre:str):
        self.__nombre = nombre

    @property
    def getNombre(self):
        return self.__nombre

    def setNombre(self, new_nombre):
        self.__nombre = new_nombre

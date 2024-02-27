class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.control = None

        TV.numTV += 1

    # Métodos get
    def get_marca(self):
        return self.marca

    def get_canal(self):
        return self.canal

    def get_precio(self):
        return self.precio

    def get_volumen(self):
        return self.volumen

    def get_control(self):
        return self.control

    def get_estado(self):
        return self.estado

    @staticmethod
    def get_num_tv():
        return TV.numTV

    # Métodos set
    def set_marca(self, marca):
        self.marca = marca

    def set_canal(self, canal):
        if self.estado:
            if 1 <= canal <= 120:
                self.canal = canal

    def set_volumen(self, volumen):
        if self.estado:
            if 0 <= volumen <= 7:
                self.volumen = volumen

    def set_precio(self, precio):
        self.precio = precio

    def set_control(self, control):
        self.control = control

    @staticmethod
    def set_num_tv(num_tv):
        TV.numTV = num_tv

    # Métodos controladores
    def turn_off(self):
        self.estado = False

    def turn_on(self):
        self.estado = True

    def canal_up(self):
        if self.estado and self.canal < 120:
            self.canal += 1

    def canal_down(self):
        if self.estado and self.canal > 1:
            self.canal -= 1

    def volumen_down(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1

    def volumen_up(self):
        if self.estado and self.volumen < 7:
            self.volumen += 1
####    control
    
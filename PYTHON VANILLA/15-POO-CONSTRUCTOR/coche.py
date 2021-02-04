class Coche:

    color = ""
    marca = ""
    modelo = ""
    velocidad = 0
    caballaje = 0
    plazas = 0
    __precio = 0

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas, precio):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje =caballaje
        self.plazas = plazas
        self.__precio = precio

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getVelocidad(self):
        return self.velocidad

    def setCaballaje(self, caballaje):
        self.caballaje = caballaje

    def getCaballaje(self):
        return self.caballaje

    def setPlazas(self, plazas):
        self.plazas = plazas

    def getPlazas(self):
        return self.plazas

    def setPrecio(self, precio):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "---- Información del Coche ----"
        info += f"\n Marca: {self.getMarca()}"
        info += f"\n Modelo: {self.getModelo()}"
        info += f"\n Color: {self.getColor()}"
        info += f"\n Plazas: {self.getPlazas()}"
        info += f"\n Caballaje: {self.getCaballaje()}"
        info += f"\n Velocidad Máxima: {self.getVelocidad()}"
        info += f"\n Precio: {self.getPrecio()}€"
        info += "\n ---- ---- ---- ---- ---- ----"
        return info

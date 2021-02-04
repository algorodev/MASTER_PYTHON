"""
    Una clase es un molde para crear más objetos con las mismas características
"""

# DEFINIR UNA CLASE
class Coche:
    # PROPIEDADES -> CARACTERISTICAS DE LA CLASE
    color = "Rojo"
    marca = "Ferrari"
    modelo = "F-50"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # METODOS -> ACCIONES QUE HACE EL OBJETO
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

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# CREAR OBJETO -> INSTANCIAR CLASE
coche = Coche()

coche.setColor("Amarillo")
coche.setMarca("Lamborghini")
coche.setModelo("Aventador")
print(coche.marca, coche.modelo, coche.color)

print("Velocidad actual: ", coche.getVelocidad(), "km/h")
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()
print("Velocidad actual: ", coche.getVelocidad(), "km/h")

print("--------------------------------")

coche2 = Coche()

coche2.setColor("Azul")
coche2.setMarca("Volkswagen")
coche2.setModelo("Golf")
print(coche2.marca, coche2.modelo, coche2.color)

print("Velocidad actual: ", coche2.getVelocidad(), "km/h")
coche2.acelerar()
coche2.acelerar()
coche2.acelerar()
coche2.frenar()
print("Velocidad actual: ", coche2.getVelocidad(), "km/h")

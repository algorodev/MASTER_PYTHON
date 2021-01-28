# Tipo de dato que no tiene nada
nada = None
print(nada)
# NoneType
print(type(nada))

# Tipo de dato que contiene una cadena
cadena = "Hola, ¿que tal?"
print(cadena)
# str
print(type(cadena))

# Tipo de dato que contiene un entero
entero = 1997
print(entero)
# int
print(type(entero))

# Tipo de dato que contiene un número de coma flotante
flotante = 19.97
print(flotante)
# float
print(type(flotante))

# Tipo de dato que contiene un booleano
booleano = True
print(booleano)
# bool
print(type(booleano))

# Tipo de dato que contiene una matriz
lista = [10, "veinte", 30, "cuarenta"]
print(lista)
# list
print(type(lista))

# Tipo de dato que contiene una matriz que sus valores no cambian
tupla = ("master", "en", "python")
print(tupla)
# tuple
print(type(tupla))

# Tipo de dato que contiene una colección de datos de clave-valor
diccionario = {
    "nombre": "Alejandro",
    "apellido": "González",
    "edad": 23
}
print(diccionario)
# dict
print(type(diccionario))

# Tipo de dato que contiene rangos
rango = range(99)
print(rango)
# range
print(type(rango))


# CONVERTIR DATOS
numero = 1997
# 1997
numero = str(1997)
# "1997"
numero = float(1997)
# 1997.0

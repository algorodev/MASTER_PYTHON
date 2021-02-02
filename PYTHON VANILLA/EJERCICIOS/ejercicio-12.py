"""
    EJERCICO 12
        Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y por último
        mostrarla. Usar while y for
"""

# MI SOLUCIÓN
numeros = []

for contador in range(0, 120):
    numeros.append(contador)
print(numeros)

while len(numeros) < 120:
    numeros.append(contador)
print(numeros)

# SOLUCIÓN DEL PROFESOR
coleccion = []

for contador in range(0, 120):
    coleccion.append(f"elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])
print(coleccion)

x = 0

while x < 120:
    coleccion.append(f"elemento-{x}")
    print("Mostrando el: " + coleccion[x])
    x += 1
print(coleccion)
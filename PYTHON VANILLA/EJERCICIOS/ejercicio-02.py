"""
 Ejercicio 2
    Escribir un script que nos muestre por pantalla todos los números pares del 1 al 120
"""

# MI SOLUCIÓN
contador = 0

while contador <= 120:
    print(f"Número: {contador}")
    contador += 2

# SOLUCIÓN DEL PROFESOR
contador = 1

for contador in range(0, 121):
    if contador % 2 == 0:
        print(contador)

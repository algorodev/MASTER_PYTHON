"""
 Ejercicio 3
    - Escribir un script que muestre los cuadrados de los 60 primeros números naturales.
    - Resolverlo con FOR
    - Resolverlo con WHILE
"""

# MI SOLUCIÓN CON WHILE
contador = 0

while contador <= 60:
    print(f"El cuadrado de {contador} = {contador * contador}")
    contador += 1

# SOLUCIÓN DEL PROFESOR CON WHILE
contador = 0

while contador <= 60:
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1

# MI SOLUCIÓN CON FOR
for numero in range(0, 61):
    print(f"El cuadrado de {numero} = {numero * numero}")

# SOLUCIÓN DEL PROFESOR CON FOR
for numero in range(0, 61):
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")
"""
 Ejercicio 9
    Escribir un script que pida indefinidamente numeros al usuario hasta que acierte el número, en este caso el 111
"""

# MI SOLUCIÓN
contador = 1

while contador < 100:
    numero = int(input("Introduce un número: "))
    if numero == 111:
        print("Acertaste el número!!")
        break
    else:
        print(f"{numero} no es válido..")

# SOLUCIÓN DEL PROFESOR
contador = 1

while contador < 100:
    numero = int(input("Introduce un número: "))
    if numero == 111:
        break
    else:
        print(numero)
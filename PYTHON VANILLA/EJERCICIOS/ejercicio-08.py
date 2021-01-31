"""
 Ejercicio 8
    - Preguntar al usuario que número quiere y cuanto porcentaje del mismo quiere
    - Resolverlo
"""

# MI SOLUCIÓN
numero = int(input("Introduce el número: "))
porcentaje = int(input("¿Cuanto porcentaje quieres del número anterior?: "))

print(f"El {porcentaje}% de {numero} = {numero * (porcentaje / 100)}")

# SOLUCIÓN DEL PROFESOR
numero = int(input("Introduce el número: "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar de {numero}?: "))

operacion = (numero * (porcentaje / 100))
print(f"El {porcentaje}% de {numero} es: {operacion}")

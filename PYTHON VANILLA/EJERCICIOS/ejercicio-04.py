"""
 Ejercicio 4
    - Pedir dos números al usuario
    - Realizar todas las operaciones
    - Mostrarlas por pantalla
"""

# MI SOLUCIÓN
numero1 = int(input("¿Primer número?: "))
numero2 = int(input("¿Segundo número?: "))

print(f"La suma de {numero1} + {numero2} = {numero1 + numero2}")
print(f"La resta de {numero1} - {numero2} = {numero1 - numero2}")
print(f"La multiplicación de {numero1} x {numero2} = {numero1 * numero2}")
print(f"La división de {numero1} / {numero2} = {numero1 / numero2}")
print(f"El resto de {numero1} / {numero2} = {numero1 % numero2}")

# SOLUCIÓN DEL PROFESOR
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

print("#### CALCULADORA ####")
print("Suma: " + str(numero1 + numero2))
print("Resta: " + str(numero1 - numero2))
print("Multiplicación: " + str(numero1 * numero2))
print("División: " + str(numero1 / numero2))

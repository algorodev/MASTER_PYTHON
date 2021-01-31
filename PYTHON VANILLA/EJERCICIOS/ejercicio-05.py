"""
 Ejercicio 5
    Escribir un script que muestre todos los números entre el rango de número que diga el usuario
"""

# MI SOLUCIÓN
numero1 = int(input("Introduce el primer valor: "))
numero2 = int(input("Introduce el segundo valor: "))

if numero1 < numero2:
    for contador in range(numero1 + 1, numero2):
        print(f"-> {contador}")
else:
    print("Introduce otros valores")

# SOLUCIÓN DEL PROFESOR
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        print(contador)
else:
    print("El número 1 debe ser menor al número 2")
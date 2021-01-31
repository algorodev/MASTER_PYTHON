"""
 Ejercicio 7
    Escribir un script que nos muestre por pantalla todos los números impares entre el rango de números que decida el usuario
"""

# MI SOLUCIÓN
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 % 2 == 0:
    numero1 += 1
while numero1 <= numero2:
    print(f"Numeros impares: {numero1}")
    numero1 += 2

# SOLUCIÓN DEL PROFESOR
numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce el siguiente número: "))

if numero1 < numero2:
    for x in range(numero1, (numero2 + 1)):
        if x % 2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")
else:
    print("El primer número debe ser menor al segundo")

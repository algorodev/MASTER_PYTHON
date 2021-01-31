"""
while condicion:
    bloque de instrucciones
    actualizacion del contador
"""

contador = 1

while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador += 1

# EJEMPLO 1 --> TABLA MÚLTIPLICAR CON BUCLE WHILE
numero_usuario = int(input("Elige un número: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### TABLA DEL {numero_usuario} ###")

contador = 0
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1

"""
for variable in elemento_iterable
    bloque de instrucciones
"""

contador = 0
resultado = 0

for contador in range(0, 5):
    print(f"Voy por el número {contador}")
    resultado += contador
    print(f"El resultado de sumar todos los números es {resultado}")

# EJEMPLO 1 --> TABLA MÚLTIPLICAR CON BUCLE FOR
numero_usuario = int(input("Elige un número: "))
numero_tabla = 0

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de múltiplicar del número {numero_usuario} -->")

for numero_tabla in range(0, 11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print(f"Tabla del {numero_usuario} finalizada")

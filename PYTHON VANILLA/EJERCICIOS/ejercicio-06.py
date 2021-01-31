"""
 Ejercicio 6
    Escribir un script que devuelva todas las tablas de multiplicar del 1 al 10
"""

# MI SOLUCIÓN
for numero in range(1, 11):
    print(f"### TABLA DE MULTIPLICAR DEL {numero} ###")
    for numero_multiplicador in range(1, 11):
        print(f"{numero} x {numero_multiplicador} = {numero * numero_multiplicador}")

# SOLUCIÓN DEL PROFESOR
for cabecera in range(1, 11):
    print("##########################")
    print(f"###### Tabla del {cabecera} ######")
    print("##########################")
    for numero in range(1, 11):
        print(f"{numero} x {cabecera} = {numero * cabecera}")
    print("\n")

"""
    EJERCICIO 13
        Programa que compruebe si una variable esta vacia y si esta vacia, rellenarla con texto en minusculas
        y mostrarla en mayusculas
"""

# MI SOLUCION
palabra = ""

if len(palabra) <= 0:
    palabra += "hola mundo"
    print(palabra.upper())
else:
    print(palabra.upper())

# SOLUCIÓN DEL PROFESOR
texto = " "

if len(texto.strip()) <= 0:
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")
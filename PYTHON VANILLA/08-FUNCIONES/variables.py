"""
    VARIABLES LOCALES:
        Se definen dentro de la función y no se pueden usar fuera, salvo con el return

    VARIABLES GLOBALES:
        Se definen fuera de la función y se usan tanto dentro como fuera de las funciones
"""

# VARIABLE GLOBAL
texto = "Hola Mundo"
def holaWorld():
    print(texto)

print(holaWorld())

# VARIABLE LOCAL
def holaMundo():
    frase = "Hola Mundo"
    return frase

print(holaMundo())

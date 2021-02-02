"""
    EJERCICIO 14
        Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima un mensaje
        según el tipo de dato de cada variable
"""

# MI SOLUCION
lista = ["Hola", "Mundo"]
texto = "Hola Mundo"
numero = 1997
booleano = True

def tipoVariable(elemento):
    if type(elemento) == str:
        print(f"{elemento} es un string")
    elif type(elemento) == int:
        print(f"{elemento} es un entero")
    elif type(elemento) == bool:
        print(f"{elemento} es un booleano")
    elif type(elemento) == list:
        print(f"{elemento} es una lista")

tipoVariable(lista)
tipoVariable(texto)
tipoVariable(numero)
tipoVariable(booleano)

# SOLUCIÓN DEL PROFESOR
mi_lista = ["hola mundo", 77]
titulo = "Master en Python"
numero = 100
verdadero = True

def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = f"Esta dato es del tipo {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    return result

def traducirTipo(tipo):
    result = ""
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
    return result

print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))

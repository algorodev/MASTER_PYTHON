"""
 Ejercicio 11
    Escribir un programa que tenga una lista de 8 números enteros.
    - Recorrer la lista y mostrarla
    - Ordenarla y mostrarla en una función
    - Mostrar su longitud
    - Buscar algún elemento que el usuario pida por teclado
"""

# MI SOLUCIÓN
lista_numeros = [1, 4, 2, 6, 7, 3, 5, 9]

for numero in lista_numeros:
    print(f"- {numero}")

def ordenarNumeros(numeros):
    numeros.sort()
    print(numeros)
ordenarNumeros(lista_numeros)

print(f"Longitud de la lista: {len(lista_numeros)}")

numero_usuario = int(input("Dime un número: "))
print(numero_usuario in lista_numeros)

# SOLUCIÓN DEL PROFESOR
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

print("###### RECORRER Y MOSTRAR ######")
def mostarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado
print(mostarLista(numeros))

print("###### ORDENAR Y MOSTRAR ######")
numeros.sort()
print(mostarLista(numeros))

print("###### MOSTRAR LONGITUD ######")
print(len(numeros))

print("###### BUSQUEDA EN LA LISTA ######")
busqueda = int(input("Introduce el número: "))
comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el número: "))
else:
    print(f"Has introducido el {busqueda}")
print(f"#### BUSCAR EN LA LISTA EL NÚMERO {busqueda} ####")
search = numeros.index(busqueda)
print(f"El número buscado existe en la lista, es el indice: {search}")

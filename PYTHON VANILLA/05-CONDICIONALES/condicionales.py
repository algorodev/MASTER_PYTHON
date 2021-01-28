# Operadores de comparación
# == igual
# != diferente
# < menor que
# > mayor que
# <= menor o igual que
# >= mayor o igual que

# Operadores lógicos
# and y
# or o
# ! negación
# not no

"""
Condicional IF

if condición:
    intrucciones
else:
    otras instrucciones


Condicional ELIF

if condición:
    intrucciones
elif condicion:
    otras instrucciones
else:
    ultimas instrucciones
"""

# EJEMPLO 1 --> USANDO IF Y COMPARADOR DE IGUAL
color = input("Acierta el color que estoy pensando: ")

if color == "azul":
    print("Exacto! Estaba pensando en el color azul")
else:
    print("Noo! Ese no es el color en el que estoy pensando")

# EJEMPLO 2 --> USANDO IF Y COMPARADOR DE DIFERENTE
year = int(input("¿En que año estamos?: "))

if year != 2021:
    print("Noo! Estamos en 2021")
else:
    print("Exacto! Estamos en 2021")

# EJEMPLO 3 --> USANDO IF Y COMPARADOR MENOR QUE
edad = int(input("¿Que edad tienes?: "))

if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

# EJEMPLO 4 --> USANDO IF Y COMPARADOR MAYOR QUE
nota = int(input("¿Que nota sacaste en el ultimo examen?: "))

if nota > 5:
    print("Aprobaste!")
else:
    print("Oh! Has suspendido..")

# EJEMPLO 5 --> USANDO IF Y COMPARADOR MENOR O IGUAL QUE
viajes = int(input("¿Cuantas veces has viajado?: "))

if viajes <= 10:
    print("Vaya! Que poco has viajado")
else:
    print("Wow! Estas hecho todo un aventurero")

# EJEMPLO 6 --> USANDO IF Y COMPARADOR MAYOR O IGUAL QUE
lenguajes = int(input("¿Cuantos lenguajes de programación sabes?: "))

if lenguajes >= 6:
    print("Estas hecho todo un full-stack!")
else:
    print("Sigue estudiando!")

# EJEMPLO 7 --> USANDO IF ANIDADOS
nombre = input("Dime tu nombre: ")
continente = input("¿En que continente vives?: ")
ciudad = input("¿En que ciudad vives?: ")
edad = int(input("¿Cuantos años tienes?: "))
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad")

    if continente != "Europa":
        print("No eres europeo")
    else:
        print(f"Es Europeo y de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")

# EJEMPLO 8 --> USANDO ELIF
dia = int(input("¿En que número del día de la semana estamos?: "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")

# EJEMPLO 9 --> USANDO IF CON MÚLTIPLES CONDICIONES CON AND
edad_minima = 18
edad_maxima = 65
edad = int(input("¿Cuantos años tienes?: "))

if edad >= edad_minima and edad <= edad_maxima:
    print("Estás en edad de trabajar")
else:
    print("No estás en edad de trabajar")

# EJEMPLO 10 --> USANDO IF CON MÚLTIPLES CONDICIONES CON OR
pais = input("¿En que país vives?: ")

if pais == "Mexico" or pais == "España" or pais == "Argentina":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

# EJEMPLO 11 --> USANDO IF CON MÚLTIPLES CONDICIONES CON NOT
pais = input("¿En que país vives?: ")

if not (pais == "Mexico" or pais == "España" or pais == "Argentina"):
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")

# EJEMPLO 12 --> USANDO IF CON MÚLTIPLES CONDICIONES CON !
pais = input("¿Dime un país en el que este pensando de habla hispana?: ")

if pais != "Mexico" and pais != "España":
    print("No has acertado el pais")
else:
    print("Has acertado el pais")

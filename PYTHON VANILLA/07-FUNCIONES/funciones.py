"""
    FUNCIONES:
        Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando
        a la función tantas veces como sea necesario

        def nombreDeLaFuncion(parametros):
            # BLOQUE / CONJUNTO DE INSTRUCCIONES

        nombreDeLaFuncion(parametro1)
        nombreDeLaFuncion(parametro2)
"""


# EJEMPLO 1 --> FUNCIONES SIN PARAMETROS
def mostrarNombres():
    print("Alex")
    print("Paco")
    print("Pepe")
    print("Jose")

mostrarNombres()

# EJEMPLO 2 --> FUNCIONES CON PARAMETROS
def mostarTuNombre(nombre_usuario, edad_usuario):
    print(f"Tu nombre es: {nombre_usuario}")
    if edad_usuario >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

nombre = input("Dime tu nombre: ")
edad = int(input("Cuantos años tienes: "))
mostarTuNombre(nombre, edad)

# EJEMPLO 3 --> FUNCIONES CON PARAMETROS: TABLA DE MULTIPLICAR
def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")
    for contador in range(11):
        print(f"{numero} x {contador} = {numero * contador}")

numero_usuario = int(input("Dame un número: "))
tabla(numero_usuario)

# EJEMPLO 4 --> FUNCIONES CON PARAMETROS: TABLAS DE MULTIPLICAR USANDO LA FUNCIÓN DE ANTES
for numero_tabla in range(1, 11):
    tabla(numero_tabla)

# EJEMPLO 5 --> FUNCIONES CON PARAMETROS OPCIONALES
def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Alex", "73101863C")

# EJEMPLO 6 --> FUNCIONES CON PARAMETROS OPCIONALES Y RETURN
def saludame(nombre):
    saludo = f"Hola, {nombre}"
    return saludo

print(saludame("Alex"))

# EJEMPLO 7 --> CALCULADORA
def calculadora(numero1, numero2, operaciones_basicas = False):
    cadena = ""
    if operaciones_basicas == True:
        suma = f"{numero1} + {numero2} = {numero1 + numero2}"
        resta = f"{numero1} - {numero2} = {numero1 - numero2}"
        cadena += f"Suma: {suma}"
        cadena += "\n"
        cadena += f"Resta: {resta}"
    else:
        multiplicacion = f"{numero1} x {numero2} = {numero1 * numero2}"
        division = f"{numero1} / {numero2} = {numero1 / numero2}"
        cadena += f"Multiplicacion: {multiplicacion}"
        cadena += "\n"
        cadena += f"Division: {division}"
    return cadena

numero_usuario1 = int(input("Dame el primer número: "))
numero_usuario2 = int(input("Dame el segundo núumero: "))
print(calculadora(numero_usuario1, numero_usuario2, True))
print(calculadora(numero_usuario1, numero_usuario2))

# EJEMPLO 8 --> FUNCIONES DENTRO DE OTRAS FUNCIONES
def getNombre(nombre_usuario):
    texto = f"Nombre: {nombre_usuario}"
    return texto

def getApellidos(apellidos_usuario):
    texto = f"Apellidos: {apellidos_usuario}"
    return texto

def getNombreApellidos(nombre_usuario, apellidos_usuario):
    texto = getNombre(nombre_usuario) + "\n" + getApellidos(apellidos_usuario)
    return texto

nombre = input("Cual es tu nombre: ")
apellidos = input("Cuales son tus apellidos: ")
print(getNombreApellidos(nombre, apellidos))

# EJEMPLO 9 --> FUNCIONES LAMBDA
dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2021))

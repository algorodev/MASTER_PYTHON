nombre = "Alex"

# FUNCIONES GENERALES
print(nombre)
print(type(nombre))

# DETECTAR TIPADO
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es un string")

# LIMPIAR ESPACIOS DE UN STRING
frase = "           mi contenido espaciado             "
print(frase.strip())

# ELIMINAR VARIABLES
year = 2021
print(year)
del year

# COMPROBAR VARIABLE VACIA
texto = "  ff  "
if len(texto) <= 0:
    print("Variable vacia")
else:
    print("La Variable tiene contenido: ", len(texto))

# ENCONTRAR CARACTERES DENTRO DE UN STRING
frase = "La vida es bella"
print(frase.find("vida"))

# REEMPLAZAR PALABRAS EN UN STRING
nueva_frase = frase.replace("vida", "comida")
print(nueva_frase)

# MAYUSCULAS Y MINISCULAS
print(nombre)
print(nombre.lower())
print(nombre.upper())
print(nombre.capitalize())

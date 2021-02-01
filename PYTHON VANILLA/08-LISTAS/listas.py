"""
    LISTAS (arrays)
        Colecciones de datos bajo un único nombre
        Para acceder a los valores podemos usar un indice númerico
"""

# DEFINIR LISTA
peliculas = ["Batman", "Spiderman", "Superman", "Iron Man"]
cantantes = list(("2pac", "Drake", "Travis Scott", "Lil Peep"))
years = list(range(2000, 2022))
variada = ["Alex", 23, True, "González"]

print(peliculas)
print(cantantes)
print(years)
print(variada)

# INDICES
peliculas[1] = "Interstellar"
peliculas[2] = "El Señor de los Anillos"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(cantantes[0:1])
print(peliculas[1:])

# AGREGAR ELEMENTOS A UNA LISTA
cantantes.append("Future")
print(cantantes)

# RECORRER Y MOSTRAR UNA LISTA
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la película: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("#######LISTADO DE PELICULAS#######")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")

# LISTAS MULTIDIMENSIONALES
# Son listas que contienen otras listas
print("\n******LISTADO DE CONTACTOS******")
contactos = [
    [
        "Antonio",
        "antonio@antonio.com"
    ],
    [
        "Luis",
        "luis@luis.com"
    ],
    [
        "Salvador",
        "salvador@salvador.com"
    ]
]
print(contactos)
print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"Email: {elemento}")
    print("\n")

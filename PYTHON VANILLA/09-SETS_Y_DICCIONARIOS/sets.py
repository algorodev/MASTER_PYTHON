"""
    SET
        Tipo de dato, para tener una colección de valores pero sin indice ni orden
"""

personas = {
    "Alex",
    "Victor",
    "Manolo",
    "Francisco"
}
print(personas)

personas.add("Paco")
print(personas)

personas.remove("Francisco")
print(personas)

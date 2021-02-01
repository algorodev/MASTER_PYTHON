"""
    DICCIONARIO (array asociativo)
        Un tipo de dato que almacena un conjunto de datos.
        En formato clave - valor
"""

persona = {
    "nombre": "Alex",
    "apellido1": "González",
    "apellido2": "Romero",
    "edad": 23,
    "mayor_edad": True,
}

print(persona)
print(persona["apellido1"])

# LISTA CON DICCIONARIOS
contactos = [
    {
        "nombre": "Alex",
        "email": "alex@alex.com",
        "edad": 23
    },
    {
        "nombre": "Paco",
        "email": "paco@paco.com",
        "edad": 42
    },
    {
        "nombre": "Luis",
        "email": "luis@luis.com",
        "edad": 32
    }
]

print(contactos)
print(contactos[0]["nombre"])

contactos[0]["nombre"] = "Alfredo"
print(contactos[0]["nombre"])

print("\nListado de contactos: ")
print("---------------------------------------")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print(f"Edad del contacto: {contacto['edad']}")
    print("---------------------------------------")

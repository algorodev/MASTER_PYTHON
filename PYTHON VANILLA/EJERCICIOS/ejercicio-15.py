"""
    EJERCICIO 15
        Crear una lista con el contenido de esta tabla:
        ACCION      AVENTURA        DEPORTES
        gta         crash           fifa 21
        cod         prince          pro 21
        pugb        assassins       moto gp 21
        Mostrar esta información ordenada
"""

# MI SOLUCION Y LA DEL PROFESOR
lista_videojuegos = [
    {
        "categoria": "Acción",
        "juegos": ["GTA", "COD", "PUGB"],
    },
    {
        "categoria": "Aventura",
        "juegos": ["Crash Bandicoot", "Prince of Persia", "Assasins Creed"],
    },
    {
        "categoria": "Deportes",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"],
    },
]

for categoria in lista_videojuegos:
    print(f"##### {categoria['categoria']} #####")
    for juego in categoria['juegos']:
        print(f"- {juego}")

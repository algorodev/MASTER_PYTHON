import sqlite3

# CONEXIÓN SQLITE
conexion = sqlite3.connect("prueba.db")

# CREAR CURSOR
cursor = conexion.cursor()

# CREAR TABLA
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INT(255));
""")

# GUARDAR CAMBIOS
conexion.commit()

# INSERTAR DATOS
productos = [
    ("Ordenador Pórtatil", "Buen PC", 750),
    ("Telefono Móvil", "Buen Telefono", 420),
    ("Placa Base", "Buena Placa", 100),
    ("Tablet", "Buena tablet", 360),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# ACTUALIZAR DATOS
cursor.execute("UPDATE productos SET precio = 999 WHERE precio = 100")
conexion.commit()

# BORRAR REGISTROS
cursor.execute("DELETE FROM productos")
conexion.commit()

# LISTAR DATOS
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(f"Id: {producto[0]}")
    print(f"Producto: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: {producto[3]}")
    print("\n")

cursor.execute("SELECT titulo FROM productos WHERE precio >= 500")
producto = cursor.fetchone()
print(producto)

# CERRAR CONEXIÓN
conexion.close()

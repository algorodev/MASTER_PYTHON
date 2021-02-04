import mysql.connector

# CONEXIÓN MYSQL

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# ¿LA CONEXIÓN HA SIDO CORRECTA?
print(database)

cursor = database.cursor()

# CREAR BASE DE DATOS
cursor.execute("CREATE DATABASE if not exists master_python")
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

# CREAR TABLAS
cursor.execute("""
    CREATE TABLE if not exists vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        constraint pk_vehiculo PRIMARY KEY(id));
""")
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

# INSERTAR DATOS
# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Ibiza', 7500),
    ('Volkswagen', 'Golf', 20000),
    ('Renault', 'Clio', 12000),
    ('Mercedes', 'Clase C', 35000)
]
# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
database.commit()

# SELECT
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

print("----- LISTA DE COCHES -----")
for coche in result:
    print(f"Id: {coche[0]}")
    print(f"Marca: {coche[1]}")
    print(f"Modelo: {coche[2]}")
    print(f"Precio: {coche[3]}")
    print("---------------------------")

# WHERE
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 10000 AND marca = 'Seat'")
result = cursor.fetchall()

print("----- LISTA DE COCHES -----")
for coche in result:
    print(f"Id: {coche[0]}")
    print(f"Marca: {coche[1]}")
    print(f"Modelo: {coche[2]}")
    print(f"Precio: {coche[3]}")
    print("---------------------------")

# BORRAR DATOS
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount, "borrados!!")

# ACTUALIZAR DATOS
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat'")
database.commit()

print(cursor.rowcount, "actualizados!!")

from io import open
import pathlib
import shutil

# ABRIR UN ARCHIVO
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

# ESCRIBIR DENTRO DE UN ARCHIVO
archivo.write("#### SOY UN TEXTO AGREGADO DESDE MI PROGRAMA DE PYTHON ####\n")

# CERRAR EL ARCHIVO
archivo.close()

# ABRIR UN ARCHIVO CON PERMISO DE LECTURA
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# LEER CONTENIDO
contenido = archivo_lectura.read()
print(contenido)

# LEER CONTENIDO Y GUARDARLO EN LISTA
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elemento in lista:
    print("- " + elemento)

# COPIAR UN ARCHIVO
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_destino = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/ficheros/fichero_alternativo.txt"
shutil.copyfile(ruta_original, ruta_alternativa)

# MOVER UN ARCHIVO
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
ruta_destino = str(pathlib.Path().absolute()) + "/ficheros/fichero_copiado_NUEVO.txt"
shutil.move(ruta_original, ruta_destino)

# ELIMINAR UN ARCHIVO
import os

ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
os.remove(ruta_original)

# COMPROBAR SI UN ARCHIVO EXISTE O NO
import os.path

print(os.path.abspath("./"))
if os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")

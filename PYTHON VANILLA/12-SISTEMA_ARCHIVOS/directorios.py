import os
import shutil

# CREAR CARPETA
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")

# ELIMINAR CARPETA
os.rmdir('./mi_carpeta')

# COPIAR CARPETAS
ruta_original = "./mi_carpeta"
ruta_destino = "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_destino)

# LISTAR CONTENIDO CARPETA
contenido = os.listdir("./mi_carpeta")
for fichero in contenido:
    print(f"Fichero: {fichero}")

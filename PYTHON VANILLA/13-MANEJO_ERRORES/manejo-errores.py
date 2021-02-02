# CAPTURAR EXCEPCIONES Y MANEJAR ERRORES EN CÓDIGO
try:
    nombre = input("¿Cual es tu nombre?: ")
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre
    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce bien el nombre")
else:
    print("Todo ha funcionado correctamente !!")
finally:
    print("Fin de la iteración !!")

# EJEMPLO EXCEPCIÓN
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

print("###### RECORRER Y MOSTRAR ######")
def mostarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado
print(mostarLista(numeros))

print("###### ORDENAR Y MOSTRAR ######")
numeros.sort()
print(mostarLista(numeros))

print("###### MOSTRAR LONGITUD ######")
print(len(numeros))

try:
    print("###### BUSQUEDA EN LA LISTA ######")
    busqueda = int(input("Introduce el número: "))
    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el número: "))
    else:
        print(f"Has introducido el {busqueda}")
    print(f"#### BUSCAR EN LA LISTA EL NÚMERO {busqueda} ####")
    search = numeros.index(busqueda)
    print(f"El número buscado existe en la lista, es el indice: {search}")
except:
    print("El número no está en la lista ..")

# MANEJAR MÚLTIPLES EXCEPCIONES
try:
    numero = int(input("Número para elevarlo al cuadrado: "))
    print(f"El cuadrado de {numero} es: {numero * numero}")
except TypeError:
    print("Debes convertir tus cadenas de texto a enteros en el código")
except ValueError:
    print("Introduce un número correcto")
except Exception as e:
    print(f"Ha ocurrido un error: {type(e).__name__}")

# EXCEPCIONES PERSONALIZADAS O LANZAR EXCEPCIONES
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es REAL")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print("Bienvenido !!")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print(f"Existe un error: {e}")
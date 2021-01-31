"""
 Ejercicio 10
    - Pedir numero de alumnos al usuario
    - Pedir las notas de dichos alumnos
    - Devolver cuantos han aprobado y cuantos han suspendido
"""

# MI SOLUCIÓN
contador = 1
aprobados = 0
suspendidos = 0
numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"Introduce la nota del alumno-{contador}: "))
    if nota >= 5:
        print("Aprobado!!")
        aprobados += 1
    else:
        print("Suspendido..")
        suspendidos += 1
    contador += 1
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")

# SOLUCIÓN DEL PROFESOR
contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al alumno \"{contador}\"?: "))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")

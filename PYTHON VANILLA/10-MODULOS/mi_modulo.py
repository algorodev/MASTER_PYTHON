def holaMundo(nombre):
    return f"Hola como estás, {nombre}"

def calculadora(numero1, numero2, operaciones_basicas=False):
    cadena = ""
    if operaciones_basicas == True:
        suma = f"{numero1} + {numero2} = {numero1 + numero2}"
        resta = f"{numero1} - {numero2} = {numero1 - numero2}"
        cadena += f"Suma: {suma}"
        cadena += "\n"
        cadena += f"Resta: {resta}"
    else:
        multiplicacion = f"{numero1} x {numero2} = {numero1 * numero2}"
        division = f"{numero1} / {numero2} = {numero1 / numero2}"
        cadena += f"Multiplicacion: {multiplicacion}"
        cadena += "\n"
        cadena += f"Division: {division}"
    return cadena

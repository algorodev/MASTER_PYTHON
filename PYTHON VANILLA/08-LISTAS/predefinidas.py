cantantes = ["2pac", "Drake", "Bad Bunny", "AA Anuel", "Travis Scott"]
numeros = [1, 2, 5, 8, 3, 4]

# ORDENAR LISTA
numeros.sort()
print(numeros)

# AGREGAR ELEMENTOS DENTRO DE UNA LISTA
cantantes.append("Natos y Waor")
cantantes.insert(1, "Yung Beef")
print(cantantes)

# ELIMINAR ELEMENTOS DE UNA LISTA
cantantes.pop(1)
cantantes.remove("Natos y Waor")
print(cantantes)

# DAR LA VUELTA A LA LISTA
numeros.reverse()
print(numeros)

# BUSCAR DENTRO DE UNA LISTA
print("Drake" in cantantes)

# CONTAR ELEMENTOS DE UNA LISTA
print(len(cantantes))

# CUANTAS VECES APARECE UN ELEMENTO DE UNA LISTA
numeros.append(8)
print(numeros.count(8))

# CONSEGUIR INDICE DE UNA LISTA
print(cantantes.index("Drake"))

# UNIR LISTAS
cantantes.extend(numeros)
print(cantantes)

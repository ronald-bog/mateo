# En , una lista es una colección ordenada y mutable de elementos. Puedes almacenar cualquier tipo de objeto en una lista: números, cadenas, booleanos, otras listas, diccionarios, funciones, etc. Las listas se definen utilizando corchetes [] y los elementos se separan por comas.

# Creación de una lista de números enteros
numeros = [1, 2, 3, 4, 5]

# Creación de una lista de cadenas
nombres = ["Ana", "Juan", "María", "Pedro"]

# Ejemplo 2: Acceso a elementos de la lista
numeros = [1, 2, 3, 4, 5]

# Acceso al primer elemento de la lista (índice 0)
primer_numero = numeros[0]
print(primer_numero)  # Output: 1

# Acceso al tercer elemento de la lista (índice 2)
tercer_numero = numeros[2]
print(tercer_numero)  # Output: 3

# Ejemplo 3: Modificación de elementos de la lista
numeros = [1, 2, 3, 4, 5]

# Modificación del segundo elemento de la lista
numeros[1] = 10
print(numeros)  # Output: [1, 10, 3, 4, 5]

# Ejemplo 4: Operaciones con listas
numeros = [1, 2, 3]
otros_numeros = [4, 5, 6]

# Concatenación de listas
concatenacion = numeros + otros_numeros
print(concatenacion)  # Output: [1, 2, 3, 4, 5, 6]

# Longitud de una lista
longitud = len(numeros)
print(longitud)  # Output: 3

# Agregar un elemento al final de la lista
numeros.append(4)
print(numeros)  # Output: [1, 2, 3, 4]

# *********************** fin clase Abril 9 ************************


# *********************** Inicio clase Abril 12 ************************
# Eliminar un elemento de la lista por índice
del numeros[1]
print(numeros)  # Output: [1, 3, 4]

# Eliminar un elemento de la lista por valor
numeros.remove(3)
print(numeros)  # Output: [1, 4]
numeros1 = [1, 2, 3, 4, 2]
numeros1.remove(2)  # Eliminar el número 2
print(numeros1)  # Output: [1, 3, 4, 2]

# Invertir el orden de los elementos en la lista
numeros.reverse()
print(numeros)  # Output: [4, 1]

# Ordenar la lista
numeros.sort()
print(numeros)  # Output: [1, 4]

# extend() Este método agrega los elementos de otra lista al final de la lista actual.
numeros = [1, 2, 3]
otros_numeros = [4, 5, 6]
numeros.extend(otros_numeros)
print(numeros)  # Output: [1, 2, 3, 4, 5, 6]

# insert() Este método inserta un elemento en una posición específica de la lista.
numeros = [1, 2, 3]
numeros.insert(1, 10)  # Insertar el número 10 en la posición 1
print(numeros)  # Output: [1, 10, 2, 3]

# pop() Este método elimina y devuelve el elemento en la posición especificada de la lista. Si no se proporciona ningún índice, elimina y devuelve el último elemento de la lista.
numeros = [1, 2, 3]
ultimo_numero = numeros.pop()  # Eliminar y obtener el último número
print(ultimo_numero)  # Output: 3
print(numeros)  # Output: [1, 2]

# clear() Este método elimina todos los elementos de la lista.
numeros = [1, 2, 3]
numeros.clear()
print(numeros)  # Output: []

# index() Este método devuelve el índice de la primera aparición del elemento especificado en la lista.
numeros = [1, 2, 3, 4, 2]
indice = numeros.index(2)  # Obtener el índice del número 2
print(indice)  # Output: 1
numerosI = [1, 2, 3, 4, 2]
indiceI = numerosI.index(2, 2, 5)  # Obtener el índice del número 2
print(indiceI)  # Output: 1

# count()# Este método devuelve el número de veces que aparece un elemento en la lista.
numeros = [1, 2, 3, 4, 2]
conteo = numeros.count(2)  # Contar el número de veces que aparece el número 2
print(conteo)  # Output: 2

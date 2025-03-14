# *********************** continua clase Abril 12 ************************

# Una tupla en  es una colección ordenada e inmutable de elementos. Es similar a una lista, pero a diferencia de las listas, las tuplas no se pueden modificar una vez creadas. Se definen utilizando paréntesis () y pueden contener elementos de diferentes tipos.

# Creación de una tupla vacía
tupla_vacia = ()

# Creación de una tupla con elementos
mi_tupla = (1, 2, 3, "a", "b", "c")

# Acceso a elementos individuales mediante índices
print(mi_tupla[0])  # Output: 1
print(mi_tupla[3])  # Output: 'a'

# Acceso a un rango de elementos mediante slicing
print(mi_tupla[1:4])  # Output: (2, 3, 'a')

# Métodos de las tuplas

# count(): Devuelve el número de veces que un elemento aparece en la tupla.
mi_tupla = (1, 2, 3, 2, 4, 2)
print(mi_tupla.count(2))  # Output: 3

# index(): Devuelve el índice de la primera aparición de un elemento en la tupla.
mi_tupla = (1, 2, 3, 2, 4, 2)
print(mi_tupla.index(2))  # Output: 1

# len(): Devuelve la longitud de la tupla, es decir, el número de elementos que contiene.
mi_tupla = (1, 2, 3, "a", "b", "c")
print(len(mi_tupla))  # Output: 6

# sorted(): Devuelve una lista ordenada de los elementos de la tupla.
mi_tupla = (3, 1, 2, 5, 4)
print(sorted(mi_tupla))  # Output: [1, 2, 3, 4, 5]

# any(): Devuelve True si algún elemento de la tupla es verdadero. Si la tupla está vacía, devuelve False.
mi_tupla = (0, False, "", None)
print(any(mi_tupla))  # Output: False

# all(): Devuelve True si todos los elementos de la tupla son verdaderos. Si la tupla está vacía, devuelve True.
mi_tupla = (1, True, "texto")
print(all(mi_tupla))  # Output: True

# max(): Devuelve el elemento máximo de la tupla.
mi_tupla = (5, 3, 9, 1)
print(max(mi_tupla))  # Output: 9

# min(): Devuelve el elemento mínimo de la tupla.
mi_tupla = (5, 3, 9, 1)
print(min(mi_tupla))  # Output: 1

# Desempaquetado de una tupla
coordenadas = (3, 4)
x, y = coordenadas
print("x:", x)  # Output: x: 3
print("y:", y)  # Output: y: 4

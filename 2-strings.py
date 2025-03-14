# F-STRINGS - LITERAL TEMPLATES
nombre = "Ronald"
print(f"Hola mi nombre es {nombre}")

# Caracteres de escape
# \n \t \' \" \\

# indices
string = "Hola Mundo"
print(string[1])

# Valor del elemento de acuerdo a vr decimal de la codigo ascii
# 'A' = 65
# 'a' = 48
print("A" < "a")  # false

# upper() y lower(): Estos métodos devuelven una copia del string con todos los caracteres en mayúsculas o minúsculas, respectivamente.
string = "hola mundo"
print(string.upper())  # Output: HOLA MUNDO
print(string.lower())
print(string.capitalize())

# strip(): Elimina espacios en blanco al principio y al final del string.
string = "   ¡Hola Mundo!   "
print(string.strip())  # Output: ¡Hola Mundo!

# split(separador): Divide el string en una lista de substrings usando el separador especificado.
string = "Hola, Mundo, Python"
print(string.split(", "))  # Output: ['Hola', 'Mundo', 'Python']

# join(iterable): Une los elementos de un iterable (como una lista) en un solo string usando el string como separador.
lista = ["Hola", "Mundo", "Python"]
print(", ".join(lista))  # Output: Hola, Mundo, Pythonname

# replace(old, new): Reemplaza todas las ocurrencias de old con new en el string.
string = "Hola Mundo"
print(string.replace("Mundo", "Python"))  # Output: Hola Python

# startswith(prefix) y endswith(suffix): Comprueba si el string comienza o termina con el prefijo o sufijo dado.
string = "Hola Mundo"
print(string.startswith("Hola"))  # Output: True
print(string.endswith("Mundo"))  # Output: True

# SLICING
string = "Hola Mundo"
print(string[::-1])

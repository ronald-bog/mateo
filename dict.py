# Los diccionarios en  son estructuras de datos que permiten almacenar pares de clave-valor de manera eficiente. Cada clave en un diccionario debe ser única y puede ser de cualquier tipo inmutable, como cadenas, números o tuplas. Los valores pueden ser de cualquier tipo, incluidos otros diccionarios o listas.

# Creación de un diccionario vacío
mi_diccionario = {}

# Creación de un diccionario con elementos
diccionario_ejemplo = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Acceso a un valor mediante su clave
print(diccionario_ejemplo["nombre"])  # Output: Juan
print(diccionario_ejemplo["edad"])  # Output: 30

# Añadir un nuevo elemento
diccionario_ejemplo["ocupacion"] = "Ingeniero"

# Modificar un elemento existente
diccionario_ejemplo["edad"] = 31
print(diccionario_ejemplo)
# Output: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniero'}

# Métodos de los diccionarios ***********

# keys(): Devuelve una vista de todas las claves en el diccionario.
print(diccionario_ejemplo.keys())
# Output: dict_keys(['nombre', 'edad', 'ciudad', 'ocupacion'])

# values(): Devuelve una vista de todos los valores en el diccionario.
print(diccionario_ejemplo.values())
# Output: dict_values(['Juan', 31, 'Madrid', 'Ingeniero'])

# items(): Devuelve una vista de todos los pares clave-valor en el diccionario.
print(diccionario_ejemplo.items())
# Output: dict_items([('nombre', 'Juan'), ('edad', 31), ('ciudad', 'Madrid'), ('ocupacion', 'Ingeniero')])

# get(): Devuelve el valor asociado a una clave. Si la clave no existe, devuelve un valor predeterminado (o None si no se especifica ningún valor predeterminado).
print(diccionario_ejemplo.get("nombre"))  # Output: Juan
print(diccionario_ejemplo.get("telefono"))  # Output: None
print(diccionario_ejemplo.get("telefono", "No encontrado"))  # Output: No encontrado

# pop(): Elimina y devuelve el valor asociado a una clave. Si la clave no existe, se puede especificar un valor predeterminado.
valor_eliminado = diccionario_ejemplo.pop("edad")
print(valor_eliminado)  # Output: 31
print(diccionario_ejemplo)
# Output: {'nombre': 'Juan', 'ciudad': 'Madrid', 'ocupacion': 'Ingeniero'}

# Eliminación de un elemento mediante la palabra clave 'del'
del diccionario_ejemplo["ciudad"]

# Eliminación de un elemento y devolución de su valor mediante pop()
valor_eliminado = diccionario_ejemplo.pop("ocupacion")
print(diccionario_ejemplo)
# Output: {'nombre': 'Juan'}

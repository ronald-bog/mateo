# #Operadores Aritmeticos + - * / % ** //

# Operadores de comparacion o relacionales: == != > < => =<

# Operadores de Asignacion
# Asignacion =
# suma y Asignacion +=      x = x + 5       x += 5
# resta y asignacion -=
# multiplica y asigna *=
# divina y asigna /=

# Operadores Logicos:
# and xxxxx and yyyyyy
# or     1expresion OR 2expresion
# not


###### Operadores Pertenencia: in  /   not in  #########
# Verificar si un elemento está presente en una lista
numeros = [1, 2, 3, 4, 5]
print(3 in numeros)  # Output: True

# Verificar si un carácter está presente en una cadena de texto
mensaje = "Hola, mundo"
print("m" in mensaje)  # Output: True

# Verificar si una clave está presente en un diccionario
persona = {"nombre": "Juan", "edad": 30}
print("nombre" in persona)  # Output: True


###### Operadores de identidad:  ########
# is: a is b
# Verificar si dos variables se refieren al mismo objeto en memoria
a = [1, 2, 3]
b = a  # b ahora apunta al mismo objeto que a
print(a is b)  # Output: True

# Verificar si dos variables se refieren al mismo objeto en memoria
x = 10
y = 10
print(x is y)  # Output: True

# is not
# Verificar si dos variables no se refieren al mismo objeto en memoria
a = [1, 2, 3]
b = [1, 2, 3]  # Se crea un nuevo objeto, aunque tenga los mismos valores que a
print(a is not b)  # Output: True

# Verificar si dos variables no se refieren al mismo objeto en memoria
x = 10
y = 20
print(x is not y)  # Output: True

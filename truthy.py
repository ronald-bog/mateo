""" los conceptos de "truthy" y "falsy" son comunes en la programación y se aplican en muchos lenguajes de programación, incluido Python. Estos términos se utilizan para describir valores que se evalúan como True o False en contextos booleanos, como condiciones en declaraciones if o bucles while.

Truthy y Falsy en Python
En Python, los valores que se consideran "falsy" (falsos) en contextos booleanos son:

*False
*None
*Cero en cualquier tipo numérico (0, 0.0, 0j para números complejos)
*Secuencias o colecciones vacías ('', [], (), {}, set())
*Instancias de clases personalizadas que implementan el método __bool__() o __len__() que devuelve cero o False
Todos los demás valores se consideran "truthy" (verdaderos) en Python. Esto incluye cualquier valor que no esté en la lista de "falsy".

Ejemplos de Truthy y Falsy en Python """

# Falsy
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

# Truthy
print(bool(True))
print(bool(22))
print(bool(8.55))
print(bool("palabra"))
print(bool([89, 54, 74]))
print(bool((654, 982)))
print(bool({"nombre": "Andres", "edad": 40, "ciudad": "Cali"}))

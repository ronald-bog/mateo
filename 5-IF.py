""" if en  se utiliza para ejecutar un bloque de código si una condición es verdadera. Puede ir seguida de una o más cláusulas opcionales como elif (abreviatura de "else if") y else para manejar múltiples casos. """

""" Sintaxis básica """
x = 5
if x > 0:
    print("x es positivo")


""" Cláusula elif """
x = 5
if x > 0:
    print("x es positivo")
elif x == 0:
    print("x es cero")
else:
    print("x es negativo")


""" Cláusula else """
x = 5
if x > 0:
    print("x es positivo")
else:
    print("x no es positivo")

""" Anidamiento de estructuras if """
x = 5
y = 10
if x > 0:
    if y > 0:
        print("x y y son positivos")
    else:
        print("x es positivo pero y no lo es")
else:
    print("x no es positivo")

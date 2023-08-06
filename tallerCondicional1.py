"""

Punto 1. Para tributar un determinado impuesto se debe ser mayor de 18 años y tener
unos ingresos iguales o superiores a 2.500.000 mensuales. Escribir un
programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no.

""" 

edad= int (input("Digite su edad "))
ingreso= int (input("Digite sus ingresos mensuales "))


if edad > 18 and ingreso >= 2500000:
    print ("El usuario tiene que tributar")
else:
    print ("El usuario no tiene que tributar")
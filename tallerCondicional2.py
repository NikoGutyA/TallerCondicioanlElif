"""
Punto 2 Escribir un programa donde se ingrese la nota de las materias: desarrollo de
software, matemáticas, lógica programación, si el promedio es mayor o igual
que 3,0 muestre
"""

desarrolloSoftware =float(input("Digite su nota de desarrollo de software de 0 a 5 "))

matematicas =float(input("Digite su nota de matematicas 0 a 5 "))

lógicaProgramación =float(input("Digite su nota de logica de programación 0 a 5 "))

promedio= (desarrolloSoftware+matematicas+lógicaProgramación+lógicaProgramación)/5

if promedio>=3.0:
    print(f"Aprobo el curso con un promedio de {promedio}")
    
else:
    print(f"Perdio el curso su promedio es de  {promedio} ")
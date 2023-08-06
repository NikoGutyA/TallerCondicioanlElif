"""
Punto 3 Comparar 4 números solicitados al usuario, escribir condiciones que permita
mostrar que un número fue escrito 2 veces, que todos son iguales o por el contrario
todos son diferentes.
"""

num1 =int (input ("Escribe un número entero "))
num2 =int (input ("Escribe un número entero "))
num3 =int (input ("Escribe un número entero "))
num4 =int (input ("Escribe un número entero "))

if num1 == num2  and num2== num3 and num3 == num4:
    print(f"todos los numeros son igules")
elif num1==num2 and num3==num4:
    print(f"el primer y segundo numero estan repetidos y son {num1} y el tercer y cuarto tambien estan repetidos y el numero es {numero3} ")
elif num1==num2 :
    print(f"el primer y segundo numero estan repetidos y son {num1}  ")
elif num3==num4:
     print(f"el tercer y cuarto numero estan repetidos y son {num3}  ")
elif num1==num4:
 print(f"el primer y cuarto numero estan repetidos y son {num1} ")
elif num1==num3:
 print(f"el primer y el tercero numero estan repetidos y son {num1} ")

elif num2==num3:
     print(f"el segundo y tercero numero estan repetidos y son {num2} ")
elif num2==num4:
     print(f"el segundo y el cuarto numero estan repetidos y son {num2} ")
else:
    print("todos los nuemeros son diferentes y son {num1}, {num2}, {num3}, {num4} ")
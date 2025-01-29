# Hacer un programa que solicite al usuario dos numero
# y muestre el resultado de la suma, resta, multiplicacion y division
a = 0
b = 0
op = ""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

op = input("Ingrese la operacion que desea realizar: ")

if op.lower() == "suma":
    suma = a + b
    print(f"La suma de {a} + {b} es: {suma}")
    input()
    
elif op.lower() == "resta":
    resta = a - b
    print(f"La resta de {a} - {b} es: {resta}")
    input()
    
elif op.lower() == "multi":
    multi = a * b
    print(f"La multiplicacion de {a} * {b} es: {multi}")
    input()
    
elif op.lower() == "div":
    div = a / b
    print(f"La division de {a} / {b} es: {div}")
    input()
    
else:
    print("Operacion no valida")
    input()

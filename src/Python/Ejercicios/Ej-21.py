# Crear una funcion recursiva que permita calcular el factorial de un numero.
# Realiza un programa principal donde se lea un entero y se muestre 
# el resultado del factorial

def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print("Calculo del factorial de un número")
fac = int(input("Ingrese un número: "))
print(F"El factorial de {fac} es {factorial(fac)}")
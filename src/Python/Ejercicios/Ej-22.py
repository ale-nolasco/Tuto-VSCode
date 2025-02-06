# Crear una funcion que calcule el MCD de dos n umero por el mÈtodo de Euclides. 
# El mÈtodo de Euclides es el siguiente:
# Se divide el n ̇mero mayor entre el menor. 
# Si la divisiÛn es exacta, el divisor es el MCD.
# Si la division no es exacta, dividimos el divisor entre el resto obtenido 
# y se contin ̇a de esta forma hasta obtener una divisiÛn exacta, siendo el  ultimo 
# divisor el MCD.
# Crea un programa principal que lea dos n ̇meros enteros y muestre el MCD.

def MCD(num1, num2):
    
    if num2 == 0:
        return num1
    else:
        return MCD(num2, num1 % num2)

print("ingrese dos numeros enteros")
numero1 = int(input("Ingrese el primero: "))
numero2 = int(input("Ingrese el segundo: "))

print(f"El Maximo comuni divisor de {numero1} y {numero2} es {MCD(numero1, numero2)}")
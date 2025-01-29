def suma(*numeros):
    
    resultado = 0
    
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 4)
suma(2, 4, 5, 42)
suma(54, 3, 1, 1)
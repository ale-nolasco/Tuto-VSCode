buscar = int(input("Proporcione un numero: "))

#For clasico en un arreglo de numeros

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado")
        break
else: print("Numero no encontrado")

# Corre el for por cada caracter de un acadena

for char in "Ultimate python":
    print(char)
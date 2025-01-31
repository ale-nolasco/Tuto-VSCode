# Crea un programa que pida dos n umero enteros al usuario 
# y diga si alguno de ellos es m ultiplo del otro. 
# Crea una funcion EsMultiplo que reciba
# los dos n umeros, y devuelve si el primero es 
# multiplo del segundo.

def EsMultiplo(a,b):
    if a % b == 0:
        print(f"{a} es multiplo de {b}")
    else:
        print(f"{a} no es multiplo de {b}")
        

a = int(input(("introduce un numero: ")))
b = int(input(("introduce otro numero: ")))

EsMultiplo(a,b)

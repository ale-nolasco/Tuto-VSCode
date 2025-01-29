# Hacer un programa que solicite un color por teclado 
# e imprima “Puede pasar “ si el color ingresado es 
# verde , “Precaución “ si es amarillo , “No pasar “ 
# si es rojo o “Color inválido” si es cualquier otro.
texto = ""

def color(texto):
    
    if texto == "verde":
        print("Puede pasar")
    elif texto == "amarillo":
        print("Precaución")
    elif texto == "rojo":
        print("No pasar")
    elif texto == "salir":
        print("Adios")
    else:
        print("Color inválido")
    
    
while texto != "salir":
    
    a = input("Ingrese un color:")
    texto = a.lower()
    color(texto)
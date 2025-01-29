# and, or , not

gas = True
encendido = True
edad = 19

if gas and encendido:
    print("1.- Puedes avanzar")

if gas or encendido:
    print("2.- Puedes avanzar")

if not gas or encendido:
    print("3.- Puedes avanzar")
    
if (gas or encendido) and edad >17:
    print("4.- Puede avanzar")
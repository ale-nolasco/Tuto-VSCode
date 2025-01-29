op = ""
respuesta = 0

mensaje = """Bienvenido a la calculadora
Para Salir escriba la palabra \"salir\" 
Las operaciones que puedes realizar son suma,resta,div,multi"""

print(mensaje)

n1 = int(input("Ingresa un numero: "))

while op.lower() != "salir":
    
    op = input("Ingresa Operacion: ")
    
    if op.lower() != "salir":
        
        n2 = int(input("Ingrese un segundo numero: "))
        
        if op.lower() == "suma":
            respuesta = n1 + n2
            print("El resultado es: ", respuesta)
        elif op.lower() == "resta":
            respuesta = n1 - n2
            print("El resultado es: ", respuesta)
        elif op.lower() == "div":
            respuesta = n1 / n2
            print("El resultado es: ", respuesta)
        elif op.lower() == "multi":
            respuesta = n1 * n2
            print("El resultado es: ", respuesta)
            
        n1 = respuesta
        
    else:
        break

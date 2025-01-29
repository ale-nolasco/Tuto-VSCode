# numero = 1

# while numero <= 100:
#     print(numero)
#     numero *= 2
    
    
comando = ""

while comando.lower() != "salir":
    comando =  input("$ ")
    print(comando)
    
# En este caso tenemos un loop indeterminado y debemos darle una salida 

while True: 
    comando =  input("$ ")
    print(comando)
    if comando.lower() == "salir": # esta parte del codigo es la salida del loop
        break
    

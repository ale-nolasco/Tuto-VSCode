usuarios = [
    
            ["chanchito",4],
            ["Felipe",1],
            ["Roberto",3],
            ["Victor",2]
]

#nombres = []
# for usuario in usuarios:
    
#     nombres.append(usuario[0])
#     print(nombres)
    

# nombres = {usuario[0] for usuario in usuarios}

# filtrar
nombres ={usuario[0] for usuario in usuarios if usuario[1] > 2}
print(nombres) # {'chanchito'}
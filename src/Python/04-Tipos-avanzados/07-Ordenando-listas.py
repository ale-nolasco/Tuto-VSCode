numeros = [1,43,234,3,12,4,23,213,21]

# numeros.sort(reverse=True) # Ordena la lista de mayor a menor

numeros2 = sorted(numeros, reverse=True) # Ordena la lista de menor a mayor pero no modifica la lista original

print(numeros) # [1, 3, 4, 12, 21, 23, 43, 213, 234]

print(numeros2) # [1, 3, 4, 12, 21, 23, 43, 213, 234]

# usuarios = [
    
#             [4 , "chanchito"],
#             [1,"Felipe"],
#             [3,"Roberto"],
#             [2,"Victor"]
            
# ]

usuarios = [
    
            ["chanchito",4],
            ["Felipe",1],
            ["Roberto",3],
            ["Victor",2]
            
]

usuarios.sort(key=lambda el:el[1]) # Ordena la lista de menor a mayor
print(usuarios)
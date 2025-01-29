mascotas = [
    "Peluza", 
    "Copito", 
    "Rod", 
    "Zeus", 
    "Rod", 
    "Rod"
            
]
print(mascotas)
# Agregar un elemento al final de la lista
mascotas.append("Rex")
print(mascotas)

# Agregar un elemento en una posición específica
mascotas.insert(2, "Pirata")
print(mascotas)

# Eliminar un elemento de la lista
mascotas.remove("Rod")
print(mascotas)

# Eliminar un elemento de la lista por su índice
mascotas.pop(1)
print(mascotas)

del mascotas[0]
print(mascotas)

# Eliminar todos los elementos de la lista
mascotas.clear()
print(mascotas)


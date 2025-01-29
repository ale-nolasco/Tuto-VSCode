mascotas = ["Peluza", "Copito", "Rod", "Zeus"]
print(mascotas)

print(mascotas[2])

mascotas[0] = 'pulga'
print(mascotas) 

print(mascotas[:3]) #imprime desde el primer elemento hasta el tercero

print(mascotas[1:]) #imprime desde el segundo elemento hasta el final

print(mascotas[::2]) #imprime desde el primer elemento hasta el final, pero de dos en dos

print(mascotas[1::2]) #imprime desde el segundo elemento hasta el final, pero de dos en dos
print(mascotas[::-1]) #imprime la lista al revés
animal = "Chanchito Feliz"

print(animal.upper())  # Hace el string en mayusculas
print(animal.lower()) #String en minisculas
print(animal.capitalize()) #String con la primer letra en mayusculas
print(animal.title()) # mayusculas las primeras letras de cada palabra

animal2 = "  Chanchito feliz 2   "
print(animal2)
print(animal2.title().strip())  # Se pueden agregar 2 metodos sin problemas
print(animal2.lstrip())     # Quita los espacios izquierdos
print(animal2.rstrip())     #Quita los espacios derechos

print(animal.find("F"))  # Imprime la posicion de caracteres que deseamos

print(animal.replace("nch", "j"))  # Reemplaza los valores por otros

print("nch" in animal)  # Nos dice si los caracteres se encuentran en una variable
print("nch" not in animal)

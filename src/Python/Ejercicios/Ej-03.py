# Hacer un programa que solicite la edad y determine si uno es mayor de edad o no.

salir = ""

while salir != "no":
    
    edad = int(input("Ingrese su edad: "))
    
    if edad >= 18:
        print("Usted es mayor de edad.")
    
    else:
        print("Usted es menor de edad.")
    
    salir = input("Desea verificar otra edad?('si','no'): ")
    
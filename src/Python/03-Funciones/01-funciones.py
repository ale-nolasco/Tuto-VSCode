#Dedinicion de funcion que imprime nombre y apellido

def hola( nombre, apellido = "Nolasco"):  #Valor por defecto en apellido en caso de no tenerlo
    
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")
    

# Argumentos Opcionales

hola("Alejandro") # En este caso no se pasa el argumento apellido, por lo que se toma el valor por defecto
hola("Alejandro", "Nolasco",) # En este caso se pasa el argumento apellido, por lo que se toma el valor que se paso
input() #Para hacer una pausa en el programa usamos

# Pasar Argumentos a funcion de manera dinamica

nombre = input("Cual es tu nomre?: ")
apellido = input("Cual es tu apellido?: ")
hola(nombre, apellido)
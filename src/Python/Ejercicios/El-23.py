def menu():
    
    print("1.- Ingresar segundos y verlo en Horas, Minutos y Segundos")
    print("2.- Ingresar horas, minutos y segundos y verlo en segundos")
    print("3.- Salir")
    opcion = int(input("Ingrese una opción: "))     
    return opcion

def seg():
    segundos = int(input("Ingrese los segundos: "))
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    print(f"Horas: {horas} Minutos: {minutos} Segundos: {segundos}")
    


def hms():
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    segundos = horas * 3600 + minutos * 60 + segundos
    print(f"El tiempo en segundos es: {segundos}")
    

def __main__():
    print("Programa que calcula tiempos")
    
    resp = menu()
    
    while resp < 1 or resp > 3:
        print("Opción no valida")
        resp = menu()
        
    if resp == 1:
        seg()
    elif resp == 2:
        hms()
    elif resp == 3:
        print("Adios")
    else:
        print("Opción no valida")
        __main__()
        
__main__()

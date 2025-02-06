import math

def area(radio):
    
    return 3.1416 * math.pow(radio, 2)

def perimetro(radio):
    
    return 2 * 3.1416 * radio

def main():
    
    radio = float(input('Ingrese el radio del circulo: '))
    
    print(f'El area del circulo es: {area(radio)} u^2')
    print('El perimetro del circulo es: ', perimetro(radio))
    
main()
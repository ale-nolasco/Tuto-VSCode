#Crea un función EscribirCentrado, 
# que reciba como parámetro un texto y lo escriba centrado en pantalla 
# (suponiendo una anchura de 80 columnas;  
# pista: deberás escribir 40 - longitud/2 espacios antes del texto). 
# Además subraya el mensaje utilizando el carácter =.

def EscribirCentrado(texto):
    print("{:=^80}".format(texto.center(80)))  # texto.center(80) centra el texto en 80 columnas
    

texto = input("Introduce un texto: ")
EscribirCentrado(texto)
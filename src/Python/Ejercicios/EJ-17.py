# Crea un función “ConvertirEspaciado”, 
# que reciba como par·metro un texto y devuelve una cadena 
# con un espacio adicional tras cada letra.
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
# Crea un programa principal donde se use dicha funciÛn.

def ConvertirEspaciado(texto):
    
    NewTexto = " ".join(texto)

    return NewTexto


Texto = input("Ingrese un texto: ")

print(ConvertirEspaciado(Texto))

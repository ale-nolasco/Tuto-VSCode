def es_palindromo(texto):
    Tex = texto.replace(" ","")
    print(Tex)
    Tex = Tex.lower()
    
    if Tex == Tex[::-1]:   # [::-1] es para invertir los elementos de una lista
        print("Es palindromo")
    else:
        print("No es palindromo")



texto = input("Ingrese un texto para saber si es palindromo:")

es_palindromo(texto)
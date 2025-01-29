#  Programa donde se ve com poder depurar el codigo
# En este caso un error en el retur el cual ya fue corregido
#

def largo(texto):
    
    resultado = 0
    for _ in texto:
        
        resultado += 1
    return resultado

print("Largo de un texto")
p = largo("Hola mundo")
print(p)


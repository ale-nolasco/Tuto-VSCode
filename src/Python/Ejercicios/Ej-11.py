# Hacer un programa donde se muestre el siguiente dibujo              
# *  *  *  *  *  *  *  *  *  *
# *                          *
# *                          *
# *                          *
# *  *  *  *  *  *  *  *  *  *

# Solucionen el problema anterior usando un solo ciclo for
for i in range(1,6):
    if i ==1 or i == 5:
        print("* " *10)
    else:
        print("*                 *")
        
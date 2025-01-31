# Hacer un programa que muestre el siguiente dibujo.
#  *  *  *  *  *  *  *  *  *  *        
#  *  *  *  *  *  *  *  *  *  *          
#  *  *  *  *  *  *  *  *  *  *          
#  *  *  *  *  *  *  *  *  *  *         
#  *  *  *  *  *  *  *  *  *  * 

for i in range(5):
    for j in range(10):
        print(" * ", end="")
    print("\n")
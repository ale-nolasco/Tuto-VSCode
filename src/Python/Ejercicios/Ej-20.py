# Crear una subrutina llamada “Login”, que recibe un nombre de usuario 
# y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1”
# y la contraseña es “asdasd”. Además recibe el número de intentos que se ha 
# intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una 
# contraseÒa y se intente hacer login, solamente tenemos tres oportunidades
# para intentarlo.


def Login():
    j = 0

    while j !=3:
        
        password = input("Ingrese su contraseña: ")
        
        if password == "asdasd":
            
            print("Contraseña correcta")
            
            return True
        
        else:
            
                
            print("Contraseña incorrecta")
                
            j += 1
                
    return False


print("Tienes 3 intentos antes de que se bloque el sistema")
i = 0

while i !=3:
    
    usuario = input("Ingrese su usuario: ")
    
    if usuario == "usuario1":
        
        if Login() == True:
            
            print("Bienvenido")
            break
        else:
            print("Sistema bloqueado")
            break
        
    else:
        
        print("Usuario incorrecto")
        
        i += 1
    
        if i == 3:
        
            print("Sistema bloqueado")
            break
def get_product(**datos): # '**' Podemos entrar en diferentes datos nombrando un atrubuto de ellos

    print(datos["id"], datos["name"])   # De est forma podemos imprir atributos especificos de producto 
    
    
get_product(id = "id", 
            name = "iphone",
            desc = "Esto es un iphone")
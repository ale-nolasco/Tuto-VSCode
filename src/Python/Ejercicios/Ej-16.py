TemMini = []
TemMaxi = []


def TempMedia(TemMin,TemMax):
    
        media = (TemMin + TemMax)/2
        
        return media


    
dias = int(input("Ingrese la cantidad de dias: "))
    
for i in range(1, dias+1):
        
    print("Dia", i)
    
    TemMini.append(float(input("Ingrese la temperatura minima: ")))
    TemMaxi.append(float(input("Ingrese la temperatura maxima: ")))
    print("")
    

for i in range(0, dias):
    
    print("Dia", i+1)
    print("Temperatura media: ", TempMedia(TemMini[i], TemMaxi[i]))
    print(" ")
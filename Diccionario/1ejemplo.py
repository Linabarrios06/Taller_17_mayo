        #Diccionario sobre colores 
diccionario = {"Rojo": "10", "Negro": "8", "Blanco": "6", "Azul": "5"} 
animales = ['Rojo','Azul','Negro','Verde']

for word in animales: #word  es el nombre del bucle 
    if word in diccionario:
        print(word, "->", diccionario [word])
    else: 
        print(word,"¨¨NO SE ENCUENTRA EN EL DICCIONARIO¨¨" ) # si, se escribe una palabra que no este en la lista saldra este letrero 
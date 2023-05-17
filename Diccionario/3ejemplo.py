#Diccionario sobre comidas rapidas 
diccionario = {"Alitas": "100%", "Hamburguesa": "89%", "Pizza": "75%", "Gaseosa": "70%"}
animales = ['Hamburguesa','Alitas','Salchipapa','Gaseosa']

for word in animales: #Word es el nombre del bucle 
    if word in diccionario:
        print(word, "->", diccionario [word])
    else: 
        print(word,"¨¨NO SE ENCUENTRA EN EL DICCIONARIO¨¨" ) # si, se escribe una palabra que no este en la lista saldra este letrero 
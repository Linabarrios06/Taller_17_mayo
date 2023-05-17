        #Diccionario sobre animales 
diccionario = {"Lora": "Rebeca", "Gato": "Tommy", "Cerdo": "Rosita", "Becerra": "Gabriela"}
animales = ['Becerra','Gato','Lora','Perro']

for word in animales: #Word es el nombre del bucle
    if word in diccionario:
        print(word, "->", diccionario [word])
    else: 
        print(word,"¨¨NO SE ENCUENTRA EN EL DICCIONARIO¨¨" )  # si, se escribe una palabra que no este en la lista saldra este letrero 



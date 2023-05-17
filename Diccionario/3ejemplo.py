#Diccionario sobre comidas rapidas 
diccionario = {"Alitas": "100%", "Hamburguesa": "89%", "Pizza": "75%", "Gaseosa": "70%"}
clave= "Alitas"
Valor= diccionario[clave]
comidas = ['Hamburguesa','Alitas','Salchipapa','Gaseosa'] #esta sirve para hacer varias consultas a la vez 
print(Valor)
#Esto no hace parte del diccionario pero sirve para buscar varios valores a la vez 
"""for word in comidas: #Word es el nombre del bucle  
    if word in diccionario:
        print(word, "->", diccionario [word])
    else: 
        print(word,"¨¨NO SE ENCUENTRA EN EL DICCIONARIO¨¨" )""" # si, se escribe una palabra que no este en la lista saldra este letrero 
        #Diccionario sobre colores 
diccionario = {"Rojo": "10", "Negro": "8", "Blanco": "6", "Azul": "5"} #("Rojo": es clave) ("10" es el valor )
clave= "Rojo"
Valor= diccionario[clave] #valor: 10
colores = ['Rojo','Azul','Negro','Verde']
print(Valor)
#Esto no hace parte del diccionario pero sirve para buscar varios valores a la vez 
"""for word in colores: #word  es el nombre del bucle 
     if word in diccionario:
         print(word, "->", diccionario [word])
     else: 
         print(word,"¨¨NO SE ENCUENTRA EN EL DICCIONARIO¨¨" )""" # si, se escribe una palabra que no este en la lista saldra este letrero 
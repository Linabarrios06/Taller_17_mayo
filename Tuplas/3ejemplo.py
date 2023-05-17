#duplas es una especie de lista 
tupla =(1,2,3,4,5,6,7,8,9,10) #Lista mas larga similar a la anterior 

indice =int(input("Dame un indice de 0 a 10 :  "))

if indice>=0 and indice<=len(tupla): #len: sirve para contar el numero de elementos que hay en una lista

    print(tupla[indice]) 

else :

    print("Indice no valido número fuera del rango x_x.... ") 

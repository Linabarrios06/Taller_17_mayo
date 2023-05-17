tupla =(1,2,3,4,5,6,7,8)

indice =int(input("Dame un indice:  "))

if indice>=0 and indice<=len(tupla): #len: sirve para contar el numero de elementos que hay en una lista 
    print(tupla[indice])

else :
    print("Indice no valido.... ")



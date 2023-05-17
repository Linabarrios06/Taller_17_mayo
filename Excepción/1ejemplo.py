#Error al no cerrar las comas 
print("Hola, ¡Mundo!) 
#No cerrar los parentesis 
n=4
print(8*n*(7)
#no dar un valor a variable 
print(sacha , "Ella es la mascota de susi")
#dividir al 0
print(12/0)
#No escribir un numero entero 
value = input("Ingresa un número entero: ")
print(10/value)
#
try:
    value = int(input("Ingresa un número entero: "))
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except:
    print("¨¨¨¨¨¨NOOO¨¨¨¨¨¨") #L arespuesta sera entrada erronea 


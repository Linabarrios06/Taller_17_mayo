#Excepción ZeroDivisionError
try:
    resultado = 18/0 
except ZeroDivisionError:
    print("Error: División por cero")
#Excepción IndexError
try:
    lista= ["rojo","Blanco","negro"]
    elemento= lista[azul]
except IndexError:
    print("Error: Indice fuera de rango")
#Excepción TypeError
try:
    resultado = '6'/ 2
except TypeError:
    print("Error: Tipo de dato incorrecto")
#Excepción KeyError
try: 
    diccionario= {'1': 'luna','2':'Sol'}
    valor= diccionario['3']
except KeyError:
  print("Error: valor no encontrado. ")
#Excepción GeneratorExit
try:
    resultado= 50/0
except  Exception as e:
    print("Ocurrio un error:", str(e))
except GeneratorExit:






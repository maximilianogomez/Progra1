#Notas Diccionarios:
#Relacionan: Clave-Valor
# se conocen tambien como arreglos asociativos de Hash

#NO SON SECUENCIAS, POR LO TANTO NO ESTAN ORDENADOS

#NO SE PUEDEN USAR INDICES PARA ACCEDER A LOS ELEMENTOS

#NO SE PUEDE APLICAR REBANADAS, YA QUE CARECEN DE ORDEN INTERNO (NO SON SECUENCIAS)

#LOS ELEMENTOS SE ACCEDEN MEDIANTE LAS CLAVES

#FORMATO:
#cada elemento se representa mediante una dupla: clave-valor
#se crean encerrando sus duplas entre llaves y separando por comas

edades = {"Juan": 23, "Maria": 18, "Marcelo": 30 }

#Las CLAVES deben pertenecer a un tipo inmutable (numeros, cadenas, tuplas)

#Los VALOLRES pueden ser de cualquier tipo incluso listas u otros diccionarios

colores = {"rojo": [255,0,0], "verde":[0,255,0], "azul": [0,0,255] }

#suelen escribirse con un formato mas claro y legible colocando una dupla debajo de otra

colores = {"rojo": [255,0,0],
           "verde":[0,255,0],
           "azul": [0,0,255]
           }
#se accede a un valor mediante una clave
print(edades["Marcelo"])

#un mismo valor puede estar asociado a mas de una clave. Por ejemplo:
edades = {"Juan": 23, "Maria": 18, "Marcelo": 30, "Pedro": 23 }
print(edades)

#Las claves deben ser UNICAS:
#En este caso la ultima clave repetida toma el valor y posicion de la anterior
edades = {"Juan": 23, "Maria": 18, "Marcelo": 30, "Pedro": 23, "Maria": 10 }
print(edades)

edades = {"Juan": 23, "Maria": 18, "Marcelo": 30, "Pedro": 23, "Maria": 25 }
print(edades)

#Asignar un valor a una clave reemplaza el valor existente o crea una clave nueva, dependiendo de si existe o no previamente la clave
colores = {"rojo": [255,0,0],
           "verde":[0,255,0],
           "azul": [0,0,255]
           }

colores["gris"] = [128,128,128]
print(colores)

#Si trato de acceder a un elemento con una clave inexistente, me provoca una excepcion KeyError

# Se puede utilizar el método
# get (<clave>)
# Retorna el valor asociado a la clave
# None
# si no existe la clave

colores = {"rojo": [255,0,0],
           "verde":[0,255,0],
           "azul": [0,0,255]
           }

print(colores.get("rojo"))

# El método
# get (<clave>, valor)
# Admite un segundo parámetro que será devuelto si
# No existe la clave

colores = {"rojo": [255,0,0],
           "verde":[0,255,0],
           "azul": [0,0,255]
           }

print(colores.get("amarillo","no existe"))

#ITEMS:
# El método
# items (<diccionario>)
# Retorna una lista de
# tuplas con clave,valor

colores = {"rojo": [255,0,0],
           "verde":[0,255,0],
           "azul": [0,0,255]
           }
for color in colores.items():
    print(color)
    
#SE PUEDE RECORRER UN DICCIONARIO:
# for clave in diccionario:
#     print("clave: ", clave, "valor: ", diccionario[clave])

for color in colores:
    print(color,"->",colores[color])

# El método
# keys (<diccionario>)
# Retorna una lista de todas las claves (iterable) y
# actúa como un conjunto

claves = colores.keys()
print(claves)

# El método
# values (<diccionario>)
# Retorna una lista con todos los valores

valores = colores.values()
print(valores)

# Para eliminar un elemento se puede utilizar la
# instrucción del
# Retorna excepción KeyError si no existe la clave

del colores["rojo"]

print(colores)

# La instrucción del Permite eliminar Todo el diccionario
try:
    colores = {"rojo": [255,0,0],
               "verde":[0,255,0],
               "azul": [0,0,255]
               }
    del colores
    print(colores)
except NameError as mensaje:
    print(mensaje)

# El método clear Permite vaciar el contenido del diccionario
colores = {"rojo": [255,0,0],
           "verde":[0,255,0],
           "azul": [0,0,255]
           }
colores.clear()
# Se puede utilizar la función
# len (<dic>)
colores = {"rojo": [255,0,0],
           "verde":[0,255,0],
           "azul": [0,0,255]
           }
print(len(colores))

#si convierto un diccionario a lista, y lo itero se obtienen las claves.



# Eliminar de una lista de palabras las palabras que se encuentren en una segunda
# lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

import random
lista1 = [random.randint(0,20) for i in range(15)]
lista2 = [random.randint(0,20) for i in range(15)]

print(lista1)
for x in lista2:
    y = lista1.count(x)
    for i in range(y):
        lista1.remove(x)
        
    #while x in lista1:
    #    lista1.remove(x)
        

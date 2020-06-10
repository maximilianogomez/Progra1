'''
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento.
'''

import random
#FUNCIONES:
def encajan(tupla1,tupla2):
    encajan = False
    i = 0
    j = 0
    while i < len(tupla1) and not encajan:
        while j < len(tupla2) and not encajan:
            if tupla1[i] == tupla2[j]:
                encajan = True
            j += 1
        i+= 1     
    return encajan

#PROGRAMA PRINCIPAL:
def main():
    tupla1 = (random.randint(1,6),random.randint(1,6))
    tupla2 = (random.randint(1,6),random.randint(1,6))
    if encajan(tupla1,tupla2):
        print(f"Las fichas {tupla1} y {tupla2} encajan")
    else:
        print(f"Las fichas {tupla1} y {tupla2} no encajan")

main()
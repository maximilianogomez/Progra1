# Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.

import random

#Funciones

def crearMatriz(n = 2):
    matriz = []
    for f in range(n):
        matriz.append([])
        for c in range(n): #supongo cuadrada
            matriz[f].append(random.randint(0,10))
    return matriz

def intercambiarColumnas(matriz,x,z):
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            if c == x:
                aux = matriz[f][c]
                matriz[f][c] = matriz[f][z]
                matriz[f][z] = aux
    
#Funcion principal:
def main():
    n = int(input("ingrese la cantidad de filas y columnas : "))
    matriz = crearMatriz(n)
    print(matriz)
    x = int(input("Ingrese que columna será cambiada: "))
    z = int(input("Ingrese que columna será cambiada: "))
    intercambiarColumnas(matriz,x,z)
    print(matriz)
#Programa Ppal:
if __name__ == "__main__":
    main()
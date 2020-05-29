import random

#Funciones:
def mostrarmatriz(matriz):
    for f in matriz:
        print(f)

def CrearMatriz(n=4):
    matriz = [[[None] for c in range(n)] for f in range(n)]
    return matriz

def RellenaMatriz(matriz):
    cont = 1    #cuadrada
    for c in range(len(matriz)):
        matriz[0][c] = cont
        cont += 1
    for f in range(1,len(matriz)):
        matriz[f][len(matriz)-1] = cont
        cont += 1
    for c in range(len(matriz) - 2, -1 ,-1):
        matriz[len(matriz)-1][c] = cont
        cont += 1
    for f in range(-2,-4,-1):
        matriz[f][0] = cont
        cont += 1
    for c in range(1,3):
        matriz[1][c] = cont
        cont += 1
    matriz[2][2] = cont
    cont +=1
    matriz[2][1] = cont
            
            

#Programa Principal:
def main():
    matriz = CrearMatriz()
    RellenaMatriz(matriz)
    mostrarmatriz(matriz)

main()
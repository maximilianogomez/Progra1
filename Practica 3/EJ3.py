# Desarrollar un programa para rellenar una matriz de N x N con números enteros al
# azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
# Imprimir la matriz por pantalla.

import random
#Funciones:
def mostrarmatriz(matriz):
    for f in matriz:
        print(f)

def ingresarpositivos(mensaje):
    nro = int(input(mensaje))
    while nro < 0:
        print("numero invalido")
        nro = int(input(mensaje))
    return nro

def CrearMatriz(n):
    matriz = []
    agregados = []
    for f in range(n):
        matriz.append([])
        for c in range(n):
            nro = random.randint(0,(n**2)-1)
            while nro in agregados:
                nro = random.randint(0,(n**2)-1)
            agregados.append(nro)
            matriz[f].append(nro)
    return matriz

#Programa Principal:
def main():
    n = ingresarpositivos("Ingrese de que NxN sera su matriz: ")
    matriz = CrearMatriz(n)
    mostrarmatriz(matriz)

main()
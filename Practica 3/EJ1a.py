# Desarrollar cada una de las siguientes funciones y escribir un programa que permita
# verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
# a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
# teclado.
#b. Ordenar en forma ascendente cada una de las filas de la matriz

#Funciones:
def crearMatriz(n=3,m=3):
    matriz = []
    for f in range(n):
        matriz.append([])
        for c in range(m):
            nro = int(input("Ingrese un numero: "))
            matriz[f].append(nro)
    return matriz

def mostrarmatriz(matriz):
    for filas in matriz:
        print(filas)

def ordenarasc(matriz):
    for filas in matriz:
        matriz.sort()

def intercambiardosfilas(matriz):
    n = int(input("Ingrese la fila a cambiar: "))
    m = int(input("Ingrese la fila a cambiar: "))
    for filas in matriz:
        aux = matriz[n]
        matriz[n] = matriz[m]
        matriz[m] = aux
    
def intercambiardoscolumnas(matriz):
    n = int(input("Ingrese la col a cambiar: "))
    m = int(input("Ingrese la col a cambiar: "))
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            aux = matriz[f][n]
            matriz[f][n] = matriz[f][m]
            matriz[f][m] = aux
            
def intercambiarfilasporcol(matriz): #misma filas y columna
    n = int(input("Ingrese la fila y columna a cambiar: "))
    for f in range(n+1):
        for c in range(len(matriz[0])):
            aux = matriz[f][c]
            matriz[f][c] = matriz[c][f]
            matriz[c][f] = aux

#def intercambiarfilasporcol(matriz):
#     n = int(input("Ingrese la fila a cambiar: "))
#     m = int(input("Ingrese una columna a cambiar: "))
#     for f in range(n+1):
#         for c in range(len(matriz[0])):


def trasponer(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux

def promedio_fila(matriz):
    nro = int(input("Ingrese el numnero de la fila a la cual le hayará el promedio: "))
    for i in range(len(matriz[0])):
        prom = sum(matriz[nro])/3 # por ser matriz de 3 por 3
    return prom

def porcentaje(matriz):
    n = int(input("Dame el numero de la columna a analizar el porcentaje de impares: "))
    impares = 0
    for f in range(len(matriz)):
        if matriz[f][n] % 2 != 0:
            impares += 1
    porcentaje = (impares * 100) / len(matriz) #Porque tengo 3 elementos en la columna
    return porcentaje

def simdiagprincipal(matriz):
    esSim = True
    f = 0
    while f < len(matriz) and esSim:
        c = 0
        while c < len(matriz[0]) and esSim:
           if matriz[f][c] != matriz[c][f]:
               esSim = False
            c+= 1
        f+= 1
    return esSim


#Programa Principal:
def main():
    print("TP3.EJ1a")
#   matriz = crearMatriz()
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    mostrarmatriz(matriz)
    print()
#    trasponer(matriz)
#    mostrarmatriz(matriz)
    print()
#    prom = promedio_fila(matriz)
#    print(prom)
    print()
    imparespor = porcentaje(matriz)
    print("%.2f" %imparespor , end = "%")
    simdiagp = simdiagprincipal(matriz)
    print(simdiagp)
#   ordenarasc(matriz)
#   print()
#   mostrarmatriz(matriz)
#   print()
#   intercambiardosfilas(matriz)
#   print()
#   mostrarmatriz(matriz)
#   print()
#   intercambiardoscolumnas(matriz)
#   print()
#   mostrarmatriz(matriz)
#   print()
#   intercambiarfilasporcol(matriz)
#   mostrarmatriz(matriz)
#   print()


if __name__ == "__main__":
    main()
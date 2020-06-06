# Realizar una función recursiva para imprimir una matriz de M x N.

#FUNCIONES:
def imprimir_matriz(matriz, f = 0, c = 0):
    if f == len(matriz)-1 and c == len(matriz[0]):
        print()
        return None
    else:
        if c == len(matriz[0]):
            print()
            return imprimir_matriz(matriz, f + 1 , c = 0)
        else:
            print("%3d" %matriz[f][c], end = "")
            return imprimir_matriz(matriz, f , c + 1)

#PROGRAMA PRINCIPAL:
def main():
    matriz = [ [1, 2 , 3],
               [2 , 4 , 6],
               [7, 8 , 9] ]
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()
#Determinar si la matriz es simétrica con respecto a su diagonal secundaria.

def simdiagsecundaria(matriz):
    esSim = True
    f = 0
    while f < len(matriz) and esSim:
        c = len(matriz[0])-1
        while c > len(matriz[0])-(f+1) and esSim:
            if matriz[f][c] != matriz[c][f]:
                esSim = False
            c-= 1
        f+= 1
    return esSim

def matriz_simetrica_sec(matriz):
    sim=True
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range (-1,columnas-(f+1)):
            if matriz[f][c]!=matriz[c][f]:
                sim=False
    return sim

def mostrarmatriz(matriz):
    for filas in matriz:
        print(filas)

def main():
    print("TP3.EJ1a")
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    simdiags = simdiagsecundaria(matriz)
    print(simdiags)
    mostrarmatriz(matriz)

if __name__ == "__main__":
    main()
    
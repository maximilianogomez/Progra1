def simdiagprincipal(matriz):
    esSim = True
    f = 0
    while f < len(matriz) and esSim:
        c = 0
        while c < len(matriz[0]) and esSim:
            if matriz[f][c] != matriz[c][f] and f!=c:
                esSim = False
            c+= 1
        f+= 1
    return esSim

def main():
    print("TP3.EJ1a")
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    simdiagp = simdiagprincipal(matriz)
    print(simdiagp)

if __name__ == "__main__":
    main()
    
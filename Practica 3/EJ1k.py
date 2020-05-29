# Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
# una lista con los números de las mismas.

def capicuas1(matriz):
    lista = []
    z = len(matriz) - 1
    acum = 0
    for c in range(len(matriz[0])):
        acum = 0
        z = len(matriz) - 1
        for f in range(len(matriz)//2):
            if matriz[f][c] == matriz[z][c] :
                acum += 1
                if acum == len(matriz) //2:
                    for j in range(len(matriz)):
                        if matriz[j][c]:
                            lista.append(matriz[j][c])
            z -=1
    return lista


def mostrarmatriz(matriz):
    for filas in matriz:
        print(filas)

def main():
    print("TP3.EJ1a")
    matriz = [[1,2,3],[4,5,6],[7,8,9],[4,5,7],[1,2,3]]
    matriz2 = [[1,2,5],[4,5,6,],[1,9,5]]
    mostrarmatriz(matriz2)
    lista = capicuas1(matriz2)
    print("La lista con los valores capicua")
    print(lista)

if __name__ == "__main__":
    main()
    
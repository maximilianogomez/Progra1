def crearMatriz(n = 4):
    filas = n
    col = n
    matriz = [ [0] * col for f in range(filas)]
    return matriz
    
def RellenarMatriz(matriz):
    cant = len(matriz)                   
    for f in range(len(matriz)):
        for c in range(len(matriz)-(cant-1)):
            matriz[f][c] = cant
        cant -= 1
        
def imprimirMatriz(matriz):
    'Imprime la matriz con formato'
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            print("%3d" %matriz[f][c],end="")
        print()
    
def main():
    n = int(input("Ingrese el numero de filas y columnas que tendra su matriz: "))
    matriz = crearMatriz()
    RellenarMatriz(matriz)
    imprimirMatriz(matriz)
    
main()
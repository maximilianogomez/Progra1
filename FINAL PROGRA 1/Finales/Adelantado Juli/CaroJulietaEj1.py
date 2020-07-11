# Para la siguiente matriz, desarrollar una función que la genere y escribir un programa que invoque y muestre por
# pantalla la matriz obtenida. El tamaño de las matriz debe establecerse como N x N, y la funcion debe servir aunque este
# valor se modifique.
def crearMatriz(N = 4):
    'Crea matriz de NxN'
    matriz = [[0]*N for f in range(N)]
    return matriz

def llenarMatriz(matriz):
    '''Llena la matriz con los valores correspondientes.
    matriz ya creada pasada por parámetro

    '''
    cont = len(matriz)
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            if c<=f:
                matriz[f][c]=cont
        cont-=1

def imprimirMatriz(matriz):
    'Imprime la matriz con formato'
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            print("%3d" %matriz[f][c],end="")
        print()
        
def main():
    'Programa principal'
    matriz = crearMatriz()
    llenarMatriz(matriz)
    imprimirMatriz(matriz)

main()
    
# Escribir una función que sume todos los elementos de una matriz de M x N y devuelva
# el resultado.

#FUNCIONES:
def sumar_matriz(matriz, f = 0, c = 0):
    if f == len(matriz)-1 and c == len(matriz[0]):
        return 0
    else:
        if c == len(matriz[0]):
            return sumar_matriz(matriz, f + 1 , c = 0)
        else:
            return matriz[f][c] + sumar_matriz(matriz, f , c + 1)
        
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
               [4 , 5 , 6],
               [7, 8 , 9] ]
    print("La matriz es: ")
    imprimir_matriz(matriz)
    print("la suma de todos los elementos de la matriz es : ")
    print(sumar_matriz(matriz))
    
if __name__ == "__main__":
    main()
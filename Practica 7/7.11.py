# Desarrollar una función que devuelva el elemento de valor mínimo de una matriz
# de M x N.

#FUNCIONES:
def minimo_matriz(matriz, f = 0, c = 0, minimo= 9999):
    if f == len(matriz)-1 and c == len(matriz[0]):
        return minimo
    else:
        if c == len(matriz[0]):
            return minimo_matriz(matriz, f + 1 , c = 0, minimo = minimo)
        else:
            if matriz[f][c] < minimo:
                return minimo_matriz(matriz, f , c + 1, matriz[f][c])
            else:
                return minimo_matriz(matriz, f , c + 1, minimo)
            
def minimo_matriz2(matriz, f = 0,minimo= 9999):
    if f == len(matriz)-1:
        return minimo
    else:
        menor_fila = min(matriz[f])
        if menor_fila < minimo:
            return minimo_matriz2(matriz, f + 1, menor_fila)
        else:
            return minimo_matriz2(matriz, f + 1, minimo)
            
        
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
    print("el minimo elemento de la matriz es : ")
    print(minimo_matriz(matriz))
    
if __name__ == "__main__":
    main()
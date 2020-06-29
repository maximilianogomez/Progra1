from random import randint as r
#Funciones:
def IngresarPositivos(mensaje):
    nro = int(input(mensaje))
    while n < 0 :
        print("numero inválido")
        nro = int(input(mensaje))
    return nro


def MostrarMatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d"%matriz[f][c],end=" ")
        print()

def Matriz(n, x = 100, y = 999):
    matriz = []
    for f in range(n):
        matriz.append([])
        for c in range(n):
            nro = r(x,y)
            matriz[f].append(nro)
    return matriz

def doblediagp(matriz):
    lista = [matriz[f][f] * 2  for f in range(len(matriz))]
    return lista
def AgregarTriangularInf(matriz,lista):
    for f in range(len(lista)):
        for c in range(f):
            if f != c:
                lista.append(matriz[f][c])
                
def eliminarvalores(lista,prom):
    y = len(lista)-1
    while y >= 0:
        if lista[y] > prom:
            lista.pop(y)
        y-=1
        
def eliminarvalores2(lista,prom):
    for i in range(len(lista)-1,-1,-1):
        if lista[i] > prom:
            lista.pop(i)
    
def CalcularPromedio(lista):
    return sum(lista)//len(lista)

#Programa Principal:
def main():
    NumAlAzar = (lambda x = 1, y = 5: r(x,y))
    cantElementos = NumAlAzar()
    matriz = Matriz(cantElementos)
    lista = doblediagp(matriz)
    MostrarMatriz(matriz)
    print("la matriz es de :", cantElementos, "x", cantElementos)
    print()
    print(lista)
    AgregarTriangularInf(matriz,lista)
    print("La lista modificada es: ")
    print(lista)
    prom = CalcularPromedio(lista)
    print("El promedio es: ",prom)
    eliminarvalores2(lista,prom)
    print()
    print("La lista con los valores eliminados es: ")
    print(lista)
    

if __name__ == "__main__":
    main()
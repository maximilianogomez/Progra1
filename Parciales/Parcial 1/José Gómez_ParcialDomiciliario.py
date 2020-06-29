from random import randint as r

#Funciones:
comparar = (lambda x , y: True if x > y else False)


def IngresarPositivo(mensaje):
    'Comprueba que el numero sea mayor o igual a 0'
    nro = int(input(mensaje))
    while nro < 0:
        print("El numero ingresado es inválido")
        nro = int(input(mensaje))

    return nro

def CrearMatriz(n, m = 6):
    'Crea una matriz de ceros, por defecto la crea con 6 columnas, ya que representan los meses de un semestre'
    if n == 0:
        matriz = [[]]
    else:
        filas = n
        col = m
        matriz = []
        for f in range(filas):
            matriz.append([0] * m)
        return matriz
    
def RellenarMatriz(matriz , x = 100, y = 1500):
    'Rellena la matriz de numeros, por omisión las rellena de elementos entre 100 y 1500'
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            nro = r(x,y)
            matriz[f][c] = nro
            
def imprimirMatriz(matriz):
    'muestra una matriz por pantalla'
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%7d" %matriz[f][c], end = "")
        print()

def Compararmeses(matriz):
    """
    Recorre la matriz comparando  mes a mes cada producto, y si hubo un decrecimiento de ese producto en el mes se agrega a una lista donde luego se compara
    la cantidad de productos que quedaron en negativo, si es mayor a la mitad entrega que hubo un total decreciente
    
    Devuelve un valor booleano que dice si hubo un decrecimiento general en todos los meses de todos los productos o no, recibe una matriz
    
    Parámetros:
    matriz : una lista de listas
    """
    decr = 0
    productos = []
    esDecr = False
    TotalDecr = False
    for f in range(len(matriz)):
        esDecr = False
        for c in range(len(matriz[0])):
            if c+1 <= (len(matriz[0])-1) and comparar(matriz[f][c], matriz[f][c+1]):
                decr += 1
            if decr >= (len(matriz[0])//2):
                esDecr = True
                productos.append(f)
        if len(productos) >= (len(matriz)//2):
            TotalDecr = True
    return TotalDecr
        
                
def mes_menor(matriz):
    """
    Recorre por mes la cantidad total de productos vendidos.
    Devuelve el mes donde se vendio menos cantidad de productos y recibe una matriz
    Parámetros:
    matriz : lista de listas
    """
    suma = 0
    menor_mes = 0
    for c in range(len(matriz[0])):
        suma = 0
        for f in range(len(matriz)):
            suma = suma + matriz[f][c]
            if suma < menor_mes:
                menor_mes = suma 
    return menor_mes

def producto_mayor(matriz,minimes):
    """
    Recorre el mes donde menos se vendió dando la cantidad del producto que mas se vendió
    Devuelve el producto que mas se vendió en el mes donde menos se vendió, recibe como parametros una matriz y el mes donde menos se vendio
    Parámetros:
    matriz : lista de listas
    minimes : numero entero positivo
    """
    mayor = 0
    for f in range(len(matriz)):
        if matriz[f][minimes] > mayor:
            mayor = matriz[f][minimes]
    return mayor

def lista_meses(matriz):
    """
    El objetivo es hacer una lista par y otra lista impar donde cada elemento es la suma de todos los productos vendidos en ese mes
    discriminando si ese mes fue par o impar.
    Devuelve dos listas con los meses pares y los impares y recibe por parametro una matriz.
    Parámetros:
    matriz : lista de listas
    """
    pares = []
    impares = []
    acum = 0
    for c in range(len(matriz[0])):
        acum = 0
        for f in range(len(matriz)):
            acum += matriz[f][c]
        if c % 2 == 0:
            pares.append(acum)
        else:
            impares.append(acum)
    return pares, impares
        
def Promedio(lista):
    'Retorna el promedio de una lista'
    return sum(lista) / len(lista)


#Programas Principales:
def main():
    print("1")
    n = IngresarPositivo("Ingrese un numero mayor o igual a 0: ")
    if n != 0:
        matriz = CrearMatriz(n)
        RellenarMatriz(matriz = matriz)
        imprimirMatriz(matriz)
        print("2")
        TotalesDecr =  Compararmeses(matriz)
        if TotalesDecr:
            print("El total de ventas es decreciente")
        else:
            print("El total de ventas es creciente")
        print("3")
        mesMinimo = mes_menor(matriz)
        mayorproducto = producto_mayor(matriz,mesMinimo)
        print("El mes donde menos se vendió fue el: ", mesMinimo)
        print("El producto que mas se vendió en ese mes fue: ", mayorproducto)
        print("4")
        pares, impares = lista_meses(matriz)
        listafinal = pares + impares
        print("La lista pares es: ", end =" ")
        print(pares)
        print("La lista impares es: ", end =" ")
        print(impares)
        print("La lista final es: ", end =" ")
        print(listafinal)
        prom = Promedio(listafinal)
        print("El promedio es: ", prom)
        filtrada = list(filter( lambda x : x < prom, listafinal))
        print("La lista filtrada es: ", end = " ")
        print(filtrada)
    else:
        print("La matriz está vacia, no hay ningun producto que se vendió ")

if __name__ == "__main__":
    main()

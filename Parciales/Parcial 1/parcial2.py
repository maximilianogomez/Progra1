
from random import randint as r
#Funciones:
def GenerarMatriz(n = 4):
    'Devuelve una matriz n x n llenas de ceros, tiene un valor por omisión de 4'
    matriz = []
    for f in range(n):
      matriz.append([0] * n)
    return matriz

def Rellenar(m, x = 100, y = 999):
    """
    Rellena la matriz con numeros de rango x e y
    Devuelve una matriz con numeros
    Parámetros:
    m = matriz, lista de listas
    x = numero entero positivo, por defecto es 100
    y = numero entero positivo, por defecto es 999
    """
    lista = []
    for f in range(len(m)):
        for c in range(len(m[0])):
            nro = r(x,y)
            while nro in lista:
                nro = r(x,y)
            m[f][c] = nro
            lista.append(nro)

def Validación(mensaje):
    'Valida que el número este entre 0 y 20'
    nro = int(input(mensaje))
    while nro < 0 or nro > 20:
        print("numero invalido ")
        nro = int(input(mensaje))
    return nro

def Mayordiagp(matriz):
    'Recorre las filas y me dice el mayor numero de la diagonal principal y la cantidad de veces que aparece'
    mayor = 0
    cant = 1
    for f in range(len(matriz)):
        if matriz[f][f] > mayor:
            mayor = matriz[f][f]
        elif matriz[f][f] == mayor:
            cant +=1
    return mayor,cant

def MostrarMatriz(matriz):
    'Muestra la matriz por pantalla'
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d"%matriz[f][c],end=" ")
        print()
        
def ListaDiagSup(matriz):
    'Añade todos los elementos de la diagonal superior a una lista, incluidos los elementos de la diagonal principal'
    lista = []
    for f in range(len(matriz)):
        for c in range(len(matriz)-1,f-1,-1):
            lista.append(matriz[f][c])
    return lista
            
def cantidadDigitos(num):
    'Cuenta la cantidad de digitos'
    cont = 0
    while num > 0:
        num //= 10
        cont += 1
    return cont

def DigitoCentralImpar(num):
    'Halla el digito central y lo analiza para ver si es o no Impar'
    digitos = cantidadDigitos(num)
    central = digitos //2
    for i in range(central):
        num = num // 10
    digito = num % 10
    if digito % 2 != 0:
        esImpar = True
    else:
        esImpar = False
    return esImpar

#Programa Principal:
def main():
    n = Validación("Ingrese un numero para generar una matriz de NxN: ")
    matriz = GenerarMatriz(n)
    Rellenar(m = matriz)
    MostrarMatriz(matriz)
    mayor,cant = Mayordiagp(matriz)
    print()
    print("El numero mayor de la diagonal principal es: ", mayor, "y la cantidad de veces que aparece es: ", cant)
    print()
    lista = ListaDiagSup(matriz)
    print(lista)
    print("La lista filtrada es: ")
    filtrada = list(filter(DigitoCentralImpar, lista))
    print(filtrada)
    
if __name__ == "__main__":
    main()
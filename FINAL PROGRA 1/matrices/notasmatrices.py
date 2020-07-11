#Apunte Matrices:
#Crear matrices:
def CrearMatriz(n = 3, m = 4):
    filas = n                                       #matriz = [[0,0,0,0],
    col = m                                                    #[0,0,0,0],
    matriz = []                                                 #[0,0,0,0]
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(0)
    return matriz

#tecnica de replicación de elementos: (se usa si todos los elementos de la columna tienen el mismo valor)
def CrearMatriz(n = 3, m = 4):
    filas = n                                       #matriz = [[0,0,0,0],
    col = m                                                    #[0,0,0,0],
    matriz = []                                                 #[0,0,0,0]
    for f in range(filas):
        matriz.append([0] * col)                     #solo lo usamos para replicar columnas
    return matriz

#matriz por comprension:
filas = 3
col = 4
matriz = [ [0] * col for f in range(filas)]

#rellenar matrices:
def RellenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])                    #se analiza la longitud de la fila 0 (se ven todas las columnas de esa fila y como es matriz todas tienen las mismas col)
    for f in range(filas):
        for c in range(columnas):
            n = int(input("Ingrese un numero: "))
            matriz[f][c] = n
        
#Imprimir matriz por pantalla:
def imprimirMatriz(matriz):
    'muestra una matriz por pantalla'
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end = "")
        print()
    
def imprimirMatrizOperadorIn(matriz):  #queda mas piola si todos los numeros tienen la misma cantidad de digitos
    'muestra una matriz por pantalla'
    for filas in matriz:
        print(fila)

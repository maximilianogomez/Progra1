#EXAME A ENTREGAR
import random
"""
Una linea de ropa deportiva cuenta con N productos para la venta, cuenta con un listado donde se visualiza para
cada mes del año pasado la cantidad total de ventas por producto.
El archivo adjunto presenta un ejemplo.

Se solicita creando al menos una función para cada informe:
1.    Crear una matriz para representar las ventas de cada producto por mes,
creando al azar las cantidades vendidas de N productos para el primer semestre (Enero-Junio).
Considerando que la cantidad máxima de ventas es de 1500 unidades y N se obtiene por teclado cuidando
que sea positivo.  (25%)"""

"""
2.   Cuál fue el mes que realizó la menor cantidad de ventas, dentro de ese mes cuál es el producto que menos
se vendió.
(En lo posible mostrar el nombre del mes utilizando  una lista de los nombres de los meses.) (25%)

3.  Determinar si las ventas totales van en aumento continuo en el primer trimestre para todos los productos.
En caso afirmativo normalizar ese producto. ( crearlo en una lista aparte)(25%)

4.  Crear una lista con las cantidades vendidas por cada mes comenzando por los meses pares y a
continuacion los meses impares.
Filtrar las cantidades que son menores al promedio de ventas. (25%)

"""

mes=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
semestre1=['enero','febrero','marzo','abril','mayo','junio']
def ventas_sem1(n):
    filas=n
    columnas=6
    matriz=[[0]*columnas for i in range(filas)]
    
    for f in range (len(matriz)):
        for c in range (len(matriz[0])):
            x=random.randint(1000,1500)
            matriz[f][c]=x
    return matriz
def ingresar_positivo():
    n=int(input("Ingresar num positivo :"))
    while n<1:
        print("error num erroneo.")
        n=int(input("ingresar num positivo :"))
    return n
def mostrar_matriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d"%matriz[f][c],end=" ")
        print()
        
def menor_vendido(matriz):
    lista_menor=[]
    menor=matriz[0][0]
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c]<menor:
                menor=matriz[f][c]
                lista_menor.clear()
                lista_menor=["producto:",f, "mes:",c]
    return menor,lista_menor

def normalizar_ventas_crecientes(matriz):
    aumen = 0
    productos = []
    columna = len(matriz[0])
    for f in range(len(matriz)):
        for c in range(columna):
            if c+1 <= ((columna //2)-1) and matriz[f][c] < matriz[f][c+1]:
                aumen += 1
            if aumen == 3:    
    return productos
                
    suma=sum(lista)
    lista2=[]
    for i in lista:
        lista2.append(i/suma)
    return lista2               
            
            
def cant_vendidas_pi(matriz):
    lista=[]
    par=[]
    impar=[]
    suma=0
    for c in range(len(matriz[0])):
        suma=0
        for f in range(len(matriz)):
            suma =suma + matriz[f][c]
        if c%2 == 0:
            par.append(suma)
        else:
            impar.append(suma)
    for x in (par):
        lista.append(x)
    for j in (impar):
        lista.append(j)
    
    return lista
    
def promedio(lista):
    suma=sum(lista)
    p=suma/len(lista)
    return p
            

            

def main():
    #1
    n=ingresar_positivo()
    ej1=ventas_sem1(n) #matriz
    mostrar_matriz(ej1)
    
    #2
    ej2=menor_vendido(ej1)
    print("cantidad de veces vendidas:")
    print(ej2)
    
    #3
    ej3=normalizar_ventas_crecientes(ej1)
    print(ej3)
    
    #4
    ej4=cant_vendidas_pi(ej1)
    print(ej4)
    prom=promedio(ej4)
    print(prom)
    filtrado=list(filter(lambda x : x > prom, ej4))
    print(filtrado)
    
    
            
    
if __name__=="__main__":
    main()
    
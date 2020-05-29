# Generar dos listas con M y N números al azar entre 1 y 50 y construir una tercera
# lista cuyos elementos sean el resultado de la intersección de las dos listas dadas.
# # Los valores de M y N se obtienen al azar. Imprimir las tres listas por pantalla

from random import randint as r
#Funciones:
def GenerarListas():
    '''Genera las dos listas pedidas'''
    m = r(1,10)
    n = r(1,10)
    lista1 = [r(1,50) for i in range(m)]
    lista2 = [r(1,50) for z in range(n)]
    return lista1, lista2

def ListaInterseccion(lista1,lista2):
    '''Genera una lista con los elementos de la intersección de otras dos dadas como parámetros'''
    lista3 = []
    for num in lista1:
        for nume in lista2:
            if num == nume and num not in lista3:
                lista3.append(num)
    return lista3

#Programa Principal:
def main():
    print("TP2.EJ8: construir una tercera lista cuyos elementos sean el resultado de la intersección de las dos listas dadas")
    lista1, lista2 = GenerarListas()
    lista3 = ListaInterseccion(lista1,lista2)
    print("La primera lista es: ")
    print(lista1)
    print("La segunda lista es: ")
    print(lista2)
    print("La tercera lista es: ")
    print(lista3)
    
if __name__ == "__main__":
    main()
# Generar dos listas con M y N números al azar entre 1 y 50 y construir una tercera
# lista cuyos elementos sean el resultado de la intersección de las dos listas dadas.
# Los valores de M y N se obtienen al azar. Imprimir las tres listas por pantalla.
import random

def ListaInterseccion(lista1=[], lista2=[]):
    '''Genera un nueva lista con la interseccion de las listas recibidas, sin duplicados.
    
    '''
    lista3 = []
    for x in lista1:
        if x in lista2 and x not in lista3:
            lista3.append(x)
    
    return lista3

lista1 = [random.randint(1,50) for i in range(random.randint(15,25))]
lista2 = [random.randint(1,50) for i in range(random.randint(15,25))]
lista3 = ListaInterseccion(lista1, lista2)

print(lista1)
print(lista2)
print(lista3)
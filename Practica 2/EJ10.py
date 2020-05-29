# Generar una lista con números al azar entre 0 y 100, donde su cantidad de elementos
# será un número par también obtenido al azar entre 10 y 50. Luego se solicita
# partir la lista por la mitad a través de la técnica de las rebanadas, creando dos
# nuevas listas. Imprimir las tres listas por pantalla.

from random import randint as r

#Funciones:
def GenerarLista():
    '''Crea una lista de 10 a 50 elementos con valores entre 0 y 100'''
    num = r(10,50)
    while num % 2 != 0:
        num = r(10,50)
    lista = [r(0,100) for i in range(num)]
    return lista

def PartirLista(lista):
    '''Crea rebanadas de la mitad de la lista'''
    listareb1 = lista[ : len(lista)//2]
    listareb2 = lista[len(lista)//2 : ]
    return listareb1, listareb2
        
#Programa Principal:
def main():
    print("TP2.EJ10")
    lista = GenerarLista()
    print(lista)
    listareb1, listareb2 = PartirLista(lista)
    print(listareb1)
    print(listareb2)

if __name__ == "__main__":
    main()
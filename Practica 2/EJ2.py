from random import randint as r

def GenerarListaRandom():
    '''Genera una lista de 50 elementos aleatorios entre 1 y 100'''
    lista = []
    for x in range(50):
        lista.append(r(1,100))
    return lista


def TieneRepetidos2(lista):
    ''' Me dice si una lista tiene un valor repetido '''
    i=0
    while i< len(lista) and lista.count(lista[i]) <=1:
        i += 1
    return i != len(lista) #True si i es menor que len(lista)

def ListaUnicos(lista):
    '''Genera una lista con los valores unicos '''
    unicos = []
    for num in lista:
        if num not in unicos:
            unicos.append(num)
    return unicos

def main():
    print("TP2:EJ2")
    #2a
    lista = GenerarListaRandom()
    #2b
    print(lista)
    if TieneRepetidos2(lista):
        print("La lista tiene elementos repetidos")
    else:
        print("La lista no tiene elementos repetidos")
    #2c
    unicos = ListaUnicos(lista)
    print("La lista con los valores unicos es: ")
    print(unicos)
    
if __name__ == "__main__":
    main()
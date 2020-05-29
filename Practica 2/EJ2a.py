#Generar una lista de 50 números aleatorios del 1 al 100.

from random import randint as r

def GenerarListaRandom():
    '''Genera una lista de 50 elementos aleatorios entre 1 y 100'''
    lista = []
    for x in range(50):
        lista.append(r(1,100))
        
    return lista
        
def main():
    print("Ejercicio 2.2a: Generar una lista de 50 números aleatorios del 1 al 100.")
    lista = GenerarListaRandom()
    print(lista)
    
if __name__ == "__main__":
    main()
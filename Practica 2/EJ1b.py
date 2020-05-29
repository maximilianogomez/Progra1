#b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.

from EJ1a import generarLista2


#Programa Principal:
def main():
    print("EJ2.1b: Calcular y devolver la sumatoria de todos los elementos de la lista anterior.")
    lista = generarLista2() #si solo ponia import EJ1a tenia que poner EJ1a.generarLista2()
    print("La lista pedida es: ")
    print(lista)
    suma = sum(lista)
    print("La sumatoria es: ",suma)

if __name__ == "__main__":
    main()
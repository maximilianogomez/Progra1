# Desarrollar cada una de las siguientes funciones y escribir un programa que permita
# verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
# a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos
# también será un número al azar de dos dígitos.

from random import randint as r

#Funciones:
def generarLista1():
    lista = []
    for i in range(r(11,101)):
        nro = r(1000,9999)
        lista.append(nro)
    return lista
        
def generarLista2(): #lista por comprension
    lista = [r(1000,9999) for i in range(r(11,101))]
    return lista


#Programa Principal:
def main():
    print("EJ2.1a: Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.")
    lista = generarLista2()
    print("La lista pedida es: ")
    print(lista)

if __name__ == "__main__":
    main()
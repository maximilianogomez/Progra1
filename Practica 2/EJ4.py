# Definir una función superposición() que reciba como parámetros dos listas de cualquier
# tipo y devuelva True si tienen al menos un elemento en común, o False en
# caso contrario. Desarrollar un programa para verificar su comportamiento.

import EJ2

#Funciones:
def superposicion(lista1,lista2):
    booleano = False
    i = 0
    j = 0
    while i < len(lista1) and not booleano:
        while j < len(lista2) and not booleano:
            if lista1[i] == lista2[j]:
                booleano = True
            j += 1
        i += 1
    return booleano

#Programa Principal:
def main():
    print("TP2: EJ4")
    lista1 = EJ2.GenerarListaRandom()
    lista2 = EJ2.GenerarListaRandom()
    print("La lista1 es: ")
    print(lista1)
    print("La lista2 es: ")
    print(lista2)
    if superposicion(lista1,lista2):
        print("La lista tiene al menos un elemento en común")
    else:
        print("La lista no tiene elementos en común")
        
if __name__ == "__main__":
    main()
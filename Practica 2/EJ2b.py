# Recibir una lista como parámetro y devolver True si la misma contiene algún
# elemento repetido. La función no debe modificar la lista.

import EJ2a
#Funciones:
def TieneRepetidos1(lista): #metodo burbuja mejorada
    ''' Me dice si una lista tiene un valor repetido '''
    repetidos = False
    x = 0
    iteraciones = 0
    while x < len(lista) and not repetidos:
        y = x + 1
        while y < len(lista) and not repetidos:
            if lista[x] == lista[y] : repetidos = True
            y += 1
            iteraciones += 1
        x += 1
    return repetidos, iteraciones

def TieneRepetidos2(lista):
    ''' Me dice si una lista tiene un valor repetido '''
    repetidos = False
    iteraciones = 0
    for num in lista:
        cant = lista.count(num)
        if cant > 1 :
            repetidos = True
            return repetidos, iteraciones
        iteraciones += 1
    return repetidos, iteraciones

#Programa Principal:
def main():
    print("Ejercicio 2.2b: Generar una funcion que devuelva True si la misma tiene elementos repetidos")
    lista = EJ2a.GenerarListaRandom()
    print(lista)
    rep1 , iteraciones1 = TieneRepetidos1(lista)
    rep2 , iteraciones2 = TieneRepetidos2(lista)
    if TieneRepetidos1(lista):
        print("La lista tiene elementos repetidos")
        print("La cantidad de iteraciones que realiza el metodo1 son: ", iteraciones1)
    else:
        print("La lista no tiene elementos repetidos")
    if TieneRepetidos2(lista):
        print("La lista tiene elementos repetidos")
        print("La cantidad de iteraciones que realiza el metodo2 son: ", iteraciones2)
    else:
        print("La lista no tiene elementos repetidos")
    
if __name__ == "__main__":
    main()
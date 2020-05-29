# Escribir un programa que calcule la suma acumulada a partir de una lista de números.
# El programa debe generar una nueva lista donde el primer elemento es el mismo
# de la lista original, el segundo elemento es la suma del primero más el segundo,
# el tercer elemento es la suma del primero más el segundo más el tercero y así
# sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1,3,6].

from EJ2 import GenerarListaRandom as genlis

#Funciones:
def lista_acum(lista):
    acum = []
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
        acum.append(suma)
    return acum

#Programa Principal:
def main():
    print("TP2:EJ5")
    #lista = genlis()
    lista = [1,2,3]
    print("La lista generada es: ")
    print(lista)
    lista2 = lista_acum(lista)
    print("La lista con los numeros acumulados es: ")
    print(lista2)
    
if __name__ == "__main__":
    main()
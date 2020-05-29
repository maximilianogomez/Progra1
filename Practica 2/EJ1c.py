#1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita
#verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
#c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
#se ingresa desde el teclado y la función lo recibe como parámetro.

from EJ1a import generarLista2
#Funciones:
def borrar_valor(lista,num):
    """
    Borra un valor ingresado en la lista
    
    Devuelve la lista sin el valor ingresado y el valor de encontrado
    
    Parámetros:
    numero -- numero entero positivo que se quiere borrar en la lista
    
    lista -- iterable de donde se borrará el valor solicitado
    
    """
    
    encontrado = True
    if num in lista:
        cant = lista.count(num)
        while cant > 0:
            lista.remove(num)
            cant -= 1
    else:
        encontrado = False
    return encontrado
            
#Programa Principal:
def main():
    print("EJ2.1c: Eliminar todas las apariciones de un valor en la lista anterior")
    lista = generarLista2() #si solo ponia import EJ1a tenia que poner EJ1a.generarLista2()
    print("La lista pedida es: ")
    print(lista)
    num = int(input("Ingrese un numero: "))
    encontrado = borrar_valor(lista,num)
    if not encontrado:
        print("El numero no se encuentra en la lista")
    else:
        print("La lista sin el numero es: ")
        print(lista)

if __name__ == "__main__":
    main()
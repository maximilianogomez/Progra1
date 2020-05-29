# Escribir una función que reciba una lista como parámetro y devuelva True si la lista
# está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
# ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
# además un programa para verificar el comportamiento de la función.

#Funciones:
def ordenasc(lista):
    '''Copia una lista, la ordena y la compara con la original'''
    orden = False
    listaord = lista.copy() #otra forma es listaord = lista[ : ]
    listaord.sort()
    if listaord == lista:
        orden = True
    return orden
        

#Programa Principal:
def main():
    print("TP2:EJ7")
    lista = [1, 2, 3]
    lista2 = ['b', 'a']
    print(lista)
    print(lista2)
    if ordenasc(lista2):
        print("La lista esta ordenada Ascendentemente")
    else:
        print("La lista no esta ordenada  ascendentemente")
    
if __name__ == "__main__":
    main()
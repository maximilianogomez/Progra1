# Realizar la implementación recursiva del método de selección para ordenar una
# lista de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera
# posición, y luego ordenar el resto de la lista con una llamada recursiva.

#FUNCIONES:
def seleccion(lista, i= 0):
    posMenor = lista.index(min(lista[i:]))
    lista[i], lista[posMenor] = lista[posMenor], lista[i]
    if i == len(lista)-2:
        return lista
    else:
        return seleccion(lista,i+1)


#PROGRAMA PRINCIPAL:
def main():
    lista = [ 15 , 18 , 20 , 5 , 3 , 58, 10 , 68]
    print(lista)
    print("La lista ordenada con selección: ")
    print(seleccion(lista))
    
if __name__ == "__main__":
    main()
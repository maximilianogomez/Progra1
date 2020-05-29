# El método index permite buscar un elemento dentro de una lista, devolviendo la
# posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
# produce una excepción de tipo ValueError. Desarrollar un programa que cargue
# una lista con números enteros ingresados a través del teclado (terminando con -1)
# y permita que el usuario ingrese el valor de algunos elementos para visualizar la
# posición que ocupan, utilizando el método index. Si el número no pertenece a la
# lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
# proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

#FUNCIONES:
def cargar_lista():
    try:
        lista = []
        nro = int(input("Ingrese un numero(-1 para terminar): "))
        while nro != -1:
            lista.append(nro)
            nro = int(input("Ingrese un numero(-1 para terminar): "))
    except ValueError:
        print("Error, no ingresó un numero entero ")
        print("Se dejo de cargar numeros a la lista ")
    return lista

def buscar_numero(lista):
    intentos = 0
    while intentos != 3:
        nro = int(input("Ingrese un numero: "))
        try:
            pos = lista.index(nro)
            print(f"La posición de su numero es: {pos} ")
        except ValueError:
            print(f"Error, {nro} no está en la lista")
            intentos += 1

#PROGRAMA PRINCIPAL:
def main():
    try:
        lista = cargar_lista()
        print("La lista es: ")
        print(lista)
        if lista != []:
            buscar_numero(lista)
            print("El programa abortó, porque puso 3 veces un numero que no está en la lista ")
        else:
            print("Su lista esta vacia ")
        
    except ValueError:
        print("Se esperaba un numero entero")
    
if __name__ == "__main__":
    main()
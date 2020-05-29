# Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
# donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores
# de la lista.

#Funciones:
def IngresarPositivo(mensaje):
    '''Comprueba que se ingresen numeros mayores a 1 '''
    n = int(input(mensaje))
    while n <= 1:
        print("El numero ingresado es invalido")
        n = int(input(mensaje))
    return n

def cuadrados(n):
    lista = [i ** 2 for i in range(1, n+1)]
    return lista

def Imprimir_ult10(lista):
    if len(lista) >= 10:
        desde = -10
    else:
        desde = -len(lista)
    for i in range(desde,0):
        print(lista[i], end = " ")


#Programa Principal:
def main():
    print("TP2:EJ3")
    n = IngresarPositivo("Introduzca un numero mayor a 1: ")
    lista = cuadrados(n)
    print(lista)
    Imprimir_ult10(lista)

if __name__ == "__main__":
    main()
#Hacer el 3 por rebanadas
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


#Programa Principal:
def main():
    print("TP 2: EJ3")
    n = IngresarPositivo("Introduzca un numero mayor a 1: ")
    lista = cuadrados(n)
    print(lista)
    if len(lista) >= 10:
        desde = -10
    else:
        desde = -len(lista)
    print(lista[desde:])

if __name__ == "__main__":
    main()
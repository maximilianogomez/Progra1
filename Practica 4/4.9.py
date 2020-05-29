# Desarrollar una función que devuelva una subcadena con los últimos N caracteres
# de una cadena dada. La cadena y el valor de N se pasan como parámetros.

#Funciones:
def subcadena(cad,n):
    inicio = len(cad) - 1 - n
    if inicio >= 0:
        subcadena = cad[inicio::]
    else:
        subcadena = cad[::]
    return subcadena

def main():
    cadena = "El número de teléfono es 4356-7890"
    n = int(input("Ingrese un valor: "))
    print("La cadena es: ")
    print(cadena)
    print(f"La subcadena con los ultimos {n} caracteres es: ")
    print(subcadena(cadena,n))

#Programa Principal:
if __name__ == "__main__":
    main()
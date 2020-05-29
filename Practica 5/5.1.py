# Desarrollar una función para ingresar a través del teclado un número natural. La
# función rechazará cualquier ingreso inválido de datos utilizando excepciones y
# mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
# número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando
# éste sea correcto. Escribir también un programa que permita probar el correcto
# funcionamiento de la misma.

#FUNCIONES:
def num_natural(mensaje):
    try:
        nro = int(input(mensaje))
        if nro < 0:
            raise ZeroDivisionError("Se ingreso un numero menor a 0")
    except ValueError:
        raise
    return nro


#PROGRAMA PRINCIPAL:
def main():
    try:
        nro = num_natural("Ingrese un numero natural: ")
        print(f"El nuemero ingresado fue: {nro}")
    except ValueError as b:
        print(b)
        print("Se esperaba un numero entero")
    except ZeroDivisionError as mensaje:
        print(mensaje)
if __name__ == "__main__":
    main()
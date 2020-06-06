# Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
# utilizar cadenas de caracteres.

#FUNCIONES:
def cant_digitos(num):
    if num < 0:
        num = -num
    if num < 10:
        return 1
    else:
        digito = num % 10
        return 1 + cant_digitos(num//10)

#PROGRAMA PRINCIPAL:
def main():
    num = int(input("Ingrese un numero: "))
    cant = cant_digitos(num)
    print(f"la cantidad de digitos que el número {num} tiene son: {cant}")

main()
# Desarrollar una función que reciba un número binario y lo devuelva convertido a
# base decimal.

#FUNCIONES:
class NoBinario(Exception):
    pass

def binario_decimal(num, exp = 0):
    if num == 0:
        return 0
    else:
        digito = num % 10
        if digito != 0 and digito != 1:
            raise NoBinario("El numero contiene algun digito distinto de 0 o 1")
        termino = digito * 2**exp
        return termino + binario_decimal(num // 10, exp + 1)

#PROGRAMA PRINCIPAL:
def main():
    try:
        num = int(input("Ingrese un numero: "))
        decimal = binario_decimal(num)
        print(f"el numero binario {num} en decimal es: {decimal}")
    except NoBinario as mensaje:
        print(mensaje)
    except ValueError:
        print("Se esperaba que ingrese un numero: ")

main()
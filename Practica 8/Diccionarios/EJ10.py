# Escribir una función que reciba un número entero N y devuelva un diccionario con
# la tabla de multiplicar de N del 1 al 12. Escribir también un programa para probar
# la función.

#PROGRAMA PRINCIPAL:
def main():
    while True:
        try:
            dic = {}
            nro = int(input("Ingrese un numero(-1 para terminar) : "))
            if nro == -1:
                break
            for _ in range(1,13):
                 dic[_] = _ * nro
            for claves in dic:
                print(f"clave: {claves}, {claves}*{nro} = {dic[claves]}")
        except ValueError as mensaje:
            print(mensaje)
main()
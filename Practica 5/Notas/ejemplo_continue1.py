def sumaDigitos(nro):
    '''Suma los digitos pares de un numero.
    Utiliza continue cuando el digito es impar'''
    suma = 0
    while nro > 0:
        digito = nro % 10
        nro = nro // 10
        if digito % 2 != 0:
            continue                            #deja de ejecutar la presente iteración, pasa a la siguiente.
        suma = suma + digito
    return suma

def main():
    n = int(input("Ingrese un numero: "))
    print(f"La suma de sus digitos pares es: {sumaDigitos(n)}")

if __name__ == "__main__":
    main()
    
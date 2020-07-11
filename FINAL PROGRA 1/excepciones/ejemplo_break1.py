def sumaNDigitos(nro, n = 5):
    '''Suma los últimos n digitos del numero que recibe,
    o todos los digitos si son menos que n'''
    cont = 0
    suma = 0
    while nro > 0:
        dig = nro % 10
        nro //= 10
        suma += dig
        cont += 1
        if cont == n:
            break
    return suma

def verificarN():
    'Verifica que el n ingresado sea mayor que 0 o -1'
    n = int(input("Ingrese la cantidad de digitos (-1 para 5): "))
    while n < 0 and n!= -1:
        print("Ingreso un numero negativo y distinto a -1")
        n = int(input("Ingrese la cantidad de digitos (-1 para 5): "))
    return n

def main():
    nro = int(input("Ingrese un numero: "))
    n = verificarN()
    if n==-1:
        print(f"La suma de los ultimos 5 digitos son: {sumaNDigitos(nro)}")
    else:
        print(f"La suma de los ultimos {n} digitos son: {sumaNDigitos(nro,n)}")

if __name__ == "__main__":
    main()
    
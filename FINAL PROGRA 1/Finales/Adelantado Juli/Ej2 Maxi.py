def sumapares(nro, i = 0):
    if i == nro:
        if i % 2 != 0:
            return 0
        else:
            return i
    else:
        if i % 2 == 0:
            return i + sumapares(nro, i +  1)
        else:
            return sumapares(nro, i +  1)

def sumaRecursiva(n):
    if n == 0:
        return 0
    if n %2 == 0:
        return n + sumaRecursiva(n-1)
    else:
        return 0 + sumaRecursiva(n-1)

def main():
    while True:
        try:
            nro = int(input("Ingrese un numero (una letra o vacio para terminar): "))
            assert nro > 0, "El numero es negativo"
            valor = sumaRecursiva(nro)
            print(valor)
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError:
            print()
            resp = input("Desea terminar de cargar?(s/n): ")
            print()
            if resp.lower() != "n":
                break
            
    
main()
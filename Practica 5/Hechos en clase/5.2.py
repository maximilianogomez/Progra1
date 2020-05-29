def sumarNumeros(strNat1, strNat2):
    try:
        suma = float(strNat1) + float(strNat2)
    except ValueError:
        suma = -1
        
    return suma

def main():
    n1 = input("Ingrese un número: ")
    n2 = input("Ingrese otro número: ")
    nro = sumarNumeros(n1, n2)
    if nro == -1:
        print("Algún valor ingresado no es numérico.")
    else:
        print("La suma es: ", nro)
        
main()
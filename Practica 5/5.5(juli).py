from math import sqrt
def main():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            print("Raiz cuadrada: %.2f"%sqrt(num))
            break
        except ValueError:
            print("Error, se ingresó un numero negativo")
            resp = input("Desea intentar de nuevo? s/n: ")
            if resp.lower() == "n":
                break

# PROGRAMA PRINCIPAL
main()
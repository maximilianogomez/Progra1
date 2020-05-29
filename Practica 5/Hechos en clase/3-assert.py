def esTriangulo (lado1, lado2, lado3):
    assert lado1>0 and lado2>0 and lado3>0, "Todos los lados deben ser positivos"
    return lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2

def main():
    for vez in range(3):
        try:
            if esTriangulo(int(input("Lado 1: ")), int(input("Lado 2: ")), int(input("Lado 3: "))):
                print("Los lados ingresados forman un triangulo.")
            else:
                print("No puede formarse un triangulo con los lados ingresados")
        except ValueError:
            print("Se deben ingresar numeros enteros")
        except AssertionError as mensaje:
            print(mensaje)

if __name__ == "__main__":
    main()
def ingresarNumeroPositivo():
    """Solicita ingreso de número positivo.
    Si no se ingresa un número válido, devuelve 0
    """
    try:
        nro = int(input("Ingrese un número: "))
        while nro < 1:
            nro = int(input("Ingrese un número: "))
    except ValueError:
        print("No se ingreso un número válido.")
        nro = 0
    
    return nro

def main():
    numero = ingresarNumeroPositivo()
    if numero != 0:
        print(f"Se ingreso el número {numero}")
    else:
        print("Error")

if __name__ == "__main__":
    main()
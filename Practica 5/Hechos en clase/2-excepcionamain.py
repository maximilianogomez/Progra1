def ingresarNumeroPositivo():
    """Solicita ingreso de número positivo.
    Si no se ingresa un número válido, genera una excepcion ValueError
    """
    try:
        nro = int(input("Ingrese un número: "))
        while nro < 1:
            nro = int(input("Ingrese un número: "))
    except ValueError:
        print("No se ingreso un número válido.")
        raise
    
    return nro

def main():
    try:
        numero = ingresarNumeroPositivo()
        print(f"Se ingreso el número {numero}")
    except ValueError:
        print("Error")
        
if __name__ == "__main__":
    main()
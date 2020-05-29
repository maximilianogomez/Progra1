def contarLetrasYNumeros(cadena):
    '''Recibe una cadena y devuelve la cantidad de letras y la cantidad de numeros que contiene la cadena'''
    cantLetras = 0
    cantNumeros = 0
    for car in cadena:
        if car.isdigit():
            cantNumeros += 1
        elif car.isalpha():
            cantLetras += 1
    
    return cantLetras, cantNumeros

def main():
    cadena = input("Ingrese una cadena: ")
    cantLetras, cantNumeros = contarLetrasYNumeros(cadena)
    print(f"Cantidad de numeros: {cantNumeros}, cantidad de letras: {cantLetras}")
    
if __name__ == "__main__":
    main()
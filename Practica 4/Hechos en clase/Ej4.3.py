def obtenerClaves(numero):
    '''Recibe un numero entero con las claves 1 y 2 intercaldas y devuelve dos enteros'''
    strNumero = str(numero)
    strClave1 = strNumero[::2]
    strClave2 = strNumero[1::2]
    
    return int(strClave1), int(strClave2)

def main():
    numero = int(input("Ingresar un numero: "))
    clave1, clave2 = obtenerClaves(numero)
    print(f"La clave 1 es {clave1} y la clave 2 es {clave2}")
    
if __name__ == "__main__":
    main()
# Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo
# Común Divisor (también llamado Divisor Común Mayor) basándose en las siguientes
# propiedades:
# MCD(X, X) = X
# MCD(X, Y) = MCD(Y, X)
# Si X > Y => MCD(X, Y) = MCD(X–Y, Y).
# Utilizando la función anterior calcular el MCD de todos los elementos de una lista
# de números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite
# utilizar iteraciones en ninguna etapa del proceso.

#FUNCIONES:
def mcd(x,y):
    'Maximo común divisor entre dos numeros'
    if x == y:
        return x
    else:
        if x > y:
            return mcd(x-y,y)
        else:
            return mcd(y,x)
        
def ValidarIngreso(mensaje):
    try:
        nro = int(input(mensaje))
        while nro < 0:
            print("El numero es negativo")
            nro = int(input(mensaje))
    except ValueError:
        raise ValueError("Se esperaba un numero entero")
    else:
        return nro

#PROGRAMA PRINCIPAL:
def main():
    try:
        x = ValidarIngreso("Ingrese un numero entero positivo: ")
        y = ValidarIngreso("Ingrese otro numero entero positivo: ")
        print(mcd(x,y))
    except ValueError as mensaje:
        print(mensaje)
    

if __name__ == "__main__":
    main()
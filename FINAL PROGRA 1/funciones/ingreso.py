def IngresarPositivo(mensaje):
    '''Solicita el ingreso de un numero entero positivo '''
    nro = int(input(mensaje))
    while nro < 0:
        print("El numero ingresado es negativo")
        nro = int(input(mensaje))
    return nro

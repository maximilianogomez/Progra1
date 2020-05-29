# Desarrollar una función que reciba como parámetros dos números enteros y devuelva
# el número que resulte de concatenar ambos valores. Por ejemplo, si recibe
# 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no
# vistas en clase

#Funciones:
def IngresarPositivo(mensaje):
    """Ingresa el valor y lo verifica"""
    nro = int(input(mensaje))
    while nro < 0:
        print("El numero ingresado es negativo: ")
        nro = int(input(mensaje))
    return nro

def cifras(nro):
    """ Devuelve la cantidad de cifras que tiene un numero """
    i = 0
    while nro != 0:
        nro = nro // 10
        i += 1
    return i 


def main():
    n = IngresarPositivo("Ingrese un numero positivo: ")
    y = IngresarPositivo("Ingrese un numero positivo: ")
    cal_cifras = cifras(y)
    n *= 10**cal_cifras # al primer numero le agrego cuantos ceros por cifras tiene el segundo numero
    r = n + y
    print("El resultado pedido es: ", r)


#Programa Principal:
if __name__ == "__main__":
    main()
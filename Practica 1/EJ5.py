# Un comercio de electrodomésticos necesita para su línea de cajas un programa que
# le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
# dos números enteros, correspondientes al total de la compra y al dinero recibido.
# Informar cuántos billetes de cada denominación deben ser entregados al cliente
# como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que
# existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error
# si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona
# con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
# de $20, 1 billete de $10 y 3 billetes de $1.

#Funciones:
def IngresarPositivo(mensaje):
    """Ingresa el valor y lo verifica"""
    nro = int(input(mensaje))
    while nro < 0:
        print("El numero ingresado es negativo: ")
        nro = int(input(mensaje))
    return nro

def Billetes_entregar(dcompra,drecibido):
    """ Devuelve que billetes debe entregar """
    valor = drecibido - dcompra
    b500 = 0
    b100 = 0
    b50 = 0
    b20 = 0
    b10 = 0
    b5 = 0
    b1 = 0
    if valor < 0 :
        #El valor es negativo, no alcanza para efectuar la compra
        return False
    else:
        while valor != 0:
            if valor // 500 != 0:
                b500 = valor // 500
                valor = valor % 500
            elif valor // 100 != 0:
                b100 = valor // 100
                valor = valor % 100
            elif valor // 50 != 0:
                b50 = valor // 50
                valor = valor % 50
            elif valor // 20 != 0:
                b20 = valor // 20
                valor = valor % 20
            elif valor // 10 != 0:
                b10 = valor // 10
                valor = valor % 10
            elif valor // 5 != 0:
                b5 = valor // 5
                valor = valor % 5
            elif valor // 1 != 0:
                b1 = valor // 1
                valor = valor % 1
        return b500, b100, b50, b20, b10, b5, b1
    
def main():
    dcompra = IngresarPositivo("Ingrese el valor del producto: ")
    drecibido = IngresarPositivo("Ingrese el valor del dinero recibido ")
    if Billetes_entregar == False:
        print("El valor recibido no es suficiente para hacer la compra")
    else:
        bi500, bi100, bi50, bi20, bi10, bi5, bi1 = Billetes_entregar(dcompra, drecibido)
        print("La cantidad de Billetes de 500 a entregar: ", bi500)
        print("La cantidad de Billetes de 100 a entregar: ", bi100)
        print("La cantidad de Billetes de 50 a entregar: ", bi50)
        print("La cantidad de Billetes de 20 a entregar: ", bi20)
        print("La cantidad de Billetes de 10 a entregar: ", bi10)
        print("La cantidad de Billetes de 5 a entregar: ", bi5)
        print("La cantidad de Billetes de 1 a entregar: ", bi1)
        

#Programa Principal:
if __name__ == "__main__":
    main()
# Escribir dos funciones para imprimir por pantalla cada uno de los siguientes
# patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:

#Funciones:
def IngresarPositivo(mensaje):
    """Ingresa el valor y lo verifica"""
    nro = int(input(mensaje))
    while nro < 0:
        print("El numero ingresado es negativo: ")
        nro = int(input(mensaje))
    return nro

def imprimir_asteriscos1(nro):
    """Primera secuencia de asteriscos que se imprimen"""
    for i in range(nro):
        print(" ")
        for f in range(10):
            print("*", end = " ")
            
            
def imprimir_asteriscos2(nro):
    """Segunda secuencia de asteriscos que se imprimen"""
    for i in range(1,nro+1):
        print(" ")
        for f in range(i):
            print("**", end = "")



def main():
    n = IngresarPositivo("Ingrese el numero de asteriscos ")
    imprimir_asteriscos1(n)
    print (" ")
    imprimir_asteriscos2(n)




#Programa Principal:
if __name__ == "__main__":
    main()

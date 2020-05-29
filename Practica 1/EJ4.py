# Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo
# dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema
# de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar
# una función que reciba como parámetro la cantidad de viajes realizados en un
# determinado mes y devuelva el total gastado en viajes. Realizar también un programa
# para verificar el comportamiento de la función.

#Funciones:
def IngresarViajes(mensaje):
    """Ingresa el valor y lo verifica"""
    nro = int(input(mensaje))
    while nro < 0:
        print("El numero ingresado es negativo: ")
        nro = int(input(mensaje))
    return nro

def Descuento_por_viaje(nro):
    """Calcula cuanto será el descuento del viaje"""
    if nro == 0:
        valor = 0
    elif nro > 0 and nro <= 20:
        # 11 por la cantidad de viajes
        valor = 11 * nro
    elif nro > 20 and nro <= 30:
        # el numero de viajes menos el descuento por la tarifa maxima dentro de ese rango
        valor = (11 * nro) - (((11 * 30) * 20) / 100)
    elif nro > 30 and nro <= 40:
        # el numero de viajes menos el descuento por la tarifa maxima dentro de ese rango
        valor = (11 * nro) - (((11 * 40) * 30) / 100) 
    else:
        # el numero de viajes menos el descuento del 40 sobre esa cantidad de viajes
        valor = (11 * nro) - ((11 * nro) * 40 / 100)
    return valor

def main():
    n = IngresarViajes("Ingrese un numero de viajes, debe ser positivo: ")
    valor = Descuento_por_viaje(n)
    print("El valor total por los viajes fue de : ", valor)
    


#Programa Principal:
if __name__ == "__main__":
    main()
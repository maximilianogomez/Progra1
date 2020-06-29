def cantidadDigitos(num):
    cont = 0
    while num > 0:
        num //= 10
        cont += 1
    return cont

def DigitoCentralImpar(num):
    digitos = cantidadDigitos(num) 
    central = digitos //2    #es la posicion donde se encuentra el digito central
    for i in range(central):  #recorre los digitos desde el principio hasta el centro (donde esta el digito central)
        num = num // 10        #cuando sale del ciclo for se llego a los primeros digitos con el ultimo siendo el central
    digitocentral = num % 10          #al central se le hace modulo 10 y eso me devuelve el ultimo que en este caso es el ultimo
    if digitocentral % 2 != 0:
        esImpar = True
    else:
        esImpar = False
    return digito

asd = DigitoCentralImpar(12345)
print(asd)
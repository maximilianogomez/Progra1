# Escribir una función que reciba como parámetro número del 1 al 9 y devuelva el
# resultado de sumar n + nn + nnn + nnnn, donde n corresponde al número recibido.
# Por ejemplo, si se ingresa 3 debe devolver 3702 (3+33+333+3333). Escribir
# también un programa para verificar el comportamiento de la función. No se
# permite utilizar facilidades de Python no vistas en clase.

#Funciones:
def IngresarValido(mensaje):
    """Ingresa el valor y lo verifica"""
    nro = int(input(mensaje))
    while nro <= 0 or nro > 9:
        print("El numero ingresado no esta entre el 1 y el 9: ")
        nro = int(input(mensaje))
    return nro

def suma(nro):
    """ Sumo el n + nn + nnn + nnnn """
    return nro + ((nro * 10) + nro) + ((nro*100)+ ((nro * 10) + nro)) + ((nro*1000) + ((nro*100)+ ((nro * 10) + nro)))
    

def main():
    n = IngresarValido("Ingrese un numero del 1 al 9: ")
    resultado = suma(n)
    print("El resultado de la suma es: ")
    print(resultado)


#Programa Principal:
if __name__ == "__main__":
    main()
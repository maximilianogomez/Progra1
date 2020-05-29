# Desarrollar una función que reciba tres números positivos y devuelva el mayor de
# los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto
# devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también
# un programa para ingresar los tres valores, invocar a la función y mostrar el
# máximo hallado, o un mensaje informativo si éste no existe.


#Funciones:
def IngresarPositivo(mensaje):
    """Ingresa un numero y lo valida """
    numero = int(input(mensaje))
    while numero < 0:
        print("El numero ingresado es negativo")
        numero = int(input(mensaje))
    return numero

def devolvermaximo(nro1,nro2,nro3):
    """Dice si existe o no un maximo unico y devuelve el valor maximo """
    maximoUnico = True
    maximo = max(nro1,nro2,nro3)
    if maximo == nro1:
        if nro1 == nro2:
            maximoUnico = False
        if nro1 == nro3:
            maximoUnico = False
    elif maximo == nro2:
        if nro2 == nro1:
            maximoUnico = False
        if nro2 == nro3:
            maximoUnico = False
    else:
        if nro3 == nro1:
            maximoUnico = False
        if nro3 == nro2:
            maximoUnico = False
    return maximoUnico, maximo
    
    
def main():
    nro1 = IngresarPositivo("Ingrese un numero: ")
    nro2 = IngresarPositivo("Ingrese un numero: ")
    nro3 = IngresarPositivo("Ingrese un numero: ")

    maximoUnico,maximo = devolvermaximo(nro1,nro2,nro3)
    
    if maximoUnico:
        print("El numero maximo es: ", maximo)
    else:
        print("No existe un valor maximo estricto")

#Programa Principal:
if __name__ == "__main__":
    main()
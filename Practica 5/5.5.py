# La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
# módulo math. Escribir un programa que utilice esta función para calcular la raíz
# cuadrada de un número cualquiera ingresado a través del teclado. El programa
# debe utilizar manejo de excepciones para evitar errores si se ingresa un número
# negativo.

from math import sqrt as r

#FUNCIONES:
def raiz_cuadrada(nro):
    try:
        raiz = r(nro)
    except ValueError:
        raise
    return raiz


#PROGRAMA PRINCIPAL:
def main():
    try:
        nro = int(input("Ingres un numero :"))
        print("La raiz cuadra de",nro," es: %.2f"%raiz_cuadrada(nro))
    except ValueError as mensaje:
        print(mensaje)
    
    
main()
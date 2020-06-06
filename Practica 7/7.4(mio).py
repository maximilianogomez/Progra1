# Desarrollar una función que devuelva el producto de dos números enteros por sumas
# sucesivas.

#FUNCIONES:
def mult(x,y):
    # 3 * 2 = 3 + 3
    'Recibe dos numeros y va haciendo la suma sucesiva'
    if y < 0:
        return mult(y,x)
    elif y == 0:
        return 0
    else:
        return x + mult(x,y-1)
#PROGRAMA PRINCIPAL:
def main():
    try:
        x = int(input("Ingrese un numero: "))
        y = int(input("Ingrese el numero por el que multiplicará: "))
        mult_recursiva = mult(x,y)
        print(f"La multiplicacion de {x} y {y} es {mult_recursiva}")
    except ValueError:
        print("Se esperaba un numero entero: ")

main()
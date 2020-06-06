def MultiplicacionRecursiva(x,y):
    if x == 0 or y == 0:
        return 0
    else:
        return y + MultiplicacionRecursiva(x-1,y)


def Main():
    x = int(input("Ingrese un número positivo: "))
    y = int(input("Ingrese otro número positivo: "))
    solucion = MultiplicacionRecursiva(x,y)
    print (f"El resultado del producto entre {y} y {x} es {solucion}")
    
#Programa
Main()
# Realizar una función que devuelva el resto de dos números enteros, utilizando restas
# sucesivas.

#FUNCIONES:
def resto(x,y):
     # 15 % 2 = 15 - 2 -2 - 2 -2 -2 - 2 -2 = 1
    'Recibe dos numeros y va haciendo la resta sucesiva, hasta hallar el resto'
    if (x-y) < 0:
        return x
    else:
        return resto(x-y,y)
        
    
#PROGRAMA PRINCIPAL:
def main():
    try:
        x = int(input("Ingrese un numero: "))
        y = int(input("Ingrese el numero por el que restará: "))
        if y == 0:
            raise ZeroDivisionError
        resta_recursiva = resto(x,y)
        print(f"La resta entre {x} y {y} es {resta_recursiva}")
    except ValueError:
        print("Se esperaba un numero entero: ")
    except ZeroDivisionError:
        print("Está dividiendo por 0")

if __name__ == "__main__":
    main()
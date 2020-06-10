# Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
# usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido
# del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
# Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
# inexistentes.

#FUNCIONES:
def validar_num(nro):
    while nro < 0 or nro > 9 :
        raise ValueError("El numero es menor a 0 o mayor a 9")

#PROGRAMA PRINCIPAL:
def main():
    conj = {0,1,2,3,4,5,6,7,8,9}
    print(conj)
    while True:
        try:
            print()
            nro = int(input("Ingrese un numero entero del 0 al 9 para borrar del conjunto(-1 para terminar): "))
            if nro == -1:
                break
            validar_num(nro)
            print()
            conj.remove(nro)
            print(conj)
            print()
        except ValueError as mensaje:
            print(mensaje)
        except KeyError:
            print("Ese numero ya se eliminó")

def main2():
    conjunto = {1,2,3,4,5,6,7,8,9,0}
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            if num == -1:
                break
            assert (num in conjunto), "El numero no está en el conjunto"
            assert (num>0),"Se espera el ingreso de un positivo"
            conjunto.remove(num)
            print(conjunto)
        except AssertionError as error:
            print(error)
        
        except ValueError:
            print("Se espera el ingreso de un numero")
            
def main3():
    conjunto = {0,1,2,3,4,5,6,7,8,9}
    while True:
        try:
            num = int(input("Ingrese un numero a eliminar: "))
            if num == -1:
                break
            if num not in conjunto:
                raise ValueError("Ese numero no está en el conjunto")
            if not type(num) is int:
                raise TypeError("Se espera el ingreso de un numero")
            if num in conjunto:
                conjunto.remove(num)
            print(conjunto)    
        except ValueError as mensaje:
            print(mensaje)
        except TypeError as error:
            print(error)

main()
# Crear una función recursiva para sumar los primeros N números pares.  
# Ejemplo:
# - Si recibe un 5, debe sumar 6 ya que sólo debe tener en cuenta 2 y 4 
# - Si recibe un 8, debe sumar 20, ya que solo debe tener en cuenta los numeros 2 + 4 + 6 + 8
# Desarrollar un programa principal para permitir ingresar numeros del teclado y mostrar la suma calculada mediante la
# funcion recursiva. Finalizar cuando no se ingresa un número capturando una excepción.
# FUNCIONES
def sumaRecursiva(n):
    '''Suma los primeros N numeros pares en forma recursiva.
    n numero entero como parámetro
    Retorna la suma
    
    '''
    if n == 0:
        return 0
    if n %2 == 0:
        return n + sumaRecursiva(n-1)
    else:
        return 0 + sumaRecursiva(n-1)

def main():
    'Programa principal'
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            assert (num>0),"Error, debe ser positivo"
        except AssertionError as error:
            print(error)
        except ValueError:
            print("Error, se esperaba el ingreso de un número")
            break
        else:
            print(f"Suma de los numeros pares: {sumaRecursiva(num)}")
                
main()
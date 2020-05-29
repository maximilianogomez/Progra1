#el continue se usa para saltar la iteración en la que se esta en el while.
#ver ejemplo continue 1.

#El break finaliza por completo la ejecución del ciclo
#ver ejemplo break1

#Hay un bloque try, except para evitar que el programa finalicé por un error.
try:
    nro = int(input("Ingrese un numero: "))
    print(f"El numero ingresado es: {nro}")
except ValueError:
    print("Error,debe ingresar un numero entero")

print("Se termino de procesar el programa")

#assert: si le paso algo que es True o veradadero no pasa nada, si le paso algo falso me genera un error de tipo AssertionError
#por ejemplo: assert 7 > 3 no pasa nada

#ejemplo:
x = "Hola Curso"
y = "hola curso"
assert x == y, "X e Y son distintas"

#class: se usa para crear un error.
class CustomError(Exception):
    pass
raise CustomError("Mensaje Error")
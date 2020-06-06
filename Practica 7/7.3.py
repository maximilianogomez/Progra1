# Escribir una función que devuelva la suma de los N primeros números naturales

#FUNCIONES:
def suma_recursiva(i):
    if i == 0:
        return 0
    else:
        return i + suma_recursiva(i-1)
   

#PROGRAMA PRINCIPAL:
def main():
    num = int(input("Ingrese un numero: "))
    suma = suma_recursiva(num)
    print(f"La suma es {suma} para el numero {num} de sus naturales")
   

main()
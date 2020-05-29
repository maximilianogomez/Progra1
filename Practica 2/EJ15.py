#TP2_EJ15
"""
15.Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera
que sean impares.
El proceso deberá realizarse utilizando listas por comprensión.
Imprimir las dos listas por pantalla."""
import random

def main():
    lista=[random.randint(1,100) for i in range(random.randint(5,10))]
    lista2=[num for num in lista if num  % 2 != 0]
    print(lista)
    print(lista2)

if __name__ == "__main__":
    main()
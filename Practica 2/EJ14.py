# Escribir un programa para generar una lista con los múltiplos de 7 que no sean
# múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida.
#Repetir el ejercicio anterior, pero utilizando la técnica de listas por comprensión

#Funciones:
def mult7yno5():
    lista = [i for i in range(2000,3501) if i % 7 == 0 and i % 5 != 0 ]
    return lista
        
#Programa Principal:
def main():
    print("TP2.EJ14")
    lista = mult7yno5()
    print(lista)

if __name__ == "__main__":
    main()
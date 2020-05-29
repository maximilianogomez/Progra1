# Escribir un programa para generar una lista con los múltiplos de 7 que no sean
# múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida.

#Funciones:
def mult7yno5():
    lista = []
    condicion =(lambda x : x % 7 == 0 and x % 5 != 0)
    for i in range(2000,3501):
        if condicion(i):
            lista.append(i)
    return lista
        
#Programa Principal:
def main():
    print("TP2.EJ13")
    lista = mult7yno5()
    print(lista)

if __name__ == "__main__":
    main()
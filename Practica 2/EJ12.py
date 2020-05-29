# Utilizar la técnica de listas por comprensión para construir una lista con todos los
# números impares comprendidos entre 100 y 200.

#Funciones:
def listaimpares():
    lista = [i for i in range(100,201) if i % 2 != 0]
    return lista
        
#Programa Principal:
def main():
    print("TP2.EJ12")
    lista = listaimpares()
    print(lista)

if __name__ == "__main__":
    main()
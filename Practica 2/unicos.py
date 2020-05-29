""" c.Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original,
    sin importar el orden."""
def unicos_repetidos(lista):
    unicos=[]
    repetidos=[]
    for x in lista:
        if x not in unicos:
            unicos.append(x)
        else:
            if x not in repetidos:
                repetidos.append(x)
    print("Lista de elementos unicos :")
    print(unicos)
    print("Lista de elementos repetidos :")
    print(repetidos)
#programa
def main():
   lista=[1,2,3,1]
   respuesta=unicos_repetidos(lista)
main()
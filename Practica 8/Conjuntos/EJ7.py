# Ingresar una frase desde el teclado y eliminar las palabras repetidas, dejando un
# solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su
# longitud. La eliminación de las palabras duplicadas debe realizarse a través de un
# conjunto.

#FUNCIONES:
def eliminar_repetidas(frase):
    frase = frase.lower()
    lista = frase.split()
    conjunto = set(lista)
    return list(conjunto)


# def seleccion(lista):
#     for i in range(len(lista)-1):
#         for j in range(i+1,len(lista)):
#             if len(lista[i]) > len(lista[j]):
#                 lista[i],lista[j] = lista[j], lista[i]
    

#PROGRAMA PRINCIPAL:
def main():
    frase = input("Ingrese una frase: ")
    lista = eliminar_repetidas(frase)
    print("Las palabras sin repetir de la frase son: ")
    print(lista)
    print("Las palabras ordenadas por longitud: ")
#    seleccion(lista)
#    print(lista)
    lista.sort(key=lambda x:len(x))
    print(lista)

main()
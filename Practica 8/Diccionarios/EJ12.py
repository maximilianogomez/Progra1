# Crear una función contarvocales(), que reciba una palabra y cuente cuántas letras
# "a" contiene, cuántas "e", cuántas "i", etc. Devolver un diccionario con los resultados.
# Desarrollar un programa para leer una frase e invocar a la función por cada
# palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales
# hallada.

#FUNCIONES:
def contarvocales(cad):
    dic = {'a': 0 , 'e': 0,'i':0 , 'o': 0, 'u': 0}
    cad = cad.lower()
    for letra in cad:
        if letra in dic:
            dic[letra] += 1
    return dic

#PROGRAMA PRINCIPAL:
def main():
    frase = input("Ingrese una frase: ")
    lista = frase.split()
    for pal in lista:
        print(f"la palabra es: {pal}")
        dic = contarvocales(pal)
        for vocal in dic:
            print("vocal: ", vocal, "cantidad: ", dic[vocal])

main()
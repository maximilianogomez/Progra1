# Escribir una función que reciba como parámetro una cadena de caracteres en la
# que las palabras se encuentran separadas por uno o más espacios. Devolver otra
# cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada
# una.

#Funciones:
def ord_alfa(cad):
    lista = cad.split()
    lista.sort()
    cad = " ".join(lista)
    return cad

def main():
    cadena = "El número de teléfono es 4356-7890"
    cadena_Ord = ord_alfa(cadena)
    print(cadena_Ord)
    



#Programa Principal:
if __name__ == "__main__":
    main()
# Desarrollar una función para reemplazar todas las apariciones de una palabra por
# otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
# cantidad de reemplazos realizados. Escribir también un programa para verificar el
# comportamiento de la función.

#Funcion:
def reemplazos(cad,reemplazada,reemplazar):
    cdad_reemplazar = cad.count(reemplazada)
    cad = cad.replace(reemplazada,reemplazar)
    return cdad_reemplazar, cad

#Programa Principal:
def main():
    cadena = "Los ojos son una parte de cuerpo. Mi color favorito de ojos son los verdes"
    reemplazado = input("Ingrese la palabra a reemplazar: ")
    reemplazar = input("Ingrese la palabra por la cual reemplazara la palabra anterior: ")
    cdad_reemplazar, cad = reemplazos(cadena,reemplazado,reemplazar)
    print("La cadena original: ")
    print(cadena)
    print("La cadena con la palabra reemplazada: ")
    print(cad)
    print("La cantidad de veces que se reemplazó en la cadena fueron: ")
    print(cdad_reemplazar)

main()
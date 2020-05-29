# Escribir una función para eliminar una subcadena de una cadena de caracteres, a
# partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
# Escribir también un programa para verificar el comportamiento de la misma.
# Escribir una función para cada uno de los siguientes casos:
# a. Utilizando rebanadas
# b. Sin utilizar rebanadas

#Funciones:
def elim_subc_rebanadas(cad,pos,n):
    subcadena = cad[pos:pos+n:]
    for palabra in subcadena:
        cad = cad.replace(palabra, "")
    return cad

def elim_subc(cad, pos,n):
    subcadena = [cad[i] for i in range(pos,pos+n)]  
    i = 0
    while i < len(cad):
        if i >= pos:
            for palabra in subcadena:
                if cad[i] == palabra:
                    cad = cad.replace(palabra,"")
        i+= 1
    return cad
        
#Programa Principal:
def main():
    cadena = "El número de teléfono es 4356-7890"
    subcadena = elim_subc(cadena,25, 8)
    print(subcadena)

if __name__ == "__main__":
    main()
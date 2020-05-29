# Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
# indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
# como valor de retorno. Escribir también un programa para verificar el comportamiento
# de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
# 7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
# resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes
# casos:
# a. Utilizando rebanadas
# b. Sin utilizar rebanadas

#Funciones:
def subcadena_rebanadas(cad,pos,n):
    subcadena = cad[pos:pos+n:]
    return subcadena

def subcadena2(cad, pos,n):
    resultado = ""
    if pos+n <= len(cad):
        for i in range(pos, pos+n):
            resultado += cad[i]
    else:
        for i in range(pos):
            resultado += cad[i]
    return resultado
        
#Programa Principal:
def main():
    cadena = "El número de teléfono es 4356-7890"
    subcadena = subcadena_rebanadas(cadena,25, 9)
    print(subcadena)

if __name__ == "__main__":
    main()
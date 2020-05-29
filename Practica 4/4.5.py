# Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo
# una frase y un entero N, y devuelva otra cadena con las palabras que tengan
# N o más caracteres de la cadena original. Escribir también un programa para
# verificar el comportamiento de la misma. Hacer tres versiones de la función, para
# cada uno de los siguientes casos:
# a. Utilizando sólo ciclos normales
# b. Utilizando listas por comprensión
# c. Utilizando la función filter

#Funciones
def filtrar_palabras1(cad, n):
    lstPalabras = cad.split()
    lstPalabras_fil = []
    for palabra in lstPalabras:
        if len(palabra) >= n:
            lstPalabras_fil.append(palabra)
    cad_unificada = " ".join(lstPalabras_fil)
    return cad_unificada

def filtrar_palabras2(cad, n):
    lstPalabras = cad.split()
    lstPalabras_fil = [palabra for palabra in lstPalabras if len(palabra) >=n ]
    cad_unificada = " ".join(lstPalabras_fil)
    return cad_unificada

def filtrar_palabras3(cad,n):
    lstPalabras = cad.split()
    lstPalabras_fil = filter(lambda palabra: len(palabra) >= n, lstPalabras)
    cad_unificada = " ".join(lstPalabras_fil)
    return cad_unificada

#Programa Principal:
def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    n = int(input("Ingrese la cantidad de caracteres que deba tener cada palabra: "))
    cadena_filtrada = filtrar_palabras3(cadena , n)
    print(cadena_filtrada)

if __name__ == "__main__":
    main()
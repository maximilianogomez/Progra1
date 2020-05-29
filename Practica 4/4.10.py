# Escribir un programa que permita ingresar una cadena de caracteres e imprima un
# mensaje indicando cuántas letras y cuántos números contiene. Por ejemplo, si se
# ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3 números.

#Funciones:
def digitosyletras(cad):
    lstPalabras = cad.split()
    ctdad_pal = 0
    ctdad_num = 0
    for palabra in lstPalabras:
        if palabra.isalpha():
            ctdad_pal += len(palabra)
        elif palabra.isdigit():
            ctdad_num += len(palabra)
    return ctdad_pal, ctdad_num
        

def main():
    cadena = "Hola Mundo 123"
    cdad_pal, cdad_num = digitosyletras(cadena)
    print(f"La cadena es: {cadena}")
    print(f"La cantidad de palabras son: {cdad_pal} y la cantidad de numeros son: {cdad_num}")
    

#Programa Principal:
if __name__ == "__main__":
    main()
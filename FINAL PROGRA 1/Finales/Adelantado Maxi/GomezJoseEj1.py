'''
Crear una función recursiva para crear una nueva cadena que contenga sólo los caracteres alfabéticos y espacios de otra cadena.
Se espera que lo resuelva mediante una función recursiva.
Desarrollar un programa para ingresar frases  hasta que sea vacía y para cada frase mostrar la cadena creada con la función recursiva.
Ejemplo: Programar en Python 3.1 me encanta! la función recursiva debe retornar:
Programar en Python me encanta en una variable de tipo cadena de caracteres.
'''
#FUNCIONES:
def caracteresAlfa(cad, frase = ""):
    '''Agrega los caracteres alfabéticos a la cadena pasada por parámetro.
    Parámetro 1: cad, cadena de caracteres ingresada por teclado
    Parámetro 2: frase, cadena de caracteres vacía
    
    '''
    if cad == "":
        return frase
    else:
        if cad[0:1].isalpha() or cad[0:1] == " ":
            frase += cad[0:1]
        return caracteresAlfa(cad[1:],frase)

def main():
    'Programa principal'
    while True:
        frase = input("Ingrese una frase (vacia para terminar): ")
        if frase == "":
            break
        cadena_filtrada = caracteresAlfa(frase)
        print(f"La cadena sin los numeros y caracteres especiales es: {cadena_filtrada}")

#PROGRAMA PRINCIPAL:
main()
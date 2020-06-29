'''
Plegado de un texto.

Escribir una función que ingrese por teclado una longitud y lea de un archivo un texto "texto.txt" que contiene varias oraciones en la mismo o

diferente registro.

Se solicita crear un nuevo archivo "plegado.txt" que contenga una oración por renglón o hasta la longitud máxima indicada,

las líneas deben ser cortadas correctamente en los espacios (sin cortar las palabras).

Todas las oraciones finalizan con un punto.

Informar al finalizar para cada palabra cuántas vocales posee, mostrar las palabras ordenadas alfabéticamente sin considerar símbolos para el informe.
'''


#NOTA: El archivo plegado2.txt que subí junto con los programas lo probé con una longitud de 52

#FUNCIONES:
def quitarSimbolos(cad):
    '''Quita sin simbolos y numeros.'''
    nuevaCad=""    
    for letra in cad:
        if letra.isalpha():
            nuevaCad += letra
        elif letra == " ":
            nuevaCad += letra
            
    return nuevaCad

def contarVocales(cad):
    '''Cuenta las vocales dada la palabra'''
    vocales = ['a','e','i','o','u']
    cont = 0
    for letra in cad:
        if letra in vocales:
            cont += 1
    return cont

def listado():
    '''Crea un diccionario con cada palabra en el registro texto.txt y le asigna un valor acorde a la cantidad de vocales, si la palabra ya está en el diccionario no la considera'''
    dic = {}
    try:
        origen = open("texto.txt")
    except IOError:
        print("Hubo un error en la carga de algun archivo")
    else:
        for reg in origen:
            reg = reg.rstrip("\n")
            lstPalabras = reg.split()
            for pal in lstPalabras:
                pal = quitarSimbolos(pal.lower())
                cant_vocales = contarVocales(pal)
                if pal not in dic:
                    dic[pal] = cant_vocales 
    finally:
        try:
            origen.close()
            destino.close()
        except :
            pass
    return dic
#PROGRAMA PRINCIPAL:
def main():
    try:
        origen = open("texto.txt")
        destino = open("plegado2.txt",'w')
    except IOError:
        print("Hubo un error en la carga de algun archivo")
    else:
        long = int(input("Ingrese la longitud: "))
        reg = origen.readline()
        while reg != "":
            #quitar el "\n"
            reg = reg.rstrip("\n")
            if len(reg) <= long:
                for letra in reg:
                    if letra != ".":
                        destino.write(letra)
                    else:
                        destino.write("\n")
            else:
                '''
                mi registro es mayor a la longitud por lo que le pido que vaya cortando con "," hasta que llegué al final de la longitud sin cortar la palabra.
                siempre que termine un ciclo hasta la longitud al registro se le hace una rebanada y se lo vuelve a analizar hasta que llegué al punto
                '''
                while reg != "":
                    i = 0
                    while reg[i] != "." and (i < long or reg[i] != " ") :
                        destino.write(reg[i])
                        i += 1
                    if reg[i:] == ".":
                        destino.write("." + " " + "\n")
                    else:
                        destino.write("," + " " + "\n")
                    reg = reg[i+1:]
            reg = origen.readline()
        print("Se creo el archivo ")
    finally:
        try:
            origen.close()
            destino.close()
        except :
            pass
    #Informe
    dic = listado()
    lista = list(dic)
    lista.sort()
    for elem in lista:
        print(f"Palabra: {elem:12s}       Vocales: {dic[elem]:11d}")
        print()

if __name__ == "__main__":
    main()

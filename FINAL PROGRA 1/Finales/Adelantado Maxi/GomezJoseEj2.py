''''
Hora de jugar!: Se requiere desarrollar un juego de preguntas, en que se puede responder "si" o "no". 
Las preguntas a formular se encuentran en un archivo de texto enumeradas desde el 1 hasta 8, la pregunta a formular
y la respuesta correcta (si o no) separada por punto y coma.
Ejemplo:
1;Los diccionarios en Python poseen índice?;no
2;El caracter $ se utiliza para comentarios en Python;no
3;se pueden crear funciones con la instrucción lambda?;si
Gana quien responde correctamente 3 preguntas seleccionadas al azar entre las 8 existentes del archivo. 
Si se responde mal alguna, no se formula la siguiente y termina el juego. Resolver utilizando estructura while-true y manejo de excepciones.
(utilizar el block de notas para crear el archivo de preguntas, crear 8 preguntas relacionadas a PrograI con su correspondiente respuesta)
No olvide entregar el archivo preguntasApellido.txt, las preguntas y respuestas que formule en el archivo se tendrán en cuenta para asignar la
nota del exámen.
'''

from random import randint as r

#FUNCIONES:
def juegoDificil(cont,preguntados,nro_azar,verif):
    '''Abre el archivo de textos 'preguntasGomez' y lee preguntas al azar, hasta que el usuario contesta
    erroneamente o responde tres preguntas correctamente.
    Parámetro 1: cont, entero, son las veces que respondió bien el usuario
    Parámetro 2: preguntados, lista con los numeros de las preguntas
    Parámetro 3: nro_azar, es el que indica el numero de la pregunta
    Parámetro 4: verif, es la verificación de que puede seguir en juego. No ganó ni perdio si es True, False si paso alguna de estos supuestos.
    Retorna las veces que acertó, los numeros de las preguntas que ya se hicieron, el numero al azar y verif
    
    '''

    try:
        arch = open('preguntasGomez.txt')
    except IOError:
        print("Hubo un error al abrir el archivo de preguntas ")
    else:
        verif = True
        while True:
            try:
                reg = arch.readline()
                while reg != "":
                    reg = reg.rstrip("\n")
                    lstPreg = reg.split(";")
                    while lstPreg[0] != str(nro_azar):
                        reg = reg.rstrip("\n")
                        lstPreg = reg.split(";")
                        reg = arch.readline()
                    print(f"{lstPreg[0]:3s} {lstPreg[1]:15}")
                    resp = input("Responda Si o No (si/no): ")
                    if resp.lower() == lstPreg[2] and cont < 3:
                        cont += 1
                        if cont == 3:
                            raise ZeroDivisionError
                        print("Correcto, la siguiente pregunta es: ")
                        
                        if cont == 1:
                            nro_azar = r(nro_azar + 1,7)
                            while nro_azar in preguntados:
                                nro_azar = nro_azar = r(nro_azar + 1,7)
                        if cont == 2:
                            nro_azar = r(nro_azar + 1,8)
                            while nro_azar in preguntados:
                                nro_azar = nro_azar = r(nro_azar + 1,7) 
                        preguntados.append(nro_azar)
                    else:
                        raise ValueError
                    
            except ValueError:
                print("Respuesta equivocada, fin del juego ")
                verif = False
                arch.close()
                break
            except ZeroDivisionError:
                print("Felicitaciones, ha ganado ")
                verif = False
                arch.close()
                break
            else:
                try:
                    arch.close()
                except:
                    pass
    return cont, preguntados, nro_azar, verif
        
def main():
    'Programa principal'
    cont = 0
    #en el caso de que sea 6 tengo dos registros más para leer
    nro_azar = r(1,6)
    preguntados = []
    preguntados.append(nro_azar)
    verif = True
    while verif and cont < 3 :
        #El programa no funciona bien siempre ya que una vez que se pasa quise volver a abrir el archivo de vuelta con los registros desde la pregunta 1 pero no me lo permite.
        cant,preguntados,nro_azar,verif = juegoDificil(cont,preguntados,nro_azar, verif)
    #una posible solución es ir restringiendo el nro al azar para que este dentro del rango de lectura de los registros pero no sería un numero al azar propiamente dicho entre los valores
            
#PROGRAMA PRINCIPAL:
main()
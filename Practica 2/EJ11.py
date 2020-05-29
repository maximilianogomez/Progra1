# Intercalar los elementos de una lista entre los elementos de otra. La intercalación
# deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
# una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
# y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

#Funciones:
def IntercalarElementos(lista1,lista2): #supongo que tienen la misma cantidad de elementos.
    '''Intercala los elementos de una lista entre los elementos de otra'''
    long = len(lista1 + lista2)
    x = 0 
    for i in range(1,long,2):
        lista1[ i:i ] = lista2[x:x+1]
        x += 1
#solo funciona para listas de igual longitud.
def Intercalar(lista1, lista2): #esta funciona para cualquier lista dada.
    largo = len(lista2)
    for i in range(1,largo*2,2):
        lista1[i:i] = [lista2[i//2]]
        
#Programa Principal:
def main():
    print("TP2.EJ11")
    lista3 = [random.randint(1,50) for i in range(random.randint(5,10))]
    lista4 = [random.randint(1,50) for i in range(random.randint(5,10))]
    lista1 = [8, 1, 3, 6, 0]
    lista2 = [5, 9, 7, 2, 4]
    IntercalarElementos(lista1,lista2)
    print(lista1)

if __name__ == "__main__":
    main()
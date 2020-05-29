#Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
#auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

#Funciones:
def esCap(lista):
    ''' Me dice si la lista es o no capicua, se corta el ciclo cuando encuentra una condicion que no la hace '''
    capicua = True
    x = 0
    y = len(lista) - 1
    centro = (len(lista) // 2)
    while x < centro and y > centro and capicua == True:
        if lista[x] != lista[y]:
            capicua = False
        x += 1
        y -= 1
    return capicua

def esCap2(lista):
    ''' Me dice si la lista es o no capicua, se corta el ciclo cuando encuentra una condicion que no la hace '''
    capicua = True
    x = 0
    y = len(lista) - 1
    while y > x and capicua == True:
        if lista[x] != lista[y]:
            capicua = False
        x += 1
        y -= 1
    return capicua

#Programa Principal:
def main():
    lista = [50, 17, 91, 17, 50]
    print(lista)
    boolCap = esCap(lista)
    if boolCap:
        print("La lista es capicua")
    else:
        print("La lista no es capicua")

    
if __name__ == "__main__":
    main()
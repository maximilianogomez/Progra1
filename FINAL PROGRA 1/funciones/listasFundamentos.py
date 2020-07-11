#Video donde se explican todos los algoritmos de estos metodos:
#https://www.youtube.com/watch?v=VJ_EUuURRg4

#Ordenamientos:
def ordenamiento_por_insercion(lista): #ordena de menor a mayor desplazando.
    for i in range (1,len(lista)):
        valor = lista[i] #indice que empieza en 1 hasta el final de la lista
        j = i #un valor anterior al indice con el que estoy trabajando, quiero que disminuya para comparar siemrpe con los de la izquierda hasta que i sea 0
        while j > 0 and lista[j-1] > valor :
            aux = lista[j] #el valor de la derecha y el mas chico lo guardo
            lista[j] = lista[j-1] # pongo el valor mas grande a la derecha
            lista[j-1] = aux #pongo el valor mas chico antes guardado a la izquierda
            j -= 1
def ordenamiento_por_insercion2(lista):
    for i in range(1,len(lista)):
        valor = lista[i]
        j = i
        while j > 0 and lista[j-1] > valor :
            lista[j] = lista[j-1] #ponele el valor de la izquierda a la derecha 
            j -= 1 #bajame el valor de j (coincide con el indice del elemento al que le copiaste el valor
        lista[j] = valor #reemplaza el valor grande en ese indice donde le robaste el elemento (el elemento de la izquierda)
        
def metodoburbujamejorado(lista):
    ordenado = False #supongo que no esta ordenado
    recorrido = 1 # para ver la cantidad de veces que itera hasta que se ordena
    while ordenado == False: #pongo esta condición para que no siga iterando si ya hizo un ciclo y no cambio nada.
        ordenado = True #supongo que esta ordenada para salir si no se itera
        for i in range(len(lista)):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                ordenado = False #pongo que es Falso porque se cambiaron valores, asi que puede que todavia no este ordenada a pesar de ese cambio
        recorrido += 1 #cuenta todas las iteraciones mas la ultima que se hace cuando esta todo ordenado.
        
def seleccion(lista):
    for i in range(0, len(lista)-1): #va de 0 hasta un el anteultimo elemento
        for j in range( i + 1, len(lista)): #va desde 1 mas que el anterior hasta el fianl de la lista (o sea recorre el resto de la lista)
            if lista[i] > lista[j]: #se va guardando el mas chico de los 2 elementos que se comparan en el [i] que no se mueve hasta que termina el segundo for
                aux = lista[i]      #se va guardando el valor mas grande en j
                lista[i] = lista[j]
                lista[j] = aux

#Formas de busquedas
def BuscarValorSecuencial(lista,nro): #esto es un metodo de busqueda no un ordenamiento por eso lleva return.
    i = 0
    while i < len(lista) and lista[i] != nro: #se va moviendo un indice a la derecha siempre y cuando el valor en ese indice sea distinto
        i += 1                                #al valor que estoy buscando
        
    if i == len(lista): #si se llego hasta el final de la lista y el numero no coincidio con el que busco 
        encontrado = False #mi funcion me dice que no se encontró
    else:
        encontrado = True #si el indice se paro antes de llegar al final, se encontró el numero.
    return encontrado #quiero saber el valor de encontrado True o False.

def BusquedaBinaria(lista,dato):  #LA LISTA DEBE ESTAR ORDENADA. Este metodo consiste en ir hasta la mitad e ir comparando
    izq = 0                        #si el valor donde cai (la mitad de la lista) es menor o mayor al numero que busco y a partir de eso
    der = len(lista) - 1           #vuelvo a buscar la mitad por ese lado
    pos = -1 #pos -1 es que no se encontró
    while izq <= der and pos == -1: 
        centro = (izq+der) // 2
        if lista[centro] == dato: #el dato estaba en el centro de la izq y la derecha por defecto izq es 0 y derecha es el ultimo elemento de la lista
            pos = centro
        elif lista[centro] < dato: #significa que mi dato buscado está a la derecha del centro
            izq = centro + 1       #aumento la izq de 0 a un valor despúes del centro, el centro ya lo analicé antes.
        else:                      #significa que mi dato está a la izquierda
            der = centro -1        #mi derecha, va del centro -1, ya que el centro ya lo analicé.
    return pos

a = [ 1 , 9 , 6 , 5  , 3 , 2]

ordenamiento_por_insercion2(a) # para probar que ande bien.

print(a)
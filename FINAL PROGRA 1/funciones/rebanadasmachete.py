#Rebanadas (incio : fin : paso ) #con las rebanads creas una nueva lista, no modificas la lista.
lista = [2,  34 ,  25 , 1 , 19 , 23, 48]
        # 0   1    2    3    4    5   6
        #-7  -6   -5   -4   -3   -2  -1

print(lista[2:5]) #como el range no se toma el ultimo valor

print(lista[ : 5]) #omitiendo el primer subindice

print(lista[2 : ]) # si omito el fin lo hace hasta el final de la lista

#podes meterles funciones o sumas aritmeticas adentro

#lista[funcion():]
#lista[inicio: inicio+4]

#se puede exceder el indice en una rebanada.

lista[2:100] #me hace la rebanada del elemento 2 hasta el 100 pero como hay 7 elementos va hasta el final de la lista.


print(lista[-5:-1]) #me muestra del 25 hasta el 23

print(lista[2:7:2]) #[25, 19, 48]

#incremento negativo

print(lista[7:1:-2]) #[48,19,25]

#quiero la lista que tiene los indices pares. un ejemplo de uso de rebanadas

print(lista[::2])

#si quiero invertir usando rebanadas:

print(lista[::-1]) #otra forma es usar el lista.sort(reverse=True) o con un lista.reverse()

#Reemplazar elementos:
print(lista[2:4]) # [25,1]
lista[2:4] = [80, 88] #cambia los 25 y 1 por 80 y 88 si hago por [80, 88 , 90] por ejemplo en esa porcion se agregarán los 3 elementos
                      #puedo darle elementos de menos.

lista[2:4] = [] #estoy eliminando los elementos en esa porcion

#si quiero insertar elementos puedo usar rebanadas nulas:
lista[2:2]= [115,110,118]          #lista[2:2]    esto da []
                                #inserta elementos en el indice 2, en este caso el print daría [2,  34 , 115,110,118, 25 , 1 , 19 , 23, 48]

#copiar listas
#metodo copy
listaOriginal = [2, 34, 25]
listaCopia = listaOriginal.copy()        #si no le hago el metodo copy lo que hace es referenciar la misma lista y ambas las tendrias con el 18 al final
listaCopia.append(18)

#copiar por rebanadas
listaOriginal = [2, 34, 25]
listaCopia = listaOriginal[:]         #listaCopia = [2, 34, 25, 18]
listaCopia.append(18)                  #listaOriginal = [2, 34, 25]

#recorrer lista (con funcion enumarate)
lista = [2,  34 ,  25 , 1 , 19 , 23, 48]   #enumarate(lista,inicio)
for i, valor in enumerate(lista,3): #devuelve el indice y valor de cada elemento si le doy inicio 3 me muestra del indice 3 en adelante
    print("pos", i, "valor: ", valor)
    
#recorrer lista por rebanadas:
lista = [2,  34 ,  25 , 1 , 19 , 23, 48]
for i in lista[3:6]:
    print(i , end = " ")              #recorre la lista del indice 3 al 5 en este caso devolveria 1,19,23

#listas por comprension:
lista = [2,  34 ,  25 , 1 , 19 , 23, 48]
listaCubos = [n ** 3 if n % 2 == 0 else n ** 2 for n in lista] #haceme el cubo del numero cuando el num es divisible por 2 y el cuadrado cuando no lo es
print(listaCubos)
#sintaxis de lista por comprension
<nombre> = [ <definicion> <ciclo> <condicional>]




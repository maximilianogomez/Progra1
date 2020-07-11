#funciones en la lista
lista = [3,4,5,5]
lista.insert(0,2)  #.insert<pos><elem> en este caso daría [2,3,4,5]
lista.pop(indice) #me borra el elemento en ese indice por defecto borra el ultimo
lista.remove(4) #me remueve el elemento que le digo .remove(<valor>) IMP : solo lo hace una vez con el primer 4 en este caso que encuentra
print(lista.index(5)) #2 .index(<valor>) devuelve el indice donde se encuentra el valor, si hay mas de un elemento solo me da el indice del primero
                        # print(lista.index(5,2,4) el valor, donde empieza, y el final
lista.count(5)   #me muestra la cantidad de veces que esta un elemento en la lista en este caso 2
lista.clear() #te limpia la lista, daria []
lista.reverse() #te da vuelta los valores, aca daria [5,5,4,3] otra forma es con el .sort(reverse =True) o con rebanadas lista[::-1]
lista.sort() #ordena los elementos de la lista




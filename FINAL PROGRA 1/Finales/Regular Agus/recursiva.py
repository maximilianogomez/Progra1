'''
Ejercicio 1 
Desarrollar una función recursiva para buscar el mayor elemento par de una lista. 
La función recursiva sólo debe recibir por parámetro la lista.
'''

def mayor_recursiva(lista, mayor = "inicial"):
    if len(lista) == 0:
        if mayor == "incial":
            print("No hay numero par")
        else:
            return mayor
    else:
        if lista[0] % 2 == 0:
            if mayor == "inicial":
                mayor = lista[0]
            else:
                if lista[0] > mayor:
                    mayor = lista[0]
        lista = lista[1:]
        return mayor_recursiva(lista, mayor)
                       
lista=[-2,-6]
mayor=mayor_recursiva(lista)
print(mayor)
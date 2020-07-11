from random import randint as r

def GenerarListaRandom(tamanio = 10, minimo = 0, maximo = 100):
    """
    Genera una lista de valores aleatorios
    
    Devuelve una nueva lista con valores aleatorios
    
    Parámetros:
    tamanio -- numero entero. Cantidad de elemntos a generar (10 por defecto)
    
    minimo -- numero entero. Valor mínimo que puede tomar mi lista (0 por defecto)
    
    maximo -- numero entero. Valor máximo que puede tomar mi lista (100 por defecto)
    """
    
    lista = []
    
    for i in range(tamanio):
        lista.append(r(minimo,maximo))
        
    return lista

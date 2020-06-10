# Escribir una función buscarclave() que reciba como parámetros un diccionario y un
# valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario.
# Comprobar el comportamiento de la función mediante un programa apropiado.

#FUNCIONES:
def buscarclave(dic,valor):
    lista = []
    for nombre,val in dic.items():
        if val == valor:
            lista.append(nombre)
    return lista
#PROGRAMA PRINCIPAL:
def main():
    dic = {"Maxi":19,"Maria":56,"Juan":19}
    print(buscarclave(dic,19))
        
    
    
    
main()
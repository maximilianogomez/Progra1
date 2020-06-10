# Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
# y una lista de claves. La función debe eliminar del diccionario todas las claves
# contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad
# que indique si la operación fue exitosa. Desarrollar también un programa para verificar
# su comportamiento.

#FUNCIONES:
def eliminarclaves(dic,lista):
    terminado = False
    diferencia = (len(dic) - len(lista))
    for claves in lista:
        if claves in dic:
            del dic[claves]
        else:
            continue
    if len(dic) == diferencia:
        terminado = True
    return dic,terminado

#PROGRAMA PRINCIPAL:
def main():
    dic = {}
    clave = input("Ingrese una clave(vacia para terminar): ")
    while clave != "":
        dic[clave] = 1
        clave = input("Ingrese una clave(vacia para terminar): ")
    lista = ['hola', 'chau', 'perro', 'gato', 'hola!']
    dic, verdad = eliminarclaves(dic,lista)
    if not verdad:
        print("No se pudo eliminar del diccionario todos los valores de la lista o se eliminaron todos del diccionario y quedaron algunos de la lista sin eliminar")
    print(dic)
    
main()
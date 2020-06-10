# Una librería almacena su lista de precios en un diccionario. Diseñar un programa
# para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
# listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
# costoso que venden en el comercio.

#FUNCIONES:
def cargar_lista_precios():
    dic = {}
    while True:
        try:
            item = input("Ingrese el item (vacio para terminar): ")
            if item == "":
                return dic
            item = item.lower()
            precio = float(input(f"Ingrese el precio de {item}: "))
            dic[item] = precio
        except ValueError:
            print("Error, introdujo un valor invalido")

def aumentar_cuadernos(dic):
    if dic.get('cuadernos') != None:
        dic['cuadernos'] += ((dic['cuadernos']*15)/100)
    return dic

def imprimir_diccionario(dic):
    precios = dic.values()
    maximo = max(precios)
    for item in dic:
        if dic[item] == maximo:
            mas_caro = item
        print("item: ", item, "precio: ", dic[item])
    print()
    print(f"y el elemento mas caro es: {mas_caro} con un precio de: {maximo} ")

#PROGRAMA PRINCIPAL:
def main():
    dic = cargar_lista_precios()
    print(dic)
    print()
    print("Se le subio el precio a cuadernos un 15% si existen en los items")
    aumentar_cuadernos(dic)
    imprimir_diccionario(dic)
    
    
    
main()
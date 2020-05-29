# Eliminar de una lista de palabras las palabras que se encuentren en una segunda
# lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

#Funciones:
def eliminar_num(lista1,lista2):
    for num in lista1:
        if num in lista2:
            while lista1.count(num) > 0:
                lista1.remove(num)
        

#Programa Principal:
def main():
    print("TP2:EJ6")
    lista1 = [4 , 16 ,7 , 20 , 48 , 95 , 100 , 4 , 2]
    lista2 = [1 , 4 , 20 , 50 , 60 , 70]
    print("La lista original es: ")
    print(lista1)
    print("La lista con los elementos a borrar es: ")
    print(lista2)
    eliminar_num(lista1,lista2)
    print("La lista original con los elementos borrados es: ")
    print(lista1)
    
if __name__ == "__main__":
    main()
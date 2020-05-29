# Escribir una función que reciba una lista de números enteros como parámetro y la
# normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones
# relativas que cada elemento tiene en la lista original. Desarrollar también
# un programa que permita verificar el comportamiento de la función. Por ejemplo,
# normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].

#Funciones:
def NormalizarLista(lista):
    '''Genera una lista con los valores normalizados respetando las proporciones relativas de cada elemento'''
    suma = sum(lista)
    for i in range(len(lista)):
        lista[i] /= suma
        
#Programa Principal:
def main():
    print("TP2.EJ9: Crear una lista normalizada")
    lista = [1, 1, 2]
    print(lista)
    NormalizarLista(lista)
    print(lista)

if __name__ == "__main__":
    main()
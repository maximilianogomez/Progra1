# Para un número entero N menor de 100 recibido como parámetro, escribir un programa
# que utilice una función para devolver la suma de los cuadrados de aquellos
# números entre 1 y N que están separados entre si por cuatro unidades. (12 + 52 +
# 92 + 132 + …)


#Funciones:
def esmenora100(mensaje):
    """Numero comprueba que es menor a 100"""
    nro = int(input(mensaje))
    while nro >= 100:
        print("El numero es mayor o igual a 100")
        nro = int(input(mensaje))
    return nro

def suma_cuadrados(n):
    """devuelve la suma de los cuadrados de los numeros entre 1 y n separados por 4 numeros"""
    suma = 0
    i = 1 
    while i < n:
        suma += i**2
        i += 4
    return suma



def main():
    n = esmenora100("Ingrese un numero menor a 100: ")
    sumatoria = suma_cuadrados(n)
    print("El numero de la suma total es ")
    print(sumatoria)
    
    



#Programa Principal:
if __name__ == "__main__":
    main()
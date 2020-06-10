# Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo
# basta calcular su producto escalar y verificar si es igual a 0. Ejemplo:
# A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
# Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
# de verdad indicando si son ortogonales o no. Desarrollar también un programa
# que permita verificar el comportamiento de la función.

#FUNCIONES:
def es_ortogonal(vector1,vector2):
    bol = False
    if len(vector1) == len(vector2):
        i = 0
        suma = 0
        while i < len(vector1):
            suma += vector1[i] * vector2[i]
            i += 1
        if suma == 0:
            bol = True
    else:
        raise ValueError("Los vectores son de distinto tamaño")
     
    return bol


#PROGRAMA PRINCIPAL:
def main():
    try:
        vector1 = (int(input("Ingrese un numero del vector1: ")),int(input("Ingrese otro numero del vector1: ")))
        vector2 = (int(input("Ingrese un numero del vector2: ")),int(input("Ingrese otro numero del vector2: ")))
        if es_ortogonal(vector1,vector2):
            print(f"Los vectores {vector1} y {vector2} son ortogonales ")
        else:
            print(f"Los vectores {vector1} y {vector2} no son ortogonales ")
            
    except ValueError as mensaje:
        print(mensaje)
    
    
    
    
main()
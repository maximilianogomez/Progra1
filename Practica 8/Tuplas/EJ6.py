# Ídem anterior, pero determinando si los vectores son paralelos. Cuando dos vectores
# son paralelos los cocientes de sus coordenadas correspondientes son iguales
# entre sí. Ejemplo: U = (3,-1) y V = (-9,3)

#FUNCIONES:
def es_paralelo(v1,v2):
    bol = False
    lista = []
    for componente in v2:
        if componente == 0:
            raise ZeroDivisionError("Alguno de las componentes del segundo vector es 0 y estaria dividiendo por 0")
    if len(v1) == len(v2):
        i = 0
        cociente = 0
        while i < len(v1):
            cociente = v1[i] // v2[i]
            lista.append(cociente)
            if i != 0:
                if lista[i] == lista[i-1]:
                    bol = True
            i += 1
    else:
        raise ValueError("Los vectores son de distinto tamaño")
     
    return bol

#PROGRAMA PRINCIPAL:
def main():
    try:
        v1 = (int(input("Ingrese un numero del vector1: ")),int(input("Ingrese otro numero del vector1: ")))
        v2 = (int(input("Ingrese un numero del vector2: ")),int(input("Ingrese otro numero del vector2: ")))
        if es_paralelo(v1,v2):
            print(f"Los vectores {v1} y {v2} son paralelos ")
        else:
            print(f"Los vectores {v1} y {v2} no son paralelos ")
            
    except ValueError as mensaje:
        print(mensaje)
    except ZeroDivisionError as mensaje2:
        print(mensaje2)
    
main()
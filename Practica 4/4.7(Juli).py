'''7. Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y
cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar
el comportamiento de la misma. Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
'''

#FUNCIONES
def rebanadas(cad, pos, cant):
    eliminar = cad[pos:cant+pos]
    cadena = cad.split(eliminar)
    cadena = "".join(cadena)
    return cadena

def sinRebanadas(cad, pos, cant):
    eliminar = []
    for i in range (pos, cant+pos):
         eliminar.append(cad[i])
        
    eliminar = "".join(eliminar)
    cadena = cad.strip(eliminar)
    cadena = "".join(cadena)
    return cadena
         
         
def main():
    cadena = "El número de teléfono es 4356-7890"
    posic = 25
    cantidad = 8
    cadReb = rebanadas(cadena, posic, cantidad)
    print("Utilizando rebanadas")
    print(cadReb)
    cadSin = sinRebanadas(cadena, posic, cantidad)
    print("Sin utilizar rebanadas")
    print(cadSin)
    

#PROGRAMA PRINCIPAL
main()
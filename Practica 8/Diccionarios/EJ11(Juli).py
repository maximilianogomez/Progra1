# Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
# y una lista de claves. La función debe eliminar del diccionario todas las claves
# contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad
# que indique si la operación fue exitosa. Desarrollar también un programa para verificar
# su comportamiento.

def eliminarClaves(dic, lista):
    try:
        for clave in lista:
            del dic[clave]
        return True
    except KeyError:
        return False
    
def main():
    dic = {"Juan":18,"Maria":52,"Ana":74,"Jose":14}
    lista = ["Juan","Jose","Julieta"]
    if eliminarClaves(dic,lista):
        print("Se eliminaron las claves")
    else:
        print("Error al eliminar las claves")

main()
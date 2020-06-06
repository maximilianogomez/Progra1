# Archivo 2: Los campos están separados por el signo #.
# Pérez Juan#20080211#Corrientes 348
# González Ana M#20080115#Juan de Garay 1111 3er piso Dto A

#PROGRAMA PRINCIPAL:
def main():
    try:
        origen = open("Archivo2.txt")
        destino = open("CSVArchivo2.txt",'w')
    except IOError as mensaje:
        print(mensaje)
    else:
        for registro in origen:
            registro = registro.replace("\n","")
            lista = registro.split("#")
            nombre = lista[0]
            legajos = lista[1]
            dire = lista[2]
            destino.write(nombre+","+legajos+","+dire+"\n")
        print("Se finalizó la carga del Archivo2.txt")
    finally:
        origen.close()
        destino.close()
    
main()

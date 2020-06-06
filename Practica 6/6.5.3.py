# Archivo 3: Todos los campos de este archivo están precedidos por un
# número de dos dígitos que indica la longitud del campo a leer.
# 10Pérez Juan082008021114Corrientes 348
# 14González Ana M082008011533Juan de Garay 1111 3er piso dto A

#PROGRAMA PRINCIPAL:
def main():
    try:
        origen = open("Archivo3.txt")
        destino = open("CSVArchivo3.txt",'w')
    except IOError as mensaje:
        print(mensaje)
    else:
        for registro in origen:
            registro = registro.replace("\n","")
            #nombre
            long = int(registro[:2:])
            nombre = registro[2:long+2:]
            registro = registro[long+2::]
            #legajo
            long = int(registro[:2:])
            legajo = registro[2:long+2:]
            registro = registro[long+2::]
            #direccion
            long = int(registro[:2:])
            dire = registro[2::]
            destino.write(nombre+","+legajo+","+dire+"\n")
        print("Se finalizó la carga del Archivo3.txt")
    finally:
        origen.close()
        destino.close()
    
main()

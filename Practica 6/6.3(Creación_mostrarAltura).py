def promedio_gen():
    try:
        origen = open("PromedioAlturas.txt",'r')
    except IOError as mensaje:
        raise
    else:
        ctdad = 0
        suma = 0
        #Recorró todos los registros para guardar el promedio general
        for registro in origen:
            registro = registro.replace("\n","")
            if registro.isalpha():
                continue
            suma += float(registro)
            ctdad += 1
        prom_general = round(suma/ctdad,2)
        origen.close()
        return prom_general

def main():
    try:
        prom_general = promedio_gen()
        origen = open("PromedioAlturas.txt",'r')
    except IOError as mensaje:
        print(mensaje)
    else:
        lista = []
        linea = origen.readline()
        while linea != "":
            linea = linea.replace("\n","")
            if linea.isalpha():
                deporte = linea
                linea = origen.readline()
            if float(linea) >= prom_general and deporte not in lista:
                lista.append(deporte)
            linea = origen.readline()
        print(f"El promedio general es: {prom_general}")
        print("La lista de los deportes que tienen deportistas mas altos que el promedio general son: ")
        print(lista)
        origen.close()
    
main()
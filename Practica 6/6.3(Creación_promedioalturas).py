#PROGRAMA PRINCIPAL:
def main():
    try:
        origen = open("RangoAlturas.txt",'r')
        destino = open("PromedioAlturas.txt",'w')
    except IOError as mensaje:
        print(mensaje)
    else:
        print("Se procede a grabar un archivo con el promedio de las alturas")
        ctdad = 0
        suma = 0
        for registro in enumerate(origen):
            registro = list(registro)
            registro[1] = registro[1].replace("\n","")
            if registro[1].isalpha():
                if suma != 0:
                    try:
                        prom = suma / ctdad
                        prom = round(prom,2)
                    except ZeroDivisionError:
                        prom = 0
                    prom = str(prom) + "\n"
                    destino.write(prom)
                    suma = 0
                    ctdad = 0
                registro[1] += "\n"
                destino.write(registro[1])
                if registro[0] == 0:
                    continue
            else:
                ctdad += 1
                suma += float(registro[1])
                registro[1] += "\n"
        try:
            prom = suma / ctdad
            prom = round(prom,2)
        except ZeroDivisionError:
            prom = 0
        prom = str(prom) + "\n"
        destino.write(prom)
        origen.close()
        destino.close()

main()
            
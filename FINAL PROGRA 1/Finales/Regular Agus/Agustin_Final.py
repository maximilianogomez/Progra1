def leerArchivo(letra):
    try:
        origen = open("subtes.txt")
    except IOError:
        print("Hubo un error de carga")
    else:
        dic = {}
        linea = origen.readline() 
        # Compruebo que la linea sea la que ingrese
        while linea:
            linea = linea.replace('\n','')
            lista = linea.split(";")
            if lista[0] != letra:
                linea = origen.readline()
            else:
                i = 0
                while i < len(lista):
                    x = lista[i].find(":")
                    if x != -1:
                        lista2 = lista[i:i+1]
                        cad = ' '.join(lista2)
                        estacion_comb = cad.split(":")
                        estacion = estacion_comb[0]
                        combi = estacion_comb[1:]
                        cad_comb = ' '.join(combi)
                        dic[estacion] = cad_comb
                    i += 1
                try:
                    origen.close()
                else:
                    pass
                return dic

def main():
    while True:
        try:
            linea = input("Ingrese la linea que desea consultar(enter para terminar): ")
            if linea == '':
                break
            assert linea.isalpha(),'Debe ingresar letras'
            linea = linea.upper()

        except AssertionError as mnsj:
            print(mnsj)
        else:
            dic = leerArchivo(linea)
            try:
                print(f" Linea {linea} ")
                for clave,valor in dic.items():
                   print(f' Combinacion con linea {valor} en {clave}')
            except AttributeError:
                print('No existe la linea ingresada')

main()
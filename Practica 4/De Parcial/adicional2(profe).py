def quitarSimbolos(cad):
    '''Quita de la cadena los simbolos - y _'''
    ncad=cad.replace("-","")
    ncad=ncad.replace("_","")
    return ncad
def esValida(dire):
    '''Verifica si una dirección web es válida. '''
    ext=["com","edu","org"]
    valida = True
    #Separo en partes por el punto
    partes = dire.split(".")
    if dire[0:4]!="www.": #comenzar en www.
        valida= False
    elif len(partes)<3 or len(partes)>4: #tener tres o cuatro partes separadas por punto
        valida = False
    elif len(partes[1]) == 0:    #direccion al menos un caracter
        valida = False
    elif partes[1][0] in ["-","_"]: #No comience en _ o -
        valida = False
    elif not quitarSimbolos(partes[1]).isalnum(): #veo s es alfanumerico o _ o -
        valida = False
    elif len(partes)== 4 and len(partes[3])!=2 and not partes[3].isalpha(): #dos caracteres para pais
        valida = False
    elif partes[2] not in ext: #extensiones válidas
        valida = False
    
    return valida

def paises(listaDire):
    '''Arma una lista de Paises unicos.'''
    unicos=[]
    for dire in listaDire:
        if dire[-2:] not in unicos:
            unicos.append(dire[-2:])
    return unicos

def __main__():
    listaDires = []
    direccion = input("Ingrese una URL: ")
    while direccion != "":
        #la paso a minúscula y quito los espacios inicio y fin
        direccion = direccion.lower().strip()
        #verifico si es válida
        if esValida(direccion)==True:
            #Armo lista única, agrego us si corresponde a ese pais.
            if direccion.count(".") ==2:
                direccion=direccion+".us"
            if direccion not in listaDires:
                listaDires.append(direccion)
        else:
            print("La dirección no es válida")
        direccion = input("Ingrese una URL: ")
    #listado por pais
    listaPais=paises(listaDires)
    print(listaPais)
    print("Listado cantidad por pais")
    for ext in listaPais:
        lista = [dire for dire in listaDires if ext == dire[-2:]]
        print("Pais:",ext,"Cantidad:",len(lista))
    print(listaDires)
    #Eliminar las que contienen guión medio por comprensión
    listaDires=[dire for dire in listaDires if "-" not in dire]
    print(listaDires)
    
if __name__ == "__main__":
    __main__()
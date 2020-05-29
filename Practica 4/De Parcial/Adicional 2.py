# Desarrollar un programa que ingrese direcciones web y verifique si es una dirección válida, considerando que las direcciones web deberán:
# Comenzar con www. Continuar con caracteres alfanuméricos, guión medio, guión bajo en cualquier orden, al menos un caracter.
# No puede comenzar con guiones.
# Ignorar los espacios al inicio y fin de la cadena.
# Finalizar con .com .edu .org  puede contener a continuación . y dos caracteres alfabéticos representando un país.
# Finalizar el ingreso de direcciones web al no ingresar una cadena. 
#   Luego se solicita:    
# Informar un listado por pais cuántas direcciones se ingresaron (tener en cuenta que hay direcciones que no tienen el pais y corresponden a “us”).
#     Luego se pide eliminar de la lista aquellas direcciones que contienen guión medio.         
#     Mostrar un listado orden alfabético de todas las direcciones que son válidas, sin repetir considerando que no son “case sensitive”. 
#     Informar cuántas pertenecen a Argentina, las que finalizan con “ar”,
#     resolver este punto utilizando un método por comprensión o filtros. 
#     Ingresar por teclado una extensión válida ( se considera válida de tres caracteres alfabéticos, por ejemplo “com”) y
#     luego eliminar de la lista todas las direcciones que tienen esa extensión. Informar cuántos fueron eliminados.

#FUNCIONES:
def validar_pagina(dire):
    '''La funcion recibe una dirección y devuelve si esta dirección es o no válida'''
    valido = True
    dire = dire.strip(" ")
    dire = dire.lower()
    if dire.find(".com") != -1 or dire.find(".edu") != -1 or dire.find(".org") != -1:
        valido = True
    else:
        valido = False
    if dire.find("www.") == -1 :
        valido = False
    else:
        lstPalabras = dire.split("www.")
        if (lstPalabras[1])[0] == "-" or (lstPalabras[1])[0] == "_" or (lstPalabras[1])[0].isalnum() == "False":
            valido = False
        elif lstPalabras[1].count("-") != 0 or lstPalabras[1].count("_") != 0:
            valido = True
        else:
            valido = False
        dire = "".join(lstPalabras)
        if dire.count(".com") == 1:
            lstDire = dire.split(".com")
        elif dire.count(".edu") == 1:
            lstDire = dire.split(".edu")
        elif dire.count(".org") == 1:
            lstDire = dire.split(".org")
        if lstDire[1] != "" and not lstDire[1].isalpha() and len(lstDire[1]) != 3:
            valido = False
    return valido

def listado_paises_direcciones(web,paises,direcciones):
    '''La funcion busca si tiene o no algo seguido del com, edu u org. Si no lo tiene agrega la terminacion us a la lista de paises
    y si tiene alguna terminación de algún país valido la agrega a la lista de paises.
    Adicionalmente, la función me devuelve una lista con las direcciones no repetidas'''
    ''' la paginas no son case sensitive '''
    web = web.lower()
    if web not in direcciones:
        '''si no esta la agrego'''
        direcciones.append(web)
    if web.count(".com") == 1:
        lstDire = web.split(".com")
        if lstDire[1] == "":
            paises.append("us")
        else:
            paises.append(lstDire[1])
    elif web.count(".edu") == 1:
        lstDire = web.split(".edu")
        if lstDire[1] == "":
            paises.append("us")
        else:
            paises.append(lstDire[1])
    elif web.count(".org") == 1:
        lstDire = web.split(".org")
        if lstDire[1] == "":
            paises.append("us")
        else:
            paises.append(lstDire[1])
    return paises, direcciones

def arreglo_lstPaises(paises):
    ''' La idea de esta funcion es modificar la lista paises, eliminando los paises que se repiten y haciendo otra lista
    que muestra la cantidad de veces que se repite cada pais respectivamente'''
    listaContador = []
    i = 0
    while i < len(paises):
        listaContador.append(paises.count(paises[i]))
        while paises.count(paises[i]) != 1:
            pos = paises.index(paises[i],i+1)
            paises.pop(pos)
        i+= 1
    return paises, listaContador

def direcciones_singuion(direcciones):
    '''como es pedido en una parte del ejercicio, se borran todas las direcciones que contengan guion medio'''
    for direccion in direcciones:
        if direccion.count("-") >= 1:
            direcciones.remove(direccion)
    return direcciones

def comprension_arg(direcciones):
    '''informa cuantas direcciones tienen el ar utilizando el metodo listas por comprensión'''
    lstArg = [direccion for direccion in direcciones if direccion.index(".ar") == (len(direccion)-3) ]
    return lstArg
    
def filtro_arg(direcciones):
    '''informa cuantas direcciones tienen el ar utilizando el metodo filtro'''
    lst_filtrada = list(filter(lambda direccion:direccion.index(".ar") == (len(direccion)-3) ,direcciones))
    return lst_filtrada

def cadena_valida(mensaje):
    '''Verifica que la cadena sea valida'''
    cad = input(mensaje)
    while not cad.isalpha() and len(cad) != 3:
        print("Error, la cadena no es válida")
        cad = input(mensaje)
    return cad

def eliminar_ext(cad,direcciones_act):
    '''Recibe una cadena y la lista de direcciones. Elimina todos los elementos de la lista que contenga la cadena pasada
    y devuelve la cantidad de elementos que elimino y la lista actualizada.
    '''
    acum = 0
    for direccion in direcciones_act:
        if direccion.count(cad) >= 1:
            direcciones_act.remove(direccion)
    return direcciones_act, acum
        
        
#PROGRAMA PRINCIPAL:
def main():
    paises = []
    direcciones = []
    dire = input("Ingrese una dirección web que termine con .org, .edu o .com(no ingrese nada para terminar): ")
    esValido = validar_pagina(dire)
    while esValido and dire!= "":
        paises, direcciones = listado_paises_direcciones(dire,paises,direcciones)
        dire = input("Ingrese una dirección web que termine con .org, .edu o .com(no ingrese nada para terminar): ")
        esValido = validar_pagina(dire)
    if paises == []:
        print("no ingreso ni una dirección web válida")
    else:
        paises, lstContador = arreglo_lstPaises(paises)
        print("Los paises que aparecen en las direcciones web ingresadas son: ")
        print(paises)
        
        
        print("La cantidad de veces que aparecen respectivamente son: ")
        print(lstContador)
        
        
        direcciones.sort()
        print("La lista de las direcciones en orden alfabetica es: ")
        print(direcciones)
        
        
        print("La lista de las direcciones sin las que tienen '-' es: ")
        direcciones_actualizadas = direcciones_singuion(direcciones)
        print(direcciones_actualizadas)
        
        if len(direcciones_actualizadas) >= 1:
            print("La lista por comprension de todas las direcciones argentinas son: ")
            print(comprension_arg(direcciones_actualizadas))
            
            print("La lista por filtro de todas las direcciones argentinas son: ")
            print(filtro_arg(direcciones_actualizadas))
            
            cad = cadena_valida("Ingrese una cadena de tres caracteres alfabéticos: ")
            nuevas_direcciones, cdad_elim = eliminar_ext(cad,direcciones_actualizadas)
            print("La nueva lista de direcciones sin la cadena propuesta es: ")
            print(nuevas_direcciones)
            
            print(f"La cantidad de elementos eliminados fueron: {cdad_elim}")
        else:
            print("La cadena actualizada está vacia")
            

if __name__ == "__main__":
    main()
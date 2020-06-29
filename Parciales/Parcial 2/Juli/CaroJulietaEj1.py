# Se solicita un programa para ingresar cadenas de caracteres hasta ingresar una cadena vacía. Resolver utilizando while-true
# y creando o generando una excepción para rechazar las cadenas que no corresponden a una dirección de mail.
# Un mail válido tiene un solo @ y al menos un “punto” luego del @, y como máximo dos “puntos” (luego del arroba). Tener en
# cuenta que no siempre tiene una extensión referenciando al código del país. 
# Ejemplo: usuario@yahoo.com.ar, otro_usuario@gmail.com, nombre.apellido@yahoo.com.
# Al finalizar el ingreso informar:
# Listado de dominios que aparecen más de una vez ordenado alfabéticamente, indicando cuantas veces se ingresaron. Recorda que
# el dominio se refiere al tipo de organizacion y país, segun el ejemplo seria:
# Dominio     Cantidad
# com             2
# com.ar          1
# Informar también la cantidad de mails no válidos.
# FUNCIONES
def verificarDireccion(cad):
    val = False
    if cad.count("@") == 1:
        lista = cad.split("@")
        if lista[1].count(".") == 1 or lista[1].count(".") == 2:
            val = True
    return val

def SepararDominio(cad):
    dominio = ""
    lista = cad.split("@")
    dom = lista[1].split(".")
    if len(dom) == 2:
        dominio += f"{dom[1]}"
    else:
        dominio +=f"{dom[1]}.{dom[2]}"
    return dominio

def repeticionesDom(dom):
    dic = {}
    for elemento in dom:
        dic[elemento] = dom.count(elemento)
    return dic
    
def main():
    '''Programa principal'''
    dominios = []
    cont = 0
    while True:
        try:
            cadena = input("Ingrese una direccion de mail: ")
            if cadena == "":
                break
            assert (verificarDireccion(cadena)), "Se debe ingresar una cadena correspondiente a un mail"
            dominios.append(SepararDominio(cadena))
            
        except AssertionError as error:
            cont = cont+1
            print(error)
    
    dicConRep = repeticionesDom(dominios)
    lista = list(dicConRep)
    lista.sort()
    print("Dominio    Cantidad")
    for elemento in lista:
        print(f"{elemento:6s}{dicConRep[elemento]:9d}")
    print()
    print(f"Cantidad de mails no válidos: {cont}")
    
main()
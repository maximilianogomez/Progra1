# Se solicita crear un programa que ingrese direcciones de correo electrónico y verifique si representa una dirección válida
# del tipo .com.ar :
# usuario@dominio.com.ar
# Paraser considerada una dirección válida suponemos que el usuario está compuesto solamente por caracteres alfanuméricos,
# debe contener un solo caractér @,
# el dominio debe tener al menos un carácter y debe finalizar en .com.ar 
# El ingreso de direcciones finaliza al no ingresar una dirección de correo.
# Al finalizar mostrar un listado de todos los dominios sin repetir y recordar que las direcciones de mail no son case sensitive,
# ordenados alfabéticamente

#FUNCIONES:
def validar_correo(correo):
    valido = True
    correo = correo.lower()
    if correo.find(".com.ar") == -1:
        valido = False
    elif correo.find("@") == -1:
        valido = False
    else:
        lstPalabras = correo.split("@")
        if not lstPalabras[0].isalnum or len(lstPalabras[1]) < 8:
            valido = False
    return valido

def procesar_correo(correo, lstDominios):
    lstCorreos = (correo).split("@")
    for correos in lstCorreos:
        if lstCorreos[1] not in lstDominios:
            lstDominios.append(lstCorreos[1])
    return lstDominios
    
#PROGRAMA PRINCIPAL:
def main():
    lstDominios = []
    correo = input("Ingrese una dirección de correo del tipo usuario@dominio.com.ar: ")
    esValido = validar_correo(correo)
    while esValido:
        lstDominios = procesar_correo(correo,lstDominios)
        correo = input("Ingrese una dirección de correo del tipo usuario@dominio.com.ar: ")
        esValido = validar_correo(correo)
    lstDominios.sort()
    print(f"La lista de dominios ingresados es: {lstDominios} ")

if __name__ == "__main__":
    main()
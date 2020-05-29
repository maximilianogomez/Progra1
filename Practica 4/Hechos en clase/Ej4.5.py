def  filtrar_palabras_comprension(cadena, N):
    '''Recibe una cadena y un numero, devuelve una cadena con la palabras cuyo largo sea igual o mayor al numero'''
    lstPalabras = cadena.split()
    lstPalabrasFiltradas = [palabra for palabra in lstPalabras if len(palabra) >= N]
    espacio = " "
    cadenaFiltrada = espacio.join(lstPalabrasFiltradas)
    
    return cadenaFiltrada
    
def  filtrar_palabras_filter(cadena, N):
    '''Recibe una cadena y un numero, devuelve una cadena con la palabras cuyo largo sea igual o mayor al numero'''
    lstPalabras = cadena.split()
    palabrasFiltradas = filter(lambda palabra : len(palabra) >= N, lstPalabras)
    espacio = " "
    cadenaFiltrada = espacio.join(palabrasFiltradas)
    
    return cadenaFiltrada
    
def main():
    cadena='Recibe una cadena y un numero, devuelve una cadena con la palabras cuyo largo sea igual o mayor al numero'
    print(filtrar_palabras_filter(cadena,6))
    
if __name__ == "__main__":
    main()
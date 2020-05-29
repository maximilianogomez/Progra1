def EsCapicua(cadena):
    i = 0
    while i < len(cadena)//2 and cadena[i] == cadena[len(cadena)-i-1]:
        i += 1
        
    return i >= len(cadena)//2

def main():
    cadena = "Yo tengo un ojo de un color y otro de un color distinto"
    lstPalabras = cadena.split()
    for palabra in lstPalabras:
        if EsCapicua(palabra):
            print(f"La palabra {palabra} es capicua")
        else:
            print(f"La palabra {palabra} no es capicua")
            
if __name__ == "__main__":
    main()
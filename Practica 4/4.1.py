# Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
# utilizar cadenas auxiliares. Escribir además un programa que permita verificar su
# funcionamiento.

def cad_cap(cad):
    x = 0
    while x < (len(cad)//2) and cad[x] == cad[len(cad)-1-x]:
        x += 1
    return x >= (len(cad)//2)

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    lstPalabras = cadena.split()
    for cad in lstPalabras:
        if cad_cap(cad):
            print(f"La cadena {cad} es capicua")
        else:
            print(f"La cadena {cad} no es capicua")

if __name__ == "__main__":
    main()
        
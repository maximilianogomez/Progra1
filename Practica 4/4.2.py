# Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
# misma tiene 80 columnas

def centrar_cad(cad):
    print(cad.center(80, " "))

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    centrar_cad(cadena)

if __name__ == "__main__":
    main()